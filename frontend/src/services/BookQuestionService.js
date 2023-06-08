import axios from 'axios';

const BASE_URL = 'http://your-api-base-url.com'; // Replace with your actual API base URL

const BookQuestionService = {
  getQuestion: async (bookId, questionId) => {
    const response = await axios.get(`${BASE_URL}/book/${bookId}/questions/${questionId}/`);
    return response.data;
  },
  createQuestion: async (bookId, questionData) => {
    const response = await axios.post(`${BASE_URL}/book/${bookId}/questions/`, questionData);
    return response.data;
  },
  updateQuestion: async (bookId, questionId, questionData) => {
    const response = await axios.put(`${BASE_URL}/book/${bookId}/questions/${questionId}/`, questionData);
    return response.data;
  },
  deleteQuestion: async (bookId, questionId) => {
    const response = await axios.delete(`${BASE_URL}/book/${bookId}/questions/${questionId}/`);
    return response.data;
  },
};

export default BookQuestionService;
