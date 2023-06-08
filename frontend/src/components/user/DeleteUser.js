import React from 'react';
import { useHistory, useParams } from 'react-router-dom';
import UserService from '../../services/UserService';

const DeleteUser = () => {
  const { userId } = useParams();
  const history = useHistory();

  const handleDelete = async () => {
    try {
      await UserService.deleteUser(userId);
      history.push('/users');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Delete User</h2>
      <p>Are you sure you want to delete this user?</p>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default DeleteUser;
