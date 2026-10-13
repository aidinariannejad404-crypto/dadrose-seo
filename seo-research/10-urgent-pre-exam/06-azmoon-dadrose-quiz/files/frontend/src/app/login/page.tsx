import type { Metadata } from "next";
import Link from "next/link";
import { OtpLogin } from "@/components/auth/otp-login";
import { ThemeToggle } from "@/components/theme/theme-toggle";
import { Logo } from "@/components/ui/logo";
import { IS_MOCK } from "@/lib/env";
import { toFaDigits } from "@/lib/format/digits";
import { MOCK_OTP_CODE } from "@/lib/mock/constants";

// noindex (not a robots.txt Disallow): Google must be able to crawl the page to see it.
export const metadata: Metadata = { title: "ورود", robots: { index: false, follow: true } };

export default async function LoginPage({
  searchParams,
}: {
  searchParams: Promise<{ next?: string | string[] }>;
}) {
  const sp = await searchParams;
  const next = Array.isArray(sp.next) ? sp.next[0] : sp.next;
  return (
    <main id="main" className="flex min-h-dvh flex-col">
      <div className="flex items-center justify-between px-4 py-3">
        <Link href="/" aria-label="بازگشت به صفحه اصلی">
          <Logo />
        </Link>
        <ThemeToggle />
      </div>
      <div className="flex flex-1 items-start justify-center px-4 pt-6 pb-16 sm:items-center sm:pt-0">
        <div className="w-full max-w-sm rounded-xl border border-border bg-surface p-6 shadow-md sm:p-8">
          <h1 className="text-2xl font-bold">ورود به دادرز</h1>
          <p className="mt-2 mb-6 text-sm text-fg-muted">با شماره موبایل وارد شوید یا حساب بسازید.</p>
          <OtpLogin
            next={next}
            mockHint={IS_MOCK ? `حالت نمایشی: کد ورود همیشه ${toFaDigits(MOCK_OTP_CODE)} است.` : undefined}
          />
        </div>
      </div>
    </main>
  );
}
