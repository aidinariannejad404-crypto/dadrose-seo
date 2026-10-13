# Google Search Central: SEO Knowledge Base for the dadrose network

Scope: dadrose.com (legal articles and topic courses, WordPress-like), book.dadrose.com (law and bar-exam bookstore, likely WooCommerce), azmoon.dadrose.com (online bar-exam quiz center, being rebuilt in Next.js 16).

Method: every rule below comes from an official Google page fetched on **2026-10-13** ("checked 2026-10-13" applies to every line unless a different date is given). A few dates come from secondary reporting because Google's blog post bodies did not render in the fetch tool. Those lines are marked **[secondary]** and name the outlet.

Abbreviations: SD = structured data, GSC = Google Search Console, RR = rich result(s).

Base URLs:
- `GSC-DOCS` = https://developers.google.com/search/docs
- `UPD` = https://developers.google.com/search/updates (documentation changelog)

---

## 0. Most important changes for this network (2023–2026)

The table below gives each feature's status as of 2026-10-13. Source for every row is `UPD` unless another source is named.

| Feature | Status | Date |
|---|---|---|
| HowTo RR | Removed on desktop and mobile; docs deleted | 2023-09-14 |
| FAQ RR | Restricted to well-known government and health sites | 2023-09-14 |
| FAQ RR | Shown for nobody ("will no longer appear in Google Search starting May 7, 2026") | 2026-05-07 |
| FAQ docs | Deleted ("no longer shown in Google Search results") | 2026-06-15 |
| FAQ in GSC report and Rich Results Test | Dropped June 2026; Search Console API support ends August 2026 **[secondary: ppc.land, quoting the Google doc]** | 2026-06 and 2026-08 |
| Sitelinks search box | Retired ("Farewell, Sitelinks Search Box" blog post); phased out in November 2024 **[secondary: stanventures]** | 2024-10 |
| Book actions, Course info, ClaimReview, Estimated salary, Learning video, Special announcement, Vehicle listing | Phase-out announced in "Simplifying the search results page" (2025-06-12); banners added to their docs that day | 2025-06-12 |
| Course info, Estimated salary, Learning video, Special announcement, Vehicle listing | Docs removed ("no longer shown in Google Search results") | 2025-09-09 |
| Special announcement | Deprecated effective 2025-07-31 | announced 2025-04-23 |
| Book actions | Deprecation banner removed, so it is still supported (feed partners only) | 2025-11-05 |
| Practice problem | Deprecation notice, with GSC reporting ending January 2026 | 2025-11-05 |
| Practice problem | Docs removed ("no longer shown in Google Search results") | 2026-01-06 |
| Dataset | Clarified: used only by Dataset Search, not by Google Search | 2025-11-05 |
| Breadcrumbs in mobile results | Mobile results now show the domain only (blog "Simplifying the visible URL element on mobile search results"); the breadcrumb doc now says "available on desktop" | 2025-01 |
| INP | Replaced FID as a Core Web Vital (`UPD` 2023-05-10: "as a replacement for FID in March 2024") | 2024-03 |
| Helpful content system | Became part of the core ranking systems (`GSC-DOCS/appearance/ranking-systems-guide`) | 2024-03 |

### Structured data features still listed in the Search Gallery

Source: `GSC-DOCS/appearance/structured-data/search-gallery`, page last updated 2026-06-15.

Article, Breadcrumb, Carousel, Course list, Dataset, Discussion forum, Education Q&A, Employer aggregate rating, Event, Image metadata, Job posting, Local business, Math solver, Movie, Organization, Product, Profile page, Q&A, Recipe, Review snippet, Software app, Speakable, Subscription/paywalled content, Vacation rental, Video.

FAQ, HowTo, Practice problems, Course info and Sitelinks search box are not in the list.

### Language limits that rule out the learning rich results for Persian
- **Course list:** available "in English in all regions" only (`GSC-DOCS/appearance/structured-data/course`).
- **Education Q&A:** available only in English, Portuguese and Vietnamese (all regions), plus Spanish in Mexico. Persian is not supported (`GSC-DOCS/appearance/structured-data/education-qa`).

---

## 1. How Search works and the SEO Starter Guide

### How Search works
Source: `GSC-DOCS/fundamentals/how-search-works`.
- Search runs in three stages: crawling, indexing and serving. Not every page passes all three, and Google "doesn't guarantee that it will crawl, index, or serve your page."
- Googlebot renders pages with a recent version of Chrome.
- Google groups duplicate pages into clusters and picks one canonical, "the one that's most representative of the group."
- Google does not accept payment to crawl more often or to rank higher.
- A page can be indexed and still not appear in results, because of relevance, quality or robots rules.

### SEO Starter Guide
Source: `GSC-DOCS/fundamentals/seo-starter-guide`.
- **Discovery:** Google finds pages mainly through links. A sitemap helps but is not required.
- **Directories:** "For larger sites (several thousand URLs or more)", grouping topics into directories helps Google learn how often each section changes.
- **Reorganizing:** don't reorganize a site just for SEO.
- **Duplicates:** pick one canonical per piece of content, using a redirect or `rel=canonical`. Duplicate content is "inefficient" but is "not something that will cause a manual action". Copying other sites' content is a different matter.
- **Myths the guide tells you to ignore:**
  - Google "doesn't use the keywords meta tag".
  - Keyword stuffing violates the spam policies.
  - Keywords in the domain or URL path "have hardly any effect beyond appearing in breadcrumbs".
  - The TLD matters only when you target one country.
  - "The length of the content alone doesn't matter for ranking purposes."
  - Heading order and heading count don't matter.
  - E-E-A-T is not a ranking factor ("No, it's not").
- **Subdomains vs subdirectories:** "From a business point of view, do whatever makes sense for your business." Subdirectories can be easier to manage.
- **Links:** use descriptive link text. Mark user-generated or untrusted links with `nofollow` or `ugc`.

