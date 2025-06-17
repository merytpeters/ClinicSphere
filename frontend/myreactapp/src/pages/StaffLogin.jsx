import axios from 'axios';
import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useAuth } from "../provider/authProvider";


const Login = () => {
    const { setToken } = useAuth();
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setError(null);
        setSuccessMessage(null);

        console.log("Submitting login form:", formData); // Debugging log

        try {
            const response = await axios.post("http://localhost:8000/api/login/", formData, {
                headers: {
                    "Content-Type": "application/json",
                },
            });

            console.log("Login Response:", response.data); // Debugging log

            if (response.data.access && response.data.refresh) {
                localStorage.setItem("accessToken", response.data.access);
                localStorage.setItem("refreshToken", response.data.refresh);

                setSuccessMessage("Login Successful!");
                
                // Navigate after ensuring token is stored
                setTimeout(() => {
                    navigate("/");
                }, 500);
            }
        } catch (error) {
            console.error("Error during Login:", error.response?.data || error.message);

            if (error.response) {
                const message = error.response.data.detail || "Invalid email or password.";
                setError(message);
            } else {
                setError("An unexpected error occurred. Please try again.");
            }
        } finally {
            setIsLoading(false);
        }
    };

    const getAuthHeader = () => {
        const token = localStorage.getItem("accessToken");
        return token ? { Authorization: `Bearer ${token}` } : {};
    };
    
    const fetchEmployeeProfile = async () => {
        try {
            const response = await axios.get("http://localhost:8000/api/profile/", {
                headers: getAuthHeader(),
            });
            console.log("Employee Profile:", response.data);
        } catch (error) {
            console.error("Error fetching profile:", error.response?.data || error.message);
        }
    };

    return (
        <div>
            {error && <p style={{ color: "red" }}>{error}</p>}
            {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <label>Email:</label><br />
                <input
                type="email"
                name='email'
                value={formData.email}
                onChange={handleChange}
                required
                /><br /><br />
                <label>Password:</label><br />
                <input
                type="password"
                name='password'
                value={formData.password}
                onChange={handleChange}
                required
                /><br /><br />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Logging in ...' : 'Login'}
                </button>
            </form>
        </div>
    )
};

export default Login;