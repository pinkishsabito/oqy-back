import React from 'react';
import { useHistory, useParams } from 'react-router-dom';
import BookQuestionService from '../../services/BookQuestionService';

const BookQuestionDeleteButton = () => {
  const { bookId, questionId } = useParams();
  const history = useHistory();

  const handleDelete = async () => {
    try {
      await BookQuestionService.deleteQuestion(bookId, questionId);
      history.push(`/book/${bookId}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <button onClick={handleDelete}>Delete</button>
    </div>
  );
};

export default BookQuestionDeleteButton;
