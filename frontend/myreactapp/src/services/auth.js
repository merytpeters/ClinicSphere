// src/services/auth.js

import api from './api'; // Import the axios instance

export const login = async (username, password) => {
  try {
    const response = await api.post('/token/', { username, password });
    localStorage.setItem('token', response.data.access); // Store JWT token
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const logout = () => {
  localStorage.removeItem('token'); // Remove token
};