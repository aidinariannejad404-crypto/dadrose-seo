// Exam-night load test for dadrose (G2).
// Run with k6 (https://grafana.com/docs/k6/latest/):
//   k6 run exam-night.k6.js                                  # default: dadrose.com, stepped ramp
//   k6 run -e BASE=https://staging.dadrose.com exam-night.k6.js
//   k6 run -e PEAK=400 -e HOLD=5m exam-night.k6.js           # push higher
//   k6 run -e MODE=smoke exam-night.k6.js                    # 1 user, 30s, sanity check
//
// What it simulates: a candidate leaves the exam hall, opens the answer-key page,
// then opens the percent calculator and (optionally) loads it a few more times.
// Traffic split mirrors that path: ~55% answer key, ~35% calculator, ~10% home.
//
// IMPORTANT: run it against production only in a quiet hour (e.g. 02:00–05:00 Tehran),
// with the host/CDN owner informed, and from a machine INSIDE Iran as well as one
// outside (the two paths hit different network routes). Stop with Ctrl+C at any time.

import http from "k6/http";
import { check, sleep, group } from "k6";
import { Rate, Trend } from "k6/metrics";

const BASE = (__ENV.BASE || "https://dadrose.com").replace(/\/$/, "");
const PEAK = parseInt(__ENV.PEAK || "200", 10); // concurrent virtual users at the top step
const HOLD = __ENV.HOLD || "3m";
const MODE = __ENV.MODE || "ramp";

// Paths are the existing URLs named in 00-master-plan.md §5 (do not create new ones).
const ANSWER_KEY = __ENV.ANSWER_KEY || "/questions-and-answer-key-of-the-1405-bar-exam/";
const CALCULATOR = __ENV.CALCULATOR || "/score-percentage-calculator/";
const HOME = "/";

const cacheHit = new Rate("cache_hit");
const ttfb = new Trend("ttfb_ms", true);

const stages =
  MODE === "smoke"
    ? [{ duration: "30s", target: 1 }]
    : [
        { duration: "1m", target: Math.round(PEAK * 0.1) },
        { duration: HOLD, target: Math.round(PEAK * 0.1) },
        { duration: "1m", target: Math.round(PEAK * 0.25) },
        { duration: HOLD, target: Math.round(PEAK * 0.25) },
        { duration: "1m", target: Math.round(PEAK * 0.5) },
        { duration: HOLD, target: Math.round(PEAK * 0.5) },
        { duration: "1m", target: PEAK },
        { duration: HOLD, target: PEAK },
        { duration: "1m", target: 0 },
      ];

export const options = {
  stages,
  thresholds: {
    // Pass criteria for "ready for exam night". Tune only with a written reason.
    http_req_failed: [{ threshold: "rate<0.01", abortOnFail: true, delayAbortEval: "1m" }],
    "http_req_duration{page:answer_key}": ["p(95)<2000"],
    "http_req_duration{page:calculator}": ["p(95)<2000"],
    ttfb_ms: ["p(95)<800"],
  },
  // Count HTML only; static assets are expected to come from browser/CDN cache.
  discardResponseBodies: false,
  userAgent: "dadrose-loadtest/1.0 (+exam-night G2)",
};

// Response headers that reveal whether a page cache answered (LiteSpeed, WP Rocket,
// nginx fastcgi_cache, Cloudflare, ArvanCloud, generic Varnish/CDN).
function isCacheHit(res) {
  const h = res.headers;
  const v = [
    h["X-Litespeed-Cache"],
    h["X-Cache"],
    h["X-Cache-Status"],
    h["Cf-Cache-Status"],
    h["X-Proxy-Cache"],
    h["Ar-Cache"],
    h["X-Rocket-Nginx-Serving-Static"],
  ]
    .filter(Boolean)
    .join(" ")
    .toLowerCase();
  return v.includes("hit");
}

function hit(path, page) {
  const res = http.get(BASE + path, {
    tags: { page },
    headers: { "Accept-Language": "fa-IR,fa;q=0.9", Accept: "text/html" },
    redirects: 3,
  });
  ttfb.add(res.timings.waiting, { page });
  cacheHit.add(isCacheHit(res), { page });
  check(res, {
    [`${page}: status 200`]: (r) => r.status === 200,
    [`${page}: has <title>`]: (r) => typeof r.body === "string" && r.body.includes("<title"),
    [`${page}: not an error page`]: (r) =>
      typeof r.body === "string" && !/Error establishing a database connection|Service Unavailable|502 Bad Gateway/i.test(r.body),
  });
  return res;
}

export default function () {
  const roll = Math.random();
  if (roll < 0.55) {
    group("answer key → calculator", () => {
      hit(ANSWER_KEY, "answer_key");
      sleep(5 + Math.random() * 20); // reading the key
      hit(CALCULATOR, "calculator");
    });
  } else if (roll < 0.9) {
    group("calculator direct", () => {
      hit(CALCULATOR, "calculator");
      sleep(10 + Math.random() * 30);
      if (Math.random() < 0.3) hit(CALCULATOR, "calculator"); // reload to re-enter answers
    });
  } else {
    group("home", () => hit(HOME, "home"));
  }
  sleep(2 + Math.random() * 5);
}

export function handleSummary(data) {
  const m = data.metrics;
  const p95 = (name) => (m[name] && m[name].values["p(95)"] ? Math.round(m[name].values["p(95)"]) : "n/a");
  const line = (k, v) => `${k.padEnd(34)} ${v}\n`;
  let out = "\n=== dadrose exam-night summary ===\n";
  out += line("base", BASE);
  out += line("peak VUs", MODE === "smoke" ? 1 : PEAK);
  out += line("requests", m.http_reqs ? m.http_reqs.values.count : 0);
  out += line("req/s (avg)", m.http_reqs ? m.http_reqs.values.rate.toFixed(1) : 0);
  out += line("failed rate", m.http_req_failed ? (m.http_req_failed.values.rate * 100).toFixed(2) + "%" : "n/a");
  out += line("p95 answer key (ms)", p95("http_req_duration{page:answer_key}"));
  out += line("p95 calculator (ms)", p95("http_req_duration{page:calculator}"));
  out += line("p95 TTFB (ms)", p95("ttfb_ms"));
  out += line("page-cache hit rate", m.cache_hit ? (m.cache_hit.values.rate * 100).toFixed(1) + "%" : "n/a");
  out += "Paste this block into 00-RUNBOOK.md §results with date, time and source location.\n";
  return { stdout: out, "summary.json": JSON.stringify(data, null, 2) };
}
