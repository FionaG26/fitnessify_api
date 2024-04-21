import sys
import os
import unittest
from flask import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add parent directory to path

from app import app, db, User

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.ctx = app.app_context()
        self.ctx.push()

        # Clean up the database before each test
        with app.app_context():
            db.session.query(User).delete()
            db.session.commit()
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
        self.ctx.pop()

    def test_register_user(self):
        # Test valid registration
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'StrongPassword123!'
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], 'User registered successfully')

        # Test missing data
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Missing username, email, or password')

        # Test invalid email format
        data = {
            'username': 'test_user',
            'email': 'invalid_email',
            'password': 'StrongPassword123!'
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Invalid email format')

        # Test weak password
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'weak'
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Weak password')

        # Test duplicate username
        new_user = User(username='test_user', email='test@example.com', password='hashed_password')
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'StrongPassword123!'
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Username already exists')

        # Test duplicate email
        data = {
            'username': 'new_user',
            'email': 'test@example.com',
            'password': 'StrongPassword123!'
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)['error'], 'Email already registered')

        # Clean up
        with app.app_context():
            db.session.delete(new_user)
            db.session.commit()

    def test_login_user(self):
        # Test valid login
        new_user = User(username='test_user', email='test@example.com', password='hashed_password')
        with app.app_context():
            db.session.add(new_user)
            db.session.commit()

        data = {
            'email': 'test@example.com',
            'password': 'StrongPassword123!'
        }
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', json.loads(response.data))

        # Test invalid credentials
        data = {
            'email': 'test@example.com',
            'password': 'WrongPassword123!'
        }
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data)['error'], 'Invalid email or password')

        # Clean up
        with app.app_context():
            db.session.delete(new_user)
            db.session.commit()

if __name__ == '__main__':
    unittest.main()
