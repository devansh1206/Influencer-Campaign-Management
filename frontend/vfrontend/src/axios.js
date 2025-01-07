import axios from 'axios';
import store from './store';

const instance = axios.create({
  baseURL: 'http://127.0.0.1:5000/api',
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add a request interceptor to include the token
instance.interceptors.request.use(config => {
  const token = store.state.token;
  if (token) {
    config.headers['Authentication-Token'] = token; 
  }
  return config;
}, error => {
  return Promise.reject(error);
});

export default instance;