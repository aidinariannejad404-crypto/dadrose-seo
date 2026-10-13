# 04: Keyword analysis for dadrose.com, the book store and azmoon.dadrose.com

Prepared 2026-10-13 (21 Mehr 1405). The keyword map is in `04-keyword-map.csv` (456 rows, UTF-8 with BOM).

> **No search volumes.** This study had no paid tools. Semrush was not used because the account has no API units. Every "demand" value below and in the CSV is a **qualitative estimate** taken from autocomplete behaviour. None of it is a volume figure. Section 8 lists the data sources that would confirm the estimates.

---

## 1. Method

| Step | What was done | Source label used in CSV |
|---|---|---|
| Autocomplete harvest | About 70 seeds were queried against `suggestqueries.google.com/complete/search?client=firefox&hl=fa&gl=ir`. Each call returns up to 10 suggestions. The seeds were the brief's own list plus seeds found along the way, such as جزوه، برنامه ریزی، تراز، مواد مهم، اختبار، کارآموزی and دفترچه. | `Google Autocomplete (hl=fa, gl=ir) \| seeds: …` |
| Bing cross-check | `api.bing.com/osjson.aspx?market=fa-IR` was queried for the head term آزمون وکالت. | `Bing Autosuggest (fa-IR)` |
| SERP observation | WebSearch was run for about 20 head and mid terms. **WebSearch is US-based and not Iran-localised**: several queries returned English (US bar exam) results, and the results show no PAA boxes and no SERP features. The Persian results still show clearly which domains dominate. | `WebSearch SERP observation 2026-10-13` |
| Site check | The dadrose.com homepage was fetched. It has `/courses/{slug}/`, `/blog/`, a **score calculator at `/score-percentage-calculator/`** and course types (صفر تا صد، جمع‌بندی، نکته و تست، رایگان). The store link points to **dadrosebook.com**, not book.dadrose.com. Fetches of azmoon.dadrose.com and dadrosebook.com were blocked by robots. | n/a |
| Normalisation | Persian and Latin digits were merged (۱۴۰۵ = 1405), as were ازمون and آزمون, and انلاین and آنلاین. When several spellings appeared, the extra spellings are listed in `notes` ("Variants seen") and count as a demand signal. Off-topic suggestions were dropped, such as company fraud and bankruptcy news for کلاهبرداری and ورشکستگی, and "کیم کارداشیان". | n/a |
| Rows not from autocomplete | 13 rows come from SERP titles or from dadrose's existing products. Their `source` says "SERP observation" or "Derived (unvalidated)". | n/a |

**Demand estimate (the `demand_signal` column):**
- **High**: the suggestion was in position 1–2 for its seed, or it appeared in 2 or more seed lists, or it appeared in 2 or more spellings.
- **Medium**: position 3–6.
- **Low**: position 7–10.

Autocomplete rank reflects relative popularity *among completions of that prefix only*. It does not compare across seeds. For example, "قانون مدنی ماده ۱۰" at position 1 says nothing about its size relative to "آزمون وکالت".

**Priority** = business value (1–3) × demand estimate (1–3) × feasibility (1–3).
- P1 is a score of 18 or more. P2 is 8–17. P3 is below 8.
- Navigational and competitor-brand queries are always P3.
- Lower feasibility was given to: statute-article lookups (edalatsara.com and wikihoghoogh.net dominate), city "کلاس" queries (dadrose is online) and queries naming a rival author or publisher.
- Business value reflects the KPIs: signups on azmoon and purchases in courses and books score 3; generic doctrine articles score 2 or below.

**Counts:**
- Priority: 104 P1, 235 P2, 117 P3.
- Many P1 rows point to the **same URL**. In practice, P1 means about 20 pages, listed in section 4.

---

## 2. Topic clusters (pillar → supporting pages)

