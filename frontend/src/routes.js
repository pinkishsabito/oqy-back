import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './components/Home';
import UserDetails from './components/user/UserDetails';
import UpdateUser from './components/user/UpdateUser';
import DeleteUser from './components/user/DeleteUser';
import UserGroups from './components/user/UserGroups';

const Routes = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/users/:userId" component={UserDetails} />
        <Route exact path="/users/:userId/update" component={UpdateUser} />
        <Route exact path="/users/:userId/delete" component={DeleteUser} />
        <Route exact path="/users/:userId/groups" component={UserGroups} />
      </Switch>
    </Router>
  );
};

export default Routes;
