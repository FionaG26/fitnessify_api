from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from config import SQLALCHEMY_DATABASE_URI
from flask_restplus import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create Flask-RESTPlus API instance
api = Api(app, version='1.0', title='Fitnessify API',
          description='API documentation for Fitnessify')

# Register Blueprint
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def root():
    return 'Root endpoint'

if __name__ == "__main__":
    app.run(debug=True)
