from flask import Blueprint, request, jsonify, render_template
from models import db, User
from utils import validate_email, validate_password
from flask_bcrypt import Bcrypt

api_bp = Blueprint('api', __name__)

bcrypt = Bcrypt()

@api_bp.route('/')
def index():
    return render_template('index.html')

@api_bp.route('/register', methods=['POST'])
def register():
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
