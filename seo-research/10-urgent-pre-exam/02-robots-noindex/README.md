# T1: اول noindex، بعد Disallow

**مشکل:** اگر صفحه‌ای در robots.txt بسته شود، گوگل دیگر آن را نمی‌خواند و noindex داخلش را هم نمی‌بیند. پس URL ایندکس‌شده در نتایج می‌ماند، فقط بدون توضیح ([Google: Block indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing)).

**وضع فعلی dadrose.com** (`03-technical-audit.md` §1.2، F1): robots.txt یک گروه جدا برای Googlebot دارد با `Allow: /`. پس گوگل همهٔ Disallowهای گروه `*` را نادیده می‌گیرد و الان cart، checkout، `?s=` و بقیه را می‌خواند. این را با `check_noindex.py` روی نسخهٔ خلاصهٔ فایل فعلی تست کردیم: برای Googlebot هیچ مسیری بسته نیست.

**خطر:** اگر کسی F1 را «درست» کند (گروه گوگل را بردارد) پیش از اینکه این صفحه‌ها از ایندکس خارج شوند، دقیقاً در تلهٔ T1 می‌افتیم.

**قاعدهٔ فوری تا بعد از آزمون:** به robots.txt دست نزنید. فقط noindex و ریدایرکت.

## ترتیب اجرا

### گام ۱ (همین هفته): noindex روی صفحه‌های غیرجست‌وجویی
در Rank Math:
1. **Titles & Meta ← Misc Pages:** «Noindex Search Results» روشن؛ «Noindex Password Protected Pages» روشن.
2. **Titles & Meta ← Others/Date Archives:** آرشیو تاریخ خاموش یا noindex. **Tags:** noindex.
3. برای هر صفحهٔ زیر، در ویرایشگر صفحه ← Rank Math ← Advanced ← Robots Meta: **No Index** (در فایل بازرسی، `/checkout/` همین الان noindex است):
   `/cart/`، `/cart-2/`، `/checkout/`، `/my-account/`، `/account/`، `/dashboard/`، `/login/`، `/login-2/`، `/login-page/`، `/user-login/`، `/forgot-password/`.
4. Rank Math صفحه‌های noindex را خودش از sitemap برمی‌دارد. چک: `https://dadrose.com/page-sitemap.xml` نباید این‌ها را داشته باشد (F2).

> صفحهٔ ورود تکراری (`cart-2`، `login-2`، ...) را اگر کاربر لازمش ندارد، به‌جای noindex با ۳۰۱ به نسخهٔ اصلی ببرید (گام ۲).

### گام ۲ (همین هفته): ۳۰۱ برای آدرس‌های تکراری که نمایش می‌گیرند
از `gsc/00-gsc-findings.md` §۳.۳ [م]. در Rank Math ← Redirections (نوع 301):

| از | به | نمایش در بازهٔ GSC |
|---|---|---|
| `/?p=22450` | `/if-the-tenant-does-not-vacate/` | ۴٬۵۰۶ |
| `/?p=22315` | `/what-are-the-exceptions-to-debt/` | ۴۸۶ |
| `/?p=22570` | `/age-requirement-for-the-bar-exam/` | ۳۵۱ |
| `/?p=22367`، `/?p=22620` | اول در سرچ کنسول «Test live URL» بزنید ببینید کدام نوشته‌اند | ۵۱۰، ۲۴۲ |
| `/خانه/` | `/` | ۶۳۰ |
| `/درباره-ما/` | صفحهٔ «دربارهٔ ما» اصلی (یکی از `/about-us/` یا `/درباره-سجاد-یوسفی/`، تصمیم شما) | ۲۹۱ |
| `/وکالت404/` | `/score-percentage-calculator/` | ۲٬۱۳۷ |
| `/dadrose404/` | صفحه‌ای که محتوایش نزدیک‌تر است؛ اگر نیست 410 | ۲۸۶ |

نکته: برای `?p=` قانون Redirection در Rank Math با «Exact match» روی `?p=22450` گاهی کار نمی‌کند. اگر نکرد، از گزینهٔ Regex استفاده کنید: منبع `^\?p=22450$`، یا مطمئن شوید نوشتهٔ تکراری حذف یا پیش‌نویس شده تا وردپرس خودش ریدایرکت کند.

### گام ۳: چک
```bash
python3 check_noindex.py
```
هر خط باید `OK` باشد. خط `T1 TRAP` یعنی صفحه noindex دارد ولی robots.txt بسته‌اش کرده.
در سرچ کنسول برای ۳ نمونه «URL Inspection ← Test live URL»: باید «Excluded by 'noindex' tag» یا «Page with redirect» بگوید.
(اختیاری، برای سرعت) ابزار **Removals** در سرچ کنسول این URLها را ۶ ماه از نتایج پنهان می‌کند؛ جای noindex را نمی‌گیرد.

### گام ۴ (بعد از آزمون مرکز وکلا، ۲۱ آذر؛ زودتر نه): robots.txt نهایی
شرط شروع: در سرچ کنسول ← Pages، صفحه‌های گام ۱ در گروه «Excluded by 'noindex' tag» باشند و `site:dadrose.com/cart` چیزی نشان ندهد.
1. پیش از تغییر:
   `python3 check_noindex.py --robots robots.txt.final` ← نباید هیچ صفحهٔ «index» (کلید، ماشین‌حساب) بسته باشد.
2. robots.txt را با `robots.txt.final` جایگزین کنید (Rank Math ← General Settings ← Edit robots.txt، یا فایل روی سرور).
3. سرچ کنسول ← Settings ← robots.txt ← «Request a recrawl».
4. یک هفته بعد: Pages ← «Blocked by robots.txt» فقط مسیرهای عمدی را داشته باشد؛ هیچ صفحهٔ محتوایی نباشد.

**چه تغییری در robots.txt.final هست و چرا:**
- گروه جدای Googlebot حذف شده، تا قانون‌ها برای گوگل هم اعمال شوند (F1).
- `*?*` حذف شده، چون صفحه‌های `?pg=2` دوره‌ها را هم برای بینگ می‌بست.
- `/wp-includes/` و `*.php` حذف شده‌اند. بستن JS و CSS جلوی رندر درست صفحه در گوگل را می‌گیرد.
- `/tag/` و `/date/` با noindex مدیریت می‌شوند، نه Disallow (همان قاعدهٔ T1).
- sitemap به `sitemap_index.xml` (خروجی Rank Math) اشاره می‌کند.
- اگر AdSense دارید، گروه `User-agent: Mediapartners-Google` با `Allow: /` را نگه دارید؛ روی گوگل‌بات اثر ندارد.

## همین قاعده برای سایت‌های دیگر
- **book.dadrose.com:** الان عمداً `noindex` (هدر) و `Disallow: /` دارد. روز راه‌اندازی **هر دو** باید برداشته شوند (T6). اگر فقط Disallow برداشته شود، هدر noindex می‌ماند.
- **azmoon (Next.js):** صفحه‌های `/login` و `/offline` با متای noindex بسته شدند، نه robots (در PR جدا روی dadrose-quiz).
