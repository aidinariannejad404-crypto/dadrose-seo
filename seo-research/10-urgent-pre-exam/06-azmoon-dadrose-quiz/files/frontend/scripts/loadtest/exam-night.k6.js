// Exam-night load test for azmoon.dadrose.com (public pages + API health).
// Companion to the dadrose.com test in the dadrose-seo repo (seo-research/10-urgent-pre-exam/).
//
//   k6 run -e MODE=smoke frontend/scripts/loadtest/exam-night.k6.js
//   k6 run -e BASE=https://staging.azmoon.dadrose.com -e PEAK=200 frontend/scripts/loadtest/exam-night.k6.js
//
// Only anonymous, read-only routes are hit; no OTP is requested and no attempt is created,
// so the test never sends SMS or writes to the database. Run in a quiet hour and tell the host.

import http from "k6/http";
import { check, sleep } from "k6";

const BASE = (__ENV.BASE || "https://azmoon.dadrose.com").replace(/\/$/, "");
const PEAK = parseInt(__ENV.PEAK || "200", 10);
const HOLD = __ENV.HOLD || "3m";

const stages =
  __ENV.MODE === "smoke"
    ? [{ duration: "30s", target: 1 }]
    : [0.1, 0.25, 0.5, 1].flatMap((f) => [
        { duration: "1m", target: Math.max(1, Math.round(PEAK * f)) },
        { duration: HOLD, target: Math.max(1, Math.round(PEAK * f)) },
      ]).concat([{ duration: "1m", target: 0 }]);

export const options = {
  stages,
  thresholds: {
    http_req_failed: [{ threshold: "rate<0.01", abortOnFail: true, delayAbortEval: "1m" }],
    "http_req_duration{route:home}": ["p(95)<1500"],
    "http_req_duration{route:guide}": ["p(95)<1500"],
    "http_req_duration{route:health}": ["p(95)<500"],
  },
  userAgent: "dadrose-loadtest/1.0 (+azmoon exam-night)",
};

function get(path, route) {
  const res = http.get(BASE + path, { tags: { route } });
  check(res, { [`${route}: 200`]: (r) => r.status === 200 });
  return res;
}

export default function examNight() {
  get("/", "home");
  sleep(3 + Math.random() * 7);
  if (Math.random() < 0.5) get("/guide", "guide");
  get("/api/v1/health", "health");
  sleep(2 + Math.random() * 5);
}