| # | Cluster (CSV `cluster`) | Rows | Pillar page (site · slug) | Supporting pages | Main KPI |
|---|---|---|---|---|---|
| 1 | **Bar exam: hub & calendar** | 49 | dadrose.com `/blog/bar-exam/` — "آزمون وکالت ۱۴۰۵: زمان، شرایط، منابع، دروس" | `/blog/bar-exam/registration/`, `/eligibility/` (شرایط، ظرفیت، بدون لیسانس، طلاب، خانم‌ها، پایان خدمت), `/kanoon-vs-markaz/`, اختبار definition section | Assisted signups |
| 2 | **Past papers & keys** (سوالات/نمونه سوالات/کلید/دفترچه/پاسخنامه تشریحی) | 32 (+2 SERP) | azmoon `/past-papers/bar-exam/` | One practice exam per year × body: `kanoon-1404`, `markaz-1404`, `kanoon-1403`, … Each has a dadrose article with the key and explained answers | **Signups (highest)** |
| 3 | **Mock exams / online tests** (آزمون آزمایشی، آزمون آنلاین، تست آزمون وکالت) | 18 (+1) | azmoon `/mock-exams/bar-exam/` | A free mock (signup-gated), the paid series schedule, and the 1405 series | Signups, purchases |
| 4 | **Results & score** (کارنامه، رتبه، تراز، نصاب، نتایج، تخمین، درصدگیری) | 33 (+2) | dadrose `/score-percentage-calculator/` (exists) | `/blog/bar-exam/results-cutoff/` (تراز, حد نصاب, how تراز is calculated, past cut-offs) | Signups (calculator → account) |
| 5 | **Resources & key articles** (منابع، مواد مهم) | 19 (+1) | dadrose `/blog/bar-exam/sources-1405/` | One "مواد مهم {درس} در آزمون وکالت" page per subject, in `/blog/{subject}/key-articles-bar-exam/`, plus `/blog/bar-exam/unified-rulings/` | Book and course clicks |
| 6 | **Books** (کتاب/جزوه آزمون وکالت) | 21 (+2) | book `/category/bar-exam/` | `/category/bar-exam/test-books/`, `/category/bar-exam/summaries/` (جزوه), a 1405 sources bundle, `/category/law-collections/` | Purchases |
| 7 | **Courses & planning** (دوره، کلاس، برنامه ریزی، مشاوره، جمع‌بندی) | 23 (+2) | dadrose `/courses/bar-exam/` | `/blog/bar-exam/study-plan/` (برنامه ریزی ۱۴۰۵، برای شاغلین), `/consultation/`, `/courses/bar-exam/review/` (جمع‌بندی) | Purchases, leads |
| 8 | **Subject tests ×7** (تست حقوق مدنی / آ.د.م / جزا / آ.د.ک / تجارت / اساسی / ثبت) | 58 | azmoon `/tests/{subject}/` | Sub-topic tests, e.g. مدنی ۱ اشخاص و محجورین, جزای عمومی ۱, ماده به ماده. Each subject links to its book category and course | **Signups** |
| 9 | **Subject books ×5** | 23 | book `/category/{subject}/` | Author pages for titles you stock (توکلی، شمس، کاتوزیان، بیات، سید جعفری…) | Purchases |
| 10 | **Subject pillars** (حقوق مدنی، حقوق جزا چیست، آ.د.ک چند ماده دارد…) | 22 | dadrose `/blog/{subject}/` | Links down to the doctrine articles and across to the course | Course clicks |
| 11 | **Doctrine articles** (ابطال معامله، مهلت تجدیدنظر، دستور موقت، واخواهی، اعاده دادرسی، خلع ید، الزام به تنظیم سند، خسارت تاخیر تادیه، ضمان قهری، مسئولیت مدنی، فسخ، چک) | 65 | dadrose `/blog/{subject}/{topic}/` | Each article has a "در آزمون وکالت" box plus 5 embedded tests linking to the azmoon topic page | Top-of-funnel traffic → signups |
| 12 | **Statute article lookups** (قانون مدنی/آ.د.م/ق.م.ا/تجارت ماده X) | 31 | dadrose `/laws/{code}/article-{n}/` | Only for exam-critical articles, each with exam notes and tests | Low (P3) |
| 13 | **Other exams**: قضاوت (20), ارشد حقوق (14), سردفتری (9), کارشناس رسمی (4) | 47 | dadrose `/blog/judiciary-exam/`, `/blog/law-masters-exam/`, `/blog/notary-exam/` | azmoon past papers for قضاوت and سردفتری | Phase 2 |
| 14 | Navigational (کانون وکلای X، مرکز وکلا، سایت اختبار) | 12 | No dedicated page; link to them from the hub | n/a | n/a |
| 15 | Internship (کارآموزی وکالت…) | 7 | `/blog/bar-exam/internship/` (post-exam content) | n/a | Retention |

---

## 3. Competitor and SERP observations

These are from WebSearch (US-located, so treat as indicative), checked 2026-10-13.

