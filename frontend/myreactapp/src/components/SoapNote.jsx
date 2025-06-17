import React, { useState } from 'react';


const SoapNote = ({ onSubmit }) => {
    const [subjective, setSubjective] = useState('');
    const [objective, setObjective] = useState('');
    const [assessment, setAssessment] = useState('');
    const [plan, setPlan] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ subjective, objective, assessment, plan });
        setSubjective('');
        setObjective('');
        setAssessment('');
        setPlan('');
    };

    return (
        <div className='soap-note'>
        <form onSubmit={handleSubmit}>
            <div>
                <label>Subjective:</label>
                <textarea
                    value={subjective}
                    onChange={(e) => setSubjective(e.target.value)}
                />
            </div>
            <div>
                <label>Objective:</label>
                <textarea
                    value={objective}
                    onChange={(e) => setObjective(e.target.value)}
                />
            </div>
            <div>
                <label>Assessment:</label>
                <textarea
                    value={assessment}
                    onChange={(e) => setAssessment(e.target.value)}
                />
            </div>
            <div>
                <label>Plan:</label>
                <textarea
                    value={plan}
                    onChange={(e) => setPlan(e.target.value)}
                />
            </div>
            <button type="submit">Submit</button>
        </form>
        </div>
    );
};

export default SoapNote;