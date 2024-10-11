import { DashboardHeader } from '@/components/dashboard/header';
import { Overview } from '@/components/dashboard/overview';
import { RecentTransactions } from '@/components/dashboard/recent-transactions';
import { AccountsCard } from '@/components/dashboard/accounts-card';

export default function DashboardPage() {
  return (
    <div className="flex min-h-screen flex-col">
      <DashboardHeader />
      <main className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Dashboard</h2>
        </div>
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          <AccountsCard title="Total Balance" amount="$5,231.89" type="total" />
          <AccountsCard title="Income" amount="$2,838.00" type="income" />
          <AccountsCard title="Expenses" amount="$1,412.00" type="expenses" />
        </div>
        <div className="grid gap-4 md:grid-cols-7">
          <Overview className="col-span-4" />
          <RecentTransactions className="col-span-3" />
        </div>
      </main>
    </div>
  );
}