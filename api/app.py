import sys
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from models import User
from utils import validate_email, validate_password

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Fiona:Fiona@localhost/Fitnessify'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '32b2ac3412fcba55ed561c14e2de4e5'

# Initialize SQLAlchemy for database management
db = SQLAlchemy(app)

# Initialize Flask-Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Define API endpoints
@app.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({'error': 'Missing username, email, or password'}), 400

        # Check email format
        if not validate_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Check password strength
        if not validate_password(password):
            return jsonify({'error': 'Weak password'}), 400

        # Check username availability
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists'}), 400

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already registered'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/')
def index():
    return render_template('index.html')

# Create database tables based on models
with app.app_context():
        db.create_all()
# Define main function
if __name__ == '__main__':
    app.run(debug=True)
