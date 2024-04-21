# Fitnessify API Documentation

## Endpoints

### User Registration

- **URL:** `/register`
- **Method:** POST
- **Description:** Registers a new user with the provided information.
- **Request Body:**
  - `username` (string, required): User's username.
  - `email` (string, required): User's email address.
  - `password` (string, required): User's password.
- **Success Response:**
  - **Code:** 201 Created
  - **Content:** `{ "message": "User registered successfully" }`
- **Error Responses:**
  - **Code:** 400 Bad Request
    - **Content:** `{ "message": "Missing username, email, or password" }`
  - **Code:** 400 Bad Request
    - **Content:** `{ "message": "Invalid email format" }`
  - **Code:** 400 Bad Request
    - **Content:** `{ "message": "Weak password" }`
  - **Code:** 400 Bad Request
    - **Content:** `{ "message": "Username already exists" }`
  - **Code:** 500 Internal Server Error
    - **Content:** `{ "message": "An error occurred" }`
