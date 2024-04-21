from app import app, db
from models import User

try:
    # Create all database tables within the application context
    with app.app_context():
        # Create all database tables
        db.create_all()
        # Commit the changes
        db.session.commit()
        print("Database tables created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
