# 22 - llms.txt and GA4 AI-assistants channel (prepared, NOT applied)

## Files
- `llms.txt` - hand-curated Persian llms.txt (104 lines, 81 links, no duplicate anchors/URLs). Sections: intro, courses, azmoon + tools, dates/registration/answer keys, exam prep guides, 30 top legal articles (GSC clicks 2026-07-17..10-13), Optional. Excluded: noindex, `new-course-N`, forms, cart/account, `?p=` URLs.
- `dadrose-llms.php` - mu-plugin fallback (`php -l` clean). Reads `dadrose-llms.txt` next to it.
- `ga4-channel-group.json` - Admin API v1alpha channelGroups create payload.
- `ga4-report-ai-by-source.json` - Data API report by sessionSource regex (works now, no admin change).
- `ga4-report-custom-channel.json` - Data API report on the custom group (fill CHANNEL_GROUP_ID).

## Findings that change the plan
1. Live `/llms.txt` is a PHYSICAL STATIC FILE (Last-Modified 2026-02-10, served by the web server/CDN as `text/plain`, no PHP headers, same Last-Modified on cache-busted URLs). It is a leftover from All in One SEO v4.9.3. AIOSEO is not active now: no `aioseo` strings on the front end and its plugin folder returns 404. A mu-plugin would never fire while that file exists.
2. Therefore the least risky method is replacing the file, not a plugin (below).
3. Only Rank Math (PRO) outputs SEO meta - no duplicate SEO output (details in the report).
4. GA4 property already has the Google-defined default channel "AI Assistant" (19th rule of the default group). A custom group is only needed to guarantee Perplexity/Claude/DeepSeek/Meta etc. land in it (the research notes say Perplexity/Claude were not named in the default definition); check first with `ga4-report-ai-by-source.json` and the Default channel group.

## Apply llms.txt (recommended: replace the static file)
1. Backup: download the current `/llms.txt` from the web root via FTP (`tools/ftp_backup.py` / `tools/wpftp.sh`) to `backups/llms.txt.2026-xx-xx`.
2. Upload `llms.txt` over `public_html/llms.txt` (UTF-8 without BOM; the old file has a BOM).
3. Purge the CDN (WCDN) cache for `/llms.txt`.
4. Verify: `curl -sI https://dadrose.com/llms.txt` shows 200 and `text/plain`; ideally `charset=utf-8` (if the server omits it, use the mu-plugin route below). `curl -s .../llms.txt | wc -l` is 104.
5. Avoid the week before an exam only by habit - this change cannot affect rankings or the site.

Fallback (only if charset must be forced or file cannot be overwritten): rename the web-root file to `llms.txt.bak`, copy `dadrose-llms.php` and `llms.txt` (as `dadrose-llms.txt`) into `wp-content/mu-plugins/`, purge CDN, verify.

Rollback: restore the backed-up file (or delete mu-plugin files and restore `llms.txt.bak`), purge CDN.
Note: if AIOSEO is ever reactivated its llms feature will regenerate the junk file; disable "LLMs.txt" under AIOSEO > General Settings first.

## Apply GA4 channel (optional, after checking the default AI Assistant channel)
1. Read-only check: `python tools/ga4.py report "$(cat ga4-report-ai-by-source.json)"` (strip `_comment`). Compare with the Default channel group AI Assistant row (Reports > Acquisition > Traffic acquisition).
2. Create (write call; ga4.py only does GET, so use curl or a small script with the same token helper; scope analytics.edit is already requested):
   `POST https://analyticsadmin.googleapis.com/v1alpha/properties/558855395/channelGroups` with body = `ga4-channel-group.json` minus `_comment`.
3. Copy the numeric id from the response `name`, put it in `ga4-report-custom-channel.json` and run it. In GA4 UI the group is selectable as a secondary dimension / in Explorations. Custom groups are not retroactive in standard reports, only going forward and via Data API/explorations.
4. Caveats: `bing.com/chat` never appears as a source (GA4 source is `bing`, medium `referral`); the regex keeps it as requested but real Copilot traffic usually shows as `copilot.microsoft.com`. `you\.com` also matches any host ending in you.com - check the source list for false positives. Traffic via VPN still gets the referrer source, so Iran blocking is not a measurement problem.

Rollback: `DELETE https://analyticsadmin.googleapis.com/v1alpha/properties/558855395/channelGroups/<ID>` (the system default group cannot be touched; nothing else depends on the custom one).
