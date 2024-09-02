import { BrowserRouter as Router, Route, Switch } from react-router-dom
import HomePage from './HomePage';
import Login from './Login';
import React from 'react';
import Signup from './Signup';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1> CLINICSPHERE </h1>
        </header>
        <main>
          <Switch>
            <Route path="/" exact component={HomePage} />
            <Route path="/login" component={Login} />
            <Route path="/signup" component={Signup} />
         </Switch>
       </main>
      </div>
    </Router>
  );
}

export default App;