### Ranking systems guide
Source: `GSC-DOCS/appearance/ranking-systems-guide`.
- **Site diversity:** Google generally shows no more than two listings from the same site in the top results. "Subdomains are usually treated as part of the root domain", though not always. For dadrose, the three subdomains will usually count as one site for diversity.
- **Retired systems:** Helpful content (merged into core in March 2024), Panda (merged into core in 2015), Penguin (merged in 2016).
- **Systems still listed:** reliable information systems, reviews system, original content systems, freshness, passage ranking, SpamBrain, and others.

---

## 2. Crawling control

### robots.txt
Source: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec. This is the new canonical location; the crawler docs moved on 2025-11-20 (`UPD`).

**Scope**
- A robots.txt file applies only to its own protocol, host and port.
- Each subdomain (book., azmoon.) needs its own `/robots.txt`. A robots.txt in a subdirectory is invalid.

**Choosing the user-agent group**
- Each crawler obeys only the single group with the **most specific matching user-agent**.
- Matching is case-insensitive, and the order of groups doesn't matter.
- Several groups for the same user-agent are merged.
- A specific group is **not** combined with the `*` group. If you add a `Googlebot` group, it must repeat every rule from `*` that should also apply to Googlebot.

**Rule precedence**
- The most specific rule wins, meaning the one with the longest path.
- When an allow rule and a disallow rule tie, the least restrictive one (allow) wins.
- `*` matches any sequence of characters and `$` marks the end of the URL. Paths are case-sensitive.

**Limits and caching**
- Maximum file size is **500 KiB**; content past that is ignored.
- The file must be UTF-8.
- Google usually caches robots.txt for up to **24 hours**, and may adjust that based on `Cache-Control: max-age`.

**Status code handling**
- 3xx: Google follows at least **5** redirect hops, then treats the file as a 404.
- 4xx except 429: treated as "no robots.txt", so there are no restrictions. Don't use 401 or 403 to limit crawl rate.
- 5xx or unreachable: crawling stops for **12 hours**. After that, Google uses the last cached copy for up to **30 days**. With no cached copy, there are no restrictions.

**Directives**
- `Sitemap:` takes an absolute URL. You may list several, and the line belongs to no user-agent group.
- `crawl-delay` is **not supported**. `noindex` in robots.txt is not supported either (`GSC-DOCS/crawling-indexing/block-indexing`).

**Indexing still possible**
- A URL blocked by robots.txt can still be indexed without its content (`GSC-DOCS/crawling-indexing/consolidate-duplicate-urls`).
- To keep a URL out of results, use `noindex` instead (`GSC-DOCS/appearance/title-link`).

### Googlebot
Source: `GSC-DOCS/crawling-indexing/googlebot`.
- Googlebot fetches the first **2 MB** of HTML and other supported files, and the first **64 MB** of a PDF. Limits apply to uncompressed bytes.
- Each CSS and JS resource is fetched separately under its own 2 MB limit. Content past the cutoff is not indexed.
- Most sites should see Googlebot no more than "once every few seconds on average."
- Googlebot Smartphone does most crawling. It shares the `Googlebot` token with the desktop crawler, so the two can't be targeted separately.
- Verify Googlebot by reverse DNS or by Google's published IP ranges. The IP range files moved location in March 2026 (blog archive).

### Google-Extended
Source: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers.
- Google-Extended is a robots.txt control token only; it has no separate user-agent string.
- It controls whether content is used to train future Gemini models and for grounding in Gemini Apps and Vertex AI.
- It "does not impact a site's inclusion in Google Search" and is not a ranking signal.
- The control for AI Overviews and AI Mode is Googlebot plus the snippet controls (`GSC-DOCS/appearance/ai-features`), not Google-Extended.

### Crawl budget
Source: `GSC-DOCS/crawling-indexing/large-site-managing-crawl-budget`.

**Who needs it** (Google calls these "rough estimates")
- Sites with 1 million+ unique pages whose content changes weekly.
- Sites with 10,000+ unique pages whose content changes daily.
- Sites with many URLs in "Discovered – currently not indexed."

**Budget model**
- Crawl budget is crawl capacity (server health; it drops on 5xx or 429) combined with crawl demand (inventory, popularity, staleness).

**Recommendations**
- Consolidate duplicates.
- Block unimportant URLs with robots.txt.
- Don't use `noindex` to save budget; Google still has to fetch the page.
- Return 404 or 410 for removed pages.
- Fix soft 404s.
- Keep sitemaps fresh with `lastmod`.
- Shorten redirect chains.
- Support `304 Not Modified`.

**Emergency slowdown** (`GSC-DOCS/crawling-indexing/reduce-crawl-rate`)
- Return 500, 503 or 429 (with `Retry-After` on 503 or 429) for "a couple of hours, or 1-2 days".
- If the same URL keeps returning these codes for several days, it may be dropped from the index.
- The slowdown applies to the whole hostname.

### Faceted navigation and URL parameters
Source: `GSC-DOCS/crawling-indexing/crawling-managing-faceted-navigation`.

**If filter URLs don't need to be indexed** (the usual case)
- Disallow the filter parameters in robots.txt, and keep the unfiltered listing crawlable.
- Alternatively, put filters in the `#fragment`, which Google ignores.
- `rel=canonical` and `nofollow` are weaker options. `nofollow` works only if every link to the URL carries it.

**If filter URLs must be indexed**
- Use `&` as the separator.
- Keep filter order consistent and prevent duplicate filters.
- Return **404** for filter combinations with no results and for pagination past the end. Don't redirect these.

**Pagination** (`GSC-DOCS/specialty/ecommerce/pagination-and-incremental-page-loading`)
- Give each page an `<a href>` link to the next page.
- Give each page a unique `?page=n` URL and its own canonical. Don't canonicalize to page 1.
- `rel=next/prev` is no longer used by Google.
- Infinite scroll and "load more" also need crawlable links.
- Keep sort and filter variants out of the index with `noindex` or robots.txt.

---

## 3. Indexing control and canonicalization

### Robots meta tag and X-Robots-Tag
Source: `GSC-DOCS/crawling-indexing/robots-meta-tag`.

**Supported rules:** `all`, `noindex`, `nofollow`, `none`, `nosnippet`, `indexifembedded`, `max-snippet:[n]`, `max-image-preview:[none|standard|large]`, `max-video-preview:[n]`, `notranslate`, `noimageindex`, `unavailable_after:[date]`.

