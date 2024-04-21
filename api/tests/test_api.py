import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add the parent directory to the Python path

import unittest
import json
from app import app, db
from models import User

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Create a test user
        self.test_user = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPassword123'
        }

        # Create tables in the test database
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Clean up the test database after each test
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_user(self):
        # Test user registration endpoint
        response = self.app.post('/register', json=self.test_user)
        data = json.loads(response.data.decode('utf-8'))

        # Assert status code and response message
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'User registered successfully')

    def test_register_user_missing_fields(self):
        # Test user registration with missing fields
        incomplete_user = {'username': 'testuser'}
        response = self.app.post('/register', json=incomplete_user)
        data = json.loads(response.data.decode('utf-8'))

        # Assert status code and response message
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Missing username, email, or password')

    # Add more test cases for validation, error handling, etc.

if __name__ == '__main__':
    unittest.main()
