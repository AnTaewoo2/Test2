from pathlib import Path


def test_index_contains_todo_controls_and_error_area():
    content = Path("frontend/index.html").read_text(encoding="utf-8")

    assert 'id="todo-form"' in content
    assert 'id="todo-input"' in content
    assert 'id="todo-list"' in content
    assert 'id="error"' in content
    assert "app.js" in content


def test_app_references_all_api_operations():
    content = Path("frontend/app.js").read_text(encoding="utf-8")

    assert "/api/todos" in content
    assert "/api/todos/" in content
    assert "/complete" in content
    assert "GET" in content
    assert "POST" in content
    assert "DELETE" in content


def test_app_renders_and_handles_errors():
    content = Path("frontend/app.js").read_text(encoding="utf-8")

    assert "todo-list" in content
    assert "error" in content
    assert "fetch" in content
    assert "catch" in content or "try" in content


def test_frontend_assets_exist():
    assert Path("frontend/index.html").exists()
    assert Path("frontend/app.js").exists()
