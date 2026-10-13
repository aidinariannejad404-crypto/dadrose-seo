# جعبه‌ابزار SEO دادرز

نصب‌شده و تست‌شده در ۲۱ مهر ۱۴۰۵ (2026-10-13). ارزیابی هر ابزار در `../seo-research/06-github-repos.md` است.

## نصب روی سیستم خودتان
```bash
bash setup.sh          # venv در ~/seo-venv و دو ریپوی بررسی‌شده در ~/seo-vendor
```
بعد از نصب:
1. در Google Cloud یک Service Account بسازید، Search Console API را فعال کنید و ایمیل آن را در Search Console به‌عنوان کاربر اضافه کنید.
2. فایل JSON را در `~/.config/gsc/service-account.json` بگذارید.
3. `mcp.json.example` را به `.mcp.json` پروژه کپی کنید و مسیرها را درست کنید. ابزارهای حذف خاموش‌اند (`GSC_ALLOW_DESTRUCTIVE=false`).
4. پلاگین claude-seo در Claude Code:
   `/plugin marketplace add AgriciDaniel/claude-seo` و بعد `/plugin install claude-seo@agricidaniel-claude-seo`
   (کد در کامیت 4b99de2 بررسی شد. اسکریپت indexing_notify آن را برای مقاله و کتاب استفاده نکنید.)

## چه چیزی نصب است
| ابزار | کار |
|---|---|
| advertools | کرال، تحلیل sitemap و robots، لاگ سرور |
| extruct | استخراج و بررسی JSON-LD صفحات |
| hazm | نرمال‌سازی فارسی (ك→ک، ي→ی، نیم‌فاصله) |
| searchconsole | خروجی زمان‌بندی‌شده از Search Console |
| sentence-transformers + BERTopic | خوشه‌بندی کلیدواژه، پیشنهاد لینک داخلی، کنیبالیزیشن |
| mcp-gsc (کامیت d49eea9) | اتصال Claude به Search Console |
| claude-seo (کامیت 4b99de2) | اسکیل‌های ممیزی، اسکیما و GEO برای Claude Code |

در ریپوی آزمون (PR #1): schema-dts و Lighthouse CI.

## محدودیت محیط ابری
در محیط ابری Claude، دسترسی به Hugging Face بسته است، پس مدل‌های embedding فقط روی سیستم شما دانلود می‌شوند. torch نسخهٔ CUDA نصب شد (حدود ۶ گیگ). روی سرور بدون GPU قبل از requirements این را بزنید:
`pip install torch --index-url https://download.pytorch.org/whl/cpu`