**How rules are applied**
- When rules conflict, the more restrictive one wins.
- A crawler can be named in the header, for example `X-Robots-Tag: googlebot: nofollow`.
- Use the header for PDFs and images.
- Google also honors robots meta tags outside `<head>`. This was documented on 2026-03-24 (`UPD`) and is not a behavior change.
- Rules are ignored if the URL is blocked by robots.txt, because Google never sees them.

**Effect on AI features**
- `nosnippet` also stops the content from being used "as a direct input for AI Overviews and AI Mode."
- `max-snippet` limits how much content those features can use.

**`data-nosnippet`**
- Valid only on `span`, `div` and `section`.
- Don't toggle it with JavaScript.
- An unclosed `div` can hide everything after it.

**`noindex` timing** (`GSC-DOCS/crawling-indexing/block-indexing`)
- The page drops out once it is recrawled, which "may take months". Use URL Inspection to speed this up.

### Canonicalization
Source: `GSC-DOCS/crawling-indexing/consolidate-duplicate-urls`.

**Signal strength**
- 301 or 308 redirect: strong.
- `rel=canonical` in HTML or an HTTP header: strong. The header form works for PDFs.
- Listing in a sitemap: weak.

**Rules**
- Don't use robots.txt or `noindex` to canonicalize.
- Use absolute URLs, and give every canonical page a self-referencing canonical.
- Link internally to the canonical URL, and keep all signals consistent.
- Never use a fragment as a canonical.
- Google prefers HTTPS. Avoid HTTPS-to-HTTP redirects and broken certificates.
- For hreflang, the canonical should be in the same language as the page.
- On JS sites, set the canonical in the initial HTML, and make sure JS doesn't change it (`GSC-DOCS/crawling-indexing/javascript/javascript-seo-basics`).

### HTTP status codes
Source: `GSC-DOCS/crawling-indexing/http-network-errors`.
- A 2xx status doesn't guarantee indexing. A 2xx page with empty or error-like content is a **soft 404**.
- 301 and 308 are treated alike as a "strong" canonical signal. 302 and 307 are a "weak" signal.
- Google follows up to **10** redirect hops.
- 404 and 410 are treated the same. All 4xx codes except 429 mean "content doesn't exist", and indexed URLs drop out over time.
- 429 and 5xx slow crawling. URLs that keep returning them are eventually removed.
- Since 2025-12-18 (`UPD`) the docs state that 200 pages are sent to rendering and non-200 pages may not be. Don't rely on client-side JS on error pages.

### Redirects
Source: `GSC-DOCS/crawling-indexing/301-redirects`.
- Prefer server-side redirects.
- Instant meta refresh (0 seconds) is treated as permanent. A delayed meta refresh is treated as temporary.
- JavaScript redirects are a last resort, because rendering may fail.
- Crypto redirects (a link with an explanation) are unreliable.

### Site moves
Source: `GSC-DOCS/crawling-indexing/site-move-with-url-changes`.

**Steps**
- Build a full old-to-new URL map, using sitemaps, logs, CMS and GSC as sources.
- Redirect each old URL with a 301 or 308 straight to its final target. If chains are unavoidable, keep them under 5 hops (Google says "no more than 3 and fewer than 5").
- Don't redirect many URLs to the homepage.
- Use the **Change of Address** tool when moving domains or subdomains. It isn't needed for HTTP-to-HTTPS, www, or path changes.
- Keep redirects "generally at least 1 year". 301s don't lose PageRank.

**Timing**
- Small and medium sites take a few weeks. Move them all at once.
- Large sites take longer. Move them section by section.

### JavaScript SEO
Source: `GSC-DOCS/crawling-indexing/javascript/javascript-seo-basics`. This matters for azmoon on Next.js.
- Google processes JS sites in three phases: crawl, render, index.
- Only `<a href>` elements are reliably discovered as links.
- Use the History API for routing, not fragments.
- Titles and meta descriptions can be set with JS.
- A `noindex` in the initial HTML may stop Google from rendering at all, so JS can't remove it later.
- In SPAs, avoid soft 404s: redirect to a server 404, or add `noindex` with JS.
- Google recommends server-side rendering or pre-rendering, because not all bots run JS.
- Lazy-loaded content must still be indexable.

### Mobile-first indexing
Source: `GSC-DOCS/crawling-indexing/mobile/mobile-sites-mobile-first-indexing`.
- Google indexes and ranks the mobile version, crawled with the smartphone agent.
- Mobile and desktop need the same content, structured data, titles, meta descriptions and robots meta.
- Don't lazy-load primary content on user interaction, because Google doesn't click or swipe.
- Don't block CSS or JS.
- Keep image URLs and alt text identical across versions.

---

## 4. Sitemaps, recrawl, and APIs

### Sitemaps
Sources: `GSC-DOCS/crawling-indexing/sitemaps/build-sitemap` and `.../large-sitemaps`.

**Limits and format**
- Each sitemap: up to **50,000 URLs** and **50 MB** uncompressed. Must be UTF-8 with absolute URLs.
- Sitemap index: up to **50,000** `<loc>` entries.
- GSC accepts up to **500 sitemap index files** per site.

**Tags**
- Google uses `<lastmod>` only when it is "consistently and verifiably accurate", meaning significant content, structured data or link changes. A copyright-year change doesn't count.
- `<priority>` and `<changefreq>` are ignored.

**Location and submission**
- Unless submitted in GSC, a sitemap covers only its own directory and below.
- Cross-site submission in GSC requires verified ownership of every host in the sitemap.
- Submit through GSC, the Search Console API, or a `Sitemap:` line in robots.txt. For feeds, use WebSub.
- A sitemap is a hint, not a guarantee.
- The sitemaps "ping" endpoint was announced as "going away" in June 2023 (blog post `2023/06/sitemaps-lastmod-ping`). Don't use it.

