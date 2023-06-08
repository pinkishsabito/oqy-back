import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api';

const BookService = {
  createBook: async (title, author, publicationDate, groupId) => {
    try {
      const response = await axios.post(`${BASE_URL}/book/`, {
        title,
        author,
        publication_date: publicationDate,
        group_id: groupId,
      });
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  getBook: async (bookId) => {
    try {
      const response = await axios.get(`${BASE_URL}/book/${bookId}/`);
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  updateBook: async (bookId, data) => {
    try {
      const response = await axios.put(`${BASE_URL}/book/${bookId}/`, data);
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  deleteBook: async (bookId) => {
    try {
      await axios.delete(`${BASE_URL}/book/${bookId}/`);
    } catch (error) {
      throw error.response.data;
    }
  },
};

export default BookService;