| Query observed | Who ranks | Content type | Notes |
|---|---|---|---|
| آزمون وکالت ۱۴۰۵ زمان ثبت نام | **ekhtebar.ir** (many URLs), iranestekhdam.ir, e-estekhdam.com | News and timeline posts | ekhtebar.ir runs a news cadence: one post per announcement ("فردا ۷ مهر؛ آخرین فرصت…"). These are news sites, not prep providers. |
| منابع آزمون وکالت ۱۴۰۵ | **ekhtebar.ir** only (separate کانون and مرکز pages, plus a "تهیه کتاب منابع ۱۴۰۵" sales page) | Guide plus commercial page | ekhtebar.ir also **sells the sources bundle**, so it competes directly with the book store. |
| نمونه سوالات آزمون وکالت با پاسخنامه تشریحی | e-estekhdam.com (paid ebooks, separate کانون and قوه قضاییه products), ekhtebar.ir (explained answers, "بانک سوالات" category) | Product pages and explained-answer posts | Nobody here offers **interactive** practice of past papers. That is azmoon's opening. |
| کتاب آزمون وکالت (خرید) | ekhtebar.ir, taaghche.com (ebooks: مجموع آزمون‌های وکالت و قضاوت، قانون یار) | Sales post, ebook store | Autocomplete names the publishers people look for: **چتر دانش، دوراندیشان، قوه قضاییه**, plus "دست دوم" and "رایگان". |
| آزمون آزمایشی وکالت | irantahsil.org (plus US noise) | Landing | Autocomplete names the mock-exam competitors: **مشاهیر، چتر دانش، دادستان، دادآفرین**. |
| دوره آمادگی آزمون وکالت آنلاین | irantahsil.org, heyvalaw.com | Landing and article | Autocomplete: مشاهیر, plus city "کلاس" queries (تهران، مشهد، شیراز، کرج، رشت، قزوین). |
| تست آیین دادرسی کیفری آزمون وکالت | ekhtebar.ir (explained answers per subject per year), 3gaam.com | Article | Subject-test queries carry **author names** (عمروانی، غفوری، کامفر، شهبازی، قربانی، توکلی…). People look for those textbooks as PDFs. |
| تفاوت کانون وکلا و مرکز وکلا | 3gaam.com, heyvalaw.com, ekhtebar.ir | Comparison article | Autocomplete also gives "تفاوت منابع …" and "تفاوت کارآموزی …". This is an easy comparison page to win. |
| مهلت تجدیدنظرخواهی | wikihoghoogh.net, wikifeqh.ir, edalatsara.com, davoudabadi.ir, heyvalaw.com | Wiki and law-firm articles | Legal reference wikis rank for doctrine terms. Practising law firms target the layperson angle. |
| شرایط ابطال معامله به قصد فرار از دین | edalatsara.com (rulings, نشست قضایی), magiran.com | Rulings and statute pages | edalatsara is strong on نمونه رای and نشست قضایی. dadrose should take the "for exam takers" angle. |
| قانون مدنی ماده ۱۰ | wikihoghoogh.net, edalatsara.com, heyvalaw.com | Statute pages | Low feasibility, so P3. |
| آزمون قضاوت ۱۴۰۵ / سردفتری ۱۴۰۵ | ekhtebar.ir | News | n/a |

**Takeaways:**
1. **ekhtebar.ir is the dominant SERP owner** for exam news, sources, explained answers and a book-sales page. To compete on news, dadrose needs a faster update cadence. It can beat ekhtebar on interactivity: online practice of past papers and per-topic tests.
2. **The prep brands people search by name** (مشاهیر، چتر دانش، دادستان، دادآفرین، دوراندیشان) appear only as brand modifiers in autocomplete. Plain "dadrose" queries never appeared, so brand demand is still small. Monitor this in GSC.
3. **"pdf / رایگان" modifiers recur** across every test and book cluster. Use free, signup-gated sample tests and PDFs as the conversion device.
4. **Forum intent** (نی نی سایت) appears for 1405, mock exams, classes, سردفتری and اختبار. Users want peer opinions, so add FAQ and "تجربه قبولی" sections.

---

## 4. Quick wins

The bar exam is about **3 weeks away**. The کانون exam is reported for 14 Aban 1405 (see section 6).

