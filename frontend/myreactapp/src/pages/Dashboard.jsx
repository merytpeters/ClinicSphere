import React, { useState, useEffect } from "react";
import Sidebar from "../components/sidebar";
import StatisticsChart from "../components/StatisticsChart";
import SoapNote from "../components/SoapNote";
import "../styles/dashboard.css"; 
import '../styles/soapnote.css';

const Dashboard = () => {
    const [isSidebarOpen, setSidebarOpen] = useState(true);

    const toggleSidebar = () => {
        setSidebarOpen(!isSidebarOpen);
    };

    {/*useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("http://your-api-url/statistics");
                const data = await response.json();
                setChartData(data);
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };
    
        fetchData();
    }, []);*/}

    // Sample Data (Replace with API Data)
    const [chartData, setChartData] = useState([]);

    useEffect(() => {
        // Simulate fetching data from API
        const fetchData = () => {
            const newData = [
                { time: "Monday", patients: 50, appointments: 30, payments: 1000, activeHours: 6 },
                { time: "Tuesday", patients: 60, appointments: 40, payments: 1500, activeHours: 7 },
                { time: "Wednesday", patients: 45, appointments: 35, payments: 1200, activeHours: 5 },
                { time: "Thursday", patients: 70, appointments: 50, payments: 2000, activeHours: 8 },
                { time: "Friday", patients: 80, appointments: 55, payments: 2200, activeHours: 9 },
            ];
            setChartData(newData);
        };

        fetchData();
    }, []);

    return (
        <div className="dashboard-container">
            {/* Toggle button outside the sidebar */}
            <button className="toggle-btn" onClick={toggleSidebar}>
                {isSidebarOpen ? "☰ Close" : "☰ Open"}
            </button>
            <Sidebar
                isOpen={isSidebarOpen}
                toggleSidebar={toggleSidebar}
                links={[
                    { href: "/dashboard", text: "Dashboard" },
                    { href: "/registration", text: "Register Patient" },
                    { href: "/inventory", text: "Inventory" },
                    { href: "/appointment", text: "Appointments" },
                    { href: "/patient-files", text: "Patient Files" },
                    { href: "/admin", text: "Admin" },
                    { href: "/login", text: "Logout" },
                    { href: "/financial", text: "Financial" },
                ]}
            />

            
            <div className="main-content">
                <h1>Electronic Medical Record Dashboard</h1>
                <div>
            <h2>Patient and Appointment Statistics</h2>
            </div>
            <div className="charts">
            <StatisticsChart data={chartData} title="No. of Patients" dataKey="patients" />
            <StatisticsChart data={chartData} title="No. of Appointments" dataKey="appointments" />
            <StatisticsChart data={chartData} title="Payments Collected" dataKey="payments" />
            <StatisticsChart data={chartData} title="Active Hours" dataKey="activeHours" />
            </div>
                <div className="dashboard-sections">
                    {["Patient Files", "Registration", "Inventory", "Prescription", "Appointment", "Payment"].map(
                        (section, index) => (
                            <div key={index} className="section">
                                <h2>{section}</h2>
                                {/* Add relevant content here */}
                            </div>
                        )
                    )}
                </div>
                <div className="soap-note">
                    <h2>SOAP Note</h2>
                    <SoapNote onSubmit={(data) => console.log(data)} />
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
