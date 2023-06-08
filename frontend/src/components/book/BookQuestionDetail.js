import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import BookQuestionService from '../../services/BookQuestionService';

const BookQuestionDetail = () => {
  const { bookId, questionId } = useParams();
  const [question, setQuestion] = useState(null);

  useEffect(() => {
    fetchQuestion();
  }, []);

  const fetchQuestion = async () => {
    try {
      const response = await BookQuestionService.getQuestion(bookId, questionId);
      setQuestion(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  if (!question) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Question Detail</h2>
      <p>Question: {question.question_text}</p>
    </div>
  );
};

export default BookQuestionDetail;
