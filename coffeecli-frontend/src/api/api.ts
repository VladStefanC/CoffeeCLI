import axios from "axios";

const api = axios.create({
  baseURL:
    import.meta.env.VITE_API_URL ||
    (import.meta.env.DEV
      ? "http://localhost:8000"
      : "https://coffeecli-api.onrender.com"), // <-- your backend Render URL
  withCredentials: true,
});

export default api;