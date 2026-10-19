# بررسی تکرار و کانیبالیزیشن — ۱۰ مقاله‌ی مدنی (۲۶ مهر ۱۴۰۵)

روش: سایت‌مپ‌های post/page/courses/product دادرز (حدود ۳۸۰ آدرس؛ ۲۱۴ پست) خوانده شد؛ پست‌ها و صفحه‌های نامزد واکشی و H1/محتوا بررسی شد؛ داده‌ی GSC زنده (۲۰۲۶-۰۷-۰۱ تا ۲۰۲۶-۱۰-۱۷؛ `gsc.py` فقط خواندنی) و CSVهای `seo-research/gsc` استفاده شد. شمارش کلمه تقریبی است (متن اصلی هر پست حدود ۱٫۳ تا ۱٫۵ هزار کلمه).

- فایل `21-new-articles/E4-inheritance.md` در مخزن `dadrose-seo` وجود ندارد (جست‌وجو شد)؛ `19-topic-map-civil` هم نیست. در `04-keyword-map.csv` فقط سه ردیف برنامه‌ریزی‌شده (P2) مرتبط هست: فرار از دین، ابطال معامله فضولی، آرای وحدت رویه — هیچ‌کدام نوشته نشده.
- azmoon.dadrose.com: سایت‌مپ فقط صفحه‌های دسته‌ای (`/azmoon/civil`، `/questions/civil`، `/notes/civil`) و دو آزمون لینکی دارد؛ صفحه‌ی مقاله‌ای برای این ده موضوع ندارد.

## خلاصه‌ی احکام

| # | موضوع | حکم |
|---|---|---|
| 1 | تست حقوق مدنی آزمون وکالت | NEW (عبارت «ماده به ماده» را هدف نگیر) |
| 2 | قوانین خاص مدنی | MERGE در `/list-of-special-laws-for-the-bar-exam/` (یا بازتعریف موضوع) |
| 3 | معامله فضولی | NEW (دو پست نزدیک دارد؛ تمایز لازم) |
| 4 | انواع خیارات | NEW |
| 5 | فسخ/انفساخ/اقاله | NEW |
| 6 | فرار از دین | NEW |
| 7 | شروط باطل و مبطل | NEW (محدود به مواد ۲۳۲–۲۳۳؛ هم‌پوشانی با `/types-of-stipulations-within-a-contract/`) |
| 8 | طبقات ارث | NEW مکمل (`/inheritance-laws/` بسیار پربازدید است؛ لمس نشود) |
| 9 | انتفاع و ارتفاق | NEW |
| 10 | وحدت رویه مدنی | NEW (با دوره‌ی وحدت رویه رقابت نکند) |

## جدول به‌تفکیک موضوع

### 1) تست حقوق مدنی آزمون وکالت (`civil-law-bar-exam-tests`)
- موجود: `/courses/حقوق-مدنی-1-تا-8/` (۲۰۰؛ برای «تست حقوق مدنی ماده به ماده»: ۳۷۳ نمایش، ۱۷ کلیک، رتبه ۴٫۸). `/civics-tip-and-test/` («نکته و تست مدنی | سجاد یوسفی»؛ ۶۲ نمایش برای «نکته و تست مدنی»، رتبه ۶٫۵). `/bar-exam-test/` (عمومی، بدون درس). `/civil-law-for-preparing-for-the-bar-exam/` (مرور مواد ۱–۱۰۰).
- GSC برای «تست حقوق مدنی (آزمون وکالت)»: عملاً صفر (۵ نمایش، رتبه ۷٫۶ برای «تست حقوق مدنی» روی `/civics-tip-and-test/`).
- حکم: **NEW**. «تست حقوق مدنی ماده به ماده» مال صفحه‌ی دوره است؛ در Title/H1/H2 نیاور. اسلاگ مشکلی ندارد.

