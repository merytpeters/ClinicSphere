import axios from 'axios';
import React, {useState} from 'react';


const Signup = () => {

    const [message, setMessage] = useState('');
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password1: "",
        password2: "",
        EmployeeName: "",
        Employee_Title: "",
        DateEmployed: "",
        token: "",
    });

    const [isTokenValid, setIsTokenValid] = useState(false);

    const [isLoading, setIsLoading] = useState(false);
    const [successMessage, setSuccessMessage] = useState(null);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        setFormData({
        ...formData,
        [e.target.name]: e.target.value,
        });
        console.log(formData)

    };

    const verifyToken = async () => {
        const token = formData.token;
        const email = formData.email;
        console.log('Retrieved token:', token);
        if (!token) {
            setIsTokenValid(false);
            setMessage('No token found.');
            return;
        }

        try{
            const response = await axios.post("http://localhost:8000/api/validate-token/", { token, email });
            setIsTokenValid(true);
            setMessage('Token is valid!');
            console.log('Token is valid!', response.data);
        } catch(error) {
            setIsTokenValid(false);
            setMessage('Token has expired or invalid');
            console.error('Token has validation failed:', error.response?.data)
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        setIsLoading(true);
        setError(null);
        setSuccessMessage(null);

        const signupData = {
            ...formData,
            token: formData.token,
            email: formData.email,
        }

        // Verify token
        await verifyToken();

        if (!isTokenValid) {
            setError("Invalid token provided.");
            setIsLoading(false);
            return;
        }

        // Proceed with signup
        try{
            const response = await axios.post("http://localhost:8000/api/registration/", signupData);
            localStorage.setItem('token', response.data.tokens.access);
            console.log("Success!", response.data);
            setSuccessMessage("Signup Successful!");
        } catch (error) {
            console.log("Error during Signup:", error.response?.data);
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
                <label>Username:</label><br/>
                <input type="text" name="username" value={formData.username}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>Name:</label><br/>
                <input type="text" name="EmployeeName" value={formData.EmployeeName}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>Email:</label><br/>
                <input type="email" name="email" value={formData.email}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>Password:</label><br/>
                <input type="password" name="password1" value={formData.password1}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>Confirm password:</label><br/>
                <input type="password" name="password2" value={formData.password2}
                onChange={handleChange} required
                ></input><br/>
                <br/>
                <label>Employee Title:</label><br />
                <select name="Employee_Title" value={formData.Employee_Title} onChange={handleChange} required>
                    <option value="">Select Employee Title</option>
                    <option value="DR">Doctor</option>
                    <option value="RN">Registered Nurse</option>
                    <option value="LT">Laboratory Technician</option>
                    <option value="PH">Pharmacist</option>
                    <option value="CT">Consultant</option>
                    <option value="MD">Medical Director</option>
                    <option value="OB-GYN">Obstetrician and Gynaecologist</option>
                    <option value="Admin">Administrator</option>
                    <option value="Recept">Receptionist</option>
                    <option value="CS">Clinical Staff</option>
                    <option value="OT">Other Staff</option>
                </select><br /><br />
                <label>Date Employed:</label><br />
                <input type="date" name="DateEmployed" value={formData.DateEmployed} onChange={handleChange} required /><br /><br />
                <label>Token:</label><br/>
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