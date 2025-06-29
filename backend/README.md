# Task Management System

A FastAPI-based task management application for managing and organizing tasks efficiently.

## 🚀 Features

- User authentication and authorization
- Create, read, update, and delete tasks
- Task categorization and prioritization
- Search and filter tasks
- RESTful API endpoints

## 🛠️ Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)
- SQLite (for local development)

## 🏗️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Task-Management
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r app/requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root with the following variables:
   ```env
   DATABASE_URL=sqlite:///./task_management.db
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. **Initialize the database**
   ```bash
   # Run database migrations
   cd app
   alembic upgrade head
   ```

6. **Run the application**
   ```bash
   cd app
   uvicorn main:app --reload
   ```

   The application will be available at `http://localhost:8000`

## 📚 API Documentation

Once the application is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## 🧪 Running Tests

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=app --cov-report=term-missing
```

## 🧑‍💻 Development

### Project Structure

```
app/
├── api_schemas/     # Pydantic models for request/response
├── db_models/       # SQLAlchemy models
├── helpers/         # Utility functions and helpers
├── routers/         # API route handlers
├── alembic/         # Database migrations
├── main.py          # Application entry point
└── requirements.txt # Project dependencies
```

### Code Style

This project uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting

Run code formatting:
```bash
black .
isort .
flake8
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