### 2) قوانین خاص حقوق مدنی (`civil-law-special-laws`)
- موجود: `/list-of-special-laws-for-the-bar-exam/` (۲۰۰؛ حدود ۱٫۷–۲٫۴ هزار کلمه). GSC «قوانین خاص مدنی»: ۴۰۰ نمایش رتبه ۶٫۹؛ «…کانون وکلا» ۱۸۳ نمایش رتبه ۴٫۹؛ «…۱۴۰۵» ۷۲ نمایش رتبه ۱٫۷ (۲۲ کلیک)؛ «قوانین خاص آزمون وکالت ۱۴۰۵» رتبه ۱٫۶. صفحه‌ی دوره‌ی `/courses/مجموعه-قوانین-خاص-حقوقی-و-کیفری-جزوه/` هم برای «قوانین خاص مدنی» ۵۷۵ نمایش رتبه ۶٫۳ و برای «قوانین خاص حقوق مدنی» ۱۲۸ نمایش رتبه ۵٫۸ دارد. همچنین `/a-collection-of-specific-legal-and-criminal-laws/` و `/special-civil-liability-law/`.
- حکم: **MERGE** در `/list-of-special-laws-for-the-bar-exam/` — کلمه‌ی کلیدی یکی است و دو صفحه رتبه دارند؛ مقاله‌ی سوم کانیبالیزیشن می‌سازد. اگر مالک اصرار دارد: بازتعریف به «مواد مهم قوانین خاص مدنی + تست»، اسلاگ پیشنهادی `civil-special-laws-key-articles`، بدون «قوانین خاص مدنی» در Title/H1. اصلاح خود صفحه‌ی لیست جدا و با بکاپ، نه در این اسپرینت.

### 3) معامله فضولی (`unauthorized-transaction-civil-law`)
- موجود: `/unauthorized-transaction-and-discharge-of-obligations/` («سیر تا پیاز معامله فضولی و سقوط تعهدات | پیش‌مطالعه مدنی ۳»؛ معرفی ویدیو، ~۱٫۵ هزار کلمه، ۱۹ بار «فضول»). `/disposing-of-anothers-property-without-authorization/` («معامله به مال غیر…»؛ زاویه‌ی کیفری/فروش مال غیر، ۲۰ بار «فضول»). `/civics-tip-and-test/` بخشی درباره‌ی معامله فضولی دارد. `/sale-of-property-without-the-partners-permission/` (مشاع، کیفری).
- GSC: «معامله فضولی» ۰ نمایش در کل سایت؛ هر دو پست تقریباً بدون نمایش (مال غیر: ۲ نمایش رتبه ۸ و ۲۶).
- حکم: **NEW** با لینک به هر دو پست. خطر متوسط (اسلاگ و موضوع شبیه پست اول). Title/H1 دقیقاً «معامله فضولی در قانون مدنی…» (مواد ۲۴۷–۲۶۳)؛ زاویه‌ی کیفری «فروش مال غیر» را وارد نکن. اسلاگ spec برخوردی ندارد؛ برای فاصله‌ی بیشتر: `fuzuli-transaction-civil-law`.

### 4) انواع خیارات (`options-of-rescission-in-civil-law`)
- موجود: مقاله‌ی اختصاصی نیست. فقط اشاره: `/the-importance-of-civil-law-3-in-the-attorney-exam/` (۳ بار «خیار»)، `/deception-and-fraud-in-transactions/` (تدلیس/فسخ؛ ۳۶۰ نمایش برای «شکایت کیفری فریب در معامله»)، `/civil-rights-3/`.
- GSC: «خیار» و «انواع خیار» ۰ نمایش.
- حکم: **NEW**.

### 5) فسخ، انفساخ، اقاله (`termination-cancellation-rescission`)
- موجود: `/civil-rights-3/` (صفحه‌ی فروش دوره؛ بخش کوتاه «تفاوت اقاله و فسخ»)، `/deception-and-fraud-in-transactions/`.
- GSC: ۰ نمایش.
- حکم: **NEW**. به `/civil-rights-3/` لینک بده.

