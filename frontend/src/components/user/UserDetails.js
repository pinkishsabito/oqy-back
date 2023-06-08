import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import UserService from '../../services/UserService';

const UserDetails = () => {
  const { userId } = useParams();
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await UserService.getUser(userId);
        setUser(response.data);
      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchUser();
  }, [userId]);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>User Details</h2>
      <p>Username: {user.username}</p>
      <p>Email: {user.email}</p>
    </div>
  );
};

export default UserDetails;
