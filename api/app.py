from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes import api_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://Fiona:Fiona@localhost/Fitnessify'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '32b2ac3412fcba55ed561c14e2de4e5'

db = SQLAlchemy(app)

# Register the Blueprint
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
