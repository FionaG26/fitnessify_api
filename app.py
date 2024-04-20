from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-RESTful API
api = Api(app, prefix='/v1')

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

# Define API input data model
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username')
parser.add_argument('email', type=str, required=True, help='Email')
parser.add_argument('password', type=str, required=True, help='Password')

# Define API endpoints
class UserRegistration(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        email = args['email']
        password = args['password']

        # Implement registration logic here
        # For example:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201

# Add the resource to the API
api.add_resource(UserRegistration, '/register')

@app.route('/')
def index():
        return render_template('index.html')
# Define main function
if __name__ == '__main__':
    # Create database tables based on models
    with app.app_context():
        db.create_all()
    # Run the Flask app
    app.run(debug=True)
