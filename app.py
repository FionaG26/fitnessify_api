from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from config import SQLALCHEMY_DATABASE_URI
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create Swagger blueprint
SWAGGER_URL = '/api/docs'
API_URL = '/api/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Fitnessify API Documentation"
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

db = SQLAlchemy(app)

# Register Blueprint
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def root():
    return 'Root endpoint'

if __name__ == "__main__":
    app.run(debug=True)
