#!/usr/bin/env python3
"""Second-opinion SEO/AEO/GEO audit by Gemini (dual-agent review, owner 1405/07/22).

Claude (or a person) sends a piece of work — a diff, files, or a question — and Gemini answers as an independent
technical reviewer. The answer is printed to the terminal. Gemini is a reviewer, not an authority: every finding
must be checked against live data before it is applied (see ../CLAUDE.md).

Usage:
    export GEMINI_API_KEY=...                     # never commit it; never paste it into a file in this repo
    python seo-tools/gemini_audit.py --diff                       # uncommitted changes (git diff HEAD)
    python seo-tools/gemini_audit.py --diff main~1                # changes since a ref
    python seo-tools/gemini_audit.py --file seo-research/10-urgent-pre-exam/01-load-test-cache/nginx-exam-night.conf
    python seo-tools/gemini_audit.py --file a.py --file b.md --prompt "Is the CTR maths right?"
    python seo-tools/gemini_audit.py --diff --dry-run             # show what would be sent, call nothing

Model: gemini-4-argon, then the fallbacks in MODELS; --model (or GEMINI_MODEL) pins one model with no fallback.
Requires: pip install google-genai   (listed in requirements.txt)
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

# Gemini 4 first (owner 1405/07/22). It needs a billed Google AI Studio project: its free-tier quota is 0.
# When a model answers 429 (quota) or 503 (overloaded) the next one is tried, and the output says which one answered.
MODELS = ["gemini-4-argon", "gemini-3.1-pro-preview", "gemini-3.8-flash", "gemini-flash-latest"]
MAX_CHARS = 400_000  # keeps one request well inside the model's context and the cost predictable

SYSTEM = """You are the second, independent auditor of SEO, AEO (answer-engine) and GEO (generative-engine) work
for dadrose.com (Persian legal education: WordPress + WooCommerce + Tutor LMS + Elementor + Rank Math on
LiteSpeed), azmoon.dadrose.com (Next.js exam centre) and the book store. The audience is Iranian; Google is the
main search engine; Bing feeds Copilot/ChatGPT. Review what you are given for technical correctness:
- server and cache config (nginx/LiteSpeed/CDN), robots.txt, noindex, redirects, canonicals, sitemaps;
- data-analysis scripts (Search Console/GA4 maths: aggregation, deduplication, CTR, position weighting);
- structured data (schema.org/JSON-LD validity and Google eligibility);
- content briefs (search intent, cannibalisation, E-E-A-T for YMYL legal content, Persian language quality).
Rules: cite the exact file and line; say how sure you are; separate confirmed defects from suggestions; never
recommend removing or noindexing a page that has search impressions without stating the traffic it would lose;
answer in Persian unless the input is English-only code; be concise."""

# never send these, even if asked
SECRET_PATH = re.compile(r"(^|[\\/])(\.secrets|\.env[^\\/]*|.*\.pem|.*service[_-]?account.*\.json|id_rsa.*|.*\.key)$", re.I)
SECRET_VALUE = re.compile(
    r"(AIza[0-9A-Za-z_\-]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]+?-----END [A-Z ]*PRIVATE KEY-----"
    r"|(?i:(?:api[_-]?key|secret|password|passwd|token)\s*[:=]\s*)['\"]?[^\s'\"]{8,})"
)


def redact(text: str) -> str:
    return SECRET_VALUE.sub("[REDACTED]", text)


def git_diff(ref: str | None) -> str:
    args = ["git", "diff", "--no-color", ref or "HEAD"]
    try:
        out = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", check=True).stdout
    except (OSError, subprocess.CalledProcessError) as e:
        sys.exit(f"git diff failed: {e}")
    if not out.strip():
        sys.exit("git diff is empty: nothing to review.")
    return out


def read_file(path: str) -> str:
    p = Path(path)
    if SECRET_PATH.search(str(p)):
        sys.exit(f"refusing to send a secret file: {path}")
    if not p.is_file():
        sys.exit(f"no such file: {path}")
    return p.read_text(encoding="utf-8", errors="replace")


def build(args: argparse.Namespace) -> str:
    parts: list[str] = []
    if args.prompt:
        parts.append(f"## Question from the reviewer-in-charge\n{args.prompt}")
    if args.diff is not None:
        parts.append(f"## Diff ({args.diff or 'HEAD'})\n```diff\n{git_diff(args.diff)}\n```")
    for f in args.file or []:
        parts.append(f"## File: {f}\n```\n{read_file(f)}\n```")
    if not parts:
        sys.exit("nothing to send: use --diff, --file and/or --prompt")
    if not args.prompt:
        parts.insert(0, "## Task\nAudit the material below for SEO/AEO/GEO technical defects.")
    text = redact("\n\n".join(parts))
    if len(text) > MAX_CHARS:
        sys.exit(f"request is {len(text):,} characters (limit {MAX_CHARS:,}); send fewer files or a narrower diff")
    return text


def main() -> None:
    ap = argparse.ArgumentParser(description="Send work to Gemini for an independent SEO/AEO/GEO audit.")
    ap.add_argument("--diff", nargs="?", const="", default=None, metavar="REF", help="git diff against REF (default HEAD)")
    ap.add_argument("--file", action="append", metavar="PATH", help="a file to review (repeatable)")
    ap.add_argument("--prompt", help="what to check, or a question")
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL"), help="one model, no fallback (default: the MODELS chain)")
    ap.add_argument("--dry-run", action="store_true", help="print the request size and start, do not call Gemini")
    args = ap.parse_args()

    content = build(args)
    if args.dry_run:
        print(f"[dry-run] models={args.model or ' > '.join(MODELS)} chars={len(content):,}\n{content[:2000]}")
        return

    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("GEMINI_API_KEY is not set")
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        sys.exit("google-genai is not installed: pip install google-genai")

    from google.genai import errors

    client = genai.Client(api_key=key)
    chain = [args.model] if args.model else MODELS
    failures = []
    for model in chain:
        try:
            response = client.models.generate_content(
                model=model,
                contents=content,
                config=types.GenerateContentConfig(system_instruction=SYSTEM, temperature=0.2),
            )
        except errors.APIError as e:
            failures.append(f"{model}: {e.code} {(e.message or '').splitlines()[0][:160] if e.message else ''}")
            if e.code in (429, 503) and model != chain[-1]:
                print(f"[gemini] {model} unavailable ({e.code}); trying the next model", file=sys.stderr)
                continue
            sys.exit("Gemini review failed:\n  " + "\n  ".join(failures))
        if failures:
            print(f"[gemini] NOTE: answered by {model}, not {chain[0]}", file=sys.stderr)
        print(response.text or "(empty answer)")
        usage = getattr(response, "usage_metadata", None)
        if usage is not None:
            print(f"\n[gemini] model={model} in={usage.prompt_token_count} out={usage.candidates_token_count}", file=sys.stderr)
        return


if __name__ == "__main__":
    main()