1. **Calculator + results page (now → Dey).** `/score-percentage-calculator/` already exists. Point "تخمین رتبه / تخمین تراز / محاسبه تراز / درصدگیری آنلاین / تراز چگونه محاسبه میشود" at it (P1). Add an explainer section and an internal link from the hub. Demand peaks the night of the exam, when the keys come out.
2. **"کلید آزمون وکالت ۱۴۰۵" + "دفترچه آزمون وکالت ۱۴۰۵" pages.** Publish the URL *before* the exam on the evergreen slug, with an "updated after the exam" notice. Fill it the same evening and link it to the calculator and to azmoon's past-paper version.
3. **Past papers on azmoon (P1).** Bring 1404 کانون and مرکز (then 1403 and 1402) into azmoon as free, signup-gated practice exams. Pair each with a dadrose article ("سوالات آزمون وکالت ۱۴۰۴ با پاسخنامه تشریحی"). Autocomplete shows this family at depth across years 98 to 1404.
4. **Subject test pages on azmoon (P1).** Build seven `/tests/{subject}/` pages, each with 10 free tests indexable as HTML plus a paid bank. Start with civil procedure, civil law, criminal law and commercial law, which have the deepest suggestion lists.
5. **"جمع‌بندی" and "جزوه شب آزمون" (P1, time-boxed).** Push the existing جمع‌بندی courses and sell summary booklets on the book store before the exam.
6. **کانون vs مرکز comparison page (P1, easy).** Weak competition (3gaam, heyvalaw). Cover four facets: exam, sources, internship and capacity.
7. **"مواد مهم {درس} در آزمون وکالت" ×7 (P1).** Autocomplete shows a ready-made seven-subject list. Each page ends with "practice these articles" (azmoon) and "the book that covers them" (book store).

---

## 5. Content gaps

These are demand signals with no strong targeted page in the observed results, or where dadrose has no matching asset:

- **Interactive past papers.** Competitors sell PDFs or ebooks (e-estekhdam) or publish static explained answers (ekhtebar). No one in the observed results offers a timed online version.
- **Per-sub-topic tests.** Searchers ask for "تست حقوق مدنی ۱ اشخاص و محجورین", "تست حقوق جزای عمومی ۱" and "تست حقوق مدنی ماده به ماده", so build tests per chapter and per statute article.
- **Tests for constitutional and registration law** ("تست قانون اساسی برای آزمون وکالت", "تست حقوق ثبت مرکز وکلا"). These are smaller subjects with a clear exam angle.
- **Planning content** ("برنامه ریزی آزمون وکالت ۱۴۰۵", "… برای شاغلین"). Competitor brands own this query family in autocomplete. A downloadable study plan that leads into the courses is missing.
- **Eligibility edge cases**: بدون لیسانس حقوق, بدون کارت پایان خدمت, طلاب, خانم‌ها, ظرفیت شهرها.
- **Unified rulings (آرای وحدت رویه) for the exam.** dadrose already has a course on these. The keyword is derived and needs GSC validation.
- **Other exams.** قضاوت (منابع ۱۴۰۵، جذب عمومی، سوالات ۱۴۰۴ pdf), سردفتری (سوالات ۱۴۰۳ با پاسخنامه) and ارشد حقوق (منابع ارشد حقوق خصوصی/جزا ۱۴۰۵) all show steady demand. These are phase-2 azmoon verticals.
- **Store gap.** Searchers name specific titles (توکلی، شمس، کاتوزیان، بیات، غفوری، عمروانی) and "دست دوم". Check stock and create a product or author page for each title you carry.

---

## 6. Seasonality calendar (1405 cycle)

Today is 21 Mehr 1405 (2026-10-13).

