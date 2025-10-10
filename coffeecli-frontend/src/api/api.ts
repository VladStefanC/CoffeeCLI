// src/api.ts
import axios from "axios";

const api = axios.create({
  baseURL: "https://coffeecli-api.onrender.com", // FastAPI backend
  withCredentials: true, // Important: enables sending/receiving cookies
});

export default api;