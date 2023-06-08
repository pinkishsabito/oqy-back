import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import GroupService from '../../services/GroupService';

const ManagerAdd = () => {
  const { groupId } = useParams();
  const [username, setUsername] = useState('');

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await GroupService.addManager(groupId, username);
      // Optionally, you can redirect to another page or show a success message
      // after successfully adding the manager.
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Add Manager</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={handleUsernameChange}
        />
        <button type="submit">Add</button>
      </form>
    </div>
  );
};

export default ManagerAdd;
