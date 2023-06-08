from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


class RegisterUserViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("auth-register")

    def test_register_user(self):
        payload = {
            "username": "john",
            "email": "john@example.com",
            "password": "password123",
        }
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "User registered successfully"})
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "User registered successfully")

        # Additional assertions to validate the behavior and data
        self.assertIn("user", response.json())
        user = response.json()["user"]
        self.assertIsInstance(user, dict)
        self.assertIn("id", user)
        self.assertIsInstance(user["id"], int)
        self.assertIn("username", user)
        self.assertEqual(user["username"], payload["username"])
        self.assertIn("email", user)
        self.assertEqual(user["email"], payload["email"])


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("auth-login")

    def test_login_valid_credentials(self):
        payload = {"username": "john", "password": "password123"}
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Login successful"})
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Login successful")

        # Additional assertions to validate the behavior and data
        self.assertIn("token", response.json())
        token = response.json()["token"]
        self.assertIsInstance(token, str)
        self.assertTrue(token)  # Check if the token is not empty or falsy value

    def test_login_invalid_credentials(self):
        payload = {"username": "john", "password": "wrongpassword"}
        response = self.client.post(self.url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {"message": "Invalid credentials"})
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Invalid credentials")

        # Additional assertions to validate the behavior and data
        self.assertIn("error", response.json())
        error = response.json()["error"]
        self.assertIsInstance(error, dict)
        self.assertIn("code", error)
        self.assertIsInstance(error["code"], str)
        self.assertIn("message", error)
        self.assertIsInstance(error["message"], str)
