import React from 'react';
import Navbar from '../components/Navbar';
import '../styles/landingpage.css'

const LandingPage = () => {
    return (
        <div className='landingpage'>
            <Navbar >
            </Navbar>
            <div className='landingpage-container'>
                    <h2 className='landingpage-title'>Welcome to ClinicSphere EMR System</h2>
                    <p>Streamlining healthcare management with secure and efficient electronic medical records.</p>
             </div>
        </div>
    )
}

export default LandingPage;