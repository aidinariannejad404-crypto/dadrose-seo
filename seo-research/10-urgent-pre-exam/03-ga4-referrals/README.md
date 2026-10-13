# C2: درگاه‌های پرداخت در «unwanted referrals» گوگل آنالیتیکس ۴

**مشکل:** خریدار از سایت به درگاه بانکی می‌رود و برمی‌گردد. GA4 بازگشت را یک «سشن تازه با منبع zarinpal.com» ثبت می‌کند و خرید به‌جای جست‌وجوی گوگل به درگاه نسبت داده می‌شود. نتیجه: سهم واقعی سئو در فروش کمتر دیده می‌شود.
**راه‌حل رسمی:** [Google: Identify unwanted referrals](https://support.google.com/analytics/answer/10327750).
**اثر:** فقط از زمان ثبت به بعد. داده‌های گذشته درست نمی‌شوند، پس **پیش از اوج فروش شب آزمون** انجام شود.

## پیش‌نیاز (۵ دقیقه)
1. آیا روی dadrose.com و فروشگاه تگ GA4 هست؟ (ابزار ما اسکریپت‌ها را نمی‌دید، `03-technical-audit.md` بخش ۲): در Chrome، DevTools ← Network ← فیلتر `collect?v=2`. اگر درخواستی نیست، اول تگ GA4 نصب شود (Site Kit یا تنظیمات Rank Math ← Analytics).
2. دسترسی **Editor** یا بالاتر روی property لازم است.

## گام ۱: ببینید کدام درگاه‌ها واقعاً منبع ارجاع شده‌اند
Reports ← Acquisition ← Traffic acquisition ← بُعد را به **Session source** عوض کنید، بازهٔ ۹۰ روز. در جست‌وجوی جدول این‌ها را بزنید: `shaparak`، `zarinpal`، `pay`، `bank`، `sep`.
فهرست دامنه‌هایی را که پیدا شد نگه دارید. همهٔ آن‌ها در گام ۲ وارد شوند.

## گام ۲: ثبت در GA4
Admin ← Data collection and modification ← **Data streams** ← استریم وب ← **Configure tag settings** ← Show more ← **List unwanted referrals**.

برای هر ردیف: Match type = **Referral domain contains**، و مقدار:

| مقدار | توضیح |
|---|---|
| `zarinpal.com` | روی سایت تأیید شده (صفحهٔ اعتماد زرین‌پال در `03-technical-audit.md`). `www.` و `payment.` را هم می‌گیرد. |
| `shaparak.ir` | درگاه‌های مستقیم بانکی همه از زیردامنه‌های شاپرک رد می‌شوند (sep، pec، bpm و ...). |
| `sep.ir` | سامان |
| `asanpardakht.ir` | آسان‌پرداخت |
| `sadadpsp.ir` | سداد (بانک ملی) |
| `pec.ir` | پارسیان |
| `idpay.ir` | آیدی‌پی |
| `zibal.ir` | زیبال |
| `payping.ir` | پی‌پینگ |
| `nextpay.org` | نکست‌پی |
| `pay.ir` | پی‌دات‌آی‌آر |
| `vandar.io` | وندار |

> فقط زرین‌پال روی سایت تأیید شده است. بقیه پیش‌گیرانه‌اند و ضرری ندارند، چون این سایت‌ها هیچ‌وقت منبع واقعی بازدید نیستند. اگر گام ۱ دامنهٔ دیگری نشان داد، اضافه‌اش کنید.

Save.

## گام ۳: دامنه‌های خودمان
- dadrose.com، azmoon.dadrose.com و book.dadrose.com زیر یک دامنه‌اند. اگر هر سه **یک property و یک Measurement ID** دارند، GA4 خودش بین زیردامنه‌ها سشن را نگه می‌دارد (کوکی روی `.dadrose.com`).
- **dadrosebook.com** دامنهٔ دیگری است. اگر فروشگاه قدیم هنوز فروش دارد: همان استریم ← Configure tag settings ← **Configure your domains** ← هم `dadrose.com` و هم `dadrosebook.com` را اضافه کنید (cross-domain).
- روی لینک‌های داخلی بین سایت‌ها **UTM نگذارید**. UTM سشن تازه می‌سازد و منبع واقعی را پاک می‌کند (`05-automation-pipeline.md` §5.2). سند مالک گفته بود لینک‌های فروشگاه به سایت اصلی UTM دارند؛ برداشته شوند.

## گام ۴: چک
1. **بلافاصله:** یک خرید آزمایشی (یا شروع پرداخت و انصراف) با Tag Assistant یا GA4 ← Admin ← **DebugView** باز. بعد از بازگشت از درگاه، اولین رویداد بعد از بازگشت باید پارامتر `ignore_referrer` با مقدار `true` داشته باشد و `session_start` تازه نباید ثبت شود.
2. **۴۸ ساعت بعد:** Traffic acquisition ← Session source: سشن تازه با منبع درگاه نباید اضافه شود.
3. **تاریخ ثبت را در دفتر تغییرات سئو بنویسید** (G6) تا مقایسهٔ قبل و بعد معنی داشته باشد.

## azmoon (Next.js)
CSP فعلی (`script-src 'self'`، `connect-src 'self'`) تگ GA4 را مسدود می‌کند (`03-technical-audit.md`). پیشنهاد `05-automation-pipeline.md` §5.2: `sign_up` و `purchase` از سمت سرور با Measurement Protocol ارسال شوند. این کار فوری نیست و تصمیم مالک لازم دارد. تا آن موقع، اگر azmoon از درگاه استفاده کند همین فهرست باید روی property همان سایت هم ثبت شود.
