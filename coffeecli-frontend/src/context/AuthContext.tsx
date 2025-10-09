import { createContext, useContext, useEffect, useState } from "react";
import api from "../api/api";

type User = { id: string; username: string; email: string } | null;

const AuthCtx = createContext<{ user: User; setUser: (u: User) => void }>({
  user: null,
  setUser: () => {},
});

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User>(null);

  useEffect(() => {
    let mounted = true;
    (async () => {
      try {
        const { data } = await api.get("/users/me");
        if (mounted) setUser(data);
      } catch (err) {
        console.warn("No active session:", err);
        // Don't immediately nullify user — only after verification
        if (mounted) setUser(null);
      }
    })();

    return () => {
      mounted = false;
    };
  }, []);

  return (
    <AuthCtx.Provider value={{ user, setUser }}>{children}</AuthCtx.Provider>
  );
}

export const useAuth = () => useContext(AuthCtx);
