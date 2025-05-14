// API helper for admin backend
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8001', // Admin backend
});

export default API;
