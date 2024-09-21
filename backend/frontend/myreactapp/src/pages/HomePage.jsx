import axios from 'axios';
import React, {useState} from 'react';


const Home = () => {
    const [message, setMessage] = useState('');

    const generateToken = async (email) => {
        try {
            const response = await axios.post('http://localhost:8000/api/generate-token/', { email });
            setMessage('Token has been sent to your email!');
            console.log('Token has been sent to your email!', response.data.message);
        } catch (err) {
            if (err.response) {
                setMessage(`Error: ${err.response.data.detail || 'Failed to generate token'}`);
                console.log('Error:', err.response.data.detail);
            } else if (err.request) {
                setMessage('No response from server. Please check your connection or try again later.');
                console.log('No response received:', err.request);
            } else {
                setMessage('An error occurred while generating token');
                console.log('Error:', err.messsage);
            }
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const email = e.target.email.value
        generateToken(email);  
    };

    return (
        <div>
            <h2>Generate Token:</h2>
            <form onSubmit={handleSubmit}>
                <label>Email:</label><br/>
                <input
                type="email"
                name="email"
                placeholder='Enter your email'
                required
                ></input><br/>
                <br/>
                <button type="submit">
                    Generate token
                </button>
        </form>
        {message && <p>{message}</p>} {/* Displaying the message */}
    </div>
    );
};

export default Home;