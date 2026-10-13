#!/usr/bin/env python3
"""Check T1 ordering for dadrose.com: is each URL noindexed, and is it still crawlable?

A noindex only works while Googlebot may crawl the URL. So for every URL that should
leave the index, the safe state is:  noindex = yes  AND  blocked by robots.txt = no.
Only after the URL has left Google's index (check in Search Console) may robots.txt block it.

Usage (standard library only, run from a machine that can reach the site):
    python3 check_noindex.py                       # built-in URL list below
    python3 check_noindex.py urls.txt              # one URL per line
    python3 check_noindex.py --robots robots.txt.final   # test against the proposed file

Exit code 1 if any URL is "noindex but blocked" (the T1 trap) or a redirect target is wrong.
"""
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; dadrose-t1-check/1.0)"
SITE = "https://dadrose.com"

# url -> expected: "noindex" | "301:<path>" | "index"
DEFAULT = {
    "/cart/": "noindex",
    "/checkout/": "noindex",
    "/my-account/": "noindex",
    "/dashboard/": "noindex",
    "/forgot-password/": "noindex",
    "/?s=%D9%88%DA%A9%D8%A7%D9%84%D8%AA": "noindex",          # ?s=وکالت (internal search)
    "/?p=22450": "301:/if-the-tenant-does-not-vacate/",
    "/?p=22315": "301:/what-are-the-exceptions-to-debt/",
    "/?p=22570": "301:/age-requirement-for-the-bar-exam/",
    "/%D8%AE%D8%A7%D9%86%D9%87/": "301:/",                     # /خانه/
    "/%D9%88%DA%A9%D8%A7%D9%84%D8%AA404/": "301:/score-percentage-calculator/",  # /وکالت404/
    "/questions-and-answer-key-of-the-1405-bar-exam/": "index",
    "/score-percentage-calculator/": "index",
}


def fetch(url, follow=True):
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *a, **k):
            return None

    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
    try:
        r = opener.open(req, timeout=20)
        return r.status, dict(r.headers), r.read(300_000).decode("utf-8", "replace"), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), "", url


def parse_robots(text):
    """Return Google-style rules for the group that applies to Googlebot."""
    groups, cur, agents, last_was_agent = [], None, [], False
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        k, v = [x.strip() for x in line.split(":", 1)]
        k = k.lower()
        if k == "user-agent":
            if not last_was_agent:
                agents, cur = [], []
                groups.append((agents, cur))
            agents.append(v.lower())
            last_was_agent = True
        elif k in ("allow", "disallow") and cur is not None:
            cur.append((k, v))
            last_was_agent = False
        else:
            last_was_agent = False
    for agents, rules in groups:  # most specific group wins (RFC 9309 / Google)
        if "googlebot" in agents:
            return rules
    for agents, rules in groups:
        if "*" in agents:
            return rules
    return []


def blocked(rules, path):
    def to_re(p):
        end = p.endswith("$")
        p = re.escape(p.rstrip("$")).replace(r"\*", ".*")
        return re.compile("^" + p + ("$" if end else ""))

    best = None  # (length, is_allow)
    for kind, pat in rules:
        if not pat:
            continue
        if to_re(pat).match(path):
            cand = (len(pat), kind == "allow")
            if best is None or cand[0] > best[0] or (cand[0] == best[0] and cand[1]):
                best = cand
    return best is not None and not best[1]


def has_noindex(headers, body):
    xr = " ".join(v for k, v in headers.items() if k.lower() == "x-robots-tag").lower()
    if "noindex" in xr:
        return True
    for m in re.finditer(r"<meta[^>]+name=[\"'](?:robots|googlebot)[\"'][^>]*>", body, re.I):
        if "noindex" in m.group(0).lower():
            return True
    return False


def main(argv):
    robots_file = None
    if "--robots" in argv:
        i = argv.index("--robots")
        robots_file = argv[i + 1]
        del argv[i : i + 2]
    if argv:
        urls = {l.strip(): "noindex" for l in open(argv[0], encoding="utf-8") if l.strip()}
    else:
        urls = DEFAULT

    if robots_file:
        robots_txt = open(robots_file, encoding="utf-8").read()
        print(f"robots.txt: testing proposed file {robots_file}")
    else:
        _, _, robots_txt, _ = fetch(SITE + "/robots.txt")
        print("robots.txt: live")
    rules = parse_robots(robots_txt)

    bad = 0
    print(f"{'URL':60} {'status':>6} {'noindex':>8} {'blocked':>8}  verdict")
    for u, want in urls.items():
        full = u if u.startswith("http") else SITE + u
        path = urllib.parse.urlsplit(full)
        path = path.path + ("?" + path.query if path.query else "")
        is_blocked = blocked(rules, path)
        if want.startswith("301:"):
            st, hd, _, _ = fetch(full, follow=False)
            loc = urllib.parse.unquote(hd.get("Location", ""))
            ok = st in (301, 308) and loc.rstrip("/").endswith(want[4:].rstrip("/"))
            verdict = "OK" if ok else f"FIX: want 301 → {want[4:]}, got {st} {loc}"
            ni = "-"
        else:
            st, hd, body, _ = fetch(full)
            ni_b = has_noindex(hd, body)
            ni = "yes" if ni_b else "no"
            if want == "noindex":
                if ni_b and is_blocked:
                    verdict, ok = "T1 TRAP: noindex hidden by Disallow", False
                elif ni_b:
                    verdict, ok = "OK (wait for deindex, then may Disallow)", True
                elif st in (404, 410):
                    verdict, ok = "OK (gone)", True
                else:
                    verdict, ok = "FIX: add noindex", False
            else:
                ok = st == 200 and not ni_b and not is_blocked
                verdict = "OK" if ok else "FIX: must be 200, indexable, crawlable"
        bad += 0 if ok else 1
        print(f"{urllib.parse.unquote(u)[:60]:60} {st:>6} {ni:>8} {('yes' if is_blocked else 'no'):>8}  {verdict}")
    print(f"\n{bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
