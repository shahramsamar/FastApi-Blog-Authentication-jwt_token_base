# FastAPI Blog Authentication JWT Token Base

A Python project that implements a basic blog application using **FastAPI** with JWT (JSON Web Token) authentication. This project demonstrates how to secure an API with JWT tokens, enabling user authentication and authorization for accessing blog-related features.

## Features

- **JWT Authentication**: Provides secure user authentication using JWT tokens.
- **User Registration**: Allows users to register with a username and password.
- **User Login**: Allows users to log in and receive a JWT token.
- **Protected Endpoints**: Protects certain routes (e.g., creating and managing blog posts) so only authenticated users can access them.
- **Blog CRUD Operations**: Create, read, update, and delete blog posts, with JWT-based authorization.

## Requirements

- **Python 3.x**
- **FastAPI**
- **Pydantic** (for request validation)
- **SQLAlchemy** (for database integration)
- **Uvicorn** (for running the FastAPI application)
- **PyJWT** (for handling JWT token encoding and decoding)
- **bcrypt** (for password hashing)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/FastApi-Blog-Authentication-jwt_token_base.git
    cd FastApi-Blog-Authentication-jwt_token_base
    ```

2. **Install Dependencies:**

    If you're using `pip`, run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:

    To run the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

### How to Use

1. **Register a User**: 
   - Send a POST request to `/register` with a `username` and `password`.
   - This will create a new user in the system.

2. **Login to Receive JWT Token**:
   - Send a POST request to `/login` with the correct `username` and `password`.
   - The response will include a JWT token.

3. **Access Protected Endpoints**:
   - Send a GET, POST, PUT, or DELETE request to the blog-related routes (e.g., `/posts`, `/posts/{id}`) with the `Authorization` header containing the JWT token:
     ```bash
     Authorization: Bearer your_jwt_token
     ```
   - This will allow you to create, view, update, and delete blog posts.

4. **Create, Read, Update, and Delete Blog Posts**:
   - Use the `/posts` and `/posts/{id}` endpoints for CRUD operations, which are only accessible by authenticated users.

### Project Structure

- `main.py`: Contains the FastAPI application, routes, and logic for handling authentication, blog operations, and JWT token generation.
- `models.py`: Defines the database models using SQLAlchemy.
- `schemas.py`: Contains Pydantic models for data validation.
- `requirements.txt`: Lists necessary libraries like `FastAPI`, `SQLAlchemy`, `PyJWT`, and `bcrypt`.

## Contributing

Feel free to fork the project and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.
