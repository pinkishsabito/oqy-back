import React from 'react';
import { useHistory, useParams } from 'react-router-dom';
import BookService from '../../services/BookService';

const BookDelete = () => {
  const { bookId } = useParams();
  const history = useHistory();

  const handleDelete = async () => {
    try {
      await BookService.deleteBook(bookId);
      history.push('/books');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Delete Book</h2>
      <p>Are you sure you want to delete this book?</p>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default BookDelete;
