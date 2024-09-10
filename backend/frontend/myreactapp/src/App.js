import React from 'react';
import './App.css'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Home from './pages/Home'
import Login from './pages/Login';
import ProtectedRoute from './components/ProtectedRoute';
import SignupForm from './pages/Signup';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route
              path="/dashboard"
              element={
                <ProtectedRoute>
                  <Dashboard />
                </ProtectedRoute>
              }
            />
            <Route path="/signup" element={<SignupForm />} />
         </Routes>
         </header>
      </div>
    </Router>
  );
}

export default App;
