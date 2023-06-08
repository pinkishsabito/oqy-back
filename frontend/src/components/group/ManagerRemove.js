import React from 'react';
import { useHistory, useParams } from 'react-router-dom';
import GroupService from '../../services/GroupService';

const ManagerRemove = () => {
  const { groupId, managerId } = useParams();
  const history = useHistory();

  const handleRemove = async () => {
    try {
      await GroupService.removeManager(groupId, managerId);
      history.push(`/groups/${groupId}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Remove Manager</h2>
      <p>Are you sure you want to remove this manager?</p>
      <button onClick={handleRemove}>Remove</button>
    </div>
  );
};

export default ManagerRemove;
