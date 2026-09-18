from pathlib import Path


def test_index_contains_todo_controls_and_error_area():
    content = Path("frontend/index.html").read_text(encoding="utf-8")

    assert 'id="todo-form"' in content
    assert 'id="todo-input"' in content
    assert 'id="todo-list"' in content
    assert 'id="error"' in content
    assert "app.js" in content
