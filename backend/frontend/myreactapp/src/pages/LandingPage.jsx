import React from 'react';
import Navbar from '../components/Navbar';
import '../styles/landingpage.css'

const LandingPage = () => {
    return (
        <div>
            <Navbar >
            </Navbar>
            <div className='body'>
                    <h2 className='title'>Welcome to ClinicSphere EMR System</h2>
                    <p>Streamlining healthcare management with secure and efficient electronic medical records.</p>
             </div>
        </div>
    )
}

export default LandingPage;