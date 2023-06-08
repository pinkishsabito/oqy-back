import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import BookService from '../../services/BookService';

const BookList = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const response = await BookService.getBooks();
      setBooks(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>Books</h1>
      <Link to="/book/create">Create Book</Link>
      {books.map((book) => (
        <div key={book.id}>
          <h3>
            <Link to={`/book/${book.id}`}>{book.title}</Link>
          </h3>
          <p>Author: {book.author}</p>
          <p>Publication Date: {book.publication_date}</p>
        </div>
      ))}
    </div>
  );
};

export default BookList;
