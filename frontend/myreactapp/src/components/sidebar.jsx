import React from "react";
import "../styles/sidebar.css";

const Sidebar = ({ isOpen, links }) => {
    return (
        <div className={`sidebar ${isOpen ? "open" : "closed"}`}>
            <nav>
                <ul>
                    {links.map((link, index) => (
                        <li key={index}>
                            <a className='sidebar-text' href={link.href}>{link.text}</a>
                        </li>
                    ))}
                </ul>
            </nav>
        </div>
    );
};

export default Sidebar;

