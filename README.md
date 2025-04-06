# fastapi-crud-api/fastapi-crud-api/README.md

# FastAPI CRUD API

This project is a simple CRUD API built with FastAPI. It allows you to create, read, update, and delete articles. Each article has an ID, owner name, creation date, and description. The API also includes Swagger documentation for easy testing and interaction.

## Project Structure

```
fastapi-crud-api
├── src
│   ├── main.py          # Entry point of the application
│   ├── models
│   │   └── article.py   # SQLAlchemy model for articles
│   ├── routers
│   │   └── articles.py   # CRUD operations for articles
│   └── schemas
│       └── article.py   # Pydantic schemas for article validation
├── tests
│   └── test_articles.py  # Unit tests for CRUD operations
├── requirements.txt      # Project dependencies
├── .gitignore            # Files to ignore by Git
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-crud-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn src.main:app --reload
   ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Usage

You can use the following endpoints to interact with the articles:

- **Create an article**: `POST /articles/`
- **Read all articles**: `GET /articles/`
- **Read an article by ID**: `GET /articles/{id}`
- **Update an article**: `PUT /articles/{id}`
- **Delete an article**: `DELETE /articles/{id}`

## License

This project is licensed under the MIT License.