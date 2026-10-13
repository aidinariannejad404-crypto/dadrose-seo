# 06: GitHub repos for SEO, AEO and GEO automation (dadrose)

**Checked:** 2026-10-13. This is an evaluation only. Nothing was installed.
**Sites:** dadrose.com (WordPress: articles and courses), book.dadrose.com (WooCommerce), azmoon.dadrose.com (Next.js 16 + Django).

## How the data was collected
- The GitHub REST API (`api.github.com`) was rate-limited for this session after two calls. Only **schema-dts** and **lighthouse-ci** have exact API values (stars, `pushed_at`, open issues).
- Every other star, fork and issue count comes from the public github.com repo page on 2026-10-13. GitHub rounds these on the page ("1.5k"), so they are approximate.
- GitHub pages did not show last-commit dates. In their place, the **latest package release date** is taken from the PyPI or npm registry JSON, labeled "rel". That date shows when the code last shipped. It is not the push date.
- "n/a" means the value was not available. No number here is estimated.

---

## Summary table

| # | Repo | Purpose | Stars | Latest activity | License | Verdict |
|---|------|---------|-------|-----------------|---------|---------|
| 1 | google/schema-dts | TypeScript types for Schema.org JSON-LD | 1,246 (API) | push 2026-09-25; npm 2.1.0 rel 2026-10-02 | Apache-2.0 | **Recommend** |
| 2 | GoogleChrome/lighthouse-ci | Lighthouse on every commit, with budgets | 7,072 (API) | push 2026-03-27; @lhci/cli 0.15.1 rel 2025-06-25 | Apache-2.0 | **Recommend** |
| 3 | treosh/lighthouse-ci-action | GitHub Action wrapper for LHCI | ~1.3k | n/a (uses Lighthouse 12.6) | MIT | **Recommend** |
| 4 | GoogleChrome/web-vitals | Real-user CWV measurement (LCP, INP, CLS) | ~8.6k | npm 6.2.3 rel 2026-10-05 | Apache-2.0 | **Recommend** |
| 5 | harlan-zw/unlighthouse | Lighthouse across a whole site | ~4.9k | npm 0.19.1 rel 2026-10-03 | MIT | **Recommend** |
| 6 | eliasdabbas/advertools | Python SEO toolkit: crawler, sitemaps, robots, logs | ~1.5k | PyPI 0.18.0 rel 2026-06-17 | MIT | **Recommend** |
| 7 | AminForou/mcp-gsc | GSC MCP server: analytics, URL inspection, sitemaps | ~1.3k | changelog 0.3.3 (Jul 2026) | MIT | **Recommend** |
| 8 | joshcarty/google-searchconsole | Python wrapper for the GSC Search Analytics API | 254 | PyPI 0.1.0 rel 2025-11-15 | MIT | **Recommend** |
| 9 | roshan-research/hazm | Persian NLP: normalizer, ZWNJ, lemmatizer | ~1.4k | PyPI 0.12.1 rel 2026-04-01 | MIT | **Recommend** |
| 10 | huggingface/sentence-transformers | Multilingual embeddings for clustering and internal links | ~19.2k | PyPI 6.1.0 rel 2026-09-18 | Apache-2.0 | **Recommend** |
| 11 | MaartenGr/BERTopic | Topic and keyword clustering (multilingual) | ~7.8k | PyPI 0.17.4 rel 2025-12-03 | MIT | **Recommend** |
| 12 | scrapinghub/extruct | Pulls JSON-LD, microdata and OG from HTML for schema QA | 972 | PyPI 0.18.0 rel 2024-11-08 | BSD-3 | **Recommend** |
| 13 | StJudeWasHere/seonaut | Self-hosted SEO crawler and audit dashboard (Go) | 763 | n/a | MIT | **Recommend** |
| 14 | AgriciDaniel/claude-seo | Claude Code SEO skill suite (audit, schema, GEO, GSC) | ~15.1k | changelog v2.2.5 (Aug 2026) | MIT | **Recommend** (review first) |
| 15 | AnswerDotAI/llms-txt | The llms.txt spec and reference tooling | ~2.6k | spec modified 2026-08-10 | Apache-2.0 | **Recommend** (as spec) |
| 16 | WordPress/mcp-adapter | Official WP Abilities API to MCP bridge | ~1.6k | n/a (v0.5.0 guide linked) | GPL-2.0+ | Maybe |
| 17 | google/site-kit-wp | Official Google plugin: GSC, GA4, PSI inside WP | ~1.4k | n/a | Apache-2.0 | Maybe |
| 18 | persian-tools/persian-tools | JS Persian utilities (digits, Arabic chars) | n/a (page failed) | npm 4.0.4 rel 2025-09-30 | MIT | Maybe |
| 19 | ICTRC/Parsivar | Persian preprocessing, spell check | 248 | PyPI 0.2.3.1 rel 2024-01-02 | MIT | Maybe |
| 20 | garmeeh/next-seo | Next.js SEO and JSON-LD components | ~8.5k | npm 7.3.0 rel 2026-07-29 | MIT | Maybe |
| 21 | iamvishnusankar/next-sitemap | Next.js sitemap generator | ~3.7k | npm 4.2.3 rel **2023-09-06** | MIT | Maybe / lean Avoid |
| 22 | PhialsBasement/LibreCrawl | Screaming-Frog-like crawler with JS rendering | ~1.0k | no releases | MIT | Maybe |
| 23 | zubair-trabzada/geo-seo-claude | Claude Code GEO skill (citability, llms.txt) | ~9.1k | no releases | MIT | Maybe |
| 24 | ahonn/mcp-server-gsc | Minimal GSC MCP (one search_analytics tool) | 261 | npm 0.3.0 rel 2026-02-13 | MIT | Maybe |
| 25 | every-app/open-seo | Self-hosted Semrush-like tool on DataForSEO | ~23.2k | n/a | MIT | Maybe |
| 26 | ai-search-guru/getcito-… | Self-hosted AI-visibility tracker (Elmo fork) | 413 | n/a | MIT | Maybe (with caveats) |
| 27 | sethblack/python-seo-analyzer | Basic crawler and on-page analyzer | ~1.5k | PyPI pyseoanalyzer 2025.4.3 rel 2025-04-03 | n/a on page | Avoid (superseded) |
| 28 | danishashko/geo-aeo-tracker | AI-visibility dashboard | 252 | 29 commits | MIT | Avoid |
| 29 | limelitgeo/open | Self-hosted AI-visibility tracker (Go) | 1 | pre-release | Apache-2.0 | Avoid (too early) |
| 30 | goenning/google-indexing-script | Bulk-submits URLs to Google Indexing API | ~7.7k | n/a | MIT | **Avoid** (policy) |
| 31 | ajitjasrotia/indexnow | Python IndexNow client | 6 | PyPI 0.9.9 rel 2023-08-05 | MIT | Avoid (trivial, stale) |
| 32 | firecrawl/llmstxt-generator | Hosted llms.txt generator | 539 | deprecated after 2025-06-30 | n/a | Avoid (deprecated) |
| 33 | aaron-he-zhu/seo-geo-claude-skills | Claude SEO skills (frozen signpost) | 86 | v9.9.12 (2026-06-28) | Apache-2.0 | Avoid (frozen) |
| 34 | glitchdigital/structured-data-testing-tool | CLI structured-data tester | n/a | npm 4.5.0 rel **2020-03-11** | ISC | Avoid (stale) |
| 35 | oneglanse/oneglanse | AI-visibility via real product UIs | n/a (page failed) | n/a | MIT (per search) | Avoid (UI automation, ToS) |