| Window (Solar Hijri) | Gregorian (approx.) | Event | Status / source | Keywords that spike |
|---|---|---|---|---|
| Tir 1405 | Jun–Jul 2026 | Exam date announced for کانون (اسکودا) | iranestekhdam.ir post dated 1405/04/23, titled "برگزاری آزمون وکالت در ۱۴ آبان ماه ۱۴۰۵"; ekhtebar.ir "تاریخ برگزاری آزمون وکالت ۱۴۰۵ اسکودا اعلام شد". **Headline only: the pages could not be fetched (robots)** | آزمون وکالت ۱۴۰۵ کی برگزار میشه، منابع ۱۴۰۵ |
| Late Shahrivar → 7 Mehr 1405 | ~Sep 2026 → 29 Sep 2026 | کانون registration | ekhtebar.ir headlines "ثبت‌نام آزمون وکالت ۱۴۰۵ کانون وکلای دادگستری (اسکودا) فردا آغاز می‌شود" and "فردا ۷ مهر؛ آخرین فرصت ثبت‌نام…" | ثبت نام آزمون وکالت ۱۴۰۵، شرایط، دفترچه |
| → 15 Mehr 1405 (after two extensions: 5 Mehr, then 15 Mehr) | → 7 Oct 2026 | مرکز وکلای قوه قضاییه registration | ekhtebar.ir headlines "فردا ۵ مهر؛ آخرین فرصت…", "تمدید مجدد مهلت…" and "فردا ۱۵ مهر؛ آخرین فرصت ثبت‌نام آزمون وکالت مرکز وکلای قوه قضاییه ۱۴۰۵" | ثبت نام مرکز وکلا ۱۴۰۵ |
| **14 Aban 1405** | **5 Nov 2026** | **کانون exam** | iranestekhdam.ir headline, unverified. The 1404 exam was on 15 Aban (ekhtebar.ir) and 1403 on 17 Aban (iranmoshavere.com), so mid-Aban is consistent | کارت ورود، کلید، دفترچه، درصدگیری، تخمین رتبه |
| Aban–Azar 1405 (TBC) | Nov–Dec 2026 | مرکز exam | No 1405 date found. 1403 was on 22 Azar (iranmoshavere.com) | Same as above, with مرکز modifier |
| ~1–2 months after each exam | Dey–Bahman 1405 | Results, کارنامه, تراز, حد نصاب, ظرفیت | Pattern from autocomplete ("نتایج … کی میاد", "کارنامه کانون ۱۴۰۴") | نتایج، کارنامه، حد نصاب، تراز |
| Bahman → Shahrivar 1406 | Feb–Sep 2027 | Long prep season for 1406 | Inferred | منابع ۱۴۰۶، برنامه ریزی، دوره، کتاب، آزمون آزمایشی |
| Variable | n/a | قضاوت (ekhtebar has a "تاریخ آزمون قضاوت ۱۴۰۵" page; date not retrieved). سردفتری 1405, a deferred 1404 round ("کارت آزمون سردفتری ۱۴۰۵ (معوق ۱۴۰۴)"). Also کارشناس رسمی | Unverified | n/a |

**Action:** confirm the official dates on sanjesh.org (registration and cards) and iranbar.org or scoda.ir (اسکودا), and on the قوه قضاییه مرکز وکلا portal, before publishing any date.

**Content timing:**
- Publish "1405" year pages on **evergreen URLs**, for example `/blog/bar-exam/` rather than `/blog/bar-exam-1405/`, and update the year in the title each cycle.
- Prepare the key, booklet and calculator pages at least 1 week before each exam.
- Push books and courses from Bahman onward, with a second push for جمع‌بندی and جزوه 4–6 weeks before the exam.

---

## 7. Topic-to-topic map (exam topic → article cluster → course → book)

This map is the cross-site linking scheme. Each subject node links in all three directions. Slugs are suggestions; the existing course slugs on dadrose are shown where known.

