# G2 و G1: تست بار، کش کامل، نسخهٔ ایستای پشتیبان و پایش از بیرون ایران

مهلت: **تا ۱۰ آبان ۱۴۰۵** (چهار روز پیش از آزمون کانون، ۱۴ آبان).
دو URL هدف (همان صفحه‌های موجود، URL تازه ساخته نشود؛ `00-master-plan.md` §۵):
- `https://dadrose.com/questions-and-answer-key-of-the-1405-bar-exam/` (کلید آزمون)
- `https://dadrose.com/score-percentage-calculator/` (ماشین‌حساب درصد)

**داده‌ای که داریم [م]:** ماشین‌حساب در بازهٔ ۱۰ دی ۱۴۰۴ تا ۱۹ مهر ۱۴۰۵ حدود ۱۲٬۳۱۴ نمایش و ۱٬۲۲۷ کلیک گرفته (`gsc/clean/v2_05_page_queries.csv`). این بازه شب آزمون پارسال را ندارد، پس **اوج شب آزمون اندازه‌گیری نشده** است. برای همین تست بار پله‌ای است: ظرفیت سرور را پیدا می‌کند، به‌جای اینکه یک عدد فرضی را تأیید کند.

## فایل‌ها

| فایل | کار |
|---|---|
| `exam-night.k6.js` | تست بار پله‌ای (۱۰٪، ۲۵٪، ۵۰٪، ۱۰۰٪ اوج) با معیار قبولی. روی سرور محلی اجرا و تست شد. |
| `make-static-fallback.sh` | عکس ایستای دو صفحه را در `/var/www/exam-fallback` می‌سازد. |
| `nginx-exam-night.conf` | کش ۶۰ ثانیه‌ای فقط برای همین دو URL، و سرو نسخهٔ ایستا وقتی PHP خطا می‌دهد (فقط برای nginx). |
| `static-calculator.html` | ماشین‌حساب سبک بدون وابستگی (فرمول نمرهٔ منفی یک‌سوم). اگر ماشین‌حساب فعلی به `admin-ajax.php` وصل است، همین فایل جایگزین پشتیبانش می‌شود. در مرورگر تست شد: ۲۰ سؤال، ۱۰ درست، ۳ غلط ← ۴۵٪. |
| `uptime-from-outside-iran.yml` | GitHub Actions: هر ۳۰ دقیقه صفحه‌ها و robots.txt هر سه سایت را از سرور آمریکا (سمت گوگل‌بات) چک می‌کند. در همین ریپو در `.github/workflows/` هم گذاشته شده. |

## ۱. پیش از تست: سه چیز را بفهمید (۱۵ دقیقه)

1. **وب‌سرور و کش فعلی:** در هدر پاسخ صفحه نگاه کنید:
   `curl -sI https://dadrose.com/score-percentage-calculator/ | grep -iE 'server|x-litespeed|x-cache|cf-cache|ar-cache|x-powered'`
   - `LiteSpeed` ← بخش ۲-الف. `nginx` ← بخش ۲-ب. پشت ابرآروان یا Cloudflare ← بخش ۳ هم لازم است.
2. **ماشین‌حساب کجا حساب می‌کند؟** View source صفحهٔ ماشین‌حساب: اگر `admin-ajax.php` یا فرم POST دارد، هر کلیک به PHP می‌رود و کش صفحه کافی نیست. آن وقت `static-calculator.html` را جایگزین کنید یا دست‌کم پشتیبانش قرار دهید.
3. **سقف PHP:** تعداد `pm.max_children` در PHP-FPM یا `PHP_LSAPI_CHILDREN` در LiteSpeed را از هاست بپرسید. عدد تست را با آن مقایسه کنید.

## ۲. کش کامل همین دو صفحه

### ۲-الف. LiteSpeed Cache (اگر سرور LiteSpeed است)
- LiteSpeed Cache ← Cache: Enable Cache روشن؛ **Default Public Cache TTL** حداقل ۶۰۰ ثانیه.
- Cache ← Excludes: مطمئن شوید این دو URL در «Do Not Cache URIs» **نیستند**.
- Purge ← «Purge All - LSCache» را بعد از هر ویرایش کلید در شب آزمون بزنید (یا Auto Purge on post update را روشن بگذارید).
- **Serve Stale** روشن (در Cache ← Purge)، تا موقع ساخت دوبارهٔ کش نسخهٔ قبلی سرو شود.
- اگر Guest Mode و Crawler دارد: Crawler را برای این دو URL روشن کنید تا همیشه کش گرم باشد.

