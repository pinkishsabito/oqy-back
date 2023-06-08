import React from 'react';
import { useHistory, useParams } from 'react-router-dom';
import GroupService from '../../services/GroupService';

const GroupDelete = () => {
  const { groupId } = useParams();
  const history = useHistory();

  const handleDelete = async () => {
    try {
      await GroupService.deleteGroup(groupId);
      history.push('/groups');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Delete Group</h2>
      <p>Are you sure you want to delete this group?</p>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default GroupDelete;
