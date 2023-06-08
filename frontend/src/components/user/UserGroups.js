import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import UserService from '../../services/UserService';

const UserGroups = () => {
  const { userId } = useParams();
  const [groups, setGroups] = useState([]);

  useEffect(() => {
    const fetchUserGroups = async () => {
      try {
        const response = await UserService.getUserGroups(userId);
        setGroups(response.data.groups);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchUserGroups();
  }, [userId]);

  if (groups.length === 0) {
    return <div>No groups found for this user.</div>;
  }

  return (
    <div>
      <h2>User Groups</h2>
      <ul>
        {groups.map((group) => (
          <li key={group.id}>{group.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserGroups;
