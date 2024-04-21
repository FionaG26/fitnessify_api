import unittest
import json
import os
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the Flask app and SQLAlchemy instance
from api.app import app, db
from api.models import User  # Import the User model

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True  # Set TESTING config to True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite database for testing
        db.init_app(app)  # Initialize SQLAlchemy with the Flask app
        with app.app_context():
            db.create_all()  # Create all database tables

    def tearDown(self):
        with app.app_context():
            db.session.remove()  # Remove session
            db.drop_all()  # Drop all database tables

    def test_register_user(self):
        client = app.test_client()
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpassword'}
        response = client.post('/register', json=data)
        self.assertEqual(response.status_code, 201)

        # Check if the user is successfully registered
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
