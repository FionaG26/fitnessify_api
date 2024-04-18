import sys
import unittest
from unittest.mock import patch
from flask import Flask, jsonify

# Append the project root to sys.path
sys.path.append('..')

from fitnessify_api.api.routes import api


class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(api)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    def test_register_success(self):
        # Mock request data
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'test123'}

        # Make POST request to register endpoint
        response = self.client.post('/register', json=data)

        # Assert response status code and message
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json, {
                'message': 'User registered successfully'})

    @patch('api.routes.db.session.add')
    @patch('api.routes.db.session.commit')
    def test_register_validation_failure(self, mock_commit, mock_add):
        # Mock request data with missing fields
        data = {'username': 'test_user', 'email': 'test@example.com'}

        # Make POST request to register endpoint
        response = self.client.post('/register', json=data)

        # Assert response status code and message
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'All fields are required'})

    @patch('api.routes.db.session.add')
    @patch('api.routes.db.session.commit')
    def test_register_exception_handling(self, mock_commit, mock_add):
        # Mock database exception
        mock_add.side_effect = Exception('Database error')

        # Mock request data
        data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'test123'}

        # Make POST request to register endpoint
        response = self.client.post('/register', json=data)

        # Assert response status code and message
        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            response.json, {
                'error': 'An unexpected error occurred'})


if __name__ == '__main__':
    unittest.main()
