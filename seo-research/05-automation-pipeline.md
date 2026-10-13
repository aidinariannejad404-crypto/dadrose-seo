# 05 — SEO Automation Pipeline (dadrose.com · book.dadrose.com · azmoon.dadrose.com)

Status: design, not yet built · Author: automation-architect agent · Facts checked 2026-10-13 (each source line says so)
Scope: indexing, monitoring, Claude-assisted content pipeline, cross-subdomain internal linking, reporting, implementation, rollout.
Owner principles applied throughout: every number carries a source and date; pages are chosen by search intent; no link buying; **a human approves every publish**; KPIs are signups and purchases.

> Note on numbers in this file: API limits come from official docs (URLs and dates below). Alert thresholds (e.g. "-30% clicks") are **configurable starting values to tune**, not facts. They are marked `[tunable]`.

---

## 0. TL;DR architecture

```
                 ┌───────────────────────── seo-ops (Python 3.12, one repo) ─────────────────────────┐
 cron (GitHub    │ jobs/gsc_pull.py ─► SQLite (warehouse.db) ◄─ jobs/inspect_sample.py                │
 Actions or a    │ jobs/crux_pull.py ─┘          │            jobs/crawl_check.py (links, schema, robots) │
 systemd timer   │                               ▼                                                    │
 on a VPS)       │ jobs/anomalies.py ─► alerts (Telegram/e-mail) ; jobs/weekly_report.py (Persian)    │
                 │ content/ (Claude brief→draft) ─► WP REST (status=draft) ─► HUMAN legal review      │
                 │ on publish webhook ─► indexnow.py (Bing/Yandex/Naver/Seznam/Yep…) + sitemap check  │
                 └────────────────────────────────────────────────────────────────────────────────────┘
 Sites: dadrose.com (WP) · book.dadrose.com (WP+WooCommerce) · azmoon.dadrose.com (Next.js 16 + Django)
 Shared: topic taxonomy (topic_key) in all three ─► related-content blocks + azmoon recommendation API
```

Key decisions:
1. **Google discovery = sitemaps (accurate `lastmod`) + internal links.** Submit sitemaps once via the GSC Sitemaps API; Google retired the sitemap ping endpoint. **Do not** use the Google Indexing API for articles, courses, books or exams (it is for `JobPosting` / `BroadcastEvent`-in-`VideoObject` only).
2. **IndexNow for non-Google engines** (Bing, Yandex, Naver, Seznam, Yep, and others in the official list). Google is not a listed participant.
3. **URL Inspection API = monitoring only** (a rotating sample per property, within 2,000 calls/day/property). It cannot request indexing.
4. **One small Python service**, SQLite first. Move to BigQuery only if data outgrows SQLite (the free GSC bulk export to BigQuery is an alternative; see §2.1).
5. **Claude writes briefs and drafts, never publishes.** Drafts land in WordPress as `status=draft`. A human lawyer/editor approves (YMYL legal content).

---

## 1. Indexing

### 1.1 Sitemaps (per subdomain, accurate lastmod)

Google facts (source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap, checked 2026-10-13):
- One sitemap is limited to **50 MB uncompressed or 50,000 URLs**. Split larger sets and optionally use a **sitemap index**.
- Google uses `<lastmod>` **only if it is consistently and verifiably accurate**. It should be the date of the last *significant* change. A copyright-year change is not significant.
- Google **ignores `<priority>` and `<changefreq>`**. Do not spend effort on them.
- Sitemaps must be UTF-8 and use absolute URLs.
- Submission methods listed: Search Console, Search Console API, robots.txt `Sitemap:` line, WebSub. Cross-site sitemaps require verifying every site in GSC.
- The sitemap **ping endpoint was deprecated** (Google Search Central blog, June 2023: https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping, checked 2026-10-13). Any plugin or script still "pinging Google" does nothing useful. Remove it.

Per-site plan:

| Site | Sitemap source | lastmod source | Notes |
|---|---|---|---|
| dadrose.com (WP) | Yoast or Rank Math index (`/sitemap_index.xml`), or WP core `/wp-sitemap.xml` if no SEO plugin | `post_modified_gmt` | Use one generator only. A developer comment on the WP 5.5 announcement says Yoast disables the core sitemap. Exclude tag archives, author archives and attachment pages unless they have search intent. |
| book.dadrose.com (WP+Woo) | Same plugin. Product sitemap comes from the `product` post type. | `post_modified_gmt` of product | **Risk:** stock/price syncs bump `post_modified` without a content change, which makes lastmod "inaccurate" by Google's definition. Mitigation: stock-only updates should not touch `post_modified` (check the sync plugin), or filter lastmod to a custom `_content_modified` meta. |
| azmoon.dadrose.com (Next.js) | `app/sitemap.ts` (and `generateSitemaps` if ever > 50k URLs) | Django `updated_at` of the public entity, never `new Date()` | Today only `/` and `/guide` are public. `/app/**` and `/login` stay out. |