### 6) معامله به قصد فرار از دین (`transaction-to-evade-debt`)
- موجود: هیچ صفحه‌ی مرتبطی در سایت‌مپ نیست. فقط ردیف برنامه‌ریزی‌شده در keyword map (P2، اسلاگ `/blog/civil-law/transaction-to-evade-debt/`).
- GSC: «قصد فرار» ۰ نمایش.
- حکم: **NEW**. شماره‌ی مواد (۲۱۸ و ۲۱۸ مکرر و قانون نحوه‌ی اجرای محکومیت‌های مالی) در CLAIMS تأیید شود.

### 7) شروط باطل و مبطل (`void-and-invalidating-conditions`)
- موجود: `/types-of-stipulations-within-a-contract/` («انواع شروط ضمن عقد و قوانین مربوط به آنها»؛ ~۱٫۴ هزار کلمه؛ بدون «مبطل»). GSC: «انواع شروط ضمن عقد» ۱۶۰ نمایش، ۲ کلیک، رتبه ۸٫۷؛ «شرط باطل» ۰.
- حکم: **NEW** ولی محدود به باطل/مبطل (مواد ۲۳۲–۲۳۳) و ضمانت اجرا؛ «انواع شروط ضمن عقد» را هدف نگیر (مال پست موجود). لینک به آن پست.

### 8) طبقات ارث (`inheritance-classes-in-civil-law`)
- موجود: `/inheritance-laws/` («نکات و قوانین مربوط به ارث؛ آیا ارث دختر و پسر مساوی شد؟»؛ ~۱٫۵ هزار کلمه؛ H2 «انواع رابطه برای ارث بردن (طبقات وراث نسبی)») — پرنمایش‌ترین پست بلاگ (حدود ۱۹ هزار نمایش در فایل quick-wins؛ «آیا سهم الارث پسر و دختر مساوی شده است» ۲٫۹ هزار نمایش در سه‌ماه اخیر، رتبه ۵٫۴؛ «قانون ارث» ۱۶۵ نمایش رتبه ۵٫۸). صفحه‌ی ناقص `/مبحث-ارث/` (~۱۸۶ کلمه). محصول `/product/دوره-نوین-و-نموداری-ارث/`. `/types-of-wills/`.
- GSC برای «طبقات ارث» و «حجب»: ۰ نمایش مستقل.
- حکم: **NEW مکمل** — فقط طبقات، حجب، جدول فروض، تکنیک حل؛ بدون دختر/پسر، «قانون ارث»، سهم‌الارث فرزندان و زن/شوهر (مال `/inheritance-laws/`). یک لینک طبیعی به `/inheritance-laws/`. در این اسپرینت به آن صفحه دست نزن.

### 9) تفاوت حق انتفاع و ارتفاق (`usufruct-and-easement-difference`)
- موجود: مقاله‌ی اختصاصی نیست. `/eliminative-method-for-civil-law-2/` (۶ بار «انتفاع»)، `/civil-law-for-preparing-for-the-bar-exam/` (یک اشاره).
- GSC: ۰ نمایش.
- حکم: **NEW**.

### 10) آرای وحدت رویه مدنی (`civil-law-unifying-precedents`)
- موجود: دوره‌ی `/courses/آرای-وحدت-رویه-5-سال-اخیر-1400-تا-1404/` و `/product/…` (هر دو ۲۰۰، InStock): «آرای وحدت رویه برای آزمون وکالت» ۱۳۸ و ۱۱۱ نمایش، رتبه ۶٫۱ و ۵٫۰. `/oath-in-law/` («رای وحدت رویه سوگند تکمیلی» ۱۰۶ نمایش رتبه ۸٫۰). `/4-unanimous-vote/` و `/submission-to-the-opinion-in-complicity/` (کیفری).
- حکم: **NEW**، با خطر متوسط با صفحه‌ی دوره. کلمه‌ی کلیدی «آرای وحدت رویه حقوق مدنی» (نه «…برای آزمون وکالت» که مال دوره است)؛ پیشنهاد Title: «مهم‌ترین آرای وحدت رویه حقوق مدنی (آپدیت ۱۴۰۵)». لینک به دوره و `/oath-in-law/`. شماره‌ی رأی فقط با منبع رسمی.

