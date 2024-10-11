import {
    Card,
    CardContent,
    CardHeader,
    CardTitle,
  } from '@/components/ui/card';
  
  const recentTransactions = [
    {
      id: 1,
      description: 'Grocery Shopping',
      amount: -85.50,
      date: '2024-03-10',
    },
    {
      id: 2,
      description: 'Salary Deposit',
      amount: 2500.00,
      date: '2024-03-08',
    },
    // Add more transactions...
  ];
  
  export function RecentTransactions({ className }: { className?: string }) {
    return (
      <Card className={className}>
        <CardHeader>
          <CardTitle>Recent Transactions</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-8">
            {recentTransactions.map((transaction) => (
              <div key={transaction.id} className="flex items-center">
                <div className="flex-1 space-y-1">
                  <p className="text-sm font-medium leading-none">
                    {transaction.description}
                  </p>
                  <p className="text-sm text-muted-foreground">
                    {transaction.date}
                  </p>
                </div>
                <div className={`text-sm font-medium ${
                  transaction.amount > 0 ? 'text-green-500' : 'text-red-500'
                }`}>
                  {transaction.amount > 0 ? '+' : ''}
                  ${transaction.amount.toFixed(2)}
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    );
  }