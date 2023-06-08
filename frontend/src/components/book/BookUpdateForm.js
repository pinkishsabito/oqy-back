import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import BookService from '../../services/BookService';

const BookUpdateForm = () => {
  const { bookId } = useParams();
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [publicationDate, setPublicationDate] = useState('');
  const history = useHistory();

  useEffect(() => {
    fetchBook();
  }, []);

  const fetchBook = async () => {
    try {
      const response = await BookService.getBook(bookId);
      setTitle(response.title);
      setAuthor(response.author);
      setPublicationDate(response.publication_date);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await BookService.updateBook(bookId, {
        title,
        author,
        publication_date: publicationDate,
      });
      history.push('/books');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Update Book</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
        </div>
        <div>
          <label>Author:</label>
          <input type="text" value={author} onChange={(e) => setAuthor(e.target.value)} required />
        </div>
        <div>
          <label>Publication Date:</label>
          <input
            type="text"
            value={publicationDate}
            onChange={(e) => setPublicationDate(e.target.value)}
            required
          />
        </div>
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default BookUpdateForm;