---

## Per-repo details

### 1. google/schema-dts: Recommend
- **URL:** https://github.com/google/schema-dts
- **What it does:** TypeScript types for the whole Schema.org vocabulary. Wrong JSON-LD (for example, a typo in `Course` or `Quiz` properties) fails at compile time.
- **Numbers (API):** 1,246 stars, last push 2026-09-25, 14 open issues, not archived, Apache-2.0. npm 2.1.0 released 2026-10-02.
- **Credibility:** Google organization. Types only, with no runtime code and no credentials.
- **Fit:** azmoon (Next.js 16). Types JSON-LD for `Quiz`, `Course`, `FAQPage`, `BreadcrumbList`, `Organization` and `LegalService` rendered through the native Metadata API and `<script type="application/ld+json">`.

### 2. GoogleChrome/lighthouse-ci: Recommend
- **URL:** https://github.com/GoogleChrome/lighthouse-ci
- **What it does:** Runs Lighthouse on each commit or deploy, compares results to a baseline, and fails builds on regressions through performance budgets.
- **Numbers (API):** 7,072 stars, last push 2026-03-27, 234 open issues, not archived, Apache-2.0. @lhci/cli 0.15.1 released 2025-06-25.
- **Risk:** The release cadence has slowed. The 234 open issues are a large backlog, but the project is official Chrome tooling. It needs no credentials unless you self-host the LHCI server.
- **Fit:** azmoon CI (GitHub Actions). It can also run scheduled checks on key dadrose.com and book pages.

