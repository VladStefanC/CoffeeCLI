// src/api.ts
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // FastAPI backend
  withCredentials: true, // Important: enables sending/receiving cookies
});

export default api;