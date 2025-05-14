// API helper for customer backend
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000', // Customer backend
});

export default API;
