import pytest

from app import create_app
from todo import TodoStore


@pytest.fixture
def client():
    store = TodoStore()
    app = create_app(store)
    return app.test_client()


def test_get_todos_empty(client):
    response = client.get("/api/todos")

    assert response.status_code == 200
    assert response.get_json() == []


def test_post_todo(client):
    response = client.post("/api/todos", json={"title": "Buy milk"})

    assert response.status_code == 201
    assert response.get_json() == {
        "id": 1,
        "title": "Buy milk",
        "completed": False,
    }


def test_post_todo_rejects_missing_title(client):
    missing_response = client.post("/api/todos", json={})
    blank_response = client.post("/api/todos", json={"title": "   "})

    assert missing_response.status_code == 400
    assert missing_response.get_json() == {"error": "title is required"}
    assert blank_response.status_code == 400
    assert blank_response.get_json() == {"error": "title is required"}


def test_complete_todo(client):
    client.post("/api/todos", json={"title": "Buy milk"})

    response = client.post("/api/todos/1/complete")

    assert response.status_code == 200
    assert response.get_json() == {
        "id": 1,
        "title": "Buy milk",
        "completed": True,
    }


def test_complete_missing_todo(client):
    response = client.post("/api/todos/1/complete")

    assert response.status_code == 404
    assert response.get_json() == {"error": "todo not found"}


def test_delete_todo(client):
    client.post("/api/todos", json={"title": "Buy milk"})

    response = client.delete("/api/todos/1")

    assert response.status_code == 200
    assert response.get_json() == {"deleted": 1}


def test_delete_missing_todo(client):
    response = client.delete("/api/todos/1")

    assert response.status_code == 404
    assert response.get_json() == {"error": "todo not found"}


def test_post_todo_rejects_malformed_json(client):
    response = client.post(
        "/api/todos",
        data='{"title": ',
        content_type="application/json",
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "invalid JSON"}
