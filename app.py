from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.routes import api
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Register Blueprint
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def root():
    return 'Root endpoint'

if __name__ == "__main__":
    app.run(debug=True)
