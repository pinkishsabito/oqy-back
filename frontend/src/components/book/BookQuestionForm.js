import React, { useState } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import BookQuestionService from '../../services/BookQuestionService';

const BookQuestionForm = () => {
  const { bookId } = useParams();
  const [questionText, setQuestionText] = useState('');
  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await BookQuestionService.createQuestion(bookId, { question_text: questionText });
      history.push(`/book/${bookId}`);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Create Book Question</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Question:</label>
          <textarea value={questionText} onChange={(e) => setQuestionText(e.target.value)} required />
        </div>
        <button type="submit">Create</button>
      </form>
    </div>
  );
};

export default BookQuestionForm;
