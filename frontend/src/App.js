import './App.css';
import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import RegisterUserView from './views/RegisterUserView';
import LoginView from './views/LoginView';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/register" component={RegisterUserView} />
        <Route path="/login" component={LoginView} />
      </Switch>
    </Router>
  );
};

export default App;
