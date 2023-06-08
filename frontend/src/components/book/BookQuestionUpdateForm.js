import React, { useState } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import BookQuestionService from '../../services/BookQuestionService';

const BookQuestionUpdateForm = () => {
  const { bookId, questionId } = useParams();
  const [questionText, setQuestionText] = useState('');
  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await BookQuestionService.updateQuestion(bookId, questionId, { question_text: questionText });
      history.push(`/book/${bookId}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Update Book Question</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Question:</label>
          <textarea value={questionText} onChange={(e) => setQuestionText(e.target.value)} required />
        </div>
        <button type="submit">Update</button>
      </form>
    </div>
  );
};

export default BookQuestionUpdateForm;
