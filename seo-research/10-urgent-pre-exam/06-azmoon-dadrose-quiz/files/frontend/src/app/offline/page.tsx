import type { Metadata } from "next";
import { Logo } from "@/components/ui/logo";

export const metadata: Metadata = { title: "آفلاین", robots: { index: false, follow: false } };
export const dynamic = "force-static";

export default function OfflinePage() {
  return (
    <main id="main" className="flex min-h-dvh flex-col items-center justify-center gap-4 p-6 text-center">
      <Logo />
      <h1 className="text-xl font-bold">اتصال اینترنت برقرار نیست</h1>
      <p className="max-w-sm text-sm leading-7 text-fg-muted">
        اگر وسط آزمون بودید نگران نباشید: پاسخ‌ها روی همین دستگاه ذخیره شده‌اند و پس از اتصال دوباره ارسال
        می‌شوند. ساعت آزمون روی سرور ادامه دارد.
      </p>
      <a href="/app" className="rounded-md bg-primary px-4 py-2 font-medium text-primary-fg">
        تلاش دوباره
      </a>
    </main>
  );
}