### 3. treosh/lighthouse-ci-action: Recommend
- **URL:** https://github.com/treosh/lighthouse-ci-action
- **What it does:** A one-file GitHub Action that runs LHCI against a list of URLs, applies budgets, and uploads reports.
- **Numbers:** ~1.3k stars, 31 open issues, MIT. The README says it uses Lighthouse 12.6. Release date was not shown.
- **Credibility:** treosh is a known web-performance team and the de-facto standard LHCI action.
- **Fit:** The easiest way to run #2 in CI.

### 4. GoogleChrome/web-vitals: Recommend
- **URL:** https://github.com/GoogleChrome/web-vitals
- **What it does:** A ~3 KB library that measures LCP, INP, CLS, FCP and TTFB on real users, the same way CrUX does. Its attribution build identifies the element that causes a poor score.
- **Numbers:** ~8.6k stars, 12 open issues, Apache-2.0. npm 6.2.3 released 2026-10-05.
- **Fit:** All three sites. Real-user metrics go to GA4 or a Django endpoint for Core Web Vitals (CWV) monitoring. Next.js also has a built-in `useReportWebVitals`.

### 5. harlan-zw/unlighthouse: Recommend
- **URL:** https://github.com/harlan-zw/unlighthouse
- **What it does:** Crawls a site and runs Lighthouse on every URL, with smart sampling and a UI (`npx unlighthouse --site`).
- **Numbers:** ~4.9k stars, 21 open issues, MIT. npm 0.19.1 released 2026-10-03. Requires Node 22.18 or newer.
- **Credibility:** Harlan Wilton, a well-known Nuxt SEO maintainer. Very active.
- **Fit:** Monthly whole-site performance and SEO audits of all three sites. claude-seo can use it as an extension.

### 6. eliasdabbas/advertools: Recommend
- **URL:** https://github.com/eliasdabbas/advertools
- **What it does:** A Python toolkit with a Scrapy-based SEO crawler (titles, headers, status codes, links, custom selectors), a sitemap downloader and parser that handles indexes, robots.txt to DataFrame, log-file parsing, and crawl analytics.
- **Numbers:** ~1.5k stars, 5 open PRs, MIT. PyPI 0.18.0 released 2026-06-17.
- **Credibility:** Elias Dabbas, a long-standing SEO data author. 1,528 commits.
- **Risk:** The `serp` module calls Google through an API (the Custom Search JSON API, per its docs). Use only that official path and do not scrape. The crawler respects robots.txt settings, so crawl only your own sites.
- **Fit:** Sitemap validation for WordPress and Next.js, and technical crawls. It is the data layer for internal-link and duplicate-title reports.

