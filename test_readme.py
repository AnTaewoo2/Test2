from pathlib import Path


def test_readme_contains_project_title_and_runtime_sections():
    content = Path("README.md").read_text(encoding="utf-8")

    assert "# Test2" in content
    assert "Python 실행 환경과 `Flask` 패키지가 필요합니다." in content
    assert "백엔드 실행: `flask --app app run`" in content
    assert "프런트엔드 접속: `frontend/index.html`을 브라우저로 엽니다." in content
