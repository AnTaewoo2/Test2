from pathlib import Path


def test_readme_contains_project_title_and_runtime_sections():
    content = Path("README.md").read_text(encoding="utf-8")

    assert "# Test2" in content
    assert "Python 실행 환경과 `Flask` 패키지가 필요합니다." in content
    assert "백엔드 실행: `flask --app app run`" in content
    assert "프런트엔드 접속: `frontend/index.html`을 브라우저로 엽니다." in content


def test_readme_documents_all_todo_api_routes():
    content = Path("README.md").read_text(encoding="utf-8")

    assert "GET /api/todos" in content
    assert "POST /api/todos" in content
    assert "POST /api/todos/<int:todo_id>/complete" in content
    assert "DELETE /api/todos/<int:todo_id>" in content

    assert '"title"' in content
    assert '"id"' in content
    assert '"completed"' in content
    assert '"error"' in content
    assert '"deleted": 1' in content
    assert '"title": "title is required"' not in content
    assert '"error": "title is required"' in content
    assert '"error": "invalid JSON"' in content
    assert '"error": "todo not found"' in content