### ۲-ب. nginx + PHP-FPM
فایل `nginx-exam-night.conf` را طبق توضیح داخلش اضافه کنید، `sudo nginx -t`، بعد reload. چک:
`curl -sI .../score-percentage-calculator/ | grep -i x-cache-status` ← بار دوم باید `HIT` باشد.

### ۲-ج. افزونهٔ کش وردپرسی دیگر (WP Rocket و مانند آن)
همین اصول: این دو URL کش شوند، عمر کش دست‌کم ۱۰ دقیقه، preload روشن، و بعد از هر ویرایش purge.

### ۲-د. ماشین‌حساب را از افزونه‌های سنگین جدا کنید
با Asset CleanUp یا Perfmatters روی صفحهٔ ماشین‌حساب، اسکریپت‌هایی را که آنجا لازم نیستند خاموش کنید (اسلایدر، فرم تماس، چت، ووکامرس). هدف: کمتر از ۱۰ درخواست JS.

## ۳. اگر CDN دارید (ابرآروان یا Cloudflare)
- قانون کش برای همین دو مسیر: Cache Everything / Cache Level: Standard با Edge TTL ۲ تا ۵ دقیقه، و **bypass برای کوکی `wordpress_logged_in_`**.
- **Always Online / Stale-if-error** روشن، تا اگر origin افتاد لبه نسخهٔ قبلی را بدهد.
- **خطای 5xx و 404 را کش نکنید** (T4 در `09-gap-review.md`).
- چالش ضدربات (Under Attack / JS challenge) را برای خزنده‌های تأییدشدهٔ گوگل باز بگذارید. فهرست IP: `https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot`.
- بعد از هر تغییر CDN، در سرچ کنسول برای همین دو URL «Test live URL» بزنید.

## ۴. پایش uptime از بیرون ایران (G1)
- **اصلی (هر ۵ دقیقه، رایگان):** یک مانیتور HTTP در UptimeRobot یا Better Stack برای همان ۱۰ URL فایل yml؛ هشدار به ایمیل و تلگرام.
- **پشتیبان:** workflow `uptime-from-outside-iran.yml` که در `.github/workflows/` همین ریپو هست. اجرای دستی: تب Actions ← uptime-outside-iran ← Run workflow. اگر robots.txt یکی از سایت‌ها از بیرون ایران 200 نمی‌دهد، همین‌جا معلوم می‌شود (یافتهٔ F14 در `03-technical-audit.md`).
- از **داخل ایران** هم یک چک لازم است، چون کاربرها داخل‌اند: یک cron روی یک سرور ایرانی دیگر یا یک سرویس مانیتورینگ ایرانی.

## ۵. اجرای تست بار
نصب k6: `https://grafana.com/docs/k6/latest/set-up/install-k6/`

```bash
# ۱) تست سلامت، ۳۰ ثانیه با یک کاربر
k6 run -e MODE=smoke exam-night.k6.js
# ۲) تست پله‌ای، ساعت خلوت (۲ تا ۵ بامداد)، با خبر دادن به هاست
k6 run exam-night.k6.js                  # اوج ۲۰۰ کاربر هم‌زمان
k6 run -e PEAK=400 exam-night.k6.js      # اگر ۲۰۰ راحت رد شد
```
- **معیار قبولی** (داخل اسکریپت): خطا کمتر از ۱٪، p95 هر صفحه کمتر از ۲ ثانیه، p95 TTFB کمتر از ۸۰۰ میلی‌ثانیه. اگر خطا از ۱٪ بگذرد، تست خودش متوقف می‌شود.
- **عدد ۲۰۰ فرض است [ت]**، نه پیش‌بینی ترافیک. آنچه مهم است پله‌ای است که در آن خطا یا کندی شروع می‌شود. آن را در جدول نتایج runbook بنویسید.
- یک بار از داخل ایران و یک بار از بیرون اجرا کنید.
- خروجی `page-cache hit rate` باید بالای ۹۰٪ باشد. اگر صفر است، کش این صفحه‌ها کار نمی‌کند.

## ۶. نسخهٔ ایستای پشتیبان
```bash
sudo bash make-static-fallback.sh
```
- بعد از نهایی شدن کلید، و **بعد از هر ویرایش کلید در شب آزمون**، دوباره اجرا شود.
- چک: موقتاً PHP-FPM را روی staging متوقف کنید و صفحه را باز کنید؛ باید نوار زرد «نسخهٔ پشتیبان» دیده شود. روی سایت اصلی این تست را نکنید.
- نسخهٔ ایستا عمداً `noindex` ندارد: روی همان URL اصلی سرو می‌شود، و اگر گوگل‌بات در زمان خرابی آن را ببیند، noindex صفحهٔ اصلی را از ایندکس بیرون می‌اندازد.
