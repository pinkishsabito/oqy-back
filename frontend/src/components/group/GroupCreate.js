import React, { useState } from 'react';
import GroupService from '../../services/GroupService';

const GroupCreate = () => {
  const [name, setName] = useState('');

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await GroupService.createGroup(name);
      // Optionally, you can redirect to another page or show a success message
      // after successfully creating the group.
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Create Group</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name:</label>
        <input type="text" id="name" value={name} onChange={handleNameChange} />
        <button type="submit">Create</button>
      </form>
    </div>
  );
};

export default GroupCreate;