## آدرس‌های زنده برای لینک داخلی (GET واقعی، همه ۲۰۰)

- دوره‌ی مدنی ۱ تا ۸: https://dadrose.com/courses/حقوق-مدنی-1-تا-8/ — زنده، `InStock`، دکمه‌ی خرید فعال، در منوی اصلی؛ دوره‌ی متوقف نیست. معادل محصول: https://dadrose.com/product/حقوق-مدنی-1-تا-8/ (۲۰۰). از /courses/ استفاده کن.
- https://dadrose.com/list-of-special-laws-for-the-bar-exam/
- https://dadrose.com/score-percentage-calculator/
- https://dadrose.com/important-topics-in-civil-law/
- دوره‌ی وحدت رویه: https://dadrose.com/courses/آرای-وحدت-رویه-5-سال-اخیر-1400-تا-1404/ (InStock)
- نکته و تست حقوق مدنی: https://dadrose.com/courses/نکته-و-تست-حقوق-مدنی/ (InStock)
- دوره‌ی نوین و نموداری ارث: https://dadrose.com/product/دوره-نوین-و-نموداری-ارث/ (InStock؛ آدرس /courses/ هم‌نام ۴۰۴ است)
- آزمون: https://azmoon.dadrose.com/azmoon/civil ، https://azmoon.dadrose.com/questions/civil ، https://azmoon.dadrose.com/

لینک‌های پیشنهادی (همه ۲۰۰ تأییدشده، مسیرها روی dadrose.com):

| مقاله | لینک‌های موضوعی |
|---|---|
| ۱ تست مدنی | `/civics-tip-and-test/`، `/bar-exam-test/`، `/answer-key-for-civil-law-by-the-bar-center-1404/`، `/analysis-of-civil-rights-exam-no-3/` |
| ۲ قوانین خاص | `/list-of-special-laws-for-the-bar-exam/`، `/special-civil-liability-law/`، `/a-collection-of-specific-legal-and-criminal-laws/` |
| ۳ فضولی | `/unauthorized-transaction-and-discharge-of-obligations/`، `/disposing-of-anothers-property-without-authorization/`، `/civil-rights-3/`، `/the-importance-of-civil-law-3-in-the-attorney-exam/` |
| ۴ خیارات | `/deception-and-fraud-in-transactions/`، `/civil-rights-3/`، `/the-importance-of-civil-law-3-in-the-attorney-exam/` |
| ۵ فسخ/اقاله | `/civil-rights-3/`، `/deception-and-fraud-in-transactions/` |
| ۶ فرار از دین | `/sale-of-property-without-the-partners-permission/`، `/important-topics-in-civil-law/` |
| ۷ شروط | `/types-of-stipulations-within-a-contract/`، `/civil-rights-3/` |
| ۸ ارث | `/inheritance-laws/`، `/types-of-wills/`، دوره‌ی نموداری ارث |
| ۹ انتفاع/ارتفاق | `/eliminative-method-for-civil-law-2/`، `/civil-law-for-preparing-for-the-bar-exam/`، `/important-topics-in-civil-law/` |
| ۱۰ وحدت رویه | دوره‌ی وحدت رویه، `/oath-in-law/` |

## یادداشت‌های ریسک
- `/مبحث-ارث/` و `/حقوق-مدنی-2/` صفحه‌های کم‌محتوا (~۶۰۰ کلمه یا کمتر)اند؛ لینک نده.
- بازه‌ی GSC سه‌ماهه است؛ ۰ نمایش یعنی امروز هیچ صفحه‌ای روی آن عبارت رتبه ندارد، نه نبودِ کامل تقاضا.
- کانیبالیزیشن جدی فقط در #۲ (بالا)، و کنترل‌شده در #۸ و #۱۰ و #۷ است.
