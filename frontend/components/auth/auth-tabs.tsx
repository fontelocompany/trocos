'use client';

import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Card } from '@/components/ui/card';
import { LoginForm } from './login-form';
import { RegisterForm } from './register-form';

export function AuthTabs() {
  return (
    <Tabs defaultValue="login" className="w-full">
      <TabsList className="grid w-full grid-cols-2">
        <TabsTrigger value="login">Login</TabsTrigger>
        <TabsTrigger value="register">Register</TabsTrigger>
      </TabsList>
      <TabsContent value="login">
        <Card className="p-6">
          <LoginForm />
        </Card>
      </TabsContent>
      <TabsContent value="register">
        <Card className="p-6">
          <RegisterForm />
        </Card>
      </TabsContent>
    </Tabs>
  );
}