| Exam subject | azmoon (signup) | dadrose articles (traffic) | dadrose course (purchase) | book store category (purchase) | Key demand signals |
|---|---|---|---|---|---|
| **حقوق مدنی** | `/tests/civil-law/` (+ sub-topic: اشخاص و محجورین، اموال، قواعد عمومی قراردادها، ضمان قهری) | `/blog/civil-law/` pillar → ابطال معامله / فرار از دین, ضمان قهری, مسئولیت مدنی, فسخ قرارداد, key-articles-bar-exam; `/laws/civil-code/article-n/` for exam-critical articles (10, 190, 219, 220, 221, 183…) | existing `/courses/حقوق-مدنی-1-تا-8/` + نکته و تست | `/category/civil-law/` (توکلی، بیات، کاتوزیان، صفایی) | Deepest autocomplete set: تست حقوق مدنی (10), کتاب حقوق مدنی (10), قانون مدنی ماده (10), مواد مهم مدنی |
| **آیین دادرسی مدنی** | `/tests/civil-procedure/` | `/blog/civil-procedure/` → مهلت تجدیدنظرخواهی, دستور موقت, واخواهی, اعاده دادرسی, خلع ید, الزام به تنظیم سند رسمی, خسارت تاخیر تادیه (ماده ۵۲۲), key-articles | civil-procedure course | `/category/civil-procedure/` (شمس، توکلی، سید جعفری، شکری) | Largest doctrine cluster (42 rows) |
| **حقوق جزا** (عمومی/اختصاصی) | `/tests/criminal-law/` | `/blog/criminal-law/` pillar (حقوق جزا چیست، تا ماده چند است), key-articles; `/laws/penal-code/article-n/` | existing `/courses/advanced-general-criminal-law-course/`, `/courses/criminal-law-tips-tests/` | `/category/criminal-law/` (غفوری، اردبیلی) | تست حقوق جزا (10 suggestions), many author modifiers |
| **آیین دادرسی کیفری** | `/tests/criminal-procedure/` | `/blog/criminal-procedure/` (چند ماده دارد، چیست), key-articles | criminal-procedure course | `/category/criminal-procedure/` (خالقی، غفوری) | تست آ.د.ک pdf رایگان at position 1 |
| **حقوق تجارت** | `/tests/commercial-law/` | `/blog/commercial-law/` → چک برگشتی, ورشکستگی, شرکت سهامی; `/laws/commercial-code/article-n/` | commercial-law course; special laws (چک) | `/category/commercial-law/` (اسکینی، رشیدی نسب) | تست حقوق تجارت (10), مواد مهم تجارت |
| **حقوق اساسی** | `/tests/constitutional-law/` | key-articles (مواد مهم قانون اساسی در آزمون وکالت) | constitutional course | `/category/constitutional-law/` | "تست قانون اساسی برای آزمون وکالت" at position 1 |
| **حقوق ثبت** | `/tests/registration-law/` | key-articles (مواد مهم قانون ثبت) | registration-law course | `/category/registration-law/` | تست حقوق ثبت (incl. سردفتری, مرکز وکلا) |
| **اصول فقه / متون فقه** | `/tests/usul-fiqh/` | `/blog/usul-fiqh/` | existing `/courses/principles-of-islamic-jurisprudence-course/` | category | Not harvested. Add seeds next round |
| **Exam-wide** | `/mock-exams/bar-exam/`, `/past-papers/bar-exam/` | `/blog/bar-exam/` hub, sources-1405, study-plan, kanoon-vs-markaz, results-cutoff, registration, eligibility | `/courses/bar-exam/`, `/courses/bar-exam/review/`, existing `/courses/bar-exam-test-taking-techniques/` | `/category/bar-exam/` (+ test-books, summaries, sources bundle) | Head terms |

**Linking rules:**
- Every doctrine article links to its subject test page and to the course.
- Every azmoon test result screen shows "weak topic → read the article / buy the book".
- Every book category links to the matching free test.

---

## 8. Data gaps and how to confirm

| Gap | Impact | How to close it |
|---|---|---|
| No search volumes | Priorities are relative, not absolute | **Google Keyword Planner** (needs an Ads account; the Iran location may be restricted, so try "Persian language, all locations"). Also export the **GSC Performance → Queries** report for all three properties over the last 16 months |
| Google Trends not reachable (the API URL was refused) | No relative seasonality curve | Open Trends manually: geo=IR, 5 years. Compare آزمون وکالت, کلید آزمون وکالت, منابع آزمون وکالت, تست حقوق مدنی |
| No PAA / SERP features (WebSearch is US-based) | Cannot tell which SERP features exist | Check manually from an Iranian IP or VPN-free browser, or use GSC search appearance |
| No Iranian search engines covered (Google dominates, but there is some use of Bing and Yandex) | Minor | Bing suggestions matched Google's for the head term |
| Autocomplete was rate-limited (HTTP 429) after ~60 calls. The seeds خیار غبن and شرکت سهامی خاص were lost | Some doctrine seeds missing | Re-run them, plus the a–z and Persian-letter expansions (آزمون وکالت + ا…ی) at a slower rate |
| 1405 exam dates come from headlines only | Calendar accuracy | Verify on sanjesh.org / scoda.ir / the official مرکز وکلا site |
| azmoon and the book store could not be crawled (robots) | Slugs for those sites are proposals | Share the sitemaps or URL lists to align `suggested_url_slug` |
| Store domain mismatch: the site links dadrosebook.com, the brief says book.dadrose.com | Cross-site linking and canonicals | Confirm the canonical store domain |
| Brand demand for "dadrose" / "دادرس" not measured | Unknown navigational baseline | GSC branded-query filter |
