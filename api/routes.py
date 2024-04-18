from flask import Blueprint, request, jsonify
from models import db, User

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return 'Welcome to Fitnessify!'

@api.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validation checks
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400

        # Perform user registration
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