**Image sitemaps** (`.../sitemaps/image-sitemaps`)
- Up to **1,000** `<image:image>` entries per `<url>`.
- The `caption`, `title`, `geo_location` and `license` tags were removed.
- Images hosted on a CDN are fine if you verify both domains.

**News sitemaps** (`.../sitemaps/news-sitemap`)
- For news publishers only.
- Include only articles from the last **2 days**, with up to **1,000** `news:news` tags per sitemap.
- dadrose is not a news publisher, so skip news sitemaps.

### Requesting recrawl
Source: `GSC-DOCS/crawling-indexing/ask-google-to-recrawl`.
- Use URL Inspection's "Request indexing" for a few URLs and a sitemap for many.
- Individual requests have a quota; Google publishes no number for the UI.
- Crawling takes "a few days to a few weeks". Repeat requests don't speed it up.

### Indexing API (strictly limited)
Sources: `https://developers.google.com/search/apis/indexing-api/v3/quickstart`, `.../using-api`, `.../quota-pricing`.

**Allowed content**
- "The Indexing API can only be used to crawl pages with either JobPosting or BroadcastEvent embedded in a VideoObject." That means job postings and livestream video pages only.
- Do **not** use it for articles, courses, products or quizzes.

**Quotas** (per project, default)
- 200 publish requests per day (`URL_UPDATED` and `URL_DELETED` combined), resetting at midnight Pacific Time.
- 180 `getMetadata` requests per minute.
- 380 requests per minute across all endpoints.
- Batches hold up to 100 calls, but quota still counts per URL.

**Compliance**
- All submissions undergo "rigorous spam detection".
- Using multiple accounts to get around quotas is prohibited, and access "may result in access being revoked".
- `URL_DELETED` requires the URL to return 404 or 410, or carry `noindex`.

### Search Console APIs
Source: https://developers.google.com/webmaster-tools/limits.

| API | Per site | Per user | Per project |
|---|---|---|---|
| Search Analytics | 1,200 QPM | 1,200 QPM | 40,000 QPM and 30,000,000 QPD |
| URL Inspection | 600 QPM and **2,000 QPD** | – | 15,000 QPM and 10,000,000 QPD |
| Other resources (incl. Sitemaps API) | – | 20 QPS and 200 QPM | 100,000,000 QPD |

- Search Analytics also has "load quota" limits, measured over 10-minute and 1-day windows, with no published numbers.
- The Search Analytics API has offered **hourly data** since April 2025 (blog archive, 2025-04).

---

## 5. Structured data

### General guidelines
Source: `GSC-DOCS/appearance/structured-data/sd-policies`.

**Format and access**
- JSON-LD is recommended; Microdata and RDFa also work.
- Don't block marked-up pages with robots.txt, `noindex` or a login.

**Quality rules**
- Mark up only content that is visible on the page.
- The markup must be "a true representation of the page content."
- Use the most specific type available.
- Put the markup on the page it describes. Duplicate pages get the same markup.
- Link related items with `@id`.

**Eligibility and enforcement**
- Items missing required properties aren't eligible.
- Valid markup doesn't guarantee a rich result.
- Violations can bring a manual action. That removes RR eligibility but doesn't affect web ranking.

### Article
Source: `GSC-DOCS/appearance/structured-data/article`.

**Types and properties**
- Use `Article`, `NewsArticle` or `BlogPosting`. No property is required.
- Recommended: `author`, `author.name`, `author.url` (or `sameAs`), `datePublished`, `dateModified` (ISO 8601 with time zone), `headline`, `image`.
- Images: several high-resolution images in **16x9, 4x3 and 1x1** ratios, each at least **50K pixels** (width × height).

**Authors**
- Give each author a separate entry, and include every author shown on the page.
- `author.name` holds only the name. Job titles go in `jobTitle` and the publisher goes in `publisher`.
- Use `Person` for people and `Organization` for organizations.

**Multi-page articles**
- The canonical must point to each page itself or to a view-all page, not to page 1.

### BreadcrumbList
Source: `GSC-DOCS/appearance/structured-data/breadcrumb`.
- Include at least 2 `ListItem`s, each with `position`, `name` and `item`. The last item's `item` is optional.
- Breadcrumbs should reflect a typical user path rather than mirror the URL. A page may have several trails.
- Breadcrumbs now appear on desktop only; mobile results were simplified in January 2025.

### Organization and WebSite (site name)
Sources: `GSC-DOCS/appearance/structured-data/organization` and `GSC-DOCS/appearance/site-names`.

**Organization**
- Place it on the home page or the About page. No property is required.
- Use the most specific subtype, for example `OnlineStore` for the shop.
- Logo must be at least **112x112 px**, crawlable, and look right on white.
- Recommended properties:
  - `url`, `sameAs`, `name`, `alternateName`, `legalName`
  - `contactPoint` (phone with country code), `address` (`addressCountry` as ISO 3166-1 alpha-2, e.g. "IR"), `foundingDate`, `description`
  - `taxID` (must match the country in `address`), `iso6523Code`
- Merchants can nest `hasMerchantReturnPolicy`, `hasShippingService` and `hasMemberProgram`.

**WebSite (site name)**
- Required properties are `name` and `url`. `alternateName` values are listed in order of preference.
- "Site names can appear for domain-level and subdomain-level sites." A subdomain with no markup may fall back to the domain's name.
- "Google Search does not support site names at the subdirectory level."
- Site names work in all languages.

### Product, merchant listings, and books
Sources: `GSC-DOCS/appearance/structured-data/product`, `.../merchant-listing`, `.../book`.

**Product snippets vs merchant listings**
- Product snippets are for pages where the product can't be bought.
- Merchant listings are for pages where you can buy. Merchant listing markup also makes the page eligible for product snippets.

**Merchant listing requirements**
- Required: `Product.name`, `image`, and `offers` as an `Offer` (not `AggregateOffer`).
- `price` must be greater than zero, and `priceCurrency` must be an ISO 4217 code.
- Recommended: `availability`, `itemCondition`, `shippingDetails`, `hasMerchantReturnPolicy`, `priceValidUntil`, `gtin` or `isbn`, `sku`, `brand`, `aggregateRating`, `review`, and `category` (documented 2026-07-07, `UPD`).
- Only pages where a shopper can buy are eligible. Pages must cover one product or its variants; category pages are not eligible.
- Use a separate URL per currency.

