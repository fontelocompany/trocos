// app/page.tsx
import { redirect } from 'next/navigation';
import { AuthTabs } from '@/components/auth/auth-tabs';

export default function Home() {
  // If user is already authenticated, redirect to dashboard
  // This logic should be handled by your middleware
  // redirect('/dashboard');

  return (
    <main className="min-h-screen flex items-center justify-center bg-background p-4">
      <div className="w-full max-w-md space-y-4">
        <div className="text-center space-y-2">
          <h1 className="text-3xl font-bold">Personal Finance</h1>
          <p className="text-muted-foreground">
            Track your expenses and manage your finances
          </p>
        </div>
        <AuthTabs />
      </div>
    </main>
  );
}