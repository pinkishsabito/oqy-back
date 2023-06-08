import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import GroupService from '../../services/GroupService';

const GroupUpdate = () => {
  const { groupId } = useParams();
  const [name, setName] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchGroup();
  }, []);

  const fetchGroup = async () => {
    try {
      const response = await GroupService.getGroup(groupId);
      setName(response.name);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleNameChange = (e) => {
    setName(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await GroupService.updateGroup(groupId, name);
      // Optionally, you can redirect to another page or show a success message
      // after successfully updating the group.
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Update Group</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name:</label>
        <input type="text" id="name" value={name} onChange={handleNameChange} />
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default GroupUpdate;
