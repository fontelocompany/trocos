'use client';

import { AuthProvider } from '@/context/AuthContext';
import { LoadingScreen } from '@/components/ui/loading';
import { useAuth } from '@/context/AuthContext';
import { Inter } from 'next/font/google';
import { ReactNode } from 'react';

const inter = Inter({ subsets: ['latin'] });

function RootLayoutContent({ children }: { children: ReactNode }) {
  const { auth } = useAuth();

  if (auth.isLoading) {
    return <LoadingScreen />;
  }

  return children;
}

export default function RootLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AuthProvider>
          <RootLayoutContent>{children}</RootLayoutContent>
        </AuthProvider>
      </body>
    </html>
  );
}