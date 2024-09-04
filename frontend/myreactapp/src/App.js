import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import ProtectedRoute from './components/ProtectedRoute';
import SignupForm from './components/Signup';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1> CLINICSPHERE </h1>
        </header>
        <main>
          <Routes>
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
       </main>
      </div>
    </Router>
  );
}

export default App;