### 7. AminForou/mcp-gsc: Recommend
- **URL:** https://github.com/AminForou/mcp-gsc
- **What it does:** An MCP server that gives Claude access to Google Search Console (GSC). It covers search analytics, period comparisons, page-and-query breakdowns, URL Inspection (single and batch), indexing-issue checks, and listing or submitting sitemaps.
- **Numbers:** ~1.3k stars, 183 forks, MIT. Changelog runs from 0.1.0 to 0.3.3 (July 2026). No GitHub releases.
- **Credibility:** Amin Foroutan, a known SEO practitioner. He also sells a hosted version.
- **Security:**
  - It needs OAuth or a service-account JSON.
  - Destructive tools are off by default (`GSC_ALLOW_DESTRUCTIVE`). Keep them off.
  - HTTP/SSE mode has no auth, so run it in local stdio mode only.
  - The `curl | sh` uv install is optional. Clone and review instead.
  - The PyPI name `mcp-gsc` (0.1.0, 2025-09-02) is published under the "aminfseo" GitHub URL. Install from the GitHub repo, not PyPI, unless ownership is confirmed.
- **Fit:** Day-to-day GSC reporting and URL Inspection monitoring for all three properties from Claude Code.

### 8. joshcarty/google-searchconsole: Recommend
- **URL:** https://github.com/joshcarty/google-searchconsole
- **What it does:** A small Python wrapper for GSC Search Analytics, with date ranges, dimensions, filters and export to a pandas DataFrame.
- **Numbers:** 254 stars, 2 open issues, MIT. PyPI `searchconsole` 0.1.0 released 2025-11-15 by Josh Carty.
- **Risk:** Uses OAuth. The scope is small, so it is easy to audit.
- **Fit:** Scheduled scripted pulls (cron or GitHub Action) into CSV or BigQuery for weekly reports. For URL Inspection, call the official `searchconsole` v1 API directly or use #7.

### 9. roshan-research/hazm: Recommend
- **URL:** https://github.com/roshan-research/hazm
- **What it does:** Persian NLP covering normalization (ZWNJ correction, diacritics and tatweel removal), tokenization, lemmatization, POS tagging and embeddings.
- **Numbers:** ~1.4k stars, 4 open issues, MIT. PyPI 0.12.1 released 2026-04-01. Requires Python 3.12 or newer.
- **Credibility:** Roshan (an Iranian AI company). The de-facto Persian NLP library.
- **Note:** The repo page did not explicitly mention ي→ی and ك→ک mapping. Verify it with a quick test, and if it is missing, add a two-line `str.translate` step.
- **Fit:** Keyword normalization before clustering and deduplication of GSC queries. Persian query variants (half-space and Arabic letters) otherwise split metrics.

### 10. huggingface/sentence-transformers: Recommend
- **URL:** https://github.com/huggingface/sentence-transformers
- **What it does:** Sentence and document embeddings, with pretrained models for more than 100 languages (multilingual-e5, LaBSE and others).
- **Numbers:** ~19.2k stars, Apache-2.0. PyPI 6.1.0 released 2026-09-18. Maintained by Hugging Face (originally UKP Lab).
- **Fit:**
  - Semantic keyword clustering of GSC queries.
  - Internal-link suggestions (article-to-article and article-to-book cosine similarity).
  - Cannibalization detection.
  - Runs locally, so no data leaves the server.

### 11. MaartenGr/BERTopic: Recommend
- **URL:** https://github.com/MaartenGr/BERTopic
- **What it does:** Topic modeling on top of embeddings. It groups thousands of queries or articles into labeled topics. `language="multilingual"` covers more than 50 languages.
- **Numbers:** ~7.8k stars, 437 open issues, MIT. PyPI 0.17.4 released 2025-12-03.
- **Fit:** Builds the topic and cluster map for legal articles and courses (pillar and cluster planning) and for content gaps.

