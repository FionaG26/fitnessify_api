from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize SQLAlchemy extension
db = SQLAlchemy()

# Initialize Flask-Bcrypt extension
bcrypt = Bcrypt()

# Initialize Flask-Login extension
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Specify the login view for Flask-Login
