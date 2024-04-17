# api/routes.py
from flask import Blueprint, request, jsonify
from models import db, User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
        data = request.get_json()
            username = data.get('username')
                email = data.get('email')
                    password = data.get('password')

                        # Validate data
                            if not username or not email or not password:
                                        return jsonify({'error': 'All fields are required'}), 400

                                        # Check if user already exists
                                            if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
                                                        return jsonify({'error': 'Username or email already exists'}), 409

                                                        # Hash password
                                                            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

                                                                # Create new user
                                                                    new_user = User(username=username, email=email, password=hashed_password)
                                                                        db.session.add(new_user)
                                                                            db.session.commit()

                                                                                return jsonify({'message': 'User registered successfully'}), 201

