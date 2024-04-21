# Fitnessify_api

This project is about a simple user registration API built using Python with Flask framework. It provides endpoints for user registration, data validation, secure password storage, and error handling. The API integrates with MySQL for secure storage of user data.

# Setup

1. Clone the Repository:
    ```bash
    git clone < repository_url >
    cd fitnessify_api
    ```

2. Setup Virtual Environment:
    ```
    python3 - m venv venv
    source venv / bin / activate
    ```

3. ** Install Dependencies**:
    ```
    pip install - r requirements.txt
    ```

4. ** Database Configuration**:
    - Configure the PostgreSQL database URI in `config.py`:
        ```python
        SQLALCHEMY_DATABASE_URI = 'postgresql://your_username:your_password@localhost/fitnessify'
        ```

5. ** Running the Application**:
    ```
    export FLASK_APP = app.py
    export FLASK_ENV = development
    flask run
    ```

6. ** API Endpoints**:
    - **POST / register**: Register a new user. Requires JSON payload with username, email, and password.

7. ** Testing**:
    - Run unit tests:
        ```
        python - m unittest tests.test_routes
        ```

# Directory Structure

```
fitnessify_api/
│
├── README.md               # Documentation
├── api_documentation.md    # API Documentation
├── __pycache__             # Python bytecode cache
├── api/                    # Main API package
│   ├── __init__.py         # Package initializer
│   ├── __pycache__         # Python bytecode cache for API package
│   ├── app.py              # Flask application setup
│   ├── config.py           # Configuration settings
│   ├── models.py           # Data models definition
│   ├── routes.py           # API endpoints definition
│   ├── static/             # Static files (e.g., CSS, JavaScript)
│   ├── templates/          # HTML templates
│   └── tests/              # Unit tests for the API
├── create_db.py            # Script for creating database
├── extensions.py           # Flask extensions setup
├── instance/               # Instance folder for configuration (not included in repository)
├── users.db                # Database file for storing user data
└── venv/                   # Virtual environment (Python dependencies)


```

# Contributors

- [Fiona Githaiga](https://github.com/FionaG26)

# License

This project is licensed under the[MIT License](LICENSE).
