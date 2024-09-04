import React from 'react';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        // clear the token or any authentication details
        localStorage.removeItem('token');
        navigate('/login'); //Redirect to login page after logout
    };

    return (
        <div>
          <h1>Welcome to your Dashboard</h1>
          <p>This is your dashboard to manage and view data</p>
          <button onClick={handleLogout}>Logout</button>
        </div>
    );
};

export default Dashboard;