WordPress core facts (source: https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/, checked 2026-10-13):
- The core index is `/wp-sitemap.xml`. Each sub-sitemap has a filterable maximum of 2,000 entries.
- The 5.5 core did **not** emit lastmod (add it via the `wp_sitemaps_posts_entry` filter). Core changeset 56985 (https://core.trac.wordpress.org/changeset/56985, checked 2026-10-13; trade press attributes it to WP 6.5) added lastmod.
- **Action:** confirm the WP version and plugin on both WP sites before relying on core lastmod.

Next.js facts (source: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap, doc version 16.4.0, checked 2026-10-13):
- `app/sitemap.ts` returns `MetadataRoute.Sitemap`.
- `generateSitemaps()` splits the output into `/…/sitemap/[id].xml`.
- **In v16, `id` is a `Promise<string>`.** The repo pins `next@16.3.6`, so `await props.id`.
- The docs do not describe an automatic sitemap index for `generateSitemaps`. List the parts in `robots.ts` or in a small route handler that serves an index (see §6.6).

### 1.2 Submitting sitemaps: GSC Sitemaps API

- Endpoint: `PUT https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/sitemaps/{feedpath}`. No request body. Scope `https://www.googleapis.com/auth/webmasters` (read/write) (https://developers.google.com/webmaster-tools/v1/sitemaps/submit, checked 2026-10-13).
- Quota: "all other resources" is **20 QPS / 200 QPM per user, 100,000,000 QPD per project** (https://developers.google.com/webmaster-tools/limits, checked 2026-10-13).
- Submit **once per sitemap URL** (and again only when the index URL changes). Use `sitemaps.list` / `sitemaps.get` daily for monitoring: errors, warnings, `lastDownloaded`.
- Also add `Sitemap:` lines to each subdomain's robots.txt. This also covers Bing/Yandex discovery.

### 1.3 Separate GSC properties

- Create **URL-prefix properties** `https://dadrose.com/`, `https://book.dadrose.com/`, `https://azmoon.dadrose.com/` for per-subdomain reporting.
- Optionally also create a **Domain property** `sc-domain:dadrose.com` that aggregates all three, useful for the weekly roll-up.
- The API accepts both forms in `siteUrl`. URL-prefix properties need the trailing slash (https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect, checked 2026-10-13).
- Quotas are counted **per site** (property), so separate properties also give separate URL Inspection budgets (see §1.6).

### 1.4 IndexNow (non-Google engines)

Facts (https://www.indexnow.org/documentation, https://www.indexnow.org/faq, https://www.indexnow.org/searchengines.json, checked 2026-10-13):

- **Participants** (official `searchengines.json`): Bing, Yandex, Seznam, Naver, Yep, Internet Archive, Amazonbot.
- **Google is not listed.** Google's own recrawl guidance (https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl, checked 2026-10-13) lists only URL Inspection (few URLs) and sitemaps (many). It mentions neither IndexNow nor the Indexing API. **Treat IndexNow as having no effect on Google.**
- **Submitting to one endpoint shares the URLs with all participating engines.** Use `https://api.indexnow.org/indexnow`.
- **Batches:** up to **10,000 URLs per POST**.
- **Key:** 8–128 characters `[a-zA-Z0-9-]`. Host it as `https://<host>/<key>.txt`, UTF-8, containing only the key. Each subdomain is its own `host`, so **each subdomain needs its own key file at its root.** One key value may be reused, but separate keys per host are cleaner.
- A key file placed in a sub-folder only authorises URLs under that folder (`keyLocation` rule).
- **Response codes:**
  - `200` OK; `202` received, key pending validation; `400` bad request.
  - `422` URL not on this host, or key mismatch.
  - `429` too many requests. The FAQ also lists repeated submission of unchanged URLs as a cause of problems.
- **Only submit new, updated or deleted URLs.** Do not resubmit unchanged ones.
- **Bing** (https://www.bing.com/indexnow/getstarted, checked 2026-10-13): no numeric daily cap is published. 429 is described as "potential spam". Bing Webmaster Tools shows received URLs. Bing lists the **IndexNow plugin, Yoast, Rank Math, AIOSEO, SEOPress** as WordPress options.

Hosting the key:

| Site | Option |
|---|---|
| dadrose.com, book | **Plugin** (recommended), because the plugin both hosts the key and fires on publish/update/delete. Rank Math has IndexNow in its free "Instant Indexing" module (Bing blog, Feb 2022: https://blogs.bing.com/webmaster/february-2022/Rank-Math-Supports-IndexNow-for-WordPress-Sites). Yoast offers IndexNow in Premium (https://searchengineland.com/yoast-seo-premium-now-offers-indexnow-386084). Keep whichever SEO plugin is already installed. Do not run two IndexNow senders. |
| azmoon | Static file `frontend/public/<key>.txt`, or a route `app/[indexnowKey].txt/route.ts` that reads `INDEXNOW_KEY` from env. **No conflict with `src/proxy.ts`:** its matcher is only `/app`, `/app/:path*`, `/login`. Submission is sent by Django on publish/unpublish of a public entity (signal → Celery/cron queue → `indexnow.py`). |

Custom submission only for azmoon, and for bulk back-fills on WP (e.g. after a taxonomy migration).

### 1.5 Google Indexing API — do not use for these sites

- **Supported content** (https://developers.google.com/search/apis/indexing-api/v3/quickstart, https://developers.google.com/search/apis/indexing-api/v3/using-api, checked 2026-10-13): "can only be used to crawl pages with either `JobPosting` or `BroadcastEvent` embedded in a `VideoObject`."
- **Quota:** a default quota of **200** is "for API onboarding and submission testing". More usage requires a request for approval. Quota is counted per URL, including inside batches of up to 100.
- **Spam detection:** all submissions undergo "rigorous spam detection". Abuse, including multiple accounts to exceed quota, can lead to revoked access.
- **Risk for dadrose:** articles, course pages, product pages and exam pages match neither type. Pushing them through the API is outside policy. It can cost API access and offers no supported benefit.
- **Exception:** if dadrose later posts genuine job ads (e.g. law-firm hiring) with `JobPosting` markup, that page type qualifies.

### 1.6 URL Inspection API — monitoring, not requesting indexing

- **Endpoint:** `POST https://searchconsole.googleapis.com/v1/urlInspection/index:inspect`, body `{inspectionUrl, siteUrl, languageCode}`. Scope `webmasters` or `webmasters.readonly` (https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect, checked 2026-10-13).
- It reports the **indexed** version only. It cannot test a live URL or request indexing. The "Request indexing" button exists only in the GSC UI, which has its own quota (ask-google-to-recrawl page above).
- **Quota:** **2,000 QPD and 600 QPM per site; 10,000,000 QPD and 15,000 QPM per project** (https://developers.google.com/webmaster-tools/limits, checked 2026-10-13).
- **Useful response fields** (https://developers.google.com/webmaster-tools/v1/urlInspection.index/UrlInspectionResult, checked 2026-10-13):
  - `indexStatusResult.{verdict(PASS|PARTIAL|FAIL|NEUTRAL), coverageState, robotsTxtState, indexingState(INDEXING_ALLOWED|BLOCKED_BY_META_TAG|BLOCKED_BY_HTTP_HEADER|BLOCKED_BY_ROBOTS_TXT), lastCrawlTime, pageFetchState(SUCCESSFUL|SOFT_404|NOT_FOUND|SERVER_ERROR|REDIRECT_ERROR|…), googleCanonical, userCanonical, sitemap[], referringUrls[], crawledAs}`
  - `richResultsResult.{verdict, detectedItems[].items[].issues[]}`
- **Rotating sample design (per property per day, well under 2,000):**
  1. All URLs published or updated in the last 14 days, until they show `PASS`.
  2. The top N pages by clicks in the last 28 days (watch for canonical drift: `googleCanonical != userCanonical`).
  3. A random slice of the sitemap. Rotate so every sitemap URL is inspected at least once per cycle (cycle length = sitemap size ÷ daily budget).
  4. Stop at a configured budget (`[tunable]`, e.g. 1,500/day/property, which leaves headroom for manual UI use).
- **Output:**
  - Coverage rate per template (article/course/product/exam guide).
  - A list of "Crawled/Discovered – currently not indexed" pages. These feed the **internal-link fixer** (§4), not a "request indexing" loop.

### 1.7 Internal-link-driven discovery

Every new URL must, on the day it is published, be:
- (a) in its sitemap with a correct lastmod;
- (b) linked from at least one already-indexed hub page (topic hub, category, or the azmoon `/guide`);
- (c) linked from 2–5 related pages via the shared topic taxonomy (§4).

`inspect_sample.py` flags new URLs with empty `referringUrls` after N days `[tunable]`. Those go to the editor's queue.

---

## 2. Monitoring

### 2.1 Daily GSC Search Analytics pull

API facts:
- **Endpoint:** `POST https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query` (https://developers.google.com/webmaster-tools/v1/searchanalytics/query, checked 2026-10-13).
- **Parameters:**
  - `rowLimit` 1–25,000 (default 1,000); paginate with `startRow`.
  - Dimensions: `date, query, page, country, device, searchAppearance, hour`.
  - `type`: web|image|video|news|discover|googleNews.
  - `dataState`: final|all|hourly_all.
  - `aggregationType`: auto|byPage|byProperty.
- **Quotas** (https://developers.google.com/webmaster-tools/limits, checked 2026-10-13): **1,200 QPM per site, 1,200 QPM per user, 40,000 QPM and 30,000,000 QPD per project**, plus unpublished "load quotas" in 10-minute and 1-day windows. Queries grouped by `page`+`query` over long ranges are the expensive ones.
- **Data exposure** (https://developers.google.com/webmaster-tools/v1/how-tos/all-your-data, checked 2026-10-13):
  - The API exposes **at most 50,000 rows per day per search type**, sorted by clicks.
  - Data is **typically available after 2–3 days**.
  - Recommended practice: query **one day at a time** with `startDate == endDate`, paging in 25,000 steps until 0 rows.

Job design (`jobs/gsc_pull.py`), per property:
- Pull day D = today − 3 with `dataState=final`.
- Re-pull D−1…D−3 for late-final rows (idempotent upsert keyed on `(property, date, type, query, page, country, device)`).
- Query sets, all `type=web`:
  - (a) `date,page`
  - (b) `date,page,query`
  - (c) `date,country,device`
  - (d) `date,searchAppearance`
- Add `type=discover` only if Discover traffic appears.
- Backfill on first run: up to 16 months, one day per call, throttled to well under 1,200 QPM.

Store choice:

| Store | When | Notes |
|---|---|---|
| **SQLite** (default) | Three Persian niche properties are unlikely to hit 50k rows/day/type early on. **This is an assumption:** check row counts after backfill. | One file, versioned backups, simple SQL for reports. |
| BigQuery | If rows approach the 50k/day API cap, or for 16+ months of history | GSC has a native **bulk data export to BigQuery** (GSC → Settings → Bulk data export). It is not subject to the 50k API row cap. Requires a GCP project with billing. Not verified in this pass; confirm in GSC Help before choosing. |
| Google Sheets | Only as a *view* for the owner | Not a primary store. |

Schema (SQLite):
```sql
CREATE TABLE gsc_page_query_day(
  property TEXT, date TEXT, page TEXT, query TEXT, country TEXT, device TEXT,
  clicks INT, impressions INT, ctr REAL, position REAL,
  PRIMARY KEY(property,date,page,query,country,device));
CREATE TABLE url_inspection(property TEXT, url TEXT, inspected_at TEXT, verdict TEXT,
  coverage_state TEXT, indexing_state TEXT, page_fetch_state TEXT, google_canonical TEXT,
  user_canonical TEXT, last_crawl TEXT, referring_count INT, rich_verdict TEXT, raw JSON,
  PRIMARY KEY(property,url,inspected_at));
CREATE TABLE url_registry(url TEXT PRIMARY KEY, property TEXT, template TEXT, topic_key TEXT,
  published_at TEXT, content_modified_at TEXT, status TEXT);  -- from sitemaps + CMS webhooks
CREATE TABLE crux_daily(origin_or_url TEXT, form_factor TEXT, metric TEXT, p75 REAL,
  good REAL, ni REAL, poor REAL, collected_at TEXT, PRIMARY KEY(origin_or_url,form_factor,metric,collected_at));
CREATE TABLE kpi_daily(date TEXT, site TEXT, signups INT, purchases INT, revenue REAL, source TEXT,
  PRIMARY KEY(date,site,source));
```

### 2.2 Anomaly alerts (`jobs/anomalies.py`)

Rules run after each pull. All thresholds are `[tunable]` config, not facts.
- **Property level:** the 7-day clicks sum vs the trailing 28-day weekly mean. Alert if the drop is beyond the threshold *and* impressions also dropped (this filters out CTR-only noise).
- **Page level:** among the top 50 pages by clicks, any page whose 7-day clicks fall more than X% and whose position worsens by more than Y.
- **Indexing:**
  - a new `FAIL` / `BLOCKED_BY_*` / `NOT_FOUND` / `SOFT_404` on a sitemap URL;
  - canonical mismatch on a top page;
  - `sitemaps.get` showing errors > 0 or `lastDownloaded` older than Z days.
- **Zero-data guard:** if the API returns 0 rows for D while D−7 had rows, raise "pipeline or property issue", not "traffic crash".
- **Delivery:** e-mail (SMTP) or a Telegram bot message, in Persian, with a link to the GSC report.

### 2.3 Core Web Vitals

- **CrUX API:** `POST https://chromeuxreport.googleapis.com/v1/records:queryRecord` with `origin` or `url`, and `formFactor` `PHONE|DESKTOP|TABLET` (https://developer.chrome.com/docs/crux/api, checked 2026-10-13).
  - Limit: **150 queries/minute per Google Cloud project**, free; the limit cannot be raised.
  - Data: a 28-day rolling window, updated daily around 04:00 UTC (best effort), about 2 days behind.
  - Repeated same-day calls return the same data, so pull **once a day**: origin-level for the three origins, plus URL-level for the top pages.
  - Low-traffic URLs may return no record. Fall back to origin-level data. CrUX History API for trends is a separate endpoint and not verified here.
- **PageSpeed Insights v5:** `GET https://pagespeedonline.googleapis.com/pagespeedonline/v5/runPagespeed?url=…&strategy=MOBILE&category=PERFORMANCE&category=SEO` (https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed, checked 2026-10-13).
  - An API key is optional but recommended for automation (https://developers.google.com/speed/docs/insights/v5/get-started).
  - The quota is not stated on those pages; read it in the Cloud console for the project.
  - Use for **lab** checks on template URLs after deploys (one article, one product, one course, azmoon `/` and `/guide`).
- **Iran caveat:** CrUX only contains Chrome users who opted in. Treat its coverage of the Iranian audience as unknown, and confirm with the GSC CWV report and field RUM.
- **azmoon option:** the azmoon frontend could report `web-vitals` to its own Django endpoint. This is first-party and CSP-compatible (`connect-src 'self'`).

### 2.4 Site health crawler (`jobs/crawl_check.py`, weekly)

- **Broken links:**
  - Crawl each sitemap's URLs and extract `<a href>` links.
  - HEAD/GET internal and cross-subdomain links. Flag 4xx/5xx, redirect chains of 2 or more hops, and links to `noindex` pages.
  - Rate-limit to about 1 request/second per host `[tunable]`.
- **Schema validation:**
  - Extract `application/ld+json` and validate with a JSON-Schema subset per type (Article, Course, Product/Book, BreadcrumbList, FAQPage) plus required-property checks.
  - Cross-check with `richResultsResult` from URL Inspection.
  - Google's policy (https://developers.google.com/search/docs/appearance/structured-data/sd-policies, checked 2026-10-13): markup must describe visible content and be a true representation of the page. Test with the Rich Results Test or URL Inspection.
- **robots.txt and sitemap diffs:**
  - Fetch daily and store a hash.
  - On change, send a diff to alerts.
  - Hard alert if `Disallow: /` appears, or if a `Sitemap:` line disappears.
- **Uptime:**
  - 5-minute HTTP checks on `/`, a sample article, a product, and azmoon `/guide` (UptimeRobot-type SaaS, or a cron curl from the VPS).
  - GitHub Actions `schedule` is not suitable for uptime. Its minimum is 5 minutes, it "can be delayed during periods of high loads", and it runs in UTC (https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule, checked 2026-10-13).

---

## 3. Content pipeline with Claude (human-gated)

Google's rules that shape this pipeline:
- **Scaled content abuse** = generating many pages "for the primary purpose of manipulating search rankings". The listed example is "using generative AI tools … to generate many pages without adding value for users" (https://developers.google.com/search/docs/essentials/spam-policies, checked 2026-10-13).
- **Google's generative-AI guidance:** gen-AI is fine for research and structure. It is "critical to manually factcheck and review all AI-generated content for accuracy", including titles, meta descriptions, structured data and alt text. Disclosing how content was made "can help give your readers more context" (https://developers.google.com/search/docs/fundamentals/using-gen-ai-content, checked 2026-10-13).

### 3.1 Stages

| # | Stage | Automated by | Human gate | Output |
|---|---|---|---|---|
| 1 | Keyword intake | GSC queries with impressions but no good page (position > 10, or query↔page mismatch); Semrush/Keyword Planner exports; the azmoon weak-topic stats (topics where users fail most) | Owner picks the topic list each week | `keywords.csv` with `topic_key` |
| 2 | SERP and intent analysis | Script fetches the top 10 results (SERP API or manual paste; scraping Google directly is against its terms) and classifies intent (informational / navigational / commercial / transactional), format, and the page types that rank | Editor confirms intent → **decides page type and site**: article (dadrose.com), course landing (dadrose.com), product (book), practice exam/guide (azmoon) | `intent.json` |
| 3 | Content brief | Claude: outline, questions to answer, **legal sources to cite (law article numbers, Majlis/Judiciary URLs)**, internal-link targets from the taxonomy, schema type, title/meta options | Editor edits the brief | `brief.md` |
| 4 | Draft | Claude drafts **from the brief and source excerpts** supplied in the prompt. Every legal claim must cite a provided source or be marked `[نیاز به منبع]` | — | `draft.html` |
| 5 | **Legal review (YMYL)** | Diff view, citation checklist, "unsourced claims" list auto-extracted | **Mandatory:** a licensed lawyer or legal editor approves facts, numbers, dates and law references. The byline shows a real reviewer | approved draft |
| 6 | Push as WP draft | `wp_draft.py` → `POST /wp-json/wp/v2/posts` with `status=draft` (never `publish`) | — | WP post ID |
| 7 | Schema and internal links | Auto-suggest JSON-LD (Article + BreadcrumbList; FAQPage only if a visible FAQ exists) and 3–8 internal links from the taxonomy (§4) | Editor accepts or rejects in WP | — |
| 8 | **Publish** | — | **Human clicks Publish** in WP (owner principle) | live URL |
| 9 | Notify | WP plugin sends IndexNow automatically. The sitemap updates lastmod. `url_registry` gets the URL via webhook | — | — |
| 10 | Post-publish monitoring | URL Inspection daily until PASS; GSC pulls; first-30-days report | — | — |
| 11 | Refresh loop | Triggers (§3.3) create a refresh brief, then back to stage 4 | Same gates | updated post (`modified` changes → lastmod) |

### 3.2 Guardrails against scaled content abuse (enforced in code)

- **Throughput cap:** at most N drafts per week `[tunable]`, sized to reviewer capacity. The queue refuses beyond the cap.
- **No template mass pages:** the job refuses keyword lists that differ only by a variable (city/year/number) unless the editor attaches unique data for each page.
- **Uniqueness check:** embedding similarity against existing posts across all three sites. If a draft is above a threshold `[tunable]`, merge it or refresh the existing page instead of creating a new one (this also prevents cannibalisation).
- **Source requirement:** the draft fails CI if it has numbers or dates without a citation, which mirrors "every number needs a source/date".
- **Value gate:** the editor ticks at least one "added value" box: original data (e.g. azmoon aggregate statistics with the date range stated), expert commentary, worked examples, or updated law references.
- **Disclosure:** a short Persian note, e.g. «این مطلب با کمک ابزارهای هوش مصنوعی پیش‌نویس و توسط [نام وکیل] بازبینی شده است», per Google's suggestion.
- **Audit log:** prompt, model, sources, reviewer and approval time stored per post.

### 3.3 Refresh triggers (weekly job). All thresholds `[tunable]`.

- **Decay:** 28-day clicks down more than X% vs the previous 28 days *and* the page is more than 6 months old.
- **Striking distance:** queries at average position 4–15 with impressions above a floor. Brief: add a section for that query, improve title/H1 match.
- **Low CTR:** CTR well below the property's median CTR for the same position bucket. Brief: rewrite title/meta (human approves).
- **Law changed:** the azmoon backend already flags questions when a law article changes (`content.ArticleVersion`, `QuestionArticleLink`). Expose a "law changed" feed, so dadrose articles tagged with the same law article get a review ticket. This is the strongest YMYL freshness signal available.
- **Exam calendar:** before registration or exam dates (azmoon `src/content/exams.ts` holds those facts with `verified` flags), refresh the guide and related articles.

### 3.4 Claude usage notes

- Python SDK `anthropic`, model `claude-opus-5-5`, `output_config.effort="high"` for briefs and drafts.
- Structured output (JSON schema) for briefs, so downstream code can validate.
- Server-side refusal fallbacks enabled (`fallbacks: "default"`, beta `server-side-fallback-2026-07-01`).
- **Operational constraint:** Anthropic's supported-countries page does not list Iran (https://www.anthropic.com/supported-countries, checked 2026-10-13). The Claude-calling job must be run and owned by a person or entity in a supported region and comply with Anthropic's terms. The owner decides this before Phase 2.

---

## 4. Cross-subdomain internal linking

### 4.1 Shared topic taxonomy (`topic_key`)

- **Source of truth: the azmoon Django `content.Topic` tree** (`backend/content/models.py`: `Subject` → `Topic` with `parent`). It already classifies every question.
  - Add a stable slug: `Topic.topic_key = SlugField(unique=True)`, e.g. `civil-procedure/jurisdiction`.
  - Add the same to `Subject.key`, which already exists as a SlugField.
  - Do not use DB ids across sites; ids differ per environment.
- **Export:** `GET /api/v1/taxonomy` (public, cached) → `[{topic_key, subject_key, title_fa, parent_key, aliases[]}]`.
- **WordPress (both sites):**
  - Register a custom taxonomy `dadrose_topic` (hierarchical, `show_in_rest: true`) on `post`, the course CPT, and `product`.
  - A daily sync script upserts terms via `POST /wp-json/wp/v2/dadrose_topic` with `slug=topic_key`.
  - Editors tag content with 1 primary and up to 3 secondary topics.
- **Mapping table** in seo-ops `url_registry.topic_key` (from WP REST `dadrose_topic` and the azmoon taxonomy) is used by reports ("traffic and conversions per topic across the three sites").

### 4.2 Recommendation API (azmoon exam results → articles, courses, books)

- **Signal:** `exams.AttemptQuestion` stores `topic_id_snapshot`, the result, and auto/wizard mistake tags.
  - Weak topics = topics with the lowest score or the most "didn't know" in the attempt, weighted by the section coefficient.
- **Endpoint (Django):** `GET /api/v1/attempts/<id>/recommendations`, authenticated, next to the existing `attempt-report` route in `backend/exams/urls.py`. It returns, per weak topic: 1–2 articles (dadrose.com), 1 course, 1 book, each with a UTM-tagged URL (§5.2).
- **Content index:**
  - A nightly job pulls WP REST `GET /wp-json/wp/v2/posts?dadrose_topic=<id>&_fields=id,link,title,modified` and the same for products and courses.
  - It stores the results in a Django table `CrossContent(topic_key, site, kind, url, title, rank_score)`.
  - `rank_score` = editor pin, then GSC clicks (from seo-ops), then recency.
  - No live calls to WP during the request.
- **UI:** a «برای جبران این ضعف» block in `src/components/report/report-view.tsx`.
- **SEO note:** report pages are `noindex` (`src/app/app/(shell)/layout.tsx`, `src/app/app/attempts/[attemptId]/page.tsx`), so these links serve **conversion, not ranking**. Ranking links must come from public pages (§4.3).

### 4.3 Related-content blocks (crawlable)

- **dadrose.com article:**
  - "Test yourself" → the matching azmoon public topic/practice landing page (to be built under `src/app/(public)/`, e.g. `/topics/[topicKey]`, indexable *only if* it has unique content: topic explanation, sample questions, stats);
  - "Related book" → book.dadrose.com product;
  - "Course" → course page.
- **book product:** "Articles on this topic" and "Practice test".
- **azmoon `/guide` and topic pages:** "Read" → articles; "Book" → product.
- **Implementation:** WP — one small plugin (shortcode/block) that reads the same `CrossContent` JSON from azmoon (`GET /api/v1/crosslinks?topic=`) with a transient cache. Next — a server component that fetches at build/revalidate time.

### 4.4 Anchor-text and link rules

- **Descriptive Persian anchors** that match the target's primary intent (e.g. «نمونه سؤال آیین دادرسی مدنی»). Rotate among 3–5 approved variants per target. Never use exact-match keyword stuffing, and never «اینجا کلیک کنید».
- **Volume:** at most 1 link per target per page. Related blocks hold 3–6 items.
- **Contextual links:** editors add them; the tool only suggests.
- **No links into `noindex` or login-walled pages** from public content. Exception: CTA buttons to `/login`, which are fine for users but carry no SEO value.
- **Cross-subdomain links are normal followed links** (same owner, no `nofollow`). No reciprocal link schemes with outside sites, and no paid links (owner principle; Google spam policies on link schemes).
- **Orphan check:** every indexable URL in `url_registry` must have at least 1 internal inlink (from the crawler) and at least 1 cross-site inlink when the topic exists on other sites.

---

## 5. Reporting and KPI tie-in

### 5.1 Weekly owner report (Persian)

- **Schedule:** Saturday morning Tehran time (cron in UTC).
- **Format:** HTML e-mail plus a PDF or Sheet link, with Persian digits and Jalali dates.
- **Sections:**
  1. خلاصه: clicks/impressions/CTR/avg position per property, with week-over-week and the date range stated ("داده GSC تا تاریخ X؛ تأخیر ۲–۳ روزه").
  2. **KPI:** signups (azmoon) and purchases (book, courses), by source/medium and by landing topic.
  3. Indexing: inspected/PASS/FAIL counts per template, plus new problems.
  4. Top winners and losers (pages and queries).
  5. CWV status per origin.
  6. Content: drafts in review, published this week, refresh queue.
  7. Actions for the owner (approve X, fix Y).
- **Data provenance:** each figure carries its data source and date window, per the owner principle.
- **Claude's role:** may write the narrative paragraph from the computed table only; it must not compute numbers. Numbers come from SQL.

### 5.2 GA4, events and UTM conventions

- **One GA4 property and one web data stream** for all three subdomains, so the user journey (article → exam → book) is one session/user.
- **GA4 Help** (https://support.google.com/analytics/answer/10071811, checked 2026-10-13):
  - Cross-domain configuration is *recommended* for subdomains, because self-referrals can appear when subdomains use different cookie domains.
  - Make sure all subdomains use the same cookie domain.
  - List the subdomains (or `dadrose.com`) in the cross-domain list and in the unwanted-referrals exclusions.
- **Events** (GA4 recommended event names; verify the exact parameter list in GA4 docs during implementation):

  | Site | Events |
  |---|---|
  | azmoon | `sign_up` (method: otp), `exam_start`, `exam_submit`, `begin_checkout`/`purchase` for subscriptions (Django `commerce`/`subscriptions` apps) |
  | book (WooCommerce) | `view_item`, `add_to_cart`, `begin_checkout`, `purchase` (via the official Google for WooCommerce plugin or GTM) |
  | dadrose.com | `sign_up`, course `purchase` |

  Mark `sign_up` and `purchase` as **key events**.
- **azmoon CSP conflict (repo-specific):** `frontend/next.config.ts` sets `script-src 'self'` and `connect-src 'self'` under the "no third-party runtime assets" rule (legacy incident 9). This **blocks gtag.js**. Options:
  - **(a) Recommended:** send `sign_up` and `purchase` **server-side from Django via the GA4 Measurement Protocol** at the moment of truth (OTP verified, payment confirmed). Pass the `client_id` read from the `_ga` cookie set on the WP sites (same parent domain) through the BFF.
  - (b) Self-host a first-party tagging endpoint (server-side GTM on a dadrose subdomain).
  - (c) Relax the CSP for Google domains. This contradicts the incident-9 rule; owner decision.

  Measurement Protocol details were not re-verified in this pass. Check https://developers.google.com/analytics/devguides/collection/protocol/ga4 before building.
- **UTM rules for cross-subdomain links:**
  - With a single GA4 property, **do not put UTM parameters on internal cross-subdomain links.** UTMs start a new session and overwrite the real acquisition source.
  - Instead, tag internal promos with a **custom event** `internal_promo_click` with params `{from_site, to_site, block: related|reco|cta, topic_key}`, or with `data-*` attributes read by GTM.
  - Use UTMs only for external channels (Telegram, Instagram, e-mail, SMS): `utm_source=telegram&utm_medium=social&utm_campaign=<yyyy-mm>_<topic_key>`, all lowercase, Latin, hyphens.
  - If the owner insists on separate GA4 properties per subdomain (not recommended), then UTMs on cross-links become necessary: `utm_source=azmoon&utm_medium=internal&utm_campaign=reco_<topic_key>`.
- **seo-ops KPI pull:** the GA4 Data API (`runReport`) daily → `kpi_daily`. Use this alongside the WooCommerce/Django order tables, which are authoritative for purchases.

---

## 6. Implementation

### 6.1 Runtime choice

- **Recommended: a small Python service on a VPS** (systemd timers + SQLite + backups). Reasons:
  - it needs a persistent SQLite file;
  - it needs a webhook receiver for WP publish events;
  - uptime checks need a 5-minute cadence that is not delayed.
- **GitHub Actions cron is acceptable for the batch jobs** (GSC pull, reports), with the SQLite DB committed to a private repo or stored in object storage. Its constraints: UTC, minimum 5 minutes, possible delays, and **in a public repo, scheduled workflows are disabled after 60 days of no activity** (https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule, checked 2026-10-13). Use a private repo.
- **Libraries:** `google-api-python-client`, `google-auth`, `httpx`, `anthropic`, `selectolax` (HTML parsing), `jsonschema`, `jinja2` (reports), `persiantools`/`jdatetime` (Jalali dates).

### 6.2 Google service account setup (owner + developer)

1. Create a Google Cloud project, e.g. `dadrose-seo-ops`. Enable the **Google Search Console API**, **Chrome UX Report API**, **PageSpeed Insights API**, and **Google Analytics Data API**.
2. IAM → Service Accounts → create `seo-ops@dadrose-seo-ops.iam.gserviceaccount.com` → Keys → JSON key. Prefer Workload Identity Federation if running in GitHub Actions, which avoids long-lived keys.
3. **In each GSC property** (Settings → Users and permissions), add the service-account e-mail:
   - as a **Full user** (needed to submit sitemaps);
   - as a Restricted user if the account only reads.
   - The owner must do this for all three URL-prefix properties (and the Domain property).
4. In GA4 Admin → Property access management, add the service account as **Viewer** (for the Data API).
5. Create an API key restricted to the CrUX + PSI APIs.
6. **Sanctions/eligibility:** Google Cloud account eligibility for an Iran-based owner was **not verified** in this pass. The owner must confirm who legally owns the GCP project and billing before Phase 1. The GSC UI itself is per-Google-account.

### 6.3 Secrets

| Secret | Holder | Storage |
|---|---|---|
| GCP SA key or WIF config | developer | GitHub Actions encrypted secret / VPS `/etc/seo-ops/sa.json` (mode 600, never in git) |
| WP Application Passwords (one per site, for a dedicated `seo-bot` user with **Author** role — can create drafts, cannot edit others') | owner creates | same as above |
| IndexNow key per host | developer | env var; public by design (the key file is public) |
| Anthropic API key | owner/developer | env var |
| Telegram bot token / SMTP | developer | env var |

WP Application Passwords: core since **WP 5.6**. Create them at Users → Edit User. Use them over HTTPS with Basic auth (https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/, checked 2026-10-13). Some security plugins or hosts disable them; check on both WP sites.

Note on the bot's role: the Author role can publish its own posts in WordPress. To *enforce* "human publishes", either:
- use the **Contributor** role, which can create posts but cannot publish them, so drafts can't be published by the bot even if compromised (but Contributors can't upload media), or
- keep Author and rely on code that only ever sends `status=draft`/`pending`.

**Recommended: Contributor plus `status=pending`** (a "Pending Review" queue).

### 6.4 Repo layout (`seo-ops/`, new private repo)

```
seo-ops/
├─ pyproject.toml
├─ config/
│  ├─ sites.yaml          # properties, sitemaps, wp base urls, indexnow hosts, budgets [tunable]
│  └─ thresholds.yaml     # anomaly + refresh thresholds [tunable]
├─ seoops/
│  ├─ google_auth.py      # credentials from SA/WIF
│  ├─ gsc.py              # search analytics, sitemaps, url inspection
│  ├─ indexnow.py
│  ├─ crux.py  psi.py  ga4.py
│  ├─ wp.py               # WP REST client
│  ├─ crawl.py  schema_check.py  robots_diff.py
│  ├─ taxonomy.py         # sync azmoon taxonomy -> WP terms
│  ├─ claude_content.py   # brief/draft generation (structured output)
│  ├─ store.py            # SQLite
│  └─ report_fa.py        # Persian weekly report (jinja2)
├─ jobs/                  # thin CLIs, one per cron entry
│  ├─ gsc_pull.py  inspect_sample.py  crux_pull.py  crawl_check.py
│  ├─ anomalies.py  refresh_queue.py  weekly_report.py  sitemap_submit.py
├─ webhooks/app.py        # FastAPI: WP publish hook -> url_registry (+ IndexNow for azmoon)
├─ templates/report_fa.html.j2
├─ data/warehouse.db      # gitignored; nightly backup
└─ .github/workflows/daily.yml  weekly.yml
```

### 6.5 Python snippets

**Auth + GSC client**
```python
# seoops/google_auth.py
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES_RW = ["https://www.googleapis.com/auth/webmasters"]          # sitemaps.submit needs RW
SCOPES_RO = ["https://www.googleapis.com/auth/webmasters.readonly"]

def gsc(readonly: bool = True, keyfile: str = "/etc/seo-ops/sa.json"):
    creds = service_account.Credentials.from_service_account_file(
        keyfile, scopes=SCOPES_RO if readonly else SCOPES_RW)
    # "searchconsole" v1 exposes searchanalytics, sitemaps, sites and urlInspection
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)
```

**Search Analytics daily pull (one day, paged)**
```python
# seoops/gsc.py
import time, datetime as dt
from googleapiclient.errors import HttpError

def pull_day(svc, site_url: str, day: dt.date, dims: list[str], search_type="web"):
    """Yields rows for one day. Docs: max 25,000 rows/page; paginate with startRow until 0 rows.
    API exposes at most 50k rows/day/search type (developers.google.com/webmaster-tools/v1/how-tos/all-your-data)."""
    start = 0
    while True:
        body = {
            "startDate": day.isoformat(), "endDate": day.isoformat(),
            "dimensions": dims, "type": search_type, "dataState": "final",
            "rowLimit": 25000, "startRow": start,
        }
        for attempt in range(5):
            try:
                resp = svc.searchanalytics().query(siteUrl=site_url, body=body).execute()
                break
            except HttpError as e:
                if e.resp.status in (429, 500, 503):
                    time.sleep(2 ** attempt); continue
                raise
        rows = resp.get("rows", [])
        if not rows:
            return
        for r in rows:
            yield dict(zip(dims, r["keys"]), clicks=r["clicks"], impressions=r["impressions"],
                       ctr=r["ctr"], position=r["position"])
        start += len(rows)

# jobs/gsc_pull.py (excerpt)
# day = today - 3 ; for each property in sites.yaml:
#   store.upsert("gsc_page_query_day", pull_day(svc, prop, day, ["page","query","country","device"]))
```

**URL Inspection rotating sample**
```python
def inspect_sample(svc, site_url: str, urls: list[str], budget: int, store):
    """Monitoring only: the API reports the indexed version; it cannot request indexing.
    Quota: 2,000/day and 600/min per site (developers.google.com/webmaster-tools/limits)."""
    for i, url in enumerate(urls[:budget]):
        res = svc.urlInspection().index().inspect(
            body={"inspectionUrl": url, "siteUrl": site_url, "languageCode": "fa"}).execute()
        r = res["inspectionResult"]
        idx = r.get("indexStatusResult", {})
        store.insert("url_inspection", {
            "property": site_url, "url": url, "verdict": idx.get("verdict"),
            "coverage_state": idx.get("coverageState"), "indexing_state": idx.get("indexingState"),
            "page_fetch_state": idx.get("pageFetchState"),
            "google_canonical": idx.get("googleCanonical"), "user_canonical": idx.get("userCanonical"),
            "last_crawl": idx.get("lastCrawlTime"), "referring_count": len(idx.get("referringUrls", [])),
            "rich_verdict": r.get("richResultsResult", {}).get("verdict"), "raw": res,
        })
        if i % 500 == 499:
            time.sleep(60)   # stay far below 600 QPM

def build_sample(store, site_url, budget):
    fresh   = store.urls_modified_within(site_url, days=14, not_pass=True)
    top     = store.top_pages_by_clicks(site_url, days=28, limit=200)
    rotate  = store.least_recently_inspected(site_url, limit=budget)
    seen, out = set(), []
    for u in fresh + top + rotate:
        if u not in seen:
            seen.add(u); out.append(u)
    return out[:budget]
```

**Sitemap submit + status**
```python
from urllib.parse import quote

def submit_sitemap(svc_rw, site_url: str, sitemap_url: str):
    # PUT .../sites/{siteUrl}/sitemaps/{feedpath}; no body; scope webmasters (RW)
    svc_rw.sitemaps().submit(siteUrl=site_url, feedpath=sitemap_url).execute()

def sitemap_status(svc, site_url: str):
    return svc.sitemaps().list(siteUrl=site_url).execute().get("sitemap", [])
    # alert on: errors > 0, warnings > 0, stale lastDownloaded, isPending stuck
```

**IndexNow submit (azmoon, back-fills)**
```python
# seoops/indexnow.py
import httpx

ENDPOINT = "https://api.indexnow.org/indexnow"   # shared to all participating engines

def submit(host: str, key: str, urls: list[str]) -> list[int]:
    """Max 10,000 URLs per POST; only changed/new/deleted URLs; key file at https://{host}/{key}.txt."""
    assert all(httpx.URL(u).host == host for u in urls), "URLs must belong to the host (else 422)"
    codes = []
    for i in range(0, len(urls), 10_000):
        r = httpx.post(ENDPOINT, timeout=30, json={
            "host": host, "key": key,
            "keyLocation": f"https://{host}/{key}.txt",
            "urlList": urls[i:i + 10_000],
        }, headers={"Content-Type": "application/json; charset=utf-8"})
        codes.append(r.status_code)          # 200/202 ok; 400/422/429 (or any other) -> alert
        if r.status_code == 429:
            break
    return codes
```

**WordPress REST: create a draft (pending review)**
```python
# seoops/wp.py
import httpx

class WP:
    def __init__(self, base: str, user: str, app_password: str):
        self.c = httpx.Client(base_url=f"{base}/wp-json/wp/v2", auth=(user, app_password), timeout=60)

    def create_draft(self, title, html, slug, excerpt, category_ids, topic_term_ids, meta=None):
        r = self.c.post("/posts", json={
            "title": title, "content": html, "slug": slug, "excerpt": excerpt,
            "status": "pending",            # never 'publish' -- a human publishes
            "categories": category_ids,
            "dadrose_topic": topic_term_ids,  # custom taxonomy registered with show_in_rest
            "meta": meta or {},               # e.g. {"_seoops_brief_id": "...", "_ai_assisted": "1"} (register_post_meta show_in_rest)
        })
        r.raise_for_status()
        return r.json()["id"], r.json()["link"]
```
Endpoint and arguments: `POST /wp/v2/posts`, `status ∈ {publish, future, draft, pending, private}`, `categories`, `tags`, `meta`, `slug`, `excerpt`, `featured_media` (https://developer.wordpress.org/rest-api/reference/posts/, checked 2026-10-13). SEO title/meta for Yoast or Rank Math are stored in plugin post-meta. Writing those over REST requires that the meta keys are registered `show_in_rest`, or a plugin endpoint. Verify per plugin.

**Claude brief (structured output)**
```python
# seoops/claude_content.py
import json, anthropic

client = anthropic.Anthropic()
BRIEF_SCHEMA = {
  "type": "object", "additionalProperties": False,
  "required": ["primary_intent", "page_type", "target_site", "h1", "outline", "must_cite", "internal_links", "schema_type"],
  "properties": {
    "primary_intent": {"type": "string", "enum": ["informational","commercial","transactional","navigational"]},
    "page_type": {"type": "string", "enum": ["article","course_landing","product","practice_landing","refresh_existing"]},
    "target_site": {"type": "string", "enum": ["dadrose.com","book.dadrose.com","azmoon.dadrose.com"]},
    "h1": {"type": "string"},
    "outline": {"type": "array", "items": {"type": "string"}},
    "must_cite": {"type": "array", "items": {"type": "string"}},       # law articles / official URLs from provided sources only
    "internal_links": {"type": "array", "items": {"type": "string"}},  # chosen from provided candidate URLs only
    "schema_type": {"type": "string", "enum": ["Article","Course","Product","WebPage"]},
  },
}

def make_brief(keyword: str, serp_summary: str, sources: str, link_candidates: list[str]) -> dict:
    resp = client.beta.messages.create(
        model="claude-opus-5-5", max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"], fallbacks="default",
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": BRIEF_SCHEMA}},
        system=("You write Persian SEO content briefs for an Iranian legal-education publisher. "
                "Use only the provided sources for any legal fact, number or date; never invent them. "
                "If the keyword is already covered by an existing URL in the candidates, choose page_type "
                "'refresh_existing'. Internal links must come from the candidate list."),
        messages=[{"role": "user", "content":
            f"Keyword: {keyword}\n\nSERP summary:\n{serp_summary}\n\nSources:\n{sources}\n\n"
            f"Internal link candidates:\n" + "\n".join(link_candidates)}],
    )
    if resp.stop_reason == "refusal":
        raise RuntimeError("model declined; route to human")
    text = next(b.text for b in resp.content if b.type == "text")
    return json.loads(text)
```

### 6.6 Next.js (azmoon) files to add, tailored to the repo

Current state:
- `frontend/src/app/` has `layout.tsx` (root metadata, `lang="fa" dir="rtl"`) and `manifest.ts`.
- Public pages are `(public)/page.tsx` (`/`) and `(public)/guide/page.tsx` (`/guide`).
- Private routes are `app/(shell)/**` (noindex via `app/(shell)/layout.tsx`), `app/attempts/[attemptId]` (noindex), `login`, `offline`, `api/**`.
- There is **no `sitemap.ts`, `robots.ts`, or `metadataBase`** yet.
- The exam facts live in `src/content/exams.ts` (`EXAM_GUIDES`, slugs `kanoon`, `markaz`).

`frontend/src/lib/site.ts` (new)
```ts
export const SITE_URL = (process.env.NEXT_PUBLIC_SITE_URL ?? "https://azmoon.dadrose.com").replace(/\/+$/, "");
/** Date of the last significant content change per static route (update when the content changes, not on deploy). */
export const STATIC_LASTMOD: Record<string, string> = {
  "/": "2026-10-01",        // placeholder: set from git log of (public)/page.tsx at build time
  "/guide": "2026-10-01",   // placeholder: or from max(updatedAt) of EXAM_GUIDES facts
};
```

`frontend/src/app/sitemap.ts` (new)
```ts
import type { MetadataRoute } from "next";
import { SITE_URL, STATIC_LASTMOD } from "@/lib/site";
import { apiBaseUrl } from "@/lib/env";

export const revalidate = 3600;

type PublicTopic = { topic_key: string; updated_at: string; indexable: boolean };

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const statics: MetadataRoute.Sitemap = Object.entries(STATIC_LASTMOD).map(([path, d]) => ({
    url: `${SITE_URL}${path === "/" ? "" : path}`,
    lastModified: d,                      // real content date, never new Date()
  }));
  // Future public topic pages (/topics/[topicKey]); only those with unique content are indexable.
  let topics: PublicTopic[] = [];
  try {
    const r = await fetch(`${apiBaseUrl()}/api/v1/public/topics`, { next: { revalidate: 3600 } });
    if (r.ok) topics = await r.json();
  } catch { /* backend down: still serve statics */ }
  return [
    ...statics,
    ...topics.filter((t) => t.indexable).map((t) => ({
      url: `${SITE_URL}/topics/${encodeURIComponent(t.topic_key)}`,
      lastModified: t.updated_at,
    })),
  ];
}
```
If it ever exceeds 50,000 URLs: move to `app/topics/sitemap.ts` with `generateSitemaps()` and `const id = await props.id` (v16 promise). List each `/topics/sitemap/<id>.xml` in `robots.ts` (or add an index via `app/sitemap-index.xml/route.ts` returning `<sitemapindex>`), and submit each to GSC.

`frontend/src/app/robots.ts` (new)
```ts
import type { MetadataRoute } from "next";
import { SITE_URL } from "@/lib/site";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [{ userAgent: "*", allow: "/", disallow: ["/app/", "/api/", "/login", "/offline"] }],
    sitemap: [`${SITE_URL}/sitemap.xml`],
    host: SITE_URL,
  };
}
```
Caveat: `Disallow` stops crawling, so Google can't see `noindex` on those paths. That is fine for `/app/` (behind login, redirects via `src/proxy.ts`). Keep the existing `robots: { index: false }` metadata as well. Do **not** disallow pages you need de-indexed while they are still indexed. Remove them via noindex first.

`frontend/src/app/layout.tsx` (edit): add `metadataBase: new URL(SITE_URL)` to the existing `metadata`, so canonicals and OG URLs resolve. Add `alternates: { canonical: "/" }` in `(public)/page.tsx` and `alternates: { canonical: "/guide" }` in `(public)/guide/page.tsx`. Also add `robots: { index: false }` to `login/page.tsx` and `offline/page.tsx`.

JSON-LD component `frontend/src/components/seo/json-ld.tsx` (new). It is CSP-safe, because `application/ld+json` is a data block and is not executed. The existing CSP's `'unsafe-inline'` would allow it anyway.
```tsx
export function JsonLd({ data }: { data: Record<string, unknown> | Record<string, unknown>[] }) {
  return (
    <script
      type="application/ld+json"
      // escape "<" to prevent </script> injection from content strings
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, "\\u003c") }}
    />
  );
}
```
Use in `(public)/guide/page.tsx`. Only mark up what is visible. Exam dates come from `EXAM_GUIDES` (`examDate.verified` flag); unverified facts should not be asserted in markup.
```tsx
import { JsonLd } from "@/components/seo/json-ld";
import { SITE_URL } from "@/lib/site";
// inside the component's JSX:
<JsonLd data={[
  { "@context": "https://schema.org", "@type": "BreadcrumbList", itemListElement: [
    { "@type": "ListItem", position: 1, name: "دادرز", item: SITE_URL },
    { "@type": "ListItem", position: 2, name: "راهنمای آزمون‌های وکالت", item: `${SITE_URL}/guide` } ] },
  { "@context": "https://schema.org", "@type": "WebPage", name: "راهنمای آزمون‌های وکالت ۱۴۰۵",
    inLanguage: "fa", url: `${SITE_URL}/guide`,
    isPartOf: { "@type": "WebSite", name: "دادرز", url: SITE_URL },
    publisher: { "@type": "Organization", name: "دادرز", url: "https://dadrose.com" } },
]} />
```
On the home page, add `Organization` + `WebSite` (with `sameAs` → dadrose.com and book.dadrose.com).

Do **not** add `Event` markup for the exam dates unless the page is the event's authoritative page and the dates are verified. Do not add `FAQPage` unless a visible FAQ exists.

IndexNow key on azmoon: `frontend/public/<KEY>.txt` (static).

Django on publish/unpublish of a public topic: `transaction.on_commit(lambda: enqueue_indexnow([url]))`. A management command `python manage.py indexnow_flush` runs every few minutes from cron.

---

## 7. Phased rollout

### Week 1 — foundations (no content generation yet)

| Task | Who |
|---|---|
| Verify GSC: 3 URL-prefix properties + Domain property `sc-domain:dadrose.com` (DNS TXT) | **Owner** (DNS access) |
| GCP project, enable APIs, service account; add SA e-mail as Full user in each GSC property; GA4 Viewer | **Owner** creates/approves; developer configures. Confirm GCP account eligibility (§6.2 step 6) |
| Check both WP sites: WP version, SEO plugin (Yoast or Rank Math), sitemap URL, lastmod present, ping-to-Google features off | Developer (needs **WP admin** from owner) |
| Enable IndexNow in the existing SEO plugin, or the "IndexNow" plugin listed by Bing (one sender per site); verify the key file loads | Developer |
| Add `robots.txt` `Sitemap:` lines on all three; submit sitemaps via API | Developer |
| Bing Webmaster Tools: verify, or import from GSC | **Owner** login |
| azmoon: add `sitemap.ts`, `robots.ts`, `metadataBase`, canonical, JSON-LD, noindex on login/offline, IndexNow key | Developer (PR to the rewrite) |
| `seo-ops` repo, SQLite, `gsc_pull.py` with 16-month backfill | Developer |

### Month 1 — monitoring and linking

- Daily: GSC pull, sitemap status, URL Inspection rotating sample, CrUX pull. Weekly crawl (links, schema, robots diff). Uptime monitor. Alerts to Telegram/e-mail.
- First Persian weekly report (GSC + order counts from Woo/Django). Owner reviews the format.
- **Taxonomy:** add `topic_key` to the Django `Topic`; expose `/api/v1/taxonomy`. Register the `dadrose_topic` taxonomy on both WP sites (small mu-plugin); sync. Editors tag the top 100 pages by clicks first.
- **GA4:** one property across subdomains, cookie domain plus referral exclusions. Decide the azmoon CSP option (§5.2). Implement `sign_up`/`purchase` (Measurement Protocol from Django recommended).
- **Owner provides:** a WP Application Password for a `seo-bot` user (Contributor role) on each WP site; GA4 admin access.

### Quarter — content engine and recommendations

- Claude brief → draft → `pending` pipeline with the guardrails (§3.2). Start with **refreshes** of decaying and striking-distance pages before any new pages (lower risk, faster KPI signal).
- Legal reviewer workflow and byline/reviewer markup.
- **Recommendation API** on azmoon results (`/attempts/<id>/recommendations`) + `CrossContent` index. Related-content blocks on WP (shortcode/block) and azmoon public pages. Report CTR of `internal_promo_click` → signup/purchase by topic.
- Public azmoon topic pages (`/topics/[topicKey]`) **only where search intent exists** (GSC/keyword evidence) and unique value exists (sample questions, explanations, aggregate stats with date range).
- "Law changed" feed from azmoon → refresh tickets for dadrose articles.
- Quarterly review: indexation rate per template, KPI per topic, decide whether to move to BigQuery.

### What only the owner can do or approve

1. DNS/GSC verification and adding the service account to GSC and GA4.
2. Creating the GCP project and billing (and confirming eligibility); the Anthropic account in a supported region.
3. WP admin access and Application Passwords (Contributor `seo-bot` user).
4. Choosing the azmoon analytics approach (CSP rule vs. Measurement Protocol).
5. Approving each publish (pending → publish), and naming the legal reviewer(s).
6. Setting tunable thresholds and the weekly draft cap.

---

## 8. Verified facts register (all checked 2026-10-13)

| Fact | Value | Source |
|---|---|---|
| Search Analytics quota | 1,200 QPM/site; 1,200 QPM/user; 40,000 QPM & 30,000,000 QPD/project; plus load quotas | https://developers.google.com/webmaster-tools/limits |
| URL Inspection quota | 2,000 QPD & 600 QPM per site; 10,000,000 QPD & 15,000 QPM per project | same |
| Other GSC resources | 20 QPS & 200 QPM per user; 100,000,000 QPD per project | same |
| Search Analytics rows | rowLimit max 25,000/page; ≤50,000 rows/day/search type exposed; data typically after 2–3 days | https://developers.google.com/webmaster-tools/v1/searchanalytics/query ; https://developers.google.com/webmaster-tools/v1/how-tos/all-your-data |
| URL Inspection | read-only status of indexed version; no indexing request | https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect |
| Sitemaps submit | PUT, no body, `webmasters` scope | https://developers.google.com/webmaster-tools/v1/sitemaps/submit |
| Sitemap limits | 50 MB uncompressed / 50,000 URLs; lastmod used only if accurate; priority/changefreq ignored | https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap |
| Ping endpoint | deprecated (June 2023) | https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping |
| Indexing API | only JobPosting / BroadcastEvent-in-VideoObject; default 200 quota for onboarding/testing; approval needed; spam detection | https://developers.google.com/search/apis/indexing-api/v3/quickstart ; …/using-api |
| IndexNow | ≤10,000 URLs/POST; key 8–128 chars; participants Bing, Yandex, Seznam, Naver, Yep, Internet Archive, Amazonbot; Google not listed | https://www.indexnow.org/documentation ; /faq ; /searchengines.json |
| CrUX API | 150 queries/min/project, not raisable; 28-day rolling; daily ~04:00 UTC | https://developer.chrome.com/docs/crux/api |
| PSI v5 | key optional, recommended; strategy MOBILE/DESKTOP; categories incl. PERFORMANCE, SEO | https://developers.google.com/speed/docs/insights/rest/v5/pagespeedapi/runpagespeed |
| Next.js sitemap | `generateSitemaps` → `/…/sitemap/[id].xml`; v16: `id` is a Promise | https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap |
| WP core sitemap | `/wp-sitemap.xml`, 2,000 entries/sub-sitemap (filterable); lastmod added later in core (changeset 56985) | https://make.wordpress.org/core/2020/07/22/new-xml-sitemaps-functionality-in-wordpress-5-5/ ; https://core.trac.wordpress.org/changeset/56985 |
| WP REST | POST /wp/v2/posts; status publish/future/draft/pending/private; App Passwords since 5.6 | https://developer.wordpress.org/rest-api/reference/posts/ ; https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/ |
| Scaled content abuse / gen-AI | definitions and fact-check requirement | https://developers.google.com/search/docs/essentials/spam-policies ; https://developers.google.com/search/docs/fundamentals/using-gen-ai-content |
| GA4 subdomains | cross-domain setup recommended for subdomains; same cookie domain; exclude self-referrals | https://support.google.com/analytics/answer/10071811 |
| GitHub Actions schedule | min 5 min; UTC default; may be delayed; disabled after 60 days inactivity in public repos | https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule |
| Claude API availability | Iran not in supported countries list | https://www.anthropic.com/supported-countries |

**Not verified in this pass, to check before building:**
- the GSC BigQuery bulk-export details;
- the GA4 Measurement Protocol payload/limits;
- the PSI daily quota (see Cloud console);
- Rank Math/Yoast IndexNow current tier (free vs premium); secondary sources only;
- Google Cloud eligibility for the owner's country;
- the WooCommerce default Product schema output.
