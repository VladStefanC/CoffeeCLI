import api from "../../api/api";
import {useState} from "react"

export function Register() {

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");

    const handleRegister = async () => {
        try { 
            await api.post('/auth/register', {
                username,
                email,
                password,
        });
            setMessage("Registration successful! You can now log in.");
        }catch {
            setMessage("Registration failed. Please try again.");
        }
    };

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter") {
          handleRegister();
        }
      };
 

    return (
         <div>
            <div>Enter your <strong>username</strong>:</div>
            <input className="bg-transparent border-b border-orange-500 w-full outline-none" value={username} onChange={e => setUsername(e.target.value)} />
            <div>Enter your <strong>email</strong>:</div>
            <input className="bg-transparent border-b border-orange-500 w-full outline-none" value={email} onChange={e => setEmail(e.target.value)} />
            <div>Enter your <strong>password</strong>:</div>
            <input type="password" className="bg-transparent border-b border-orange-500 w-full outline-none" 
            value={password} 
            onChange={e => setPassword(e.target.value)} 
            onKeyDown={handleKeyDown}
            />
            
            {message && <div className="mt-2">{message}</div>}
         </div>
    )
}