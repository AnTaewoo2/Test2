from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest

from todo import TodoStore, store as default_store


def create_app(todo_store=None):
    app = Flask(__name__)
    todo_store = todo_store if todo_store is not None else TodoStore()

    @app.route("/api/todos", methods=["GET"])
    def get_todos():
        return jsonify(todo_store.list()), 200

    @app.route("/api/todos", methods=["POST"])
    def post_todo():
        try:
            payload = request.get_json(silent=False)
        except BadRequest:
            return jsonify({"error": "invalid JSON"}), 400

        if not isinstance(payload, dict):
            return jsonify({"error": "title is required"}), 400

        title = payload.get("title")
        if not isinstance(title, str) or not title.strip():
            return jsonify({"error": "title is required"}), 400

        return jsonify(todo_store.create(title)), 201

    @app.route("/api/todos/<int:todo_id>/complete", methods=["POST"])
    def complete_todo(todo_id):
        todo = todo_store.complete(todo_id)
        if todo is None:
            return jsonify({"error": "todo not found"}), 404
        return jsonify(todo), 200

    @app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
    def delete_todo(todo_id):
        if not todo_store.delete(todo_id):
            return jsonify({"error": "todo not found"}), 404
        return jsonify({"deleted": 1}), 200

    return app


app = create_app(default_store)
