# Test2

## 프로젝트 개요

Test2는 Flask로 구현한 Todo 목록 백엔드와 HTML·JavaScript 프런트엔드 프로젝트입니다. 백엔드는 Todo 생성, 조회, 완료 처리, 삭제 API를 제공하며, 프런트엔드는 `/api/todos` API를 사용해 Todo 목록을 관리합니다. Todo 데이터는 메모리에 저장됩니다.

## 필요한 Python 실행 환경

Python 실행 환경과 `Flask` 패키지가 필요합니다. `app.py`는 Flask의 `Flask`, `jsonify`, `request`와 Werkzeug의 `BadRequest`를 사용합니다. 소스에는 특정 Python 버전이나 의존성 설치 파일이 지정되어 있지 않습니다.

## 백엔드 실행 방법

`app.py`에는 Flask 애플리케이션 객체 `app`이 정의되어 있으며 별도의 `__main__` 실행 블록은 없습니다. Flask CLI에서 해당 앱 객체를 지정해 실행합니다.

백엔드 실행: `flask --app app run`

소스에는 호스트나 포트가 별도로 지정되어 있지 않습니다. 백엔드는 `/api/todos` 경로에서 Todo API를 제공합니다.

## 프런트엔드 접속 방법

프런트엔드 접속: `frontend/index.html`을 브라우저로 엽니다.

프런트엔드는 `frontend/index.html`에서 `frontend/app.js`를 불러오며, JavaScript는 `/api/todos` 상대 경로로 백엔드 API를 호출합니다. `app.py`에는 프런트엔드 정적 파일을 제공하는 라우트가 없으므로 프런트엔드의 별도 호스트, 포트 또는 접속 URL은 소스에 지정되어 있지 않습니다.
