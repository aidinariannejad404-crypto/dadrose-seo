# 02 — AEO / GEO knowledge base (as of 2026-10-13)

Scope: how to appear in AI answer engines (Google AI Overviews / AI Mode / Gemini, ChatGPT, Perplexity, Copilot/Bing, Claude, Meta AI, DeepSeek, Grok, You.com, Apple) for the Persian legal-education network dadrose.com, book.dadrose.com, azmoon.dadrose.com.

Conventions:
- Every claim carries a source URL and the source's date (publication or "last updated"). "Accessed" = 2026-10-13.
- **[official]** = vendor documentation. **[study]** = third-party research/industry data. **[secondary]** = press/blog reporting of someone else's facts. **[inferred]** = my reasoning, not stated by any source. **[unverified]** = could not confirm from a primary source.
- No numbers below are invented. If a number appears, it is quoted from the source next to it.

---

## 0. Ten things to know first

1. Google says plainly that AEO/GEO for its surfaces **is SEO**: AI Overviews and AI Mode are "rooted in our core Search ranking and quality systems", use RAG over the Search index plus "query fan-out", and need **no llms.txt, no special schema, no chunking, no special phrasing** — https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (last updated 2026-07-10) [official].
2. Eligibility for Google AI features = page is indexed and eligible for a snippet. "There are no additional requirements" — https://developers.google.com/search/docs/appearance/ai-features (last updated 2025-12-10) [official].
3. Each non-Google engine has its **own crawler/index that must be allowed separately** (OAI-SearchBot, PerplexityBot, Claude-SearchBot, Bingbot, Meta-WebIndexer, YouBot, Applebot…). A `User-agent: *` disallow or a firewall/geo-block silently removes you from all of them.
4. **Training crawlers ≠ retrieval crawlers.** You can block training (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot, Meta-ExternalAgent) and still be cited in answers (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Googlebot, Bingbot, Meta-WebIndexer). Sources in §2.
5. Strongest academic evidence (GEO paper, KDD '24): adding **quotations, statistics and cited sources** raised source visibility in generative answers by up to ~40%; keyword stuffing performed **below baseline**; "Cite Sources" and "Statistics Addition" were among the best for the **Law & Government** category — https://arxiv.org/abs/2311.09735 (v3 2024-06-28) [study, peer-reviewed].
6. Citations are concentrated: "roughly 30 domains capture 67% of citations within a topic" in ChatGPT (Kevin Indig study reported 2026-03-24) — https://searchengineland.com/chatgpt-citations-domains-study-472349 [study/secondary]. Winning a slot in the Persian legal niche is a topical-authority game.
7. Off-site brand mentions correlated with AI Overview brand visibility more than backlinks (Spearman 0.664 vs 0.218; correlation only) — https://ahrefs.com/blog/ai-overview-brand-correlation/ (2025-05-26) [study].
8. Measurement now exists: GA4 has an **"AI Assistant" default channel** (excludes AI Overviews/AI Mode, which stay in Organic) — https://support.google.com/analytics/answer/9756891 [official]; Bing Webmaster Tools has an **AI Performance** report (citations, grounding queries) since 2026-02-10 — https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview [official]; Google Search Console's **Search Generative AI performance report** launched 2026-06 (UK sites first) — https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports [official, body not readable; details via secondary].
9. Iran context: ChatGPT, Claude and Gemini all list Iran as **unsupported** (official country lists, §7). Iran had near-total internet blackouts 2026-01-08 and 2026-02-28 → partial restoration 2026-05-26 — https://en.wikipedia.org/wiki/2026_Internet_blackout_in_Iran [secondary]. Users who reach AI tools do so via VPN/proxies, so they appear to engines as users in other countries [inferred].
10. **Critical local risk:** our own fetcher (an Anthropic agent that obeys robots.txt) was refused on book.dadrose.com, azmoon.dadrose.com, www.dadrose.com and dadrosebook.com with ROBOTS_DISALLOWED (see 03-technical-audit.md F14). Either robots.txt blocks non-Google agents or the hosts are unreachable from outside Iran. If that is what OAI-SearchBot / PerplexityBot / Claude-SearchBot / Bingbot also see, **those two sites are invisible to every AI answer engine** [inferred, must verify].

---

## 1. Google: AI Overviews, AI Mode, Gemini app

### 1.1 How sources are picked
- AI Overviews and AI Mode "may use 'query fan-out'", issuing multiple related searches across subtopics and data sources — https://developers.google.com/search/docs/appearance/ai-features (2025-12-10) [official].
- The 2026 guide names two techniques: RAG (retrieves "relevant, up-to-date pages from the Search index") and query fan-out — https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (2026-07-10) [official].
- AI Overviews show "only … when our systems determine that it is additive to classic Search" — ai-features page (2025-12-10) [official].
- Overlap with organic top 10:
  - Ahrefs (1.9M citations / 1M AI Overviews): 76.10% of cited pages ranked top 10; 86% in top 100; median organic rank of the first citation = 2 — https://ahrefs.com/blog/search-rankings-ai-citations (2025-07-21) [study].
  - A newer Ahrefs analysis (863k keywords, 4M AIO URLs) found only 38% of AIO-cited pages rank top 10; Ahrefs itself says methods changed so the datasets are not directly comparable — reported https://news.designrush.com/ai-overview-citations-drop-ahrefs (2026-04-24) → https://ahrefs.com/blog/ai-overview-citations-top-10/ [secondary]. Same article: Gemini 3 became the default model for AI Overviews globally in late January 2026 [secondary].
  - Takeaway [inferred]: ranking well remains the main lever, but fan-out means pages answering **sub-questions** of a topic can be cited without ranking for the head term.
- Who gets cited (US data): Wikipedia, YouTube, Reddit = 15% of AI summary sources; .gov = 6% of AI-summary sources vs 2% of standard results — Pew Research, https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ (2025-07-22) [study].
- Click impact (Pew, 900 US adults, March 2025): users clicked a traditional result on 8% of visits with an AI summary vs 15% without; clicked a link inside the summary on 1% — same Pew URL [study]. Google counters that clicks from AIO pages "tend to be higher quality" — ai-features page [official].
- Freshness: Google AI Overviews was the **only** platform in Ahrefs' 17M-citation study that cited slightly *older* content than organic (≈16 days older by publish date) — https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/ (2025-07-28) [study].

### 1.2 Persian language
- AI Mode added Persian (Farsi) in the 36-language expansion of 2025-10-08 — https://www.ghacks.net/2025/10/08/google-search-ai-mode-is-available-in-36-new-languages-and-45-regions/ [secondary]; Google's own post https://blog.google/products/search/ai-mode-expands-languages-locations/ does not list languages. A later expansion (2026-02-19) brought the list to just under 100 languages, still including Persian — https://www.seroundtable.com/google-expands-ai-mode-to-53-new-languages-40958.html [secondary]; official list: https://support.google.com/websearch/answer/16011537.
- Iran is **not** in the regions listed in the Oct-2025 expansion article [secondary]. Whether AI Overviews/AI Mode render for users physically in Iran is **[unverified]**; VPN users get the features of their exit country [inferred].
- Gemini app: Farsi is a supported language; Iran is **not** a supported country — https://support.google.com/gemini/answer/13575153 [official].

### 1.3 Controls (what each lever actually does)
| Lever | Effect | Source |
|---|---|---|
| robots.txt for Googlebot | controls crawling for Search incl. AI features | ai-features page [official] |
| `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex` | limit what is shown in Search incl. AI features | ai-features page [official] |
| `Google-Extended` (robots.txt token only) | opts out of Gemini model **training** and **grounding in Gemini Apps** and Vertex AI grounding; "does not impact a site's inclusion in Google Search"; does **not** remove you from AI Overviews/AI Mode | https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers [official]; AIO/AI-Mode point per https://www.searchenginejournal.com/google-gives-sites-ai-search-opt-out-but-not-the-data-to-use-it/577978/ (2026-06-06) [secondary] |
| Search Console AI opt-out toggle | domain-level opt-out of AI Overviews, AI Mode and Discover AI features without losing classic ranking; UK-only test since June 2026, global rollout planned; page-level controls due by March 2027 under the UK CMA requirement | SEJ 2026-06-06 (above) [secondary]; https://neilpatel.com/blog/gsc-ai-search-data-generative-ai-report/ [secondary] |
- Recommendation for dadrose [inferred]: **do not** use nosnippet/opt-out; **do not** block Google-Extended if you want to be cited in the Gemini app (grounding in Gemini Apps is inside its scope). Blocking Google-Extended is a reasonable choice only for paid course content you don't want trained on.

### 1.4 Google guidance that matters most for a legal site
- Non-commodity content: "Create the content yourself based on what you know about the topic"; avoid restating common knowledge; don't create many variant pages — ai-optimization-guide (2026-07-10) [official].
- "There's no ideal page length"; "no requirement to break your content into tiny pieces" — same [official].
- Inauthentic mentions are not helpful and are caught by spam systems — same [official].
- YMYL: trust is the most important part of E-E-A-T; Google "strongly encourage[s] adding accurate authorship information, such as bylines"; fabricated author profiles are deception — https://developers.google.com/search/docs/fundamentals/creating-helpful-content (2026-10-05) [official].
- Structured data: not required for AI features; must match visible text; still useful for rich results — ai-features page & ai-optimization-guide [official].
- Keep important content in text; allow crawling in robots.txt **and in any CDN/hosting setup** — ai-features page [official]. (Directly relevant to Iranian hosting/ArvanCloud firewalls.)

### 1.5 Measurement (Google)
- AI Overviews/AI Mode clicks are counted inside Search Console Performance → "Web" — ai-features page [official].
- New "Search Generative AI performance" reports: launched 2026-06-03; covers AI Overviews, AI Mode, Discover AI features; impressions only (no clicks/CTR/queries); dimensions page/country/device/date; data from 2026-05-18; started with UK sites — https://neilpatel.com/blog/gsc-ai-search-data-generative-ai-report/ [secondary]; official post https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports [official, content not readable by our fetcher]. Availability for an Iranian-audience property: **[unverified]** — check the GSC UI.
- GA4: AI Overviews/AI Mode traffic stays in **Organic Search**, not the AI Assistant channel — https://support.google.com/analytics/answer/9756891 [official].

---

## 2. Crawler / bot reference (training vs retrieval)

| Company | Token | Purpose | Blocking it means | Source |
|---|---|---|---|---|
| Google | Googlebot | Search index (feeds AIO, AI Mode, Gemini grounding) | gone from Google entirely | ai-features page [official] |
| Google | Google-Extended | robots token only: Gemini training + Gemini Apps/Vertex grounding | no training/grounding use; Search unaffected | google-common-crawlers [official] |
| Google | GoogleOther, Google-CloudVertexBot | R&D / customer Vertex agents | no Search effect | same [official] |
| OpenAI | **OAI-SearchBot** | ChatGPT search index | "will not be shown in ChatGPT search answers" (may still appear as bare navigational link) | https://developers.openai.com/api/docs/bots [official] |
| OpenAI | GPTBot | foundation-model training | training opt-out only | same [official] |
| OpenAI | ChatGPT-User | user-initiated fetches, GPT Actions; "robots.txt rules may not apply"; not used for search inclusion | — | same [official] |
| OpenAI | OAI-AdsBot | only visits pages submitted as ChatGPT ads | — | same [official] |
| Perplexity | **PerplexityBot** | Perplexity search index; "not used to crawl content for AI foundation models" | dropped from Perplexity results | https://docs.perplexity.ai/guides/bots [official] |
| Perplexity | Perplexity-User | user-initiated fetch; "generally ignores robots.txt" | — | same [official] |
| Anthropic | **Claude-SearchBot** | search index for Claude | "may reduce your visibility and accuracy in user search results" | https://support.claude.com/en/articles/8896518 (2026-04-07) [official] |
| Anthropic | Claude-User | fetch when a user asks Claude | reduces visibility for user-directed search | same [official] |
| Anthropic | ClaudeBot | training | training opt-out | same [official] |
| Microsoft | Bingbot | Bing index → Copilot, Bing AI summaries, partners | gone from Bing/Copilot | Bing WMT [official] |
| Meta | **Meta-WebIndexer** | Meta AI search; allowing it "helps Meta cite and link" | — | https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/ [official] |
| Meta | Meta-ExternalAgent | AI training + product indexing | — | same [official] |
| Meta | Meta-ExternalFetcher | user-requested fetch; may ignore robots.txt | — | same [official] |
| Meta | FacebookExternalHit | link previews | breaks share previews | same [official] |
| Apple | Applebot | Spotlight/Siri/Safari search; may train | — | https://support.apple.com/en-us/119829 (2026-09-04) [official] |
| Apple | Applebot-Extended | usage control only (training opt-out); "can still be included in search results" | — | same [official] |
| You.com | YouBot | You.com search index; "fully respects robots.txt", caches it 30 min | — | https://you.com/docs/youbot [official] |
| Common Crawl | CCBot | open web corpus (widely used as LLM training data) | — | https://commoncrawl.org/ccbot [official]; LLM-training use is [inferred/common knowledge, not stated on page] |
| xAI | xAI-SearchBot (and undocumented GrokBot etc.) | Grok search | — | https://knownagents.com/agents/xai-searchbot [third-party directory; no xAI doc found → unverified] |
| DeepSeek | DeepSeekBot | reportedly data collection/training | — | https://knownagents.com/agents/deepseekbot [third-party; deepseek.com/bot could not be fetched → unverified] |

- Propagation: OpenAI ~24 h after robots.txt change; Perplexity up to 24 h; Meta up to 24 h; YouBot 30 min — sources above [official].
- Verify bots by published IP lists: openai.com/searchbot.json, gptbot.json, chatgpt-user.json; perplexity.com/perplexitybot.json, perplexity-user.json; index.commoncrawl.org/ccbot.json — sources above [official]. Perplexity explicitly recommends matching UA + IP in WAF rules [official].
- Anthropic notes blocking its IPs "may not reliably opt you out"; use robots.txt per subdomain — support.claude.com article [official].

---

## 3. Per-engine coverage checklist

Format: **Index/crawler · How to get included · Controls · Signals that drive citation · How to measure.**

### 3.1 Google AI Overviews
- Index: Google Search index via Googlebot.
- Include: be indexed + snippet-eligible; rank for the head query or for fan-out sub-queries (§1.1).
- Controls: nosnippet / max-snippet / noindex; GSC AI opt-out (UK test). Google-Extended does **not** apply.
- Signals: core ranking + helpfulness; .gov/Wikipedia/YouTube/Reddit over-represented (Pew 2025); brand mentions correlate (Ahrefs 2025, correlation only).
- Measure: GSC Performance (Web) + GSC Generative AI report where available; GA4 Organic Search; manual prompt panel.

### 3.2 Google AI Mode
- Same index and controls as AIO; aimed at "complex questions and comparisons" with fan-out — ai-features page [official].
- Persian supported since 2025-10 [secondary].
- Top cited domains in a US monitored-prompt sample (Jan–Feb 2026): Fandom 7.16%, Wikipedia 5.21%, YouTube 4.91%, Reddit 4.19% — https://aisearch.similarweb.com/blog/most-cited-domains-llms/ (2026-04-14) [study, vendor data].
- Measure: as AIO.

### 3.3 Gemini app
- Grounding with Google Search; Google-Extended governs "grounding in Gemini Apps" — google-common-crawlers [official].
- Iran unsupported; Farsi supported — https://support.google.com/gemini/answer/13575153 [official].
- Gemini cited content ≈298 days newer by publish date than organic baseline — Ahrefs freshness study (2025-07-28) [study].
- Measure: GA4 AI Assistant channel (gemini.google.com listed as example) [official]; prompt panel.

### 3.4 ChatGPT (search, browsing, shopping)
- Index: OAI-SearchBot + "third-party search providers" + partner content — https://openai.com/index/introducing-chatgpt-search/ (2024-10-31) [official]. OpenAI publicly said this includes Bing (per https://searchengineland.com/openai-chatgpt-serpapi-google-search-results-461226, 2025-08-26 [secondary]); The Information reported OpenAI also used SerpApi-scraped Google results — **not confirmed by OpenAI** [secondary].
  - Practical implication [inferred]: be indexed in **both Bing and Google**, plus allow OAI-SearchBot.
- Include: "Any public website can appear in ChatGPT search"; don't block OAI-SearchBot; allow OpenAI IP ranges — https://help.openai.com/en/articles/12627856-publishers-and-developers-faq [official]. No submission form for organic search [official FAQ does not mention one].
- Controls: OAI-SearchBot disallow = out of answers; `noindex` meta excludes pages (crawler must be allowed to see it); GPTBot = training only — same FAQ [official].
- Browsing: ChatGPT-User fetches live pages on user request; robots.txt "may not apply" [official]. Pages must render server-side text for this to work [inferred].
- Signals (studies): pages ranked #1 in Google cited 43.2% of the time vs 3.5x less beyond top 20; ChatGPT retrieved ~6x more pages than it cited; ~1/3 of cited pages came from fan-out queries, 95% of which had zero search volume; key info near the top (10–20% section performed best; bottom 10% got 2.4–4.4% of citations) — Indig via SEL (2026-03-24) [study/secondary]. ChatGPT citations were 458 days newer by publish date than organic — Ahrefs (2025-07-28) [study]. Top domains (US monitored prompts): Wikipedia 13.15%, Reddit 11.97%, YouTube 2.67% — Similarweb (2026-04-14) [study].
- Shopping: merchants apply at chatgpt.com/merchants; feed spec at developers.openai.com/commerce; uploads target the US (Canada/Mexico need setup) — https://alhena.ai/blog/chatgpt-shopping-product-feed-guide/ [secondary, official URLs not opened]. **Not applicable** to book.dadrose.com (Iranian merchant, rial pricing) [inferred]; organic product-page citation still possible via OAI-SearchBot.
- Measure: `utm_source=chatgpt.com` is auto-appended to referral URLs — OpenAI FAQ [official]; GA4 AI Assistant channel [official]; prompt panel.

### 3.5 Perplexity
- Index: own index via PerplexityBot; live fetch via Perplexity-User — https://docs.perplexity.ai/guides/bots [official].
- Include: allow PerplexityBot + its IP ranges.
- Publisher program: Comet Plus ($5; 80% of revenue to participating publishers based on human visits, citations, agent actions); launch partners were major Western publishers; sign-up process not described — https://pressgazette.co.uk/news/perplexity-launches-ai-subscription-revenue-share-scheme-for-publishers/ (2025-10-02) [secondary]. Low relevance for dadrose [inferred].
- Shopping/merchant program: **[unverified]** in this research; not relevant to Iranian merchants [inferred].
- Signals: Perplexity in-text citations ≈250 days newer by publish date than organic (Ahrefs 2025) [study]. In a 12-week log study PerplexityBot fetched robots.txt 775 times and llms.txt 0 times — https://www.ezy.ai/research/do-ai-bots-read-llms-txt (window 2026-04-27→07-19) [study].
- Measure: Perplexity is **not** in GA4's AI Assistant channel definition; it stays in Referral → add a custom channel group — https://ga4-auditor.dev/en/blog/ai-traffic-ga4 [secondary].

### 3.6 Microsoft Copilot / Bing
- Index: Bing (Bingbot). AI Performance report covers "Microsoft Copilot, AI-generated summaries in Bing, and select partner integrations" — Bing blog 2026-02-10 [official].
- Include: Bing Webmaster Tools + complete XML sitemap with **accurate lastmod** (changefreq/priority ignored) + sitemap in robots.txt + IndexNow — https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search (2025-07-31) [official]. IndexNow submissions are shared with Amazon, Bing, Naver, Seznam, Yandex, Yep; Google not listed — https://www.indexnow.org/faq [official].
- Controls (Bing-specific trap): `NOARCHIVE` → "will not be included in Bing Chat answers"; `NOCACHE` → only URL/title/snippet shown — https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat (2023-09-22) [official]. Bing supports `data-nosnippet` since 2025-10-15 (Bing feed) [official]. **Audit all three sites for stray noarchive.**
- Signals — Microsoft's own guidance (Krishna Madhavan, Bing, 2025-10-08): aligned title/H1/meta description; descriptive H2/H3; Q&A pairs; lists and tables; JSON-LD schema; 1–2 sentence self-contained answers; avoid walls of text, answers hidden in tabs/accordions, core info only in PDFs or images, decorative symbols, unanchored claims — https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers [official]. AI Performance blog adds: depth around topics already cited, evidence/data, freshness via IndexNow, consistent entity descriptions across text/image/video [official].
- Measure: Bing WMT AI Performance (Total Citations, Average Cited Pages, Grounding Queries, page-level citations) [official]; GA4 AI Assistant channel lists Copilot [official].

### 3.7 Claude (web search)
- Index: Claude-SearchBot (Anthropic) + Claude-User live fetch [official]. Anthropic lists **Brave Search** (since 2025-03-19) and **turbopuffer** (2026-05-06) as web-search subprocessors — https://xponent21.com/insights/claude-web-search-brave-turbopuffer/ [secondary; primary is trust.anthropic.com]. That article states Brave won't crawl what Googlebot can't [secondary, unverified].
- Include: allow Claude-SearchBot and Claude-User on **each subdomain**; be crawlable by Brave (follow Google-accessible rules) [inferred].
- Controls: robots.txt per bot (ClaudeBot = training only) [official].
- Iran unsupported — https://www.anthropic.com/supported-countries [official].
- Measure: claude.ai referrals — GA4 definition currently does not name Claude (named in May 2026 announcement) → custom channel group [secondary: ga4-auditor].

### 3.8 Meta AI
- Index: Meta-WebIndexer for Meta AI search; Meta-ExternalAgent for training/indexing; Meta-ExternalFetcher for user fetches [official].
- Include: allow Meta-WebIndexer (and FacebookExternalHit for previews in WhatsApp/Instagram, which Iranians use heavily [inferred]).
- Measure: meta.ai referrer in custom channel group [secondary regex]. Availability in Iran **[unverified]**.
- Log anomaly worth knowing: in the ezy.ai study Meta-ExternalAgent fetched llms.txt 193 times vs robots.txt 172 [study].

### 3.9 DeepSeek
- No official crawler documentation found; DeepSeekBot appears only in third-party directories [unverified]. How DeepSeek's web-search mode sources pages is undocumented [unverified].
- GA4 AI Assistant channel names Deepseek as an example source [official].
- Practical: allow DeepSeekBot by default (no `*` block), be strong in Google/Bing [inferred].

### 3.10 Grok (xAI)
- No official crawler docs found; xAI-SearchBot listed by third-party directories [unverified]. Grok draws on X posts plus the web [secondary/common knowledge, unverified here].
- GA4 AI Assistant channel names Grok [official].
- Practical: an active X account posting summaries of new legal articles is the only Grok-specific lever [inferred, low priority for an Iranian audience].

### 3.11 You.com
- YouBot indexes for You.com search; respects robots.txt incl. crawl-delay — https://you.com/docs/youbot [official]. Low priority.

### 3.12 Apple (Siri/Spotlight/Safari)
- Allow Applebot; optionally disallow Applebot-Extended (training) without losing search — https://support.apple.com/en-us/119829 [official]. Low priority.

### 3.13 Persian-market assistants
- Iran unveiled a "first national artificial intelligence platform" (project start 2024-10-20; meant to keep working during internet disconnection); no name/LLM given — https://www.tehrantimes.com/news/510989/Iran-unveils-national-AI-platform [secondary]. No public documentation found on crawlers, citation behaviour or user numbers of any domestic Persian answer engine **[unverified]**.
- Implication [inferred]: during blackouts only domestic platforms (Iranian search engines, domestic messengers such as Eitaa/Bale, which dadrose already links per 03-technical-audit) remain reachable; keep content mirrored on domestically hosted pages and domestic channels.

---

## 4. llms.txt — status

- Google: "You don't need to create new machine readable files, AI text files, or markup" — ai-features page (2025-12-10) [official]; llms.txt "Google Search itself doesn't use them" and neither helps nor harms — ai-optimization-guide (2026-07-10) [official].
- OpenAI's publisher FAQ and bots docs do not mention llms.txt; Anthropic's crawler guidance points to robots.txt — sources in §2 [official, absence of mention]. OpenAI/Anthropic/Perplexity publish llms.txt for their own developer docs but none document consuming it in production — https://agentexperience.tech/insights/state-of-llms-txt/ (2026-09) [secondary].
- Server logs: Ahrefs (137,210 domains): 97% of llms.txt files got zero requests in May 2026; ~77% of bot requests came from non-AI tools — via agentexperience summary of https://ahrefs.com/blog/llmstxt-study/ (2026-06-15) [study/secondary]. ezy.ai (83 sites, 12 weeks): OpenAI 7 llms.txt fetches vs 3,990 robots.txt; Anthropic 9 vs 3,120; Perplexity 0 vs 775; Googlebot 67 vs 5,125 — https://www.ezy.ai/research/do-ai-bots-read-llms-txt [study].
- SE Ranking (~300k domains): no significant correlation between llms.txt and LLM citations — via agentexperience summary [study/secondary].
- Adoption estimates range 5.61% (top-10k sites, 2026-06-20) to 10.13% (~300k domains, 2025-11) — via agentexperience summary [study/secondary].
- Verdict: optional, near-zero cost, near-zero proven benefit. Ship a simple one for the course catalogue and exam guide only if a developer has 30 minutes; never prioritise over robots/crawlability [inferred].

---

## 5. Content tactics with evidence

### 5.1 GEO paper (Aggarwal et al., Princeton/IIT Delhi etc., KDD '24) — https://arxiv.org/abs/2311.09735 ; PDF https://arxiv.org/pdf/2311.09735v3
- Setup: GEO-bench, 10k queries (80% informational); generative engine = gpt-3.5-turbo over top-5 Google results; one source per query optimised; 5 seeds [study].
- Table 1, Position-Adjusted Word Count (overall), baseline 19.3: Quotation Addition 27.2, Statistics Addition 25.2, Fluency Optimization 24.7, Cite Sources 24.6, Technical Terms 22.7, Easy-to-Understand 22.0, Authoritative 21.3, Unique Words 20.5, **Keyword Stuffing 17.7 (below baseline)**. Best methods: +41% (PAWC) and +28% (Subjective Impression) [study].
- Domain fit (Table 3): Cite Sources best for Statement, Facts, **Law & Gov.**; Statistics Addition best for **Law & Gov.**, Debate, Opinion; Authoritative for Debate, History, Science; Quotation Addition for People & Society, Explanation, History [study].
- Rank effect: Cite Sources gave **+115.1%** visibility to rank-5 sources while the rank-1 site's visibility fell 30.3% — lower-ranked sites gain most [study].
- Combinations: Fluency + Statistics best, >5.5% over any single method (200-example subset) [study].
- Real engine (Perplexity.ai): improvements up to 22% (Quotation Addition, PAWC) and up to 37% on subjective metric [study].
- Caveats (authors): engines evolve, so methods may need to adapt; queries change over time; effect on search rankings not evaluated; GPT-3.5 used as evaluator; automated topic tags may be noisy [study]. My caveat [inferred]: 2023 models, English queries, synthetic setting — directionally useful, not a guarantee for 2026 Persian engines.
- Translation for legal content [inferred]: cite the **statute article** (ماده X قانون Y) with link to the official text, quote the article text verbatim, add verified figures (e.g., official exam capacity, pass marks, dates) with source, write fluently. These are the exact methods that scored best for Law & Gov.

### 5.2 Structure (answer-first, Q&A, tables)
- Microsoft: concise 1–2 sentence self-contained answers; Q&A pairs; tables; descriptive headings; no key answers hidden in tabs/accordions; no core info only in PDF/images — Bing 2025-10-08 [official].
- Google: clear paragraphs/sections/headings, but no need to "chunk" and no ideal length — 2026-07-10 [official]. Resolve the tension [inferred]: write a normal, complete article whose first paragraph directly answers the title question, then depth.
- ChatGPT: info in the first 10–30% of the page is cited most; long pages (>20k characters) averaged 10.18 citations vs 2.39 under 500 characters, except finance where short dense pages did better — Indig via SEL (2026-03-24) [study/secondary].
- Similarweb: deep, specific, single-topic pages are cited more than homepages (2026-04-14) [study].

### 5.3 Statistics, quotations, citations
- See §5.1. Bing also: "Support claims with evidence" and anchor claims in measurable facts (2026-02-10; 2025-10-08) [official].

### 5.4 Entity clarity
- Bing: keep text, images and video consistent in how they describe the same entities (2026-02-10) [official].
- Google: Organization/Person structured data must match visible content (ai-features) [official]. One Organization `@id` across hosts recommended in 03-technical-audit F17 [internal].

### 5.5 Structured data
- Google: not required for AI features; useful for rich results — [official]. Bing: recommends JSON-LD for FAQs, products, reviews, events (2025-10-08) [official]. Note: Google limited FAQ rich results to authoritative government/health sites in 2023 (post "Changes to HowTo and FAQ rich results", 2023-08, https://developers.google.com/search/blog/2023/08/howto-faq-changes; title verified, eligibility detail from prior knowledge — re-verify); FAQPage markup may still help Bing/others [inferred].

### 5.6 Freshness
- Ahrefs 17M citations: AI-cited URLs ≈25.7% fresher (publish date) than organic; Google AIO the exception; Mueller warns against changing dates without substantive changes (2025-07-28) [study].
- Bing: accurate `lastmod`, IndexNow (2025-07-31) [official].
- Legal implication [inferred]: laws change (e.g., amendments, new exam rules each year). Visible "آخرین بازبینی" date + changelog is both a trust and a freshness signal.

### 5.7 Brand mentions / off-site
- Ahrefs 75k brands: branded web mentions 0.664, branded anchors 0.527, branded search volume 0.392, DR 0.326, backlinks 0.218 (Spearman; correlation ≠ causation) (2025-05-26) [study].
- Google: seeking artificial mentions is not helpful (2026-07-10) [official]. → Earn real mentions, don't buy them.

### 5.8 Author credentials (YMYL)
- Bylines, author pages with real background; fabricated credentials = deception; trust is most important — creating-helpful-content (2026-10-05) [official].
- dadrose gap: articles bylined by a content-team member without author page/credentials; About page lacks پروانه وکالت number — 03-technical-audit F6 [internal].

---

## 6. Off-site signals that feed LLMs (training vs retrieval)

- **Two pathways** [inferred from §2 bot purposes]:
  1. *Training* (GPTBot, ClaudeBot, Google-Extended, CCBot, Meta-ExternalAgent, Applebot-Extended): the model "knows" your brand from its pretraining snapshot. Slow (model cutoffs), cannot be inspected, no citation link.
  2. *Retrieval/grounding* (Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, Claude-SearchBot, Meta-WebIndexer): live search → cited links → traffic. Fast, measurable.
  - For a small Persian brand, retrieval is where wins come from; allowing training crawlers mainly helps the model recognise "دادرز" as an entity in no-search answers [inferred]. Decision trade-off: paid course transcripts should not be crawlable by anything (they shouldn't be public at all — see F4 video leak).
- **Wikipedia/Wikidata**: Wikipedia was the #1 ChatGPT-cited domain (13.15%) in Similarweb's US sample [study]. Wikidata items require a sitelink, or a "clearly identifiable conceptual or material entity" describable with serious public references, or a structural need — https://www.wikidata.org/wiki/Wikidata:Notability [official]. Wikipedia COI rules: disclose, don't edit directly, propose on talk page; paid editors must disclose employer/client — https://en.wikipedia.org/wiki/Wikipedia:Conflict_of_interest [official]. → Don't write your own fa.wikipedia article; *do* improve neutral topic articles (e.g., «آزمون وکالت», «کانون وکلای دادگستری») with citations to official sources, and only cite dadrose where it is genuinely the best source (and disclose) [inferred].
- **Forums/Q&A**: Reddit 11.97% of ChatGPT citations in US sample [study]. Persian equivalents (legal Q&A sites, Ninisite-type forums, Telegram channels) — **no data found** on whether any LLM indexes them [unverified]. Public Telegram channels have a web view (t.me/s/…) that search engines can crawl [inferred]; private channels/Eitaa/Bale content is not indexable by foreign engines [inferred].
- **Video**: YouTube 2.67% (ChatGPT) and 4.91% (AI Mode) of citations in US sample [study]. YouTube is a Google property feeding Gemini [inferred]. Aparat: no evidence of LLM citation [unverified]. → Publish key explainer videos on YouTube with accurate Persian titles/descriptions and uploaded Persian captions; embed on the article [inferred].
- **News mentions / reviews**: brand-mention correlation (§5.7). Persian news sites covering the bar exam (results, capacity, dates) are natural places to be quoted as an expert source [inferred].

---

## 7. Iran / Persian specifics

- Service availability (official lists): ChatGPT — Iran not supported; access from unsupported locations "may result in your account being blocked or suspended" — https://help.openai.com/en/articles/7947663-chatgpt-supported-countries [official]. Claude — Iran unsupported — https://www.anthropic.com/supported-countries [official]. Gemini app — Iran not listed — https://support.google.com/gemini/answer/13575153 [official]. Copilot, Meta AI, Perplexity, Grok, DeepSeek availability in Iran — **[unverified]**.
- Usage despite restrictions: Digital Impact Lab argues Iranian traffic is routed via Azerbaijani address space (Delta Telecom AS29049) and links this to Azerbaijan rising from 44th to 3rd in OpenAI per-capita usage ranking (Q1→Q4 2025); the authors' link is inference from correlation — https://digimpactlab.substack.com/p/how-iran-made-azerbaijan-third-in-the-world-for-chatgpt-usage (2026-06-08) [study, low confidence]. No sourced figure for Persian AI-search usage share was found. **Do not quote any number for Iranian AI usage.**
- Connectivity: blackouts 2026-01-08 (whitelist mode from 01-28), renewed near-total blackout 2026-02-28 (NetBlocks ~4%, later ~1% of normal), partial restoration 2026-05-26 with heavy restrictions — https://en.wikipedia.org/wiki/2026_Internet_blackout_in_Iran ; https://www.iranintl.com/en/202605251140 [secondary].
  - Implications [inferred]: (a) AI referrals from Iran will be noisy and show up as foreign countries in analytics; (b) if dadrose servers are inside Iran, **foreign crawlers cannot reach them during blackouts** — repeated crawl failures can lead to de-indexing in Google/Bing and every AI engine at once; (c) consider a foreign-reachable origin/CDN for public content.
- Persian answer quality: FarsEval-PKBETS (4,000 items incl. **law** domain) found average accuracy below 50% for Llama3-70B, PersianMind, Dorna — https://arxiv.org/abs/2504.14690 (2025-04-20) [study; older/smaller models, not GPT/Gemini frontier]. Khayyam Challenge / PersianMMLU (20,192 Persian exam questions) — https://arxiv.org/abs/2404.06644 (2024-04-09) [study, no law track]. No benchmark found for frontier models on Iranian law [unverified]. Implication [inferred]: models are likely weak and hallucination-prone on Iranian statutes → they lean on retrieval → a precise, well-cited Persian source has an unusually good chance of being cited.

---

## 8. Measuring AI visibility (stack for dadrose)

1. **GA4**: AI Assistant default channel (medium `ai-assistant`; examples ChatGPT, Gemini, Deepseek, Copilot, Grok) — https://support.google.com/analytics/answer/9756891 [official]; switched on 2026-05-13, broad rollout ~2026-06-07, no backfill — https://ga4-auditor.dev/en/blog/ai-traffic-ga4 [secondary]. Add a custom channel group above Referral with regex `chat\.openai\.com|chatgpt\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com|grok\.|x\.ai|deepseek\.com|meta\.ai|you\.com` (same source) [secondary]. Also filter `utm_source=chatgpt.com` [official].
   - Blind spots: app traffic without referrer lands in Direct; copy-pasted URLs; AIO/AI Mode inside Organic [secondary].
   - Note: does dadrose run GA4 at all, or a domestic analytics tool? If domestic only, add server-log referrer analysis [inferred].
2. **Google Search Console**: Web performance (includes AIO/AI Mode clicks) + Generative AI report if exposed for the property [official/secondary].
3. **Bing Webmaster Tools AI Performance**: only first-party citation data any engine currently gives for Copilot/Bing [official]. Highest-value free tool for us.
4. **Server logs**: count hits by OAI-SearchBot, ChatGPT-User, PerplexityBot, Perplexity-User, Claude-SearchBot, Claude-User, Meta-WebIndexer, Bingbot, Googlebot; verify by IP JSON lists (§2). User-triggered fetchers (ChatGPT-User, Perplexity-User, Claude-User) are a proxy for "someone asked an AI about this page" [inferred].
5. **Manual prompt panel** (Playbook "Prompt panel"): monthly, same prompts, logged engine/date/cited URLs/brand mentioned. Third-party trackers exist; Google warns "No third-party tool has access to our internal ranking or AI systems" (2026-07-10) [official] — treat tool numbers as samples.

---

## 9. Risks: what counts as spam, what not to do

- Scaled content abuse: "many pages are generated for the primary purpose of manipulating search rankings", including "Using generative AI tools or other similar tools to generate many pages" without value; spam explicitly includes "attempting to manipulate generative AI responses in Google Search" — https://developers.google.com/search/docs/essentials/spam-policies (2026-08-28) [official].
- Site reputation abuse (third-party content riding host signals), expired domain abuse — same [official]. → Don't sell sponsored "guest posts" on dadrose.com; don't buy expired legal domains to redirect.
- Don't: mass-produce city × legal-topic pages ("وکیل طلاق در [شهر]"); keyword-stuff (scored below baseline in GEO paper); fake author profiles/credentials (creating-helpful-content) ; seed fake mentions on forums/Wikipedia (Google 2026-07-10; Wikipedia COI); change dates without real edits (Mueller via Ahrefs 2025-07-28); hide answers in accordions/tabs only (Bing 2025-10-08); serve different content to AI bots (cloaking, Google spam policies) [official].
- Don't add `noarchive` (kills Bing Copilot answers) or `nosnippet` (kills AIO) site-wide [official].
- Legal-specific [inferred]: an AI quoting an outdated law article from dadrose creates reputational/legal risk → every answer block needs the governing statute, effective date, and "last reviewed" date.

---

## Playbook for dadrose

Priority = impact × urgency. P0 = this week; P1 = this month; P2 = this quarter. Items marked [needs verification] depend on facts I could not observe from outside Iran.

### P0 — Make the sites reachable by every answer engine
1. **Verify reachability of azmoon.dadrose.com and book.dadrose.com from outside Iran** [needs verification]. In GSC (Domain property `dadrose.com`) run URL Inspection → Live test on each host's `/` and `/robots.txt`; in Bing WMT use URL Inspection; check Crawl Stats host status. If the firewall/ArvanCloud blocks foreign IPs, whitelist published bot IP ranges (googlebot.json, Bing, openai.com/searchbot.json, chatgpt-user.json, perplexity.com/perplexitybot.json, perplexity-user.json) or serve public pages from a foreign-reachable CDN origin.
2. **One robots.txt policy per host** (dadrose.com currently has Google-only groups that bypass the `*` rules — 03-technical-audit §1.2). Recommended shape for each host (adjust Disallow lines per host):
   ```
   # Retrieval / answer engines: allow
   User-agent: Googlebot
   User-agent: Bingbot
   User-agent: OAI-SearchBot
   User-agent: ChatGPT-User
   User-agent: PerplexityBot
   User-agent: Perplexity-User
   User-agent: Claude-SearchBot
   User-agent: Claude-User
   User-agent: Meta-WebIndexer
   User-agent: Applebot
   User-agent: YouBot
   User-agent: DuckDuckBot
   User-agent: *
   Disallow: /wp-admin/
   Disallow: /cart/
   Disallow: /checkout/
   Disallow: /my-account/
   Disallow: /*?s=
   Disallow: /*add-to-cart=
   Allow: /wp-admin/admin-ajax.php

   # Training crawlers: business decision (default below = allow public articles, block nothing extra)
   # To opt out of training only, uncomment:
   # User-agent: GPTBot
   # User-agent: ClaudeBot
   # User-agent: Google-Extended
   # User-agent: CCBot
   # User-agent: Meta-ExternalAgent
   # User-agent: Applebot-Extended
   # Disallow: /

   Sitemap: https://dadrose.com/sitemap.xml
   ```
   - Recommendation [inferred]: **allow training crawlers on dadrose.com articles** (brand/entity recognition in no-search answers is valuable for a small Persian brand); course videos/handouts must not be public at all. Keep Google-Extended allowed so Gemini-app grounding can cite you.
   - azmoon (Next.js `frontend/`, no `robots.ts`/`sitemap.ts` found in repo): add `app/robots.ts` and `app/sitemap.ts`; disallow `/login`, `/dashboard`, attempt/result URLs; allow public guide and topic pages.
3. **Remove any `noarchive`/`nocache`/`nosnippet`** from public pages (check Rank Math global robots meta and HTTP X-Robots-Tag) — Bing excludes noarchive pages from Copilot answers.
4. **Bing Webmaster Tools** for all hosts (import from GSC), submit sitemaps, enable **IndexNow** (Rank Math has an IndexNow module [inferred from plugin knowledge — verify]); make `lastmod` reflect real content edits.
5. Turn on GA4 AI Assistant channel review + custom channel group (regex §8) and a weekly server-log count of AI user-agents.

### P1 — dadrose.com (articles + courses): answer-ready legal pages
6. **Answer block on every legal article** (top of page, visible, not in an accordion):
   - H1 = the question as users ask it (e.g., «مهریه عندالمطالبه چیست و چگونه وصول می‌شود؟»).
   - 2–3 sentence direct answer that stands alone, naming the governing statute: «طبق ماده ۱۰۸۲ قانون مدنی …».
   - Bullet "نکات کلیدی" (3–5 items) + a table where comparison exists (e.g., مهریه عندالمطالبه vs عندالاستطاعه).
   - Verbatim quote of the statute article (blockquote) with link to the official text (qavanin.ir / rrk.ir) — matches GEO "Quotation Addition" + "Cite Sources".
   - Concrete figures only from official sources, each with source and date (GEO "Statistics Addition" — best for Law & Gov.).
   - Byline → real author page; «بازبینی حقوقی: [name]، وکیل پایه یک دادگستری، شماره پروانه …» + «آخرین بازبینی: [date]» + a short changelog line when the law changes.
   - Legal disclaimer line; Article + Person (`reviewedBy`) + BreadcrumbList JSON-LD matching visible text.
7. **FAQ section** (5–8 real questions from GSC queries / support tickets) at the end of key articles and course pages, as visible H3 questions with 1–3 sentence answers; FAQPage JSON-LD optional (helps Bing; no Google rich result expected).
8. **Author/entity hardening**: author pages for سجاد یوسفی and every writer (credentials, پروانه number, کانون membership, education, photo, links to profiles); Organization page with legal name, address, eNamad, founding year, sameAs (YouTube, Aparat, Telegram, Instagram, LinkedIn); single Organization `@id` reused on all hosts.
9. **Consolidate duplicates** (courses vs products, closed thin courses) so engines see one canonical answer per topic (03-technical-audit F3).
10. **Prune or merge commodity posts** that restate common knowledge; Google calls these commodity content (2026-07-10).

### P1 — azmoon.dadrose.com: the definitive «آزمون وکالت» hub
11. Build a public, server-rendered **«راهنمای جامع آزمون وکالت ۱۴۰۵»** hub (on azmoon or dadrose.com — pick one canonical; azmoon fits topical intent [inferred]):
    - Answer-first sections: چیست / شرایط ثبت‌نام / منابع و مواد آزمون با ضرایب / زمان‌بندی (ثبت‌نام، آزمون، نتایج) / نحوه محاسبه نمره و تراز / ظرفیت کانون‌ها / مرکز وکلای قوه قضاییه vs کانون وکلا / بعد از قبولی (کارآموزی).
    - Every number (dates, ظرفیت, ضرایب, minimum score) quoted from the official announcement with link and date; table per year (historical capacities) only from official sources.
    - "Updated on" stamp; update the same URL each year (don't spawn new URLs per year — keeps accumulated citations) with year-specific subsections.
12. **Topic pages per exam subject** (حقوق مدنی، آیین دادرسی مدنی، حقوق جزا، آیین دادرسی کیفری، حقوق تجارت، اصول فقه، قانون اساسی…): public page with what the subject covers, which statutes, question count/weight (official), study tips, 5–10 free sample questions with **explained answers citing the statute article**, FAQ, links to the matching course (dadrose.com) and book (book.dadrose.com).
13. **Public explained-question pages**: a curated set of past-exam questions with original explanations (genuinely written by the legal team; not mass-generated). Strong "non-commodity" content; target long-tail fan-out queries. Avoid thousands of thin auto-pages (scaled content abuse).
14. Keep app/test pages noindexed; make sure public pages render text server-side (ChatGPT-User/Claude-User fetch raw HTML [inferred]).

### P1 — book.dadrose.com: product pages AI can describe
15. Each book page: visible title, author, publisher, edition/year, ISBN, page count, price, table of contents (text, not image), "مناسب برای کدام آزمون/درس", sample pages as HTML text excerpt, honest reviews; Product/Book schema matching visible text. Merge or 301 dadrosebook.com vs book.dadrose.com (03-technical-audit F15).
16. Comparison/guide content ("بهترین منابع آزمون وکالت برای حقوق مدنی") written as genuine editorial with clear disclosure that dadrose sells some of the books; include competitors' books where they are the better option (trust) [inferred].
17. ChatGPT Shopping feeds are US/North-America focused — skip [secondary/inferred].

### P2 — Off-site entity presence
18. **Wikidata**: create/complete an item for دادرز only if it can be backed by independent published references (news coverage, official listings); otherwise wait. Never self-write a fa.wikipedia article; contribute neutral, well-sourced edits to «آزمون وکالت» / «کانون وکلای دادگستری» articles with COI disclosure where relevant.
19. **YouTube** (Gemini/AI Mode cite YouTube): one explainer video per hub section with Persian captions uploaded, description linking the canonical page. Mirror on Aparat for domestic users.
20. **Public Telegram channel** with web view (t.me/s/…) posting summary + link for each new article; same on Eitaa/Bale for domestic reach (not indexable abroad).
21. **Earned mentions**: offer expert commentary to Persian news sites when exam announcements/results drop; publish an annual "data report" on آزمون وکالت (official figures compiled + analysis) that journalists can cite. No paid link/mention schemes.
22. Optional low-effort: `/llms.txt` on dadrose.com listing hub, subject pages, top articles — zero proven benefit; only after P0–P1.

### Prompt panel (set up in P1) to track monthly (ChatGPT, Gemini, Perplexity, Copilot, Google AI Mode; logged in from a consistent VPN location; record cited URLs, whether دادرز is mentioned, and competitors cited)
1. آزمون وکالت ۱۴۰۵ کی برگزار می‌شود؟
2. شرایط ثبت‌نام آزمون وکالت چیست؟
3. منابع آزمون وکالت کانون وکلا کدام است؟
4. ضرایب دروس آزمون وکالت چقدر است؟
5. حداقل نمره قبولی در آزمون وکالت چند است؟
6. فرق کانون وکلا با مرکز وکلای قوه قضاییه چیست؟
7. بهترین کتاب برای حقوق مدنی آزمون وکالت چیست؟
8. بهترین دوره آنلاین آمادگی آزمون وکالت کدام است؟
9. برای آزمون وکالت از کجا شروع کنم؟ برنامه مطالعاتی ۶ ماهه
10. آزمون آزمایشی آنلاین وکالت رایگان
11. سوالات آزمون وکالت سال‌های قبل با پاسخ تشریحی
12. ظرفیت پذیرش کانون وکلای تهران در آزمون وکالت
13. دوره کارآموزی وکالت چند ماه است و چه مراحلی دارد؟
14. مهریه عندالمطالبه چیست و چطور وصول می‌شود؟
15. مراحل شکایت چک برگشتی چیست؟
16. شرایط طلاق توافقی چیست؟
17. تفاوت جرم کلاهبرداری و خیانت در امانت چیست؟
18. دادرز چیست؟ آیا دوره‌های دادرز معتبر است؟
19. سجاد یوسفی وکیل کیست؟
20. تراز آزمون وکالت چگونه محاسبه می‌شود؟
- Score per prompt: cited (URL), mentioned (name, no link), absent. Track share of prompts with a dadrose citation per engine per month; compare with Bing AI Performance grounding queries and GA4 AI Assistant sessions.

### What success looks like (leading indicators, no targets invented)
- Zero crawl/robots errors for all hosts in GSC + Bing WMT.
- Non-zero and rising: Bing AI Performance citations; GA4 AI Assistant + Perplexity sessions; log hits from OAI-SearchBot / Claude-SearchBot / PerplexityBot and their user-fetchers.
- Prompt panel: dadrose cited for the hub prompts (1–6, 20) and brand prompts (18–19) first; legal-topic prompts (14–17) later.
