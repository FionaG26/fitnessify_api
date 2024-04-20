# Fitnessify_api

This project is about a simple user registration API built using Python with Flask framework. It provides endpoints for user registration, data validation, secure password storage, and error handling. The API integrates with PostgreSQL for secure storage of user data.

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
├── app.py
├── models.py
├── config.py
├── api/
│   ├── __init__.py
│   └── routes.py
├── tests/
│   ├── __init__.py
│   └── test_routes.py
│   └── test_models.py
└── docs/
└── api_documentation.md
├── requirements.txt
```

# Contributors

- [Fiona Githaiga](https: // github.com / FionaG26)

# License

This project is licensed under the[MIT License](LICENSE).
