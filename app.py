from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy for database management
db = SQLAlchemy(app)

# Initialize Flask-Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Define API endpoints
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Missing username, email, or password'}), 400

    # Check email format
    if not validate_email(email):
        return jsonify({'message': 'Invalid email format'}), 400

    # Check password strength
    if not validate_password(password):
        return jsonify({'message': 'Weak password'}), 400

    # Check username availability
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    # Hash password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create new user
    new_user = User(username=username, email=email, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Email already registered'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'An error occurred'}), 500

def validate_email(email):
    # Implement email validation logic (e.g., using regex)
    # For simplicity, let's assume any non-empty string is a valid email
    return email and '@' in email

def validate_password(password):
    # Implement password strength validation logic (e.g., minimum length)
    # For simplicity, let's assume any non-empty string is a strong password
    return password and len(password) >= 8

# Define main function
if __name__ == '__main__':
    # Create database tables based on models
    with app.app_context():
        db.create_all()
    # Run the Flask app
    app.run(debug=True)
