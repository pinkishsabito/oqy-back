import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import BookService from '../../services/BookService';

const BookDetail = () => {
  const { bookId } = useParams();
  const [book, setBook] = useState(null);

  useEffect(() => {
    fetchBook();
  }, []);

  const fetchBook = async () => {
    try {
      const response = await BookService.getBook(bookId);
      setBook(response);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  if (!book) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Book Detail</h2>
      <p>Title: {book.title}</p>
      <p>Author: {book.author}</p>
      <p>Publication Date: {book.publication_date}</p>
      <p>Group ID: {book.group_id}</p>
    </div>
  );
};

export default BookDetail;
