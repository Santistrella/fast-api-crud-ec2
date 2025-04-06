from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import articles
from .database import engine
from .models import article

# Create database tables
article.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Articles API",
    description="A simple CRUD API for managing articles",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(articles.router, prefix="/api/v1", tags=["articles"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI CRUD API!"}