### 12. scrapinghub/extruct: Recommend
- **URL:** https://github.com/scrapinghub/extruct
- **What it does:** Extracts JSON-LD, microdata, RDFa, OpenGraph and microformats from HTML.
- **Numbers:** 972 stars, 40 open issues, BSD-3-Clause. PyPI 0.18.0 released 2024-11-08 (stable, slow cadence).
- **Credibility:** Zyte (formerly Scrapinghub).
- **Fit:** Automated schema QA across all three sites. For example, every WooCommerce product page must have `Product` + `Offer`, and every article must have `Article`/`BreadcrumbList`. Pair with the Google Rich Results Test for spot checks.

### 13. StJudeWasHere/seonaut: Recommend
- **URL:** https://github.com/StJudeWasHere/seonaut
- **What it does:** A self-hosted SEO crawler with a dashboard. It finds broken links, redirect chains and loops, missing or duplicate meta tags, and heading-order issues, ranked by severity.
- **Numbers:** 763 stars, 8 open issues, MIT. Go + MySQL. Docker image on ghcr.io.
- **Risk:** JavaScript rendering is not documented. That is fine for WordPress and WooCommerce. For azmoon, rely on server-side rendering (SSR) output.
- **Fit:** A free, recurring technical audit similar to Screaming Frog for dadrose.com and book.

### 14. AgriciDaniel/claude-seo: Recommend (review the code first)
- **URL:** https://github.com/AgriciDaniel/claude-seo
- **What it does:** A Claude Code plugin with 25 sub-skills, including:
  - audit, technical, content and `content-brief`
  - `schema`, `geo`, `sitemap`, `hreflang` and `ecommerce`
  - `cluster`, `drift`
  - `google` (GSC, PSI, CrUX, Indexing, GA4 reports)
