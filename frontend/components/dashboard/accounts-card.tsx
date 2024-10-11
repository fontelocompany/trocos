import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ArrowUpIcon, ArrowDownIcon, WalletIcon } from 'lucide-react';

interface AccountsCardProps {
  title: string;
  amount: string;
  type: 'total' | 'income' | 'expenses';
  className?: string;
}

export function AccountsCard({ title, amount, type, className }: AccountsCardProps) {
  const icons = {
    total: WalletIcon,
    income: ArrowUpIcon,
    expenses: ArrowDownIcon,
  };

  const Icon = icons[type];

  const colors = {
    total: 'text-blue-500',
    income: 'text-green-500',
    expenses: 'text-red-500',
  };

  return (
    <Card className={className}>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">
          {title}
        </CardTitle>
        <Icon className={`h-4 w-4 ${colors[type]}`} />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{amount}</div>
      </CardContent>
    </Card>
  );
}