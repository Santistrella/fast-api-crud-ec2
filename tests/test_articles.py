import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.article import Article
from src.schemas.article import ArticleCreate, ArticleUpdate

client = TestClient(app)

def test_create_article():
    response = client.post("/articles/", json={"owner_name": "John Doe", "description": "Test article"})
    assert response.status_code == 201
    assert response.json()["owner_name"] == "John Doe"
    assert "id" in response.json()

def test_read_article():
    response = client.post("/articles/", json={"owner_name": "Jane Doe", "description": "Another test article"})
    article_id = response.json()["id"]
    
    response = client.get(f"/articles/{article_id}")
    assert response.status_code == 200
    assert response.json()["owner_name"] == "Jane Doe"

def test_update_article():
    response = client.post("/articles/", json={"owner_name": "John Doe", "description": "Update this article"})
    article_id = response.json()["id"]
    
    response = client.put(f"/articles/{article_id}", json={"owner_name": "John Doe", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["description"] == "Updated description"

def test_delete_article():
    response = client.post("/articles/", json={"owner_name": "John Doe", "description": "Delete this article"})
    article_id = response.json()["id"]
    
    response = client.delete(f"/articles/{article_id}")
    assert response.status_code == 204
    
    response = client.get(f"/articles/{article_id}")
    assert response.status_code == 404