- **Numbers:** ~15.1k stars, ~2.2k forks, 17 open issues, MIT. Changelog reaches v2.2.5 (August 2026).
- **Security:**
  - Credentials are stored with 0600 permissions under `~/.config/claude-seo`.
  - The changelog records fixed SSRF and credential-injection bugs, which is good transparency, and there is a secret-scan CI gate.
  - The uninstall step is `curl | bash`. Avoid it and clone and review instead.
  - Optional paid extensions are DataForSEO, Ahrefs and SE Ranking.
  - Its "Indexing" feature must not be used to push normal pages (see #30).
- **Fit:** Interactive audits, content briefs and schema drafts for all sites. Overlaps with #7.

### 15. AnswerDotAI/llms-txt: Recommend (as the spec)
- **URL:** https://github.com/AnswerDotAI/llms-txt
- **What it does:** The original `/llms.txt` proposal (Jeremy Howard / Answer.AI) plus a Python reference implementation.
- **Numbers:** ~2.6k stars, 74 open issues, Apache-2.0. Spec date-modified is 2026-08-10.
- **Fit:** Defines the llms.txt format. For dadrose, generate the file from your own sitemap with a small script, or from Next.js `app/llms.txt/route.ts`, rather than with a third-party crawler service. Its GEO benefit is unproven, so treat it as low-cost and low-priority.

### 16. WordPress/mcp-adapter: Maybe
- **URL:** https://github.com/WordPress/mcp-adapter
- **What it does:** The official WordPress project that exposes Abilities API abilities as MCP tools, so Claude can read and update WP content (for example, adding internal links or meta).
- **Numbers:** ~1.6k stars, 41 open issues, GPL-2.0+. Requires WordPress 6.9 or newer.
- **Risk:** Write access to the live site. Use Application Passwords for a least-privilege editor user, never admin, and test on staging first.
- **Fit:** Later phase, applying approved internal-link and meta edits to dadrose.com and book.

### 17. google/site-kit-wp: Maybe
- **URL:** https://github.com/google/site-kit-wp
- **What it does:** Google's official WP plugin that shows GSC, GA4 and PageSpeed data in wp-admin.
- **Numbers:** ~1.4k stars, 548 open issues, Apache-2.0.
- **Fit:** Convenient dashboards for editors. It adds no automation and adds plugin weight. Skip it if GA4 and GSC are already linked elsewhere.

### 18. persian-tools/persian-tools: Maybe
- **URL:** https://github.com/persian-tools/persian-tools
- **What it does:** A JavaScript/TypeScript collection of Persian utilities: digit conversion, Arabic-to-Persian characters and more.
- **Numbers:** The GitHub page failed to load, so stars are n/a. npm `@persian-tools/persian-tools` 4.0.4 released 2025-09-30, MIT.
- **Fit:** Search-input and slug normalization on azmoon (Next.js) so search and URLs are consistent.

### 19. ICTRC/Parsivar: Maybe
- **URL:** https://github.com/ICTRC/Parsivar
- **What it does:** Persian normalizer with half-space correction, digit and date normalization, Pinglish conversion and spell check.
- **Numbers:** 248 stars, 26 open issues, MIT. PyPI 0.2.3.1 released 2024-01-02.
- **Risk:** The spell-check resources are downloaded from Dropbox. Python 2.7-era code.
- **Fit:** A backup or complement to hazm for spell-variant merging. Use hazm first.

### 20. garmeeh/next-seo: Maybe
- **URL:** https://github.com/garmeeh/next-seo
- **What it does:** SEO and JSON-LD React components for Next.js, with an App Router example.
- **Numbers:** ~8.5k stars, MIT. npm 7.3.0 released 2026-07-29.
- **Fit:** Next.js 16 already has a native Metadata API, `sitemap.ts` and `robots.ts`. Adding schema-dts with hand-written JSON-LD avoids a dependency. Use next-seo only if you want its ready-made JSON-LD components.

### 21. iamvishnusankar/next-sitemap: Maybe, lean Avoid
- **URL:** https://github.com/iamvishnusankar/next-sitemap
- **What it does:** Generates sitemaps and robots.txt for Next.js after build.
- **Numbers:** ~3.7k stars, 2 open issues, MIT. The **last npm release, 4.2.3, was on 2023-09-06**.
- **Fit:** Prefer native `app/sitemap.ts` with `generateSitemaps()` for large exam sets in Next.js 16. Use this package only if multi-file index generation becomes painful.

### 22. PhialsBasement/LibreCrawl: Maybe
- **URL:** https://github.com/PhialsBasement/LibreCrawl
- **What it does:** A Flask web crawler with Playwright JavaScript rendering, issue detection, PageSpeed integration, and CSV, XLSX and JSON export.
- **Numbers:** ~1.0k stars, 211 forks, 17 open issues, MIT. ~109 commits, no releases. Individual maintainer.
- **Fit:** JavaScript-rendered crawls of azmoon if SEOnaut is not enough. Still young.

### 23. zubair-trabzada/geo-seo-claude: Maybe
- **URL:** https://github.com/zubair-trabzada/geo-seo-claude
- **What it does:** A Claude Code skill set for GEO audits (`/geo citability`, `crawlers`, `llmstxt`, `schema` and `report-pdf`).
- **Numbers:** ~9.1k stars, 14 open issues, MIT. Only 72 commits and no releases.
- **Risk:** The installer pipes `curl | bash`, and the README promotes a paid community. It overlaps with claude-seo's `geo` skill.
- **Fit:** Optional GEO checklists. Read the code before use.

### 24. ahonn/mcp-server-gsc: Maybe
- **URL:** https://github.com/ahonn/mcp-server-gsc
- **What it does:** A minimal GSC MCP server with one `search_analytics` tool (25k rows, regex filters, "quick wins"). Service-account auth.
- **Numbers:** 261 stars, 1 open issue, MIT. npm 0.3.0 released 2026-02-13.
- **Fit:** A smaller-surface alternative to #7, but it has no URL Inspection.

### 25. every-app/open-seo: Maybe
- **URL:** https://github.com/every-app/open-seo
- **What it does:** A self-hosted "Semrush alternative" covering keyword research, rank tracking, backlinks, audits, AI visibility, and an MCP server and skills.
- **Numbers:** ~23.2k stars, ~3.0k forks, 102 open issues, 142 open PRs, MIT.
- **Risk:** All data comes from **DataForSEO, a paid service**, using your own key. DataForSEO supplies SERP data from its own collection, so Google ToS exposure sits with that vendor. Coverage of the Persian/Iran market should be checked before paying.
- **Fit:** Keyword research and rank tracking, if a DataForSEO budget is approved.

### 26. ai-search-guru/getcito: Maybe (with caveats)
- **URL:** https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool
- **What it does:** A self-hosted tracker of brand mentions and citations in ChatGPT, Perplexity, Gemini and Google AI Overviews and AI Mode (a fork of Elmo).
- **Numbers:** 413 stars, 41 commits, MIT.
- **Risk:**
  - It uses **scraper vendors** (BrightData, Oxylabs and others) for consumer AI UIs and Google AI Overviews. That is a ToS grey area.
  - Telemetry is on by default.
  - `.env.local` is in the repo listing.
  - Its "world's first" claim is marketing.
- **Fit:** GEO tracking only if run in API-only mode (OpenAI, Anthropic and Perplexity APIs with web search). A simpler alternative is a home-grown script that sends 50 to 100 Persian legal questions to the official APIs each week and logs whether dadrose.com is cited.

### 27. sethblack/python-seo-analyzer: Avoid
- ~1.5k stars. PyPI `pyseoanalyzer` 2025.4.3 released 2025-04-03.
- The author points to a successor, and the README references an old Claude model.
- advertools and SEOnaut cover the same ground better.

### 28. danishashko/geo-aeo-tracker: Avoid
- 252 stars, 29 commits.
- All live data comes through Bright Data's AI-UI scraping, a paid ToS grey area, and the README is heavy with vendor promotion.

### 29. limelitgeo/open: Avoid
- 1 star, pre-release, and the open core of a commercial product.
- Revisit in 2027.

### 30. goenning/google-indexing-script: Avoid (Google policy)
- ~7.7k stars, MIT.
- It submits URLs to the **Google Indexing API, which Google allows only for `JobPosting` and `BroadcastEvent` pages**. The README states this limit.
- Using it for legal articles, books or exams breaks the API's terms and risks losing access.
- Use sitemaps, GSC URL Inspection "Request indexing" by hand for priority URLs, and IndexNow for Bing and Yandex.

### 31. ajitjasrotia/indexnow: Avoid
- 6 stars, 1 commit. PyPI 0.9.9 released 2023-08-05.
- IndexNow is a single HTTP POST (`api.indexnow.org/indexnow` with key, host and urlList), so write that request in Django or Next.js yourself.
- For WordPress, use the official IndexNow plugin on wordpress.org (Microsoft Bing team), or the built-in IndexNow in Rank Math or Yoast.

### 32. firecrawl/llmstxt-generator: Avoid
- 539 stars.
- The README says it is deprecated and no longer maintained after 2025-06-30, and it requires Firecrawl, OpenAI and Supabase keys.

### 33. aaron-he-zhu/seo-geo-claude-skills: Avoid
- 86 stars.
- It is a frozen "signpost" repo (v9.9.12, 2026-06-28), and development has moved to another bundle.

### 34. glitchdigital/structured-data-testing-tool: Avoid
- The last npm release, 4.5.0, was on 2020-03-11.
- Use extruct plus the Google Rich Results Test, or the schema.org validator, instead.

### 35. oneglanse/oneglanse: Avoid
- The GitHub page failed to load, so numbers are n/a.
- Its own description (from search results) says it monitors AI answers "through real product UIs", which means automating consumer ChatGPT, Gemini and AI Overviews interfaces. That conflicts with those products' terms.

### Gap: internal-linking tools
No credible, maintained open-source internal-link suggester turned up; search results were mostly SaaS products or thin skills. The best approach is a short in-house script that combines four pieces:
1. advertools crawl (existing links and anchors)
2. hazm normalization
3. sentence-transformers (multilingual-e5) similarity between pages
4. Suggested links plus Persian anchor text, reviewed by a person and then applied via WP mcp-adapter or by hand

---

## Policy flags
- **Google Indexing API for non-job pages** (goenning/google-indexing-script, and any "instant indexing" plugin or skill that uses it): against Google's terms. Do not use.
- **SERP and AI-UI scraping** (getcito scraper mode, geo-aeo-tracker via Bright Data, oneglanse, DataForSEO-backed tools): the scraping is done by third-party vendors, which is a ToS grey area for Google and the AI products. Prefer official APIs: GSC API, the Custom Search JSON API, and the OpenAI, Anthropic, Perplexity and Gemini APIs with search grounding.
- **No link-building automation** was evaluated or recommended.
- **Credentials:** GSC and GA4 service-account JSONs, WP application passwords and LLM keys should live in a secrets manager or GitHub Actions secrets, never in repos. Use read-only GSC scopes where possible.

---

## Recommended stack (by pipeline step)

| Pipeline step | dadrose.com (WP) | book.dadrose.com (Woo) | azmoon (Next.js 16 + Django) | Repos |
|---|---|---|---|---|
| **Indexing** | Rank Math/Yoast sitemap + official IndexNow WP plugin | same | native `app/sitemap.ts` (+`generateSitemaps`) + own IndexNow POST from Django on publish | advertools (sitemap validation); *avoid* google-indexing-script |
| **Monitoring (GSC)** | weekly pull + URL Inspection on top pages | same | same | mcp-gsc (interactive), google-searchconsole (scheduled) |
| **Monitoring (CWV)** | web-vitals RUM to GA4 | same | `useReportWebVitals` / web-vitals | web-vitals, lighthouse-ci + treosh action (CI), unlighthouse (monthly whole-site) |
| **Auditing** | monthly crawl | monthly crawl + Product schema QA | crawl SSR output | SEOnaut (dashboard), advertools (scripted), extruct (schema QA), claude-seo `/seo audit` |
| **Structured data** | Rank Math/Yoast schema + extruct checks | Product/Offer/Book checks | typed JSON-LD | schema-dts, extruct |
| **Content (briefs, clustering)** | cluster GSC queries, then briefs | category/book topics | exam topic hubs | hazm → sentence-transformers → BERTopic; claude-seo `content-brief` |
| **Internal links** | similarity-based suggestions, human-approved | article↔book cross-links | exam↔article links | advertools + sentence-transformers (in-house script); WordPress/mcp-adapter to apply (later) |
| **GEO tracking** | weekly Persian prompt set via official LLM APIs, log citations of dadrose.com | — | — | in-house script (preferred); getcito only in API-only mode; llms.txt per AnswerDotAI spec |
| **Next.js SEO** | — | — | Metadata API + schema-dts; next-seo optional; skip next-sitemap | schema-dts, (next-seo) |
| **Persian normalization** | query/keyword dedupe | search & slugs | search input & slugs | hazm (Python), persian-tools (JS), Parsivar (backup) |

**Suggested first wave (low risk, no paid services):** schema-dts, web-vitals, lighthouse-ci + treosh action, mcp-gsc, advertools, hazm, sentence-transformers, extruct, SEOnaut.
**Second wave:** claude-seo (after reading the code), BERTopic, unlighthouse, WordPress/mcp-adapter (staging first).
**Needs budget decision:** open-seo / DataForSEO, getcito.
