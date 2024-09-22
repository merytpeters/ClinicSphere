import React from 'react';
import '../styles/Navbar.css';

const Navbar = () => {
    return (
        <nav className='navbar'>
            <div className='navbar-left'>
                <a href="/" className='logo'>
                       ClinicSphere
                </a>
            </div>
            <div className='navbar-centre'>
                <ul className='nav-links'>
                    <a href="/signup">Staff ? Signup</a>
                    <a href="/about-us">About us</a>
                    <a href="/contact-us">Contact us</a>
                    <a href="/fun-facts">Blog</a>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;