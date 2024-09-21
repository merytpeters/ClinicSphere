import axios from 'axios';
import React, {useState} from 'react';


const Signup = () => {

    const [message, setMessage] = useState('');
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password1: "",
        password2: "",
        token: "",
    });

    const [isTokenValid, setIsTokenValid] = useState(false);

    const handleChange = (e) => {
        setFormData({
        ...formData,
        [e.target.name]: e.target.value,
        });
        console.log(formData)

    };
   
    const verifyToken = async () => {
        try{
            const response = await axios.post("http://localhost:8000/api/validate-token/", { token: formData.token });
            setIsTokenValid(true);
            setMessage('Token is valid!');
            console.log('Token is valid!', response.data);
        } catch(error) {
            setIsTokenValid(false);
            setMessage('Token has expired or invalid');
            console.error('Token has validation failed:', error.response?.data)
        }
    };

    const [isLoading, setIsLoading] = useState(false);
    const [successMessage, setSuccessMessage] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        setIsLoading(true);
        setError(null);
        setSuccessMessage(null);
        // Verify token
        await verifyToken();

        if (!isTokenValid) {
            setError("Invalid token provided.");
            setIsLoading(false);
            return;
        }

        // Proceed with signup
        try{
            const response = await axios.post("http://localhost:8000/api/registration/", formData);
            console.log("Success!", response.data);
            setSuccessMessage("Signup Successful!");
        } catch (error) {
            console.log("Error during Signup:", error.respone?.data);
            if(error.response && error.response.data) {
                Object.keys(error.response.data).forEach(field => {
                    const errorMessages = error.response.data[field];
                    if (errorMessages && errorMessages.length > 0){
                        setError(errorMessages[0]);
                    }
                });
            }
        } finally {
            setIsLoading(false)
        }
    };

    return (
        <div>
            {error && <p style={{color:"red"}}>{error}</p>}
            { successMessage && <p style={{color:"yellow"}}>{successMessage}</p>}
            <h2>Staff Signup:</h2>
            <form>
                <label>username:</label><br/>
                <input type="text" name="username" value={formData.username}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>email:</label><br/>
                <input type="email" name="email" value={formData.email}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>password:</label><br/>
                <input type="password" name="password1" value={formData.password1}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>confirm password:</label><br/>
                <input type="password" name="password2" value={formData.password2}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>token:</label><br/>
                <input type="text" name="token" value={formData.token}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <button type="submit" disabled={isLoading} onClick={handleSubmit}>
                    Submit
                </button>
            </form>
            {message && <p>{message}</p>} {/* Displaying the message */}
        </div>
    )
};

export default Signup;