**Merchant Center**
- Use markup and a Merchant Center feed together to "maximize" eligibility (`GSC-DOCS/specialty/ecommerce/share-your-product-data-with-google`).
- The Shopping tab requires Merchant Center.
- **Merchant Center free listings don't list Iran** among supported countries, and **Persian isn't a supported language** (https://support.google.com/merchants/answer/160637). For book.dadrose, Merchant Center and the Shopping tab are effectively unavailable for Iranian targeting. On-page Product markup still helps Google understand the pages, but rich-result display for IRR prices is not confirmed by any official page.

**Book actions**
- Book actions are feed-based "buy" and "borrow" actions for book providers "with a wide selection of available books".
- Participation requires an interest form and onboarding. The feature is not available to ordinary self-serve sites.
- For a bookstore, use `Product` (with `isbn`) together with `Book` via multi-typing (`"@type": ["Product","Book"]`). Multi-typing is our inference from the general guidelines, not a quoted rule.

### Review snippets
Source: `GSC-DOCS/appearance/structured-data/review-snippet`.

**Supported item types**
- Reviews may be of `Book`, `Course`, `Product`, `SoftwareApplication`, `Event`, `Organization` (with restrictions) and other types.

**Self-serving reviews**
- If a business controls reviews about itself, its `LocalBusiness` or `Organization` pages are **not eligible** for stars.

**Guidelines**
- Reviews must be visible on the page and about a specific item.
- Don't aggregate reviews from other sites.
- "Don't include fake or undisclosed incentivized reviews". This guideline was added 2026-07-24 (`UPD`).

**Required properties**
- Review: `author` (under 100 characters), `reviewRating.ratingValue`, and the item's `name`.
- AggregateRating: `ratingValue` plus `ratingCount` or `reviewCount`.

### Course list (English only)
Source: `GSC-DOCS/appearance/structured-data/course`.
- Requires at least **3** courses, joined by `ItemList` carousel markup on a summary page or an all-in-one page.
- Each course needs `name` and `description` (displayed up to 60 characters). `provider` is recommended.
- The course must have an educational outcome and be "led by one or more instructors with a roster of students".
- No prices or promotional wording in the title.
- **Course info** (the per-course detail RR) was removed on 2025-09-09.

### Education Q&A (Quiz / Question / Answer)
Source: `GSC-DOCS/appearance/structured-data/education-qa`.
- Structure: `Quiz` → `hasPart` → `Question`, with `eduQuestionType: "Flashcard"`, exactly one `acceptedAnswer`, and its `text`.
- Every question must be a flashcard. Questions must be visible on the page, not only in a PDF.
- Put the markup on the most detailed leaf page.
- Not available in Persian; see the language limits in section 0.
- **Practice problems** markup (multiple-choice practice) was removed on 2026-01-06 and no longer shows.

### Q&A page
Source: `GSC-DOCS/appearance/structured-data/qapage`.
- Use it only for a single question per page where **users can submit answers**.
- Not for FAQs written by the site, and not for pages with many questions.
- Required: `mainEntity` holding a `Question` with `name`, `answerCount`, and an `acceptedAnswer` or `suggestedAnswer` with `text`.
- Supported properties for Discussion forum and Q&A were extended on 2026-03-24 (`UPD`).

### ProfilePage
Source: `GSC-DOCS/appearance/structured-data/profile-page`.
- Use it for pages about one person or organization affiliated with the site, for example an author bio or employee page. A store home page is not eligible.
- Required: `mainEntity` (a `Person` or `Organization`) and `name`.
- Recommended: `description` (byline or credential), `image`, `sameAs`, `identifier`, interaction stats, `dateCreated` and `dateModified`.

### Subscription and paywalled content
Source: `GSC-DOCS/appearance/structured-data/paywalled-content`.
- For content that requires registration or a subscription and that you want indexed, set `isAccessibleForFree: false`.
- Mark the gated sections with `hasPart` → `WebPageElement` and a `.class` `cssSelector`.
- This markup is what separates a paywall from cloaking.

### FAQPage and HowTo
- **FAQ:** there is no RR at all since 2026-05-07, and the documentation was removed. Markup may stay but has no Search benefit and causes no errors **[secondary: ppc.land]**.
- **HowTo:** gone since 2023-09-14.
- **Sitelinks search box:** retired in 2024. Don't add `SearchAction` for Google.

---

## 6. Content quality, E-E-A-T, YMYL, spam, and AI content

### Helpful, reliable, people-first content
Source: `GSC-DOCS/fundamentals/creating-helpful-content`.

**Questions Google suggests asking**
- Does the content offer original information, analysis "beyond the obvious"?
- Is it written or reviewed "by an expert or enthusiast who demonstrably knows the topic well"?
- Is it free of easily verified factual errors?

**Warning signs**
- Content made mainly for search traffic.
- Covering many topics in the hope that some will rank.
- Chasing a word count ("No, we don't" prefer a length).
- Changing dates "to make them seem fresh when the content has not substantially changed".

**Who, How, Why**
- **Who:** Google strongly encourages accurate bylines. Fake author profiles, such as AI-generated headshots or invented credentials, are deceptive.
- **How:** disclose when automation or AI substantially produced the content.
- **Why:** the content should exist to help people.

**E-E-A-T and YMYL**
- E-E-A-T "isn't a specific ranking factor". Of its parts, "trust is most important."
- YMYL topics (those affecting health, financial stability, safety or society) get extra weight on strong E-E-A-T. Legal guidance falls in this group.

### Search Quality Rater Guidelines
Source: https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf (version dated **2025-09-11**; the previous version was 2025-01-23 **[secondary: searchengineland]**).

- **YMYL categories:** Health or Safety, Financial Security, Government/Civics/Society, and Other. Legal content touching rights, money or civic processes falls within these.
- **Trust** is the core of E-E-A-T. An untrustworthy page has low E-E-A-T however expert it looks.
- **Expert sources:** some YMYL information "must come from experts".
- **Reputation research** is required for every Page Quality rating. Independent sources beat the site's own claims. For YMYL topics, raters use what experts in the field say.
- **Lowest rating:** YMYL pages that give no information about the website or its creator are rated Lowest, as are deceptive or untrustworthy pages.
- **Shopping sites:** raters look for who is responsible for the site, plus contact details and payment, exchange and returns policies.
- **Scaled and low-effort content:** sections 4.6.5 (scaled content abuse) and 4.6.6 (low-effort, low-originality main content) cover AI and mass-produced pages (cited at `GSC-DOCS/fundamentals/using-gen-ai-content`).
- Rater scores don't directly change rankings.

### Spam policies
Source: https://developers.google.com/search/docs/essentials/spam-policies.

**Full list:** cloaking, doorway abuse, expired domain abuse, hacked content, hidden text and links, keyword stuffing, link spam, machine-generated traffic, malicious practices (now including **back button hijacking**, added 2026-04-13 per `UPD`), misleading functionality, scaled content abuse, scraping, site reputation policy, sneaky redirects, thin affiliation, and user-generated spam.

**Key definitions**
- **Scaled content abuse:** "many pages are generated for the primary purpose of manipulating search rankings". This applies however the pages are made, AI or human.
- **Site reputation:** "third-party content is published on a host site mainly because of that host's already-established ranking signals".
  - The policy was introduced with the March 2024 update and enforced from 2024-05-05 **[secondary: ppc.land]**.
  - From 2026-08-30, inside the EEA the affected section is separated from the host site rather than given a manual action. Outside the EEA nothing changed (`UPD` 2026-08-28; blog `2026/08/update-site-reputation-policy`; details **[secondary: ppc.land]**).
- **Expired domain abuse:** "an expired domain name is purchased and repurposed primarily to manipulate search rankings".
- **Link spam:** paid links must carry `rel="sponsored"` or `rel="nofollow"`.
- **Generative AI:** spam now explicitly includes "attempting to manipulate generative AI responses in Google Search" (`UPD` 2026-05-15).

### Ranking updates, 2024 to 2026
Source: https://status.search.google.com.

| Update type | Dates |
|---|---|
| Core updates | Mar 2024 (03-05 to 04-19), Aug 2024, Nov 2024, Dec 2024, Mar 2025, Jun 2025 (06-30 to 07-16), Dec 2025 (12-11 to 12-29), Mar 2026 (03-27 to 04-08), May 2026 (05-21 to 06-01) |
| Spam updates | Mar 2024, Jun 2024, Dec 2024, Aug 2025, Mar 2026, Jun 2026, Aug 2026, Sep 2026 (09-24 to 10-07) |
| Other | Discover core update, Feb 2026 |

### AI-generated content
Source: `GSC-DOCS/fundamentals/using-gen-ai-content`, last updated 2026-10-01.
- AI may be used to research and structure content.
- Mass-generating pages without added value risks scaled content abuse.
- Fact-check everything, including titles, meta descriptions, structured data and alt text.
- Consider telling readers how AI was used.
- Merchant Center specifics:
  - AI-generated images need IPTC `DigitalSourceType` set to `TrainedAlgorithmicMedia`.
  - AI-generated product titles and descriptions must be labelled.

---

## 7. AI Overviews, AI Mode, and generative AI optimization

**Eligibility** (`GSC-DOCS/appearance/ai-features`)
- A page must be indexed and eligible to show with a snippet.
- There are "no additional requirements" and "no special schema.org structured data" for AI Overviews or AI Mode.
- Both features use query fan-out, meaning multiple related searches.

**Controls**
- `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex`. Googlebot's robots.txt rules govern access for Search, including AI features.

**Reporting**
- AI Mode and AI Overview traffic is counted in the GSC Performance report under "Web" (`UPD` 2025-06-16).
- A separate "Search Generative AI performance" report has been rolling out to a subset of sites since June 2026 (blog `2026/06/gen-ai-performance-reports`). It shows impressions, pages, countries, devices and dates; details **[secondary: ppc.land]**.

**Generative AI optimization guide** (`GSC-DOCS/fundamentals/ai-optimization-guide`, added 2026-05-15)
- Generative AI features run on the core ranking systems, so normal SEO applies.
- Not needed:
  - New machine-readable files, `llms.txt` or Markdown. On `llms.txt`, the guide says it "won't negatively or positively impact your visibility" (`UPD` 2026-06-15).
  - Content chunking.
  - Writing specially for AI.
  - Chasing mentions.
  - Structured data ("isn't required for generative AI search").
- "No third-party tool has access to our internal ranking or AI systems."

**Preferred sources**
- Became available in AI Overviews and AI Mode on 2026-05-27 (`UPD`).

---

## 8. Page experience, Core Web Vitals, HTTPS

**Core Web Vitals** (`GSC-DOCS/appearance/core-web-vitals`)
- "Good" thresholds: **LCP ≤ 2.5 s**, **INP < 200 ms**, **CLS < 0.1**.
- INP replaced FID in March 2024 (`UPD`).

**How page experience is used** (`GSC-DOCS/appearance/page-experience`)
- Core ranking systems use Core Web Vitals. There is no single "page experience signal".
- Page experience is assessed mostly per page, with some site-wide assessment.
- Relevance still comes first; good page experience helps most when many pages are equally helpful.
- Chasing perfect scores "may not be the best use of your time".
- Other factors to get right: serve over HTTPS (GSC has an HTTPS report), be mobile-friendly, avoid intrusive interstitials, and avoid excessive ads.

---

## 9. Titles, snippets, images, links, URLs, hreflang

### Title links
Source: `GSC-DOCS/appearance/title-link`.
- Give every page a unique, descriptive, concise `<title>`.
- Put the brand at the start or end, separated by a delimiter.
- Make the main `<h1>` clearly the page's main heading.
- Write the title in the same language and script as the page. A mismatch, such as a Latin-script title on a Persian page, invites a rewrite.
- **Sources Google may use for the title link:** `<title>`, `h1`, `og:title`, prominent text, anchor text, `WebSite` SD.
- **Common reasons Google rewrites titles:**
  - Half-empty titles.
  - Obsolete titles, for example last year's exam date.
  - Boilerplate shared across pages.
  - No single clear heading.

### Meta descriptions and snippets
Source: `GSC-DOCS/appearance/snippet`.
- Snippets come mostly from page content; the meta description is used when it describes the page better.
- Write a unique meta description per page. Programmatic descriptions are "encouraged" on large database sites.
- There is no length limit; results are truncated to the device width.

### Images
Source: `GSC-DOCS/appearance/google-images`.
- Use `<img src>`; CSS background images aren't indexed.
- Alt text is "the most important attribute". Also use descriptive filenames.
- Supported formats: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF.
- With `srcset`, keep a `src` fallback.
- Set a preferred image through `primaryImageOfPage`, a schema image, or `og:image`. Don't use the logo.
- Use an image sitemap for images on a CDN.

### Links
Source: `GSC-DOCS/crawling-indexing/links-crawlable`.
- Only `<a href>` links are reliably crawled.
- Anchor text should be "descriptive, reasonably concise, and relevant". Avoid "click here" and stuffed anchors.
- "Every page you care about should have a link from at least one other page on your site."
- Use `rel=sponsored` for paid links, `rel=ugc` for user links, and `nofollow` for links you don't trust.

### URL structure
Source: `GSC-DOCS/crawling-indexing/url-structure`.
- Use readable words and hyphens.
- Use the audience's language in URLs, with non-ASCII characters percent-encoded. Persian slugs are fine.
- Paths are case-sensitive.
- Avoid session IDs.
- Use `key=value` parameters joined with `&`.
- Don't use fragments to change content.

**Ecommerce URLs** (`GSC-DOCS/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites`)
- Give each variant its own URL, with the canonical pointing to the main product.
- `noindex` empty categories, or return 404 if the category is removed.
- Don't link internally to tracking parameters.

### hreflang
Source: `GSC-DOCS/specialty/international/localized-versions`.
- Declare hreflang through HTML, an HTTP header or a sitemap; one method is enough.
- Every version must reference itself and all others, reciprocally, using fully qualified URLs.
- Codes: ISO 639-1 language, optionally with an ISO 3166-1 alpha-2 region, for example `fa` or `fa-IR`. Use `x-default` as the fallback.
- Google doesn't use hreflang or `lang` to detect a page's language.
- The sites are Persian-only today, so hreflang isn't needed.

---

## 10. Search Console reports to monitor

Source: `GSC-DOCS/monitor-debug/search-console-start`. Google suggests checking about monthly and after site changes; Google also sends email alerts.

**Reports to watch**
- **Performance:**
  - Search types: Web, Web (multimodal, new September 2026), Image, Video, News.
  - Branded queries filter (November 2025), custom annotations (November 2025), weekly and monthly views (December 2025), all from the blog archive.
  - The Search Generative AI report, if your site is in the rollout.
- **Page indexing:** watch "Crawled – currently not indexed", "Discovered – currently not indexed", "Duplicate, Google chose different canonical", Soft 404, and Blocked by robots.txt.
- **Sitemaps:** submit one per host.
- **URL Inspection:** check the Live test and view the rendered HTML, which matters for Next.js.
- **Rich result reports:** Breadcrumb, Product or Merchant listings, Review snippets, Profile page, Videos. The FAQ and Practice problem reports are gone.
- **Health and security:** Core Web Vitals, HTTPS, Manual actions, Security issues, Crawl stats (Settings).
- **Removals:** temporary for about 6 months.
- **Change of Address:** for any domain or subdomain move.

**Property setup**
- Use a **Domain property** for dadrose.com, which covers all subdomains, plus URL-prefix properties per subdomain for granular reports and sitemaps.

---

## 11. Implications for the dadrose sites

### A. Network architecture: subdomains
1. **Keep the subdomains.** Google's position is "do whatever makes sense for your business" (Starter Guide). Moving book. or azmoon. into folders would be a site move with real risk and no documented ranking gain.
2. **Each host is configured separately:**
   - It has its own robots.txt, because robots.txt is per host.
   - Each host gets its own sitemap index, referenced in its own robots.txt.
   - Each host gets its own `WebSite` SD with a distinct `name`, for example "دادرس", "کتاب‌فروشی دادرس" and "آزمون دادرس". Site names work at subdomain level.
3. **Expect shared diversity limits.** Subdomains usually count as one site, so the three hosts share the "no more than two" listings per query. Plan keyword ownership so the hosts don't compete:
   - Articles target informational intent.
   - The book store targets buying intent.
   - azmoon targets "practice test" intent.
4. **Link the hosts deliberately.** Cross-link with descriptive anchors (articles ↔ relevant books ↔ relevant quizzes) as plain `<a href>` links. Use one `Organization` entity (with an `@id` on dadrose.com) referenced from every host.
5. **Site reputation policy is not a concern** while all three hosts are first-party dadrose content. Never rent a subdomain or folder to third-party coupon, casino or "guest" content.

### B. dadrose.com: legal articles (YMYL)
1. **Use `Article` or `BlogPosting` JSON-LD** with:
   - `headline` and `datePublished` and `dateModified` (with `+03:30` offset; Google says to include a time zone).
   - `image` in 16x9, 4x3 and 1x1, each at least 50K px.
   - `author` as a separate `Person` per author, with `url` pointing to an author profile page, plus `publisher` as the `Organization`.
2. **Build author and lawyer profile pages** with `ProfilePage` → `Person`.
   - Include `name`, `jobTitle` (for example وکیل پایه یک دادگستری), `description` holding the credentials (bar association membership and license number, if the lawyer agrees), `image` and `sameAs`.
   - YMYL pages with no information about the creator are rated Lowest by raters. Fake credentials or AI headshots are explicitly deceptive.
3. **Show trust visibly**, because trust is the most important part of E-E-A-T:
   - A byline, plus "reviewed by" a licensed lawyer.
   - Last-reviewed date and citations to statutes or official gazettes, linked.
   - A disclaimer and a contact/about page naming who is responsible.
4. **Update dates honestly.** Change `dateModified` and `lastmod` only on substantive legal updates, such as a new law or circular. Google flags "freshness" date bumps and ignores an inaccurate `lastmod`.
5. **Use AI carefully.** It may assist drafting, but a human lawyer must fact-check before publishing. Disclose substantial AI use. Never mass-generate pages such as "every article of the code × every city"; that is scaled content abuse.
6. **Drop FAQ and HowTo markup work.** Neither RR shows anymore. Existing `FAQPage` markup can stay (it is harmless) but brings no Google benefit. Keep visible FAQ text if it helps users.
7. **Course pages:** Course list RR is English-only, and Course info was removed in September 2025, so no Course RR is available in Persian. Optional: keep `Course` markup (`name`, `description`, `provider`), which costs little and may help understanding. Prioritize strong topic hub pages, `BreadcrumbList` and internal links instead.
8. **Site-wide markup:**
   - `BreadcrumbList` on every article and course (shown on desktop only).
   - `Organization` (with logo at least 112 px and `sameAs`) plus `WebSite` on the home page.
   - No `SearchAction`.
9. **WordPress hygiene:**
   - `noindex` or 404 for tag archives with thin content.
   - Self-canonical on paginated archives, with no canonical to page 1.
   - Real `?page=`/`/page/n` links.
   - Strip `?replytocom` and similar parameters via canonical or robots.

### C. book.dadrose.com: bookstore (WooCommerce)
1. **Product pages:** use `Product` + `Book` multi-type with `Offer` (`price` greater than 0, `priceCurrency` "IRR"), plus `availability`, `isbn` or `gtin13`, `itemCondition`, `shippingDetails`, `hasMerchantReturnPolicy` (preferably at `Organization` level), `aggregateRating` and `review` from real buyers only.
   - Merchant Center free listings don't support Iran or Persian, so rely on on-page markup.
   - Google pages don't confirm IRR merchant-listing display; treat any rich result as a bonus.
   - Store prices in rial in markup if the site shows toman, and keep the visible and markup values consistent. That is an inference; the docs only require ISO 4217.
2. **Faceted URLs** such as `?filter_author=`, `?orderby=`, `?min_price=`, `?pa_*`, `?add-to-cart=`:
   - Disallow them in robots.txt (Google: "there's no good reason to allow crawling of filtered items" in most cases).
   - Keep category and paginated category URLs crawlable and self-canonical.
   - Return 404 for empty filter combinations if any are left crawlable.
   - Always disallow `/cart/`, `/checkout/`, `/my-account/` and `?add-to-cart=`.
3. **Variants:** give each its own URL (path or parameter), canonical to the main product. Never use `#fragment` variants.
4. **Out-of-stock and discontinued books:** while restock is possible, keep the page at 200 with `availability` OutOfStock. When permanently discontinued, 301 to the new edition or return 404/410. Avoid "soft 404" thin pages.
5. **Store trust:** visible contact details, return and payment policies, and the legal entity. Raters check these on shopping pages.
6. **Product descriptions:** write original copy (summary, table of contents, which exam it suits). Copied publisher blurbs risk "thin affiliation" or "scraping" style low value.

### D. azmoon.dadrose.com: quiz center (Next.js 16)
1. **Rendering:**
   - Use SSR or SSG for every indexable page (exam landing pages, subject hubs, sample question pages).
   - Put titles, meta descriptions, canonical and robots in the server HTML. Never add or remove `noindex` with client JS.
   - Use `<a href>` links via `next/link`, and History API routing.
2. **Status codes:** return real 404s from the server (`notFound()`). Non-200 pages may not be rendered, and SPA "not found" screens returning 200 become soft 404s.
3. **Rich results:**
   - **Practice problems** markup is dead (removed January 2026).
   - **Education Q&A** (`Quiz` with Flashcard questions) doesn't support Persian. Its eligibility also requires visible flashcard Q&A. Adding it is optional and low-value today.
   - **QAPage** fits only if users can post answers, such as a discussion of a question.
   - Put effort into strong, indexable topic pages with `BreadcrumbList` and `Organization`.
4. **Indexing strategy:**
   - Index public value pages, such as "past exam questions of year X with explained answers" written by experts.
   - `noindex` (or keep behind login) the per-user attempt, result and score pages, plus infinite random-quiz URLs.
   - Don't auto-generate thousands of near-identical question pages without explanations; that is scaled content abuse.
   - If full explanations are subscriber-only but you want them indexed, use paywalled-content markup (`isAccessibleForFree: false` plus `cssSelector`) to avoid cloaking.
5. **Indexing API:** do not use it for quizzes, articles or books. It officially supports only JobPosting and livestream `BroadcastEvent` pages. Use sitemaps with accurate `lastmod` and GSC "Request indexing" for a few key URLs.
6. **Next.js migration:** if URLs change, follow the site-move playbook:
   - Map every old URL to a new one and 301 it.
   - Keep redirects at least 1 year.
   - Update internal links and sitemaps, then monitor Page indexing.
   - No Change of Address is needed when the host stays the same.

### E. Monitoring and automation
1. **GSC setup:** one Domain property, plus URL-prefix properties for each of the 3 hosts. Submit each host's sitemap.
2. **API budgets:**
   - Search Analytics pulls are safe up to 1,200 QPM per site.
   - URL Inspection API allows **2,000 inspections per day per site** (600 QPM), so sample important URLs rather than all of them.
3. **Weekly checks:** Page indexing (soft 404s, "Duplicate, Google chose different canonical", Crawled-not-indexed), Merchant listings and Product snippets, Core Web Vitals (INP < 200 ms), Manual actions, Security.
4. **AI visibility:**
   - Track AI-feature traffic within "Web".
   - Don't buy `llms.txt` or "AI schema" services; Google says they're unnecessary.
   - Don't use `nosnippet` on legal articles unless you deliberately want to opt out of AI Overviews; it also removes normal snippets.
5. **Core updates:** on each update (core updates in Mar, May and Dec of recent years), compare before and after windows of at least 1 week. Fix quality issues; don't make quick technical tweaks.
