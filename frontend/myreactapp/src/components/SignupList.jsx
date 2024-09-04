import React, { useEffect, useState } from 'react';
import { getSignupList } from '../services/signup';

const SignupList = () => {
    const [signupData, setSignupData] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchSignupData = async () => {
            try {
                const data = await getSignupList();
                setSignupData(data);
            } catch (error) {
                setError(error.detail || 'Failed to fectch data');
            }
        };

        fetchSignupData();
    }, []);

    return (
        <div>
            <h1>Signup List</h1>
            <ul>
                {signupData.map((signup, index) => (
                    <li key={index}>{signup.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default SignupList;