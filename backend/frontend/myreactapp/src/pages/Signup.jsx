import React, { useState } from 'react';
import axios from 'axios';

const SignupForm = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://127.0.0.1:8000/api/employees/signup/', {
                name,
                email,
                password,
        });
        } catch (err) {
            setError(err.response?.data || 'Signup failed');
        }
    };

    return (
        <div>
            <h2>Signup</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Name</label>
                    <input
                      type="text"
                      value={name}
                      onChange={(e) => setName(e.target.value)}
                      required
                    />
                </div>
                <div>
                    <label>Email</label>
                    <input
                      type="email"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      required
                    />
                </div>
                <div>
                    <label>Password</label>
                    <input
                      type="password"
                      value={password}
                      onChange={(e) => setPassword(e.target.value)}
                      required
                    />
                </div>
                {error && <p>{error}</p>}
                <button type="submit">Signup</button>
            </form>
        </div>
    );
};

export default SignupForm;