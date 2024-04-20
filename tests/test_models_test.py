import unittest
from app import create_app, db
from models import User


class TestUserModel(unittest.TestCase):

    def setUp(self):
        # Create Flask application with a temporary in-memory SQLite database
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        
        # Establish application context
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create all tables
        db.create_all()

    def tearDown(self):
        # Remove all tables and application context
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        # Create a new user
        user = User(
            username='test_user',
            email='test@example.com',
            password='test123')

        # Add and commit the user to the database
        db.session.add(user)
        db.session.commit()

        # Retrieve the user from the database
        retrieved_user = User.query.filter_by(username='test_user').first()

        # Check if the retrieved user matches the created user
        self.assertEqual(retrieved_user.username, 'test_user')
        self.assertEqual(retrieved_user.email, 'test@example.com')
        self.assertTrue(retrieved_user.password)  # Password should be hashed


if __name__ == '__main__':
    unittest.main()

