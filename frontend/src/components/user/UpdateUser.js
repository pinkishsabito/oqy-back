import React, { useEffect, useState } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import UserService from '../../services/UserService';

const UpdateUser = () => {
  const { userId } = useParams();
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const history = useHistory();

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await UserService.getUser(userId);
        const userData = response.data;
        setUsername(userData.username);
        setEmail(userData.email);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchUser();
  }, [userId]);

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await UserService.updateUser(userId, { username, email });
      history.push(`/users/${userId}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Update User</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={handleUsernameChange}
        />
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={handleEmailChange}
        />
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default UpdateUser;
