// components/commands/Logout.tsx
import { useEffect } from "react";
import api from "../../api/api";
import { useAuth } from "../../context/AuthContext";

export default function Logout() {
  const { setUser } = useAuth();

  useEffect(() => {
    (async () => {
      try {
        await api.post("/auth/logout");
        setUser(null);
      } catch {
        console.error("Logout failed");
      }
    })();
  }, []);

  return <span>✅ Logged out successfully.</span>;
}