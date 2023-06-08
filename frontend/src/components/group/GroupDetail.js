import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import GroupService from '../../services/GroupService';

const GroupDetail = () => {
  const { groupId } = useParams();
  const [group, setGroup] = useState(null);

  useEffect(() => {
    fetchGroup();
  }, []);

  const fetchGroup = async () => {
    try {
      const response = await GroupService.getGroup(groupId);
      setGroup(response);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  if (!group) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Group Detail</h2>
      <p>ID: {group.group_id}</p>
      <p>Name: {group.name}</p>
      {/* Add more details as needed */}
    </div>
  );
};

export default GroupDetail;
