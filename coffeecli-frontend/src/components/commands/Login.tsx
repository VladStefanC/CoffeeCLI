import React, { useState } from "react";
import api from "../../api/api";

const Login: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async () => {
    try {
      await api.post(
        "/auth/cookie-login",
        new URLSearchParams({
          username,
          password,
        }),
        { headers: { "Content-Type": "application/x-www-form-urlencoded" } }
      );

      setMessage("✅ Logged in successfully (cookie set)");
    } catch (err: any) {
      setMessage(`❌ Login failed: ${err.response?.data?.detail || err.message}`);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleLogin();
    }
  };

  return (
    <div>
      <div>Enter you <strong>email</strong>:</div>
      <input className="bg-transparent border-b border-orange-500 w-full outline-none" value={username} onChange={(e) => setUsername(e.target.value)}/>
      <div>Enter you <strong>password</strong>:</div>
      <input type="password" className="bg-transparent border-b border-orange-500 w-full outline-none" 
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        onKeyDown={handleKeyDown}
      />
      {message && <p className="mt-4">{message}</p>}
    </div>
  );
};

export default Login;