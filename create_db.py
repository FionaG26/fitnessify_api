from app import app, db
from models import User

# Create all database tables within the application context
with app.app_context():
    # Create all database tables
    db.create_all()
    # Commit the changes
    db.session.commit()
