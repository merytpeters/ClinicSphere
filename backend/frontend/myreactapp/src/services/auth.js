import api from './api'; // Import the axios instance

export const isAuthenticated = () => {
  const token = localStorage.getItem('token');
  return !!token; // Return true if token exists
};

export const login = async (username, password) => {
  try {
    const response = await api.post('/token/', { username, password });
    const token = response.data.access;
    localStorage.setItem('token', token); // Store JWT token
    return response.data;
  } catch (error) {
    console.error("Login error:", error.response?.data || error.message);
    throw error.response?.data || error.message;
  }
};

export const logout = () => {
  localStorage.removeItem('token'); // Remove token
};