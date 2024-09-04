import { BrowserRouter as Router, Route, Switch } from react-router-dom
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import ProtectedRoute from './components/ProtectedRoute';
import React from 'react';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1> CLINICSPHERE </h1>
        </header>
        <main>
          <Switch>
            <Route path="/login" element={<Login />} />
            <Route
              path="/dashboard"
              element={
                <ProtectedRoute>
                  <Dashboard />
                </ProtectedRoute>
              }
            />
         </Switch>
       </main>
      </div>
    </Router>
  );
}

export default App;
