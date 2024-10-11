// 'use client';

// import { createContext, useContext, useState, useEffect, ReactNode } from 'react';

// export interface User {
//   id: number;
//   email: string;
//   username: string;
// }

// export interface AuthState {
//   user: User | null;
//   accessToken: string | null;
//   refreshToken: string | null;
//   isLoading: boolean;
// }

// interface AuthContextType {
//   auth: AuthState;
//   login: (email: string, password: string) => Promise<void>;
//   register: (email: string, username: string, password: string) => Promise<void>;
//   logout: () => Promise<void>;
// }

// const defaultAuthState: AuthState = {
//   user: null,
//   accessToken: null,
//   refreshToken: null,
//   isLoading: true,
// };

// // Create context with a default value matching the type
// export const AuthContext = createContext<AuthContextType>({
//   auth: defaultAuthState,
//   login: async () => {},
//   register: async () => {},
//   logout: async () => {},
// });

// interface AuthProviderProps {
//   children: ReactNode;
// }

// export function AuthProvider({ children }: AuthProviderProps): JSX.Element {
//   const [auth, setAuth] = useState<AuthState>(defaultAuthState);

//   useEffect(() => {
//     const checkAuth = async () => {
//       try {
//         const accessToken = localStorage.getItem('accessToken');
//         const refreshToken = localStorage.getItem('refreshToken');
//         const userStr = localStorage.getItem('user');

//         if (accessToken && refreshToken && userStr) {
//           const user = JSON.parse(userStr);
//           setAuth({
//             user,
//             accessToken,
//             refreshToken,
//             isLoading: false,
//           });
//         } else {
//           setAuth(prev => ({ ...prev, isLoading: false }));
//         }
//       } catch (error) {
//         console.error('Auth check error:', error);
//         setAuth(prev => ({ ...prev, isLoading: false }));
//       }
//     };

//     checkAuth();
//   }, []);

//   const login = async (email: string, password: string) => {
//     try {
//       const response = await fetch('/api/auth/login', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ email, password }),
//       });

//       if (!response.ok) {
//         throw new Error('Login failed');
//       }

//       const data = await response.json();
      
//       localStorage.setItem('accessToken', data.access);
//       localStorage.setItem('refreshToken', data.refresh);
//       localStorage.setItem('user', JSON.stringify(data.user));

//       setAuth({
//         user: data.user,
//         accessToken: data.access,
//         refreshToken: data.refresh,
//         isLoading: false,
//       });
//     } catch (error) {
//       console.error('Login error:', error);
//       throw error;
//     }
//   };

//   const register = async (email: string, username: string, password: string) => {
//     try {
//       const response = await fetch('/api/auth/register', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ email, username, password }),
//       });

//       if (!response.ok) {
//         throw new Error('Registration failed');
//       }

//       // Login after successful registration
//       await login(email, password);
//     } catch (error) {
//       console.error('Registration error:', error);
//       throw error;
//     }
//   };

//   const logout = async () => {
//     try {
//       localStorage.removeItem('accessToken');
//       localStorage.removeItem('refreshToken');
//       localStorage.removeItem('user');
      
//       setAuth({
//         user: null,
//         accessToken: null,
//         refreshToken: null,
//         isLoading: false,
//       });
//     } catch (error) {
//       console.error('Logout error:', error);
//       throw error;
//     }
//   };

//   const value = {
//     auth,
//     login,
//     register,
//     logout,
//   };

//   return (
//     <AuthContext.Provider value={value}>
//       {children}
//     </AuthContext.Provider>
//   );
// }

// export function useAuth(): AuthContextType {
//   const context = useContext(AuthContext);
//   if (context === undefined) {
//     throw new Error('useAuth must be used within an AuthProvider');
//   }
//   return context;
// }