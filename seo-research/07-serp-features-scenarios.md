# 07 — Google SERP features: coverage checklist + win scenarios (dadrose.com · book.dadrose.com · azmoon.dadrose.com)

Checked against official Google documentation on **2026-10-13**. Every status claim cites a URL. Anything not stated by Google is marked **[inferred]**. Anything I could not verify is marked **[unverified]**. No traffic, CTR or volume numbers are given, because none were measured.

Companion files: `04-keyword-map.csv` (queries), `05-automation-pipeline.md` (jobs referenced below as `P-…`), `06-github-repos.md`. AI Overviews / AI Mode / AEO-GEO across other AI engines is covered in depth in its own research file; §2.6 here is the Google-only brief.

---

## 0. Executive summary

### 0.1 Status changes that alter the plan (verified)

| Feature | Status 2026-10-13 | Source |
|---|---|---|
| FAQ rich results | **Gone.** "will no longer appear in Google Search starting May 7, 2026"; docs removed Jun 15 2026 | https://developers.google.com/search/updates |
| Practice problems | **Gone.** Deprecated Nov 5 2025; docs removed Jan 6 2026: "no longer shown in Google Search results" | https://developers.google.com/search/updates |
| Course info | **Gone.** Docs removed Sep 9 2025 with estimated salary, learning video, special announcement, vehicle listing | https://developers.google.com/search/updates ; https://developers.google.com/search/blog/2025/06/simplifying-search-results |
| Learning video | **Gone** (same batch) | same |
| HowTo | **Gone** since Sep 13 2023 (mobile was removed first) | https://developers.google.com/search/blog/2023/08/howto-faq-changes ; https://www.searchenginejournal.com/google-completely-removes-how-to-rich-results/496479/ |
| Sitelinks search box | **Gone** (Nov 2024) | https://developers.google.com/search/blog/2024/10/sitelinks-search-box |
| Book actions | **Kept.** The deprecation banner was removed Nov 5 2025. Limited to onboarded partners "with a wide selection of available books" | https://developers.google.com/search/docs/appearance/structured-data/book |
| Course list | Live, but **English only** ("available in English in all regions") | https://developers.google.com/search/docs/appearance/structured-data/course |
| Education Q&A (flashcards) | Live, but only en, pt, vi (all regions) and es (Mexico). **No Persian** | https://developers.google.com/search/docs/appearance/structured-data/education-qa |
| Event | Live, but physical events only ("Virtual experiences that have no real-world component aren't supported") and only in the listed countries (AU, BR, CA, DE, IN, LatAm, ES, UK, US). **Not Iran, not webinars** | https://developers.google.com/search/docs/appearance/structured-data/event |
| Dataset | Used **only by Dataset Search** (Nov 5 2025 clarification) | https://developers.google.com/search/updates |
| Discussion forum, Q&A | Live. More properties were added Mar 24 2026 | https://developers.google.com/search/updates |
| Discover "Follow" | Removed Nov 19 2025. Its replacements are **Search profiles** and **Preferred sources** | https://developers.google.com/search/docs/appearance/search-profiles ; https://developers.google.com/search/docs/appearance/preferred-sources |
| Search Console Gen-AI report | "Search Generative AI performance reports" announced Jun 2026. It shows impressions for AI Overviews, AI Mode and Discover AI. Launched as a beta for a subset of sites | https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports (body summarized via https://pasqualepillitteri.it/en/news/4116/search-console-generative-ai-report-ai-overviews-ai-mode) |

Current gallery, 25 features: Article, Breadcrumb, Carousel, Course list, Dataset, Discussion forum, Education Q&A, Employer aggregate rating, Event, Image metadata, Job posting, Local business, Math solver, Movie, Organization, Product, Profile page, Q&A, Recipe, Review snippet, Software app, Speakable, Subscription/paywalled content, Vacation rental, Video. Source: https://developers.google.com/search/docs/appearance/structured-data/search-gallery

### 0.2 Iran-specific availability (verified unless marked)

| Item | Status for an Iran-based business | Source |
|---|---|---|
| Google Business Profile | **Not available.** "Business Profile currently does not support businesses in:" lists Iran (OFAC) | https://support.google.com/business/answer/6270107?hl=en |
| Merchant Center: free listings and Shopping ads | **Not available.** Iran is not a supported target country, Persian is not a supported language, IRR is not a supported currency | https://support.google.com/merchants/answer/160637 ; https://support.google.com/merchants/answer/13692890 |
| Google Ads | **Not available.** Advertisers in Iran are blocked and Iran cannot be targeted | https://support.google.com/google-ads/answer/6163740 |
| Google Play Books (sell or pay out) | **Not available.** Iran is not in the supported countries or payments table | https://support.google.com/books/partner/table/6052428 |
| AI Overviews in Persian | **[unverified].** Google's May 2025 expansion says "more than 40 languages" and does not list Persian | https://blog.google/products/search/ai-overview-expansion-may-2025-update/ |
| Google Search and Search Console | Usable for organic search. No sanctions note was found. **[inferred]** | — |
| Google Play Console (publishing a TWA app) | Likely unavailable to Iran-based developers **[inferred, unverified]**. Alternatives: Cafe Bazaar, Myket | — |
| YouTube | Filtered inside Iran by Iranian authorities. Iranian users reach it via VPN **[inferred]**. YouTube monetization for Iranian creators is not possible **[inferred]**. YouTube videos still rank in Google SERPs worldwide | — |

**Consequence.** Product-rich visibility for the bookstore must come from **on-page structured data** (product snippets, merchant-listing markup and review stars), not from Merchant Center. Local visibility must come from Organization/LocalBusiness markup plus Iranian maps (Neshan, Balad), not from GBP. Paid search is impossible, so organic SERP-feature coverage is the whole game.

### 0.3 Priority ranking (impact on signups, sales and brand × effort)

| # | Feature | Site(s) | Impact | Effort | Why |
|---|---|---|---|---|---|
| 1 | Indexable public azmoon pages + blue links/title links/site names | all | H | M | Exams behind login means azmoon has almost no organic surface. This is a prerequisite for every other feature |
| 2 | Featured snippets + People Also Ask | dadrose, azmoon public | H | M | Captures the main informational bar-exam queries. Uses the same answer-first content AI Overviews draws on |
| 3 | Product snippets / merchant-listing markup + review stars (books) | book | H | L | The only "shopping-like" SERP real estate open to an Iranian store |
| 4 | Brand SERP: Organization + WebSite + sameAs + logo + Knowledge Panel | all | H (brand) | M | Owns "دادرز" queries and lifts CTR on every result |
| 5 | Sitelinks (brand and navigational) | all | M-H | L | Brand queries convert best. Sitelinks come from site architecture |
| 6 | AI Overviews / AI Mode citations | dadrose, azmoon | H | M | Same inputs as #1-2. Separate AEO file |
| 7 | Video results + key moments (YouTube + on-site VideoObject) | dadrose, azmoon | M-H | M-H | Test-solving videos earn video packs. Key moments deep-link into answers |
| 8 | Article + ProfilePage (author E-E-A-T) + Breadcrumb | dadrose, book | M | L | Cheap. Supports Discover, AI citations and author knowledge panels |
| 9 | Discover + Preferred sources + Search profile | dadrose | M-H | L-M | Free push traffic for exam news and deadlines. Preferred sources works globally |
| 10 | Q&A / Discussion forum (user-answered questions) | azmoon | M | M-H | Only Q&A-type rich result still open to Persian education content. Feeds "Discussions and forums" |
| 11 | Top stories (exam news) | dadrose | M | M | Seasonal spikes around exam registration, exam date and results |
| 12 | Google Images (book covers, infographics) | book, dadrose | L-M | L | Low effort. Image packs on "جدول/نمودار" queries |
| 13 | Software App (azmoon PWA) | azmoon | L | L | Needs genuine ratings |
| 14 | Google Scholar (only if real research papers) | dadrose | L (brand) | M | Authority signal for the legal brand |
| 15 | Book actions interest form | book | L | L | Partner-limited, so onboarding is unlikely **[inferred]**. Costs one form |

---

## 1. Cross-cutting foundations (do once, all features depend on them)

1. **Make azmoon crawlable.** Public, server-rendered (Next.js SSR/SSG) pages need no login for: the exam hub, per-subject pages (مدنی, آیین دادرسی مدنی, تجارت, جزا, آیین دادرسی کیفری, ...), per-year past-exam pages (سوالات آزمون وکالت ۱۴۰۴ ...), and question pages with explanations. Keep personalized attempts, history and full mock exams behind login.
   - If gated content is served to Googlebot but hidden from users, mark it with paywalled-content markup (`isAccessibleForFree: false` + `hasPart.cssSelector`) to avoid cloaking. Source: https://developers.google.com/search/docs/appearance/structured-data/paywalled-content
   - Simpler: index only what anonymous users see.
2. **Three GSC properties** (Domain property + one URL-prefix property per subdomain), sitemaps with accurate `lastmod`, and URL Inspection monitoring (`P-1.1–1.6`). Use the URL Inspection API's `richResultsResult` to confirm detected schema per URL.
3. **JSON-LD conventions for Persian sites** (pitfalls hit by almost every Iranian WordPress/Woo site **[inferred]**):
   - `priceCurrency` must be ISO 4217 **`IRR`**. "IRT"/"Toman" is not ISO. Convert toman ×10. Use Latin digits for every number and date in JSON-LD.
   - Dates must be **ISO 8601 Gregorian**. Convert Jalali dates server-side.
   - Plugins (Yoast, Rank Math, Woo) often emit `IRT`. Override the output.
   - `inLanguage: "fa-IR"`.
   - One `@graph` per page, with stable `@id`s (`https://dadrose.com/#organization`, `#website`, `/author/x/#person`) so the three subdomains reference **one** Organization entity.
4. **Content guardrails.** Spam policies now explicitly apply to generative AI responses (May 15 2026, https://developers.google.com/search/updates). Use the human-gated content pipeline (`P-3`), not scaled AI pages. Rule of thumb: no question page without a human-verified explanation.
5. **Measurement backbone** (`P-2.1` daily GSC pull): add the `searchAppearance` dimension to the Search Analytics API pull and store it per property. This becomes the feature-win tracker. Search appearance filter values appear only for features the site has actually earned.

---

## 2. Feature-by-feature checklist

Format per feature: **What** · **Eligibility & requirements (source)** · **Target pages** · **Implement** · **Measure** · **Priority** · **Pitfalls**.

### 2.1 Classic blue links + title links + site names
- **What.** The standard result: title link, site name, favicon, URL/breadcrumb and snippet.
- **Requirements.** Sources Google uses for the title link: `<title>`, main visual title/`<h1>`, headings, `og:title`, anchor text and `WebSite` data (https://developers.google.com/search/docs/appearance/title-link). Site names work at domain **and subdomain** level, in all languages; subdirectories are not supported. `WebSite` needs `name` and `url`, and `alternateName` is recommended (https://developers.google.com/search/docs/appearance/site-names).
- **Target pages.** Everything.
- **Implement.**
  - Give each subdomain its own site name.
  - Unique titles per page. Brand at the end after a delimiter (`| دادرز`). The `<h1>` matches the title intent.
  - Favicon at least 48×48 on each host (https://developers.google.com/search/docs/appearance/favicon-in-search).

```json
{"@context":"https://schema.org","@type":"WebSite","@id":"https://azmoon.dadrose.com/#website",
 "name":"آزمون دادرز","alternateName":["Dadrose Azmoon","آزمون آنلاین وکالت دادرز"],
 "url":"https://azmoon.dadrose.com/","inLanguage":"fa-IR",
 "publisher":{"@id":"https://dadrose.com/#organization"}}
```
  Use `"دادرز"` for dadrose.com and `"کتابفروشی دادرز"` for book.dadrose.com.
- **Measure.** GSC Performance by page/query (`P-2.1`). Track title rewrites by comparing the `<title>` with live SERP snapshots (manual monthly check).
- **Priority.** H/M (#1).
- **Pitfalls.** Boilerplate titles ("نمونه سوال - صفحه ۲"), different brand names per host, Persian/English mixing in the site name, an un-crawlable favicon.

### 2.2 Sitelinks
- **What.** Extra same-domain links under a result, mostly on brand queries.
- **Requirements.** Fully automated. Google analyzes link structure. Use informative, compact titles and headings, clear navigation, short accurate anchor text, and no duplicate content. To remove a sitelink, use `noindex` or remove the page (https://developers.google.com/search/docs/appearance/sitelinks).
- **Target pages.** dadrose home → دوره‌ها, مقالات, آزمون, کتابفروشی. Azmoon home → per-subject hubs, past-year exams, pricing. Book home → bar-exam category, publisher pages, bundles.
- **Implement.**
  - Flat hub architecture: each hub is linked from the global nav and the footer with consistent anchors. Add BreadcrumbList.
  - Cross-host links between the three subdomains in the header (an ecosystem nav) **[inferred]**. Sitelinks are same-domain, but subdomains of one brand often appear together.
- **Measure.** Brand-query CTR in GSC (`query contains "دادرز"`). Do a manual SERP check monthly.
- **Priority.** M-H / L.
- **Pitfalls.** Thin tag pages or login/cart pages becoming sitelinks (`noindex` them). Inconsistent nav labels.

### 2.3 Sitelinks search box — **retired**
Removed Nov 2024 (https://developers.google.com/search/blog/2024/10/sitelinks-search-box). No action needed. Keeping `WebSite` markup is still required for site names. Leftover `SearchAction` markup is harmless.

### 2.4 Featured snippets (paragraph / list / table)
- **What.** An answer box above or within the results, linking to the passage and scrolling to it on click.
- **Requirements.** No markup and no way to request one. Google "elevates" pages it judges a good answer. Controls: `nosnippet`, `data-nosnippet`, `max-snippet` (https://developers.google.com/search/docs/appearance/featured-snippets).
- **Target pages.**
  - dadrose articles (definitions, procedures, conditions)
  - azmoon public hubs ("منابع آزمون وکالت", "شرایط شرکت در آزمون وکالت", "نحوه محاسبه نمره")
  - book category guides ("بهترین کتاب‌های آزمون وکالت")
- **Implement (on-page patterns).**
  - Question-form `<h2>` matching the query, then a 40–60-word direct answer paragraph **[practice, not a Google rule]**.
  - Ordered `<ol>` for steps ("مراحل ثبت‌نام آزمون وکالت").
  - Real HTML `<table>` for comparisons ("جدول منابع آزمون وکالت به تفکیک درس", "مقایسه کارآموزی وکالت و مشاوران ماده ۱۸۷").
  - Keep the answer in server-rendered HTML, never inside tabs or accordions that need JS.
- **Measure.** Not reported separately in GSC. Track position ~1 with high impressions and do SERP snapshots for the target query list (manual or a third-party rank tracker such as the Semrush SERP-features column).
- **Priority.** H/M (#2).
- **Pitfalls.** Burying the answer under long intros. Answers that drift from the visible `<h2>`. Over-using `data-nosnippet` on CTAs that wrap answer text.

### 2.5 People Also Ask (related questions)
- **What.** Expandable question boxes. Each answer is a featured-snippet-style passage. Same doc as §2.4.
- **Target pages.** A cluster article per PAA question set. Mine questions from PAA plus `04-keyword-map.csv` (e.g. "آزمون وکالت چند درصد قبولی دارد؟", "آیا بدون کلاس می‌توان قبول شد؟", "منابع آزمون وکالت ۱۴۰۵ چیست؟").
- **Implement.** An on-page question section of 3–6 `<h3>` questions with concise answers. **Do not add FAQPage markup expecting stars or dropdowns** (gone May 2026). Plain HTML Q/A still feeds PAA and AI answers.
- **Measure.** As §2.4. Also track queries starting with چطور/چگونه/آیا/چیست/چند in GSC (`P-2.1` regex).
- **Priority.** H/M.
- **Pitfalls.** Duplicate answers across many pages (cannibalization). Invented statistics such as acceptance rates. Cite the Kanoon/official announcement instead.

### 2.6 AI Overviews and AI Mode (brief; full AEO/GEO file is separate)
- **Requirements.** "There are no additional requirements to appear in AI Overviews or AI Mode." The page must be indexed and eligible to show a snippet. No llms.txt or special schema needed. Controls are `nosnippet`, `max-snippet`, `noindex` (https://developers.google.com/search/docs/appearance/ai-features).
- **Guide.** Original, non-commodity, first-hand content. Do not chunk or rewrite for AI. Do not chase inauthentic mentions. Google says Merchant Center and GBP data help products and businesses appear, and **neither is available to Iran** (https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- **Iran/Persian.** Persian AI Overview availability is unverified (§0.2). AI Mode/AIO traffic is counted under GSC "Web". Preferred sources now also badges AIO/AI Mode (https://developers.google.com/search/docs/appearance/preferred-sources).
- **Win levers specific to dadrose.**
  - Original data nobody else has: anonymized azmoon aggregates such as per-subject difficulty, most-missed questions and topic frequency across past exams. Publish these only once they are real and computed.
  - Named lawyer authors with credentials.
  - Primary-source citations (قانون, رأی وحدت رویه, Kanoon announcements).
- **Measure.** Search Generative AI performance report when available to the property. GA4 landing-page engagement from Google organic.
- **Pitfalls.** Blocking Googlebot on azmoon API/JS chunks so pages render empty. `nosnippet` on the article template.

### 2.7 Article rich result
- **What.** Better title, image and date in Search, Top stories and Discover.
- **Requirements.** No required properties. Recommended: `headline`, `image` (several ratios, large), `datePublished`, `dateModified`, and `author` with `name` + `url` (https://developers.google.com/search/docs/appearance/structured-data/article).
- **Target pages.** dadrose articles, exam-news posts, and book.dadrose blog if one exists.

```json
{"@context":"https://schema.org","@graph":[
 {"@type":"Article","@id":"https://dadrose.com/talagh-tavafoghi/#article",
  "headline":"شرایط و مراحل طلاق توافقی در سال ۱۴۰۵",
  "image":["https://dadrose.com/wp-content/uploads/talagh-16x9.jpg","https://dadrose.com/wp-content/uploads/talagh-4x3.jpg","https://dadrose.com/wp-content/uploads/talagh-1x1.jpg"],
  "datePublished":"2026-09-20T09:00:00+03:30","dateModified":"2026-10-10T12:00:00+03:30",
  "inLanguage":"fa-IR",
  "author":{"@type":"Person","@id":"https://dadrose.com/author/ali-ahmadi/#person","name":"علی احمدی","url":"https://dadrose.com/author/ali-ahmadi/","jobTitle":"وکیل پایه یک دادگستری"},
  "publisher":{"@id":"https://dadrose.com/#organization"},
  "mainEntityOfPage":"https://dadrose.com/talagh-tavafoghi/"}]}
```
  (Example names and URLs are placeholders.)
- **Measure.** GSC Enhancements. Discover and News performance.
- **Priority.** M/L (#8).
- **Pitfalls.** `dateModified` bumped without a real edit. Author name missing on the visible page. Jalali date strings in schema.

### 2.8 Breadcrumb
- **Requirements.** `BreadcrumbList` with at least 2 `ListItem`s. `item` is optional on the last item. The rich result is shown **on desktop** in all regions and languages (https://developers.google.com/search/docs/appearance/structured-data/breadcrumb). On mobile Google shows only the domain **[per Jan 2025 Search Central blog title; doc says desktop]**.
- **Target pages.** All templates: article › category, book › category › publisher, azmoon › subject › year › question.
- **Implement.** Rank Math/Yoast on WP/Woo. A `BreadcrumbJsonLd` component in Next.js. Names in Persian.
- **Measure.** GSC Enhancements → Breadcrumbs.
- **Priority.** M/L.
- **Pitfalls.** Breadcrumb names that don't match the visible breadcrumb. Linking to noindexed category pages.

### 2.9 Course list / Course info
- **Status.** Course info **removed** (Sep 2025). Course list is live but **English-only** and needs at least 3 courses (`name`, `description`, `provider` recommended) (https://developers.google.com/search/docs/appearance/structured-data/course).
- **Decision.** Persian course pages on dadrose are **not eligible**. Still emit lightweight `Course` (name, description, provider → Organization `@id`, `inLanguage: fa-IR`, `offers` in IRR) for entity clarity **[inferred benefit; no rich result]**.
- **Priority.** L/L.
- **Pitfall.** Don't spend dev time chasing a course carousel in Persian.

### 2.10 Book actions
- **Status.** Live but partner-only. Requires an interest form, onboarding, a daily Book feed (ISBN-13 preferred, ISBN-10 not accepted), canonical deep links to a buy page, and Google review of link quality (https://developers.google.com/search/docs/appearance/structured-data/book).
- **Decision.** Submit the interest form once (low cost). Expect rejection, because the feature is limited to "book providers with a wide selection" and an Iranian seller is likely blocked by sanctions **[inferred]**.
- **Regardless:** put **ISBN-13** on every book page and in the schema (`Book` + `Product` combined type, see §2.11). This helps Google match the entity to its book knowledge graph **[inferred]**.
- **Priority.** L/L.

### 2.11 Product snippets and merchant listings (book.dadrose.com), plus review snippets
- **What.** Price, availability and star rating under the blue link. Merchant-listing experiences (richer product panels) are for pages where you sell the item.
- **Requirements.**
  - Product snippet: `name` + one of `review`/`aggregateRating`/`offers` (https://developers.google.com/search/docs/appearance/structured-data/product-snippet).
  - Merchant listing: `name`, `image`, `offers.price` > 0, `priceCurrency` ISO 4217. The merchant must be the seller (https://developers.google.com/search/docs/appearance/structured-data/merchant-listing).
  - Shipping and return policies go at Organization level (Jul 11 & Nov 12 2025 updates, https://developers.google.com/search/updates).
  - Reviews: `aggregateRating` needs `ratingValue` + `ratingCount`/`reviewCount`. Don't aggregate reviews from other sites. The self-serving restriction applies to LocalBusiness/Organization, **not** to Book/Product (https://developers.google.com/search/docs/appearance/structured-data/review-snippet).
- **Iran caveat.** Merchant Center is unavailable, so markup alone must carry this. Whether Google surfaces merchant-listing panels for `IRR` offers to Iranian users is **[unverified]**. Product snippets (stars, price) are the realistic target.
- **Target pages.** Every book product page. Bundles ("پکیج کتاب آزمون وکالت") as `Product` with `isRelatedTo`/`hasPart` **[inferred]**.

```json
{"@context":"https://schema.org","@type":["Book","Product"],
 "@id":"https://book.dadrose.com/product/ayin-dadrasi-madani/#product",
 "name":"آیین دادرسی مدنی (ویژه آزمون وکالت)","isbn":"9786000000000","gtin13":"9786000000000",
 "author":{"@type":"Person","name":"نام نویسنده"},"publisher":{"@type":"Organization","name":"نام ناشر"},
 "inLanguage":"fa-IR","bookFormat":"https://schema.org/Paperback","numberOfPages":0,
 "image":["https://book.dadrose.com/wp-content/uploads/cover.jpg"],
 "description":"خلاصه کتاب...",
 "offers":{"@type":"Offer","url":"https://book.dadrose.com/product/ayin-dadrasi-madani/",
   "price":"4500000","priceCurrency":"IRR","availability":"https://schema.org/InStock",
   "itemCondition":"https://schema.org/NewCondition",
   "seller":{"@id":"https://dadrose.com/#organization"}},
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.6","reviewCount":"0"}}
```
  Placeholders: ISBN, page count, price (450,000 toman → `"4500000"` IRR) and rating values must come from real data. Omit `aggregateRating` until at least one genuine review exists.
- **Implement.**
  1. Fix the plugin currency output (IRT → IRR ×10).
  2. Woo review request email after delivery, so ratings accumulate.
  3. Real stock status.
  4. Organization-level `hasMerchantReturnPolicy` and `shippingDetails` matching the visible policy page.
- **Measure.** GSC Enhancements → Product snippets / Merchant listings. Search appearance "Product snippets", "Merchant listings", "Review snippet".
- **Priority.** H/L (#3).
- **Pitfalls.**
  - `IRT` currency.
  - Price in schema ≠ visible price (Persian digits on page are fine, but values must match).
  - Out-of-stock pages marked InStock.
  - Fake or imported reviews.
  - Variable products without a per-variant offer.

### 2.12 FAQ — **gone**
"This feature will no longer appear in Google Search starting May 7, 2026." Docs removed Jun 15 2026 (https://developers.google.com/search/updates). Keep visible Q/A HTML for PAA and AI. FAQPage markup can stay but earns nothing. Remove it from the "SEO checklist" so the team stops spending time on it.

### 2.13 HowTo — **gone** (Sep 13 2023)
Use `<ol>` steps for list featured snippets (§2.4) instead. Sources: https://developers.google.com/search/blog/2023/08/howto-faq-changes and https://www.searchenginejournal.com/google-completely-removes-how-to-rich-results/496479/

### 2.14 Education Q&A (flashcards, `Quiz`)
- **Requirements.** `Quiz` with `Question`s, `eduQuestionType: "Flashcard"`, `text`, one `acceptedAnswer`. Questions visible on the page. **Languages:** en, pt, vi (all regions) and es (Mexico) only (https://developers.google.com/search/docs/appearance/structured-data/education-qa).
- **Decision.** Not eligible in Persian. Watch the updates log for language expansion (`P-2.4` can diff https://developers.google.com/search/updates weekly). Implementation cost is small if Persian is ever added, because azmoon already has the question data.
- **Priority.** L now, H if Persian is added.

### 2.15 Practice problems — **gone** (Jan 2026)
No action. Public question pages still rank as normal results and in PAA (§2.4–2.5).

### 2.16 Q&A (QAPage)
- **Requirements.** One question per page with **user-submitted answers** (users must be able to answer). At least one answer. `mainEntity` → `Question` (`name`, `answerCount`, `acceptedAnswer` or `suggestedAnswer`), `Answer.text`. Not for site-written FAQs, blogs or how-tos (https://developers.google.com/search/docs/appearance/structured-data/qapage). The doc states no language restriction.
- **Target pages.** A new **azmoon question discussion page** per past-exam question (`/q/{id}`): the question, options and official key, plus user-posted explanations and "why option ۳ is wrong" answers, with moderators picking the accepted answer.
  - This is also the **only Q&A-type rich result open to Persian education content** and feeds "Discussions and forums" **[inferred]**.

```json
{"@context":"https://schema.org","@type":"QAPage","mainEntity":{"@type":"Question",
 "name":"سوال ۴۵ آزمون وکالت ۱۴۰۳ – حقوق مدنی: کدام عقد لازم است؟",
 "text":"متن کامل سوال و گزینه‌ها...","answerCount":3,"datePublished":"2026-10-01T10:00:00+03:30",
 "author":{"@type":"Organization","name":"آزمون دادرز","url":"https://azmoon.dadrose.com/"},
 "acceptedAnswer":{"@type":"Answer","text":"گزینه ۲ صحیح است زیرا...","upvoteCount":12,
   "url":"https://azmoon.dadrose.com/q/1403-45#a1","datePublished":"2026-10-02T08:00:00+03:30",
   "author":{"@type":"Person","name":"کاربر نمونه","url":"https://azmoon.dadrose.com/u/sample"}},
 "suggestedAnswer":[{"@type":"Answer","text":"...","upvoteCount":3,"url":"https://azmoon.dadrose.com/q/1403-45#a2","author":{"@type":"Person","name":"..."}}]}}
```
  (Counts are illustrative placeholders and must come from the database.)
- **Measure.** GSC Enhancements → Q&A. Search appearance "Q&A".
- **Priority.** M/M-H (#10).
- **Pitfalls.**
  - Marking pages without real user answers.
  - Expert-only answers with no user submission (ineligible).
  - Thin auto-generated pages at scale: launch only questions that have a human explanation.
  - Login-walled answering is fine, but answers must be visible to anonymous users.

### 2.17 Discussion forum
- **Requirements.** `DiscussionForumPosting` for user-generated forum posts (`author.name`, `datePublished`, `text`/`image`/`video`). Prefer QAPage when the forum is mainly Q&A. It feeds "Discussions and Forums" (https://developers.google.com/search/docs/appearance/structured-data/discussion-forum).
- **Target pages.** Optional community board (`انجمن داوطلبان آزمون وکالت`): study-plan threads and post-exam key discussions. These generate fresh UGC around exam day.
- **Priority.** M/H. It needs moderation capacity, so phase it after §2.16.
- **Pitfalls.** Staff-written posts marked as forum content. Spam without moderation degrades site quality.

### 2.18 Video results, video packs, key moments, LIVE badge
- **Requirements.**
  - VideoObject needs `name`, `thumbnailUrl`, `uploadDate`. Recommended: `contentUrl`/`embedUrl`, `duration`, `description`, `hasPart`.
  - Key moments: `Clip` (`name`, `startOffset`, `url` with time param) or `SeekToAction`. The video must be at least 30 s and support deep links.
  - YouTube: key moments from description timestamps.
  - LIVE badge: `BroadcastEvent` under `publication`; the Indexing API is recommended for livestreams.
  - Source: https://developers.google.com/search/docs/appearance/structured-data/video
- **Target pages.**
  - dadrose: one watch page per video lesson ("حل تست مدنی آزمون وکالت ۱۴۰۴ – سوالات ۱ تا ۲۰"), with the video as the main content.
  - azmoon: per-question video explanations.
  - book: a 60–120 s book walkthrough on each product page.
- **Strategy (YouTube vs Aparat vs self-host) [inferred].**
  - **YouTube** for global SERP video packs and key moments from chapters (Google indexes YouTube best). Its domestic reach is limited by filtering.
  - **Aparat** for domestic audience and in-Iran discovery. Google may index Aparat watch pages, but key-moment support there is not guaranteed.
  - **Self-hosted or Aparat embed on a dadrose watch page with VideoObject + Clip** to capture the video result on our own domain, which converts to signup.
  - Use the same video on all three with distinct titles and descriptions. The canonical watch page is ours.

```json
{"@context":"https://schema.org","@type":"VideoObject",
 "name":"حل تشریحی سوالات حقوق مدنی آزمون وکالت ۱۴۰۴ (۱ تا ۲۰)",
 "description":"تحلیل گزینه‌به‌گزینه ...","thumbnailUrl":["https://dadrose.com/v/madani-1404-thumb-16x9.jpg"],
 "uploadDate":"2026-09-15T18:00:00+03:30","duration":"PT24M10S",
 "contentUrl":"https://cdn.dadrose.com/v/madani-1404.mp4","embedUrl":"https://dadrose.com/embed/madani-1404",
 "inLanguage":"fa-IR","publisher":{"@id":"https://dadrose.com/#organization"},
 "hasPart":[{"@type":"Clip","name":"سوال ۱ – عقود لازم و جایز","startOffset":30,"endOffset":95,"url":"https://dadrose.com/video/madani-1404?t=30"},
            {"@type":"Clip","name":"سوال ۲ – اقاله","startOffset":96,"endOffset":170,"url":"https://dadrose.com/video/madani-1404?t=96"}]}
```
  Durations and timestamps are placeholders.
- **Live classes.** Event markup is ineligible (§2.21). Use YouTube Live, or a VideoObject with `BroadcastEvent` on a public watch page, for the LIVE badge.
- **Measure.** GSC Video indexing report. Search appearance "Videos". YouTube Studio → traffic source "Google Search".
- **Priority.** M-H/M-H (#7).
- **Pitfalls.**
  - Video not the main content of the page (not indexed).
  - Thumbnails blocked by robots.
  - Gating the video behind login.
  - Duplicate start times in Clips.

### 2.19 Organization logo, brand SERP and Knowledge Panel
- **Requirements.** Organization has no required properties. Recommended: `name`, `alternateName`, `legalName`, `url`, `logo` (at least 112×112, crawlable, works on white), `sameAs`, `address`, `contactPoint`, `telephone`, identifiers (`iso6523Code`, `vatID`, `taxID`). Place it on the home or about page (https://developers.google.com/search/docs/appearance/structured-data/organization). Use `OnlineStore` for the shop.

```json
{"@context":"https://schema.org","@type":"Organization","@id":"https://dadrose.com/#organization",
 "name":"دادرز","alternateName":["Dadrose","دادرز | آموزش حقوق و آزمون وکالت"],"legalName":"نام ثبتی شرکت",
 "url":"https://dadrose.com/","logo":"https://dadrose.com/logo-512.png",
 "description":"مرجع آموزش حقوق، دوره‌های تخصصی، آزمون آنلاین و کتاب‌های آزمون وکالت",
 "address":{"@type":"PostalAddress","addressCountry":"IR","addressLocality":"تهران","streetAddress":"...","postalCode":"..."},
 "contactPoint":[{"@type":"ContactPoint","contactType":"customer support","telephone":"+98-21-00000000","email":"support@dadrose.com","availableLanguage":["fa"]}],
 "sameAs":["https://www.wikidata.org/wiki/Q…","https://www.instagram.com/…","https://t.me/…","https://www.aparat.com/…","https://www.youtube.com/@…","https://www.linkedin.com/company/…","https://x.com/…","https://eitaa.com/…"],
 "subOrganization":[{"@type":"OnlineStore","@id":"https://book.dadrose.com/#store","name":"کتابفروشی دادرز","url":"https://book.dadrose.com/"},
                    {"@type":"EducationalOrganization","@id":"https://azmoon.dadrose.com/#org","name":"آزمون دادرز","url":"https://azmoon.dadrose.com/"}]}
```
- **Knowledge Panel actions** (panels are algorithmic **[general knowledge; no Google doc guarantees a panel]**).
  1. Use one canonical name everywhere ("دادرز" + "Dadrose").
  2. Create a **Wikidata** item: instance of = company/educational website, official website, logo, social IDs, inception. Only factual, sourced claims. Follow Wikidata notability (needs references).
  3. Persian Wikipedia only if independent coverage exists. Never self-promote there.
  4. Use consistent NAP on the site footer, the Enamad and Samandehi trust registrations, Neshan/Balad maps, social bios and publisher listings **[inferred: helps entity reconciliation; also a trust signal for Iranian buyers]**.
  5. Earn press mentions on Iranian legal and news sites (genuine PR, not paid link schemes).
  6. Once a panel appears, claim it via Google's "Get verified" flow **[availability for Iran unverified]**.
  7. Add a **Search profile** (§2.24) as an additional brand surface.
- **Measure.** Brand-query impressions/CTR (`P-2.1`). Monthly SERP screenshot of "دادرز", "Dadrose", "آزمون دادرز", "کتابفروشی دادرز".
- **Priority.** H/M (#4).
- **Pitfalls.** Multiple Organization nodes with different names across subdomains. A logo SVG Google can't index (use PNG). `sameAs` pointing to dead or unofficial profiles.

### 2.20 ProfilePage (authors, instructors)
- **Requirements.** `ProfilePage` with `mainEntity` Person/Organization + `name`. Recommended: `sameAs`, `image`, `interactionStatistic`, `agentInteractionStatistic`, `dateCreated`/`dateModified`. Use it for author and "about me" pages (https://developers.google.com/search/docs/appearance/structured-data/profile-page).
- **Target pages.** `/author/{slug}` on dadrose: lawyers and instructors with پروانه وکالت number, bar association (کانون), education, courses taught and books written (linked to book.dadrose). Azmoon public user profiles only if users opt in.

```json
{"@context":"https://schema.org","@type":"ProfilePage","dateModified":"2026-10-01T00:00:00+03:30",
 "mainEntity":{"@type":"Person","@id":"https://dadrose.com/author/ali-ahmadi/#person","name":"علی احمدی",
  "jobTitle":"وکیل پایه یک دادگستری و مدرس آزمون وکالت","image":"https://dadrose.com/authors/ali.jpg",
  "affiliation":{"@id":"https://dadrose.com/#organization"},
  "sameAs":["https://www.linkedin.com/in/…","https://www.instagram.com/…"],
  "agentInteractionStatistic":{"@type":"InteractionCounter","interactionType":"https://schema.org/WriteAction","userInteractionCount":0}}}
```
  `userInteractionCount` must equal the real article count.
- **Measure.** GSC Enhancements → Profile page. Search appearance for author-name queries.
- **Priority.** M/L.
- **Pitfalls.** Fake or stock author personas, which is a severe trust and E-E-A-T risk for YMYL legal content. Missing visible credentials.

### 2.21 Event (webinars / live classes) — **not eligible**
Physical events only, open to the public, and only in the listed countries (Iran is not among them) (https://developers.google.com/search/docs/appearance/structured-data/event). For live classes use YouTube Live plus the VideoObject LIVE badge (§2.18) and Discover/Top stories announcement posts. Event schema adds no rich result here.

### 2.22 Software App (azmoon as PWA)
- **Requirements.** `name`, `offers.price` (0 if free), and `aggregateRating` or `review`. `applicationCategory` and `operatingSystem` are recommended (https://developers.google.com/search/docs/appearance/structured-data/software-app).
- **Implement.** A `WebApplication` on the azmoon pricing/app page with `applicationCategory: "EducationalApplication"`, `operatingSystem: "Web, Android, iOS"`, offers in IRR, and genuine on-site ratings only.
- **Android distribution.** Cafe Bazaar / Myket listings, linked in `sameAs`. Google Play is likely unavailable to Iran-based developers **[inferred]**.
- **Priority.** L/L.
- **Pitfall.** Ratings must be collected from real users on the page they describe.

### 2.23 Dataset — Dataset Search only
"Dataset markup is only used by Dataset Search" (Nov 5 2025, https://developers.google.com/search/updates). Optional brand play: publish an open dataset of past-exam topic frequencies (CSV + `Dataset` schema), only if the data is real. Priority L.

### 2.24 Google Discover + Preferred sources + Search profiles
- **Discover requirements.** Indexed and policy-compliant. No markup needed. Large images at least 1200 px wide, more than 300k pixels, 16:9, with `max-image-preview:large`. Descriptive titles, no clickbait. Use `og:image`/schema to choose the image. Measure in the Discover report (https://developers.google.com/search/docs/appearance/google-discover). A Discover core update rolled out in February 2026 (https://developers.google.com/search/updates).
- **Preferred sources.**
  - Users pick your site and it gets a "preferred" badge in Top stories, AIO and AI Mode. Available globally in all Search languages for Top stories.
  - Works for domains and **subdomains**, not subdirectories.
  - Add the button or a deeplink: `https://www.google.com/preferences/source?q=dadrose.com` (https://developers.google.com/search/docs/appearance/preferred-sources).
- **Search profiles.**
  - A claimed hub for creators and publishers. Followers make linked content "more likely to appear" in Discover.
  - Badge URL `https://profile.google.com/@handle` (https://developers.google.com/search/docs/appearance/search-profiles).
  - Eligibility and country availability are not stated, so treat Iran as **[unverified]**.
- **Target pages.** Exam news, deadlines (registration, card printing, results), new-law explainers and study-plan posts.
- **Implement.**
  1. `<meta name="robots" content="max-image-preview:large">` site-wide.
  2. Custom 1200×675 featured images without text-heavy graphics.
  3. Add the Preferred-sources button to article sidebars and to Telegram/Instagram posts.
  4. Claim a Search profile and link it from `sameAs`.
- **Measure.** GSC Discover report. The Gen-AI report covers Discover AI features.
- **Priority.** M-H/L-M (#9).
- **Pitfalls.** Clickbait titles (manual action risk). Logo-only images. Stale "۱۴۰۴" content resurfacing as news.

### 2.25 Top stories / News
- **Eligibility.** Automatic; Google News has no guaranteed inclusion ("There's no guarantee...") (https://support.google.com/news/publisher-center/answer/9607104). Google News content policies apply. `author.url` is recommended.
- **Target pages.** A `/akhbar` (news) category on dadrose: timely, original reporting on Kanoon/Markaz announcements, exam schedules, capacity announcements and law amendments. Each post has a named author, a Gregorian+Jalali date and an Article schema.
- **Implement.**
  1. A dedicated news sitemap **[optional; Google News sitemap doc: https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap]**.
  2. Fast publishing on announcement day, with the `P-1` sitemap ping and the IndexNow job for others.
  3. Transparency pages: about, editorial policy, contact.
- **Measure.** GSC Performance → search type "News" (if traffic exists) and Search appearance.
- **Priority.** M/M (#11).
- **Pitfalls.** Rewriting other outlets' news (commodity content). Missing bylines.

### 2.26 Google Images (incl. licensable badge)
- **Requirements.**
  - Image SEO: descriptive filenames, `alt`, a relevant surrounding caption, an image sitemap, crawlable URLs (https://developers.google.com/search/docs/appearance/google-images).
  - Licensable badge: `ImageObject` with `contentUrl` and `license` (`acquireLicensePage` recommended), or IPTC "Web Statement of Rights" (https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata).
- **Target pages.**
  - Book covers (filename `ketab-ayin-dadrasi-madani-[author].jpg`, Persian alt).
  - Original infographics: "نقشه راه آزمون وکالت", "جدول منابع", "مقایسه مواد قانونی".
  - Author photos.
- **Implement.** Add `creditText: "دادرز"` and `copyrightNotice` on infographics. Watermark lightly. A license page is optional. Use WebP/AVIF with a fallback.
- **Measure.** GSC Performance → search type "Image".
- **Priority.** L-M/L (#12).
- **Pitfalls.** Lazy-load without `src`, so Googlebot sees no image. CDN hotlink protection blocking Googlebot-Image.

### 2.27 Local pack / Google Maps — **GBP unavailable**
- **Status.** Iran is excluded (https://support.google.com/business/answer/6270107).
- **Alternatives [inferred].**
  - `LocalBusiness`/`Organization` with `address`, `geo` and `openingHoursSpecification` on the contact page, if a physical office or publisher exists. Local business markup is in the gallery but its visible features rely on Google's local data.
  - Register on **Neshan** and **Balad** (Iranian maps).
  - Consistent NAP (§2.19).
- **Priority.** L. It only matters if there is an in-person office or book pickup.

### 2.28 Shopping tab / free product listings / Merchant Center — **unavailable**
- **Status.** Iran is not supported as a target country, and neither are Persian or IRR (https://support.google.com/merchants/answer/160637).
- **Alternatives.**
  - §2.11 on-page product markup (stars, price).
  - Iranian price-comparison and marketplace channels: Torob, Emalls, Digikala marketplace, Basalam **[inferred; drives Iranian shopping traffic Google can't]**. List the books there with backlinks to book.dadrose.
  - Book-specific: list ISBNs with Iranian book databases (e.g., ketab.ir / National Library) so the entity is consistent **[inferred]**.

### 2.29 "Perspectives" / Discussions & forums carousel
- Google surfaces forum and UGC results via the "Discussions and forums" feature, fed by discussion-forum and Q&A markup (https://developers.google.com/search/docs/appearance/structured-data/discussion-forum). "Perspectives" as a separately branded filter is **[unverified current status]**.
- **Plan.**
  - §2.16 and §2.17 on azmoon.
  - Genuine expert participation (named lawyers) in Iranian legal forums and Q&A communities, linking to dadrose only where useful **[inferred]**.
  - Short-form expert video (Instagram Reels / YouTube Shorts) gives perspective-style visibility **[inferred]**.

### 2.30 "Things to know" / related searches / "People also search for"
- Algorithmic, with no markup. **[Things to know current status: unverified]**. Related searches reveal the sub-topic map: harvest them into `04-keyword-map.csv` and cover each subtopic with a hub-and-spoke cluster (`P-3`). Refinement chips on brand queries ("دادرز آزمون", "دادرز کتاب") follow strong entity and sitelink structure **[inferred]**.

### 2.31 Google Books (Partner Program / Play Books)
- Selling and payouts are not supported for Iran (https://support.google.com/books/partner/table/6052428). Whether a non-selling preview-only partner account is possible from Iran is **[unverified]**.
- **Plan.** If dadrose publishes its own books, register ISBN-13 with the Iranian ISBN agency and keep a canonical book page with `Book` schema. This lets Google's book graph link to it **[inferred]**. Don't plan around Play Books.
- **Priority.** L.

### 2.32 Google Scholar
- **Requirements.**
  - Only scholarly works (papers, theses, technical reports). News, magazine articles and editorials are excluded.
  - Full text or the full abstract visible without login. HTML or a text PDF, one paper per URL.
  - `citation_title`, `citation_author` (one per tag), `citation_publication_date`, plus `citation_pdf_url`.
  - Reachable within 10 links of the homepage (https://scholar.google.com/intl/en/scholar/inclusion.html).
- **Fit.** Only if dadrose publishes real legal research (e.g., a `/pajouhesh` section with papers by credentialed authors). Blog articles do not qualify.
- **Priority.** L (brand authority only).

### 2.33 Chrome / Android app surfaces
- Firebase App Indexing is retired **[general knowledge]**.
- A PWA (installable from Chrome) needs a manifest, a service worker and HTTPS. This adds no SERP feature but helps retention **[inferred]**.
- Google Play is likely unavailable (§0.2).
- Use the SoftwareApplication schema (§2.22) and Cafe Bazaar/Myket deep links.
- **Priority.** L.

### 2.34 YouTube in SERP (video carousel, Shorts)
- See §2.18.
- **Add.**
  - A channel with playlists per bar-exam subject.
  - Chapters (timestamps) in every description.
  - Persian titles matching `04-keyword-map.csv` queries.
  - Shorts of one question each, linking to `azmoon.dadrose.com/q/{id}`.
  - The channel URL in Organization `sameAs`.
- **Measure.** YouTube Studio → "Google Search" traffic source.
- **Pitfall.** YouTube is filtered in Iran, so a YouTube-only plan reaches VPN users and the diaspora **[inferred]**. Dual-publish to Aparat.

### 2.35 Other gallery items — N/A
Carousel (only with Course/Movie/Recipe/Restaurant **[per carousel doc]**), Employer aggregate rating, Job posting, Math solver, Movie, Recipe, Vacation rental, Speakable: not applicable to these sites.

Job posting is an exception if the shop or academy hires (instructors). But Job posting's availability for Iran is **[unverified]**.

---

## 3. Measurement matrix (Search Console)

| Feature | GSC location | Pipeline |
|---|---|---|
| Blue links, title links | Performance → Web | `P-2.1` `gsc_pull.py` (page×query×country×device) |
| Rich results (Product, Review, Breadcrumb, Q&A, Discussion forum, Profile page, Video, Article) | Enhancements reports + Performance → **Search appearance** filter | add `searchAppearance` dimension pull to `gsc_pull.py` |
| Featured snippets / PAA | Not separated. Infer from position plus SERP snapshots | third-party rank tracker / Semrush SERP features (optional) |
| Video | Video indexing report + Performance search type "Video" | `P-2.4` `crawl_check.py` checks VideoObject presence |
| Images | Performance search type "Image" | `gsc_pull.py` with `type=image` |
| Discover | Discover report | `gsc_pull.py` with `type=discover` |
| News / Top stories | Performance search type "News" (if any) | `gsc_pull.py` with `type=googleNews` |
| AI Overviews / AI Mode | Counted in Web. Search Generative AI performance report (beta) | manual until an API exists |
| Schema validity per URL | URL Inspection API `richResultsResult` | `P-1.6` inspection job, extended |
| Brand SERP / Knowledge panel | Brand query CTR | weekly owner report `P-5.1` |

Alerting (`P-2.2` `anomalies.py`): add rules for (a) a drop in Product snippet valid items, (b) a new error type in any Enhancements report, (c) a fall in brand-query CTR.

---

## 4. End-to-end win scenarios

Each scenario lists the query, the SERP real estate we hold, the landing page, the funnel and the automation. Queries are examples from the keyword map's themes, not measured volumes.

### S1 — "نمونه سوالات آزمون وکالت" (head term, high intent for signup)
- **SERP held.**
  - Featured snippet: a list snippet of "سوالات آزمون وکالت به تفکیک سال" from the azmoon hub `<ol>`.
  - PAA: ("سوالات آزمون وکالت ۱۴۰۴ با پاسخ", "آیا سوالات تکراری است؟").
  - Video pack: a YouTube answer-solving playlist plus the dadrose watch page with key moments.
  - Sitelinks under azmoon.dadrose.com: per-subject hubs.
  - Possibly an AI Overview citation from our original stats page.
- **Landing.** `azmoon.dadrose.com/nemoone-soal-azmoon-vekalat` (SSR, public), a year×subject matrix.
- **Funnel.**
  1. **Free mini-test** of 10 questions, with no login and instant scoring.
  2. Result page: "you are weak in آیین دادرسی مدنی".
  3. **Signup** to save the result and unlock a full timed mock.
  4. Day-1/day-3 nudges (email/SMS/Telegram).
  5. Recommendation API (`P-4.2`) suggests the book on the weak subject from book.dadrose and the related dadrose course.
- **Automation.**
  - `P-1.1` sitemaps for new year/subject pages.
  - `P-3` content pipeline (human-reviewed explanations).
  - `P-4.2` recommendations.
  - `P-5.2` GA4 events: `mini_test_start` → `mini_test_complete` → `sign_up` → `purchase`.
  - `gsc_pull` tracks the hub query cluster.

### S2 — Brand queries: "دادرز", "آزمون دادرز", "کتاب دادرز"
- **SERP held.**
  - Site name "دادرز" on all three hosts.
  - Sitelinks (دوره‌ها/آزمون/کتابفروشی/مقالات), logo and favicon.
  - Knowledge panel: Wikidata + sameAs + Search profile.
  - Product stars when a book is searched with the brand.
  - Top stories with the preferred-source badge for users who chose us.
- **Landing.** The home of the relevant host.
- **Funnel.** Brand searchers have high intent, so give them a direct path: prominent pricing, "شروع آزمون رایگان" and the bestsellers.
- **Automation.**
  - `P-5.1` weekly brand-CTR report.
  - `anomalies.py` alert on brand-impression drops (possible reputation issue).
  - Monthly SERP screenshot task (manual).

### S3 — Book purchase: "خرید کتاب آیین دادرسی مدنی [نویسنده]" / "[title] pdf"
- **SERP held.**
  - Product snippet (★ rating, price, "موجود").
  - Image result of the cover.
  - Video result (book walkthrough).
  - A dadrose article "بهترین منابع آیین دادرسی مدنی برای آزمون وکالت" ranking alongside.
- **Landing.** The book product page with ISBN-13, a sample PDF chapter (legal), the table of contents and reviews.
- **Funnel.** Add to cart → upsell a "pack" (book + 1-month azmoon subscription) → after delivery, a review request (more stars, a better snippet) → cross-sell next-subject books.
  - For "pdf" queries, offer a free sample chapter plus a printable study plan in exchange for signup (email/phone). Never host pirated PDFs.
- **Automation.**
  - Schema validation via URL Inspection `richResultsResult` (`P-1.6`).
  - Price/stock sync in WooCommerce, with schema auto-generated from the same data.
  - `crawl_check.py` asserts `priceCurrency == "IRR"`.
  - Review-request email automation.

### S4 — Legal how-to for the public: "شرایط طلاق توافقی", "نحوه تنظیم دادخواست مطالبه وجه"
- **SERP held.**
  - Paragraph or list featured snippet.
  - PAA.
  - AI Overview/AI Mode citation, earned by a credentialed author with statute citations.
  - Discover for timely variants.
  - The author ProfilePage builds an author entity.
- **Landing.** A dadrose article with an `<ol>` of steps, a costs table (official tariffs cited, no invented figures) and the related article cluster.
- **Funnel.** Article → topic course CTA ("دوره جامع دعاوی خانواده") → course purchase. Secondary: "دانشجوی حقوق هستید؟ آزمون وکالت را رایگان امتحان کنید" → azmoon.
- **Automation.**
  - `P-3` refresh triggers (law changes, falling CTR).
  - Internal linking by `topic_key` (`P-4.1`).
  - GA4 `course_view` → `purchase`.

### S5 — Seasonal news: "زمان ثبت‌نام آزمون وکالت ۱۴۰۵", "نتایج آزمون وکالت", "ظرفیت پذیرش"
- **SERP held.**
  - Top stories: an original, fast, bylined news post.
  - Discover: a 1200 px image and a preferred-sources badge for followers.
  - Featured snippet for the date answer.
  - AI Mode citation.
- **Landing.** A dadrose news post that updates live, with a timeline table and an official-source link.
- **Funnel.** News → "یادآور تاریخ‌ها" signup (SMS/Telegram) → countdown study plan → mock-exam promotion in the final weeks → book bundle promotion.
- **Automation.**
  - Announcement watcher: poll official announcement pages and alert an editor (human writes).
  - Immediate sitemap `lastmod` update and IndexNow.
  - `gsc_pull` with `type=discover` and `type=googleNews`.
  - `anomalies.py` spike detection to add internal links from the home page during the spike.

### S6 — Video-first: "حل تست حقوق مدنی آزمون وکالت", "تحلیل سوالات آزمون وکالت ۱۴۰۴"
- **SERP held.**
  - Video carousel: YouTube with chapters.
  - Key moments on our own watch page (Clip markup).
  - Shorts.
  - The azmoon question page (Q&A rich result) for the per-question long tail.
- **Landing.** A dadrose watch page with an embedded mini quiz of the same questions.
- **Funnel.** Watch → answer the next 5 questions → signup to see your rank among users → paid full-subject question bank.
- **Automation.**
  - Video pipeline: generate the chapter list from the question index, then push the same chapters to the YouTube description, the Aparat description and the `hasPart` Clips.
  - `crawl_check.py` validates VideoObject.
  - YouTube Studio export into the weekly report.

### S7 — Long-tail question: "سوال ۴۵ آزمون وکالت ۱۴۰۳" / "چرا گزینه ۲ صحیح است ..."
- **SERP held.**
  - Q&A rich result: user answers with an accepted answer.
  - Discussions & forums.
  - PAA for conceptual variants.
- **Landing.** `azmoon.dadrose.com/q/{year}-{n}`.
- **Funnel.** Read the explanation → "practice 10 similar questions" (login) → signup → subscription. Each answer posted counts as engagement and adds UGC freshness.
- **Automation.**
  - Generate Q&A pages only where a human explanation exists (`P-3.2` guardrails).
  - The moderation queue.
  - Sitemaps per exam year.
  - `searchAppearance = Q&A` tracking.

### S8 — Commercial investigation: "بهترین کتاب برای آزمون وکالت", "بهترین سایت آزمون آنلاین وکالت"
- **SERP held.**
  - List featured snippet from an honest comparison article: our books **and** others, with clear criteria.
  - Product snippets on the books listed.
  - AI Overview mentions, earned via original comparison data and third-party mentions (press, forum reviews; not paid fake reviews).
  - Image pack of covers.
- **Landing.** A dadrose guide → book bundle pages.
- **Funnel.** Guide → bundle → checkout → azmoon trial included.
- **Automation.**
  - `P-3` with quarterly refresh.
  - The recommendation API supplies "most purchased by azmoon users weak in X" **only when the counts are real**.

### S9 — Visual: "نقشه راه آزمون وکالت", "جدول منابع آزمون وکالت"
- **SERP held.** Image pack (original infographic with license metadata), a table featured snippet, and Discover.
- **Landing.** An infographic article with a downloadable PDF study plan in exchange for signup.
- **Funnel.** Download → signup → 30-day plan emails → mock-exam and book offers.
- **Automation.** Image sitemap, IPTC/creditText injection at upload (WP hook), GA4 `lead_magnet_download`.

### S10 — Expert/author: "[نام وکیل] وکیل", "[نام مدرس] آزمون وکالت"
- **SERP held.** The author's ProfilePage result, a person knowledge panel (sameAs, Wikidata if notable), their YouTube videos and their books (product snippets).
- **Landing.** The author page listing articles, courses and books.
- **Funnel.** Author trust → that author's course or book → azmoon.
- **Automation.** Author-page generation from the CMS (real credentials only) and a quarterly author-entity audit in `crawl_check.py`.

---

## 5. Implementation order

1. **Week 1–2.**
   - §1 foundations: azmoon public SSR hubs, GSC properties, the IRR fix.
   - WebSite/site names, Organization `@graph`, Breadcrumb, Article + author ProfilePage, Product/Book markup.
   - `max-image-preview:large`, preferred-sources button.
2. **Month 1.**
   - Answer-first rewrites of the top informational pages (featured snippets/PAA).
   - Free mini-test.
   - Wikidata + sameAs cleanup, Search profile claim.
   - Review-request emails.
   - `searchAppearance` pull.
3. **Quarter.**
   - Q&A question pages with UGC answers.
   - Video program (YouTube + Aparat + on-site Clips).
   - News category for exam season.
   - Infographics.
   - Optional forum and dataset.
   - Submit the Book actions interest form.
4. **Watch list** (weekly diff of https://developers.google.com/search/updates): Persian support for Education Q&A or Course list, AIO language list, changes to Search profiles availability.

## 6. Sources (all accessed 2026-10-13)
- Search gallery: https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- Updates log: https://developers.google.com/search/updates
- Simplifying results (Jun 2025): https://developers.google.com/search/blog/2025/06/simplifying-search-results ; follow-up Nov 2025: https://developers.google.com/search/blog/2025/11/update-on-our-efforts
- HowTo/FAQ changes 2023: https://developers.google.com/search/blog/2023/08/howto-faq-changes
- Sitelinks search box farewell: https://developers.google.com/search/blog/2024/10/sitelinks-search-box
- Title links: https://developers.google.com/search/docs/appearance/title-link · Site names: https://developers.google.com/search/docs/appearance/site-names · Sitelinks: https://developers.google.com/search/docs/appearance/sitelinks · Featured snippets: https://developers.google.com/search/docs/appearance/featured-snippets
- AI features: https://developers.google.com/search/docs/appearance/ai-features · Gen-AI optimization guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide · Gen-AI reports: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- Article / Breadcrumb / Course / Book / Product snippet / Merchant listing / Review snippet / Education Q&A / Q&A / Discussion forum / Video / Organization / ProfilePage / Event / Software app / Image license: `https://developers.google.com/search/docs/appearance/structured-data/{article|breadcrumb|course|book|product-snippet|merchant-listing|review-snippet|education-qa|qapage|discussion-forum|video|organization|profile-page|event|software-app|image-license-metadata}`
- Discover: https://developers.google.com/search/docs/appearance/google-discover · Preferred sources: https://developers.google.com/search/docs/appearance/preferred-sources · Search profiles: https://developers.google.com/search/docs/appearance/search-profiles
- Google News: https://support.google.com/news/publisher-center/answer/9607104
- GBP countries: https://support.google.com/business/answer/6270107 · Merchant Center countries/languages/currencies: https://support.google.com/merchants/answer/160637 · Google Ads country restrictions: https://support.google.com/google-ads/answer/6163740 · Play Books countries: https://support.google.com/books/partner/table/6052428
- AIO expansion May 2025: https://blog.google/products/search/ai-overview-expansion-may-2025-update/
- Google Scholar inclusion: https://scholar.google.com/intl/en/scholar/inclusion.html
- Secondary (used only where the official page body could not be fetched): https://www.searchenginejournal.com/google-completely-removes-how-to-rich-results/496479/ ; https://www.websitebuilderexpert.com/news/google-discontinues-structured-data-types/ ; https://pasqualepillitteri.it/en/news/4116/search-console-generative-ai-report-ai-overviews-ai-mode ; https://www.seroundtable.com/google-search-profile-badge-42106.html
