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
            <h2>Signup List</h2>
            {error && <p>{error}</p>}
            <ul>
                {signupData.map((item) => (
                    <li key={item.id}>{item.someField}</li>
                ))}
            </ul>
        </div>
    );
};

export default SignupList;