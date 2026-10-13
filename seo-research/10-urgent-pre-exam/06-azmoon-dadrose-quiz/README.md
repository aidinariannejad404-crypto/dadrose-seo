# تغییرات کد مرکز آزمون (ریپوی dadrose-quiz)

این پوشه همان تغییرات [PR #2 در dadrose-quiz](https://github.com/aidinariannejad404-crypto/dadrose-quiz/pull/2) است. آن PR هنوز merge نشده و باز مانده است.

**چه چیزی عوض می‌شود:**
- صفحه‌های `/login` و `/offline` متای `noindex` می‌گیرند. noindex در متای صفحه است، نه در robots.txt، تا گوگل بتواند صفحه را بخواند و noindex را ببیند (قاعدهٔ T1).
- اسکریپت تست بار `frontend/scripts/loadtest/exam-night.k6.js` اضافه می‌شود. فقط مسیرهای عمومی و فقط‌خواندنی را صدا می‌زند، پس پیامک OTP نمی‌فرستد و چیزی در دیتابیس نمی‌نویسد.

**فایل‌ها:**
- `exam-night-readiness.patch`: دو commit به شکل git patch، روی `main` فعلی (`791630d`) تست شده و بدون تعارض اعمال می‌شود.
- `files/`: همان سه فایل نهایی با مسیر داخل ریپو، برای کپی دستی.

## روش اعمال (یکی از دو راه)

**راه ۱: patch (پیشنهادی، تاریخچه و پیام commitها حفظ می‌شود)**
```bash
cd dadrose-quiz
git checkout main && git pull
git checkout -b seo/exam-night-readiness
git am /path/to/exam-night-readiness.patch
```

**راه ۲: کپی دستی**
سه فایل داخل `files/` را با همان مسیر روی ریپو کپی کنید.

## چک پیش از انتشار
```bash
cd frontend
npx tsc --noEmit && npx eslint . && npx vitest run
npm run build:mock && node scripts/with-mock.mjs npx next start -p 3123
curl -s http://127.0.0.1:3123/login | grep -o '<meta name="robots"[^>]*>'
# باید بدهد: <meta name="robots" content="noindex, follow"/>
```
روی نسخهٔ ما همهٔ این‌ها سبز بود: ۱۰۹ تست واحد رد شدند و تست کوتاه k6 همهٔ آستانه‌ها را گذراند.

اگر مرکز آزمون از شاخهٔ اصلی خودکار منتشر می‌شود، merge یعنی انتشار روی سایت. زمانش با شماست.
