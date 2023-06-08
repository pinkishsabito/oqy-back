class AuthenticationService {
  static registerUser(username, email, password) {
    return fetch('/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, email, password }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message === 'User registered successfully') {
          // Handle successful registration
        } else {
          throw new Error('Registration failed');
        }
      })
      .catch((error) => {
        throw new Error('Registration failed');
      });
  }

  static loginUser(username, password) {
    return fetch('/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message === 'Login successful') {
          // Handle successful login
        } else {
          throw new Error('Invalid credentials');
        }
      })
      .catch((error) => {
        throw new Error('Login failed');
      });
  }
}

export default AuthenticationService;
