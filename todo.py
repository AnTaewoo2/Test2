class TodoStore:
    """An in-memory store for todo items."""

    def __init__(self):
        self._todos = {}
        self._next_id = 1

    def create(self, title):
        todo = {
            "id": self._next_id,
            "title": title,
            "completed": False,
        }
        self._todos[self._next_id] = todo
        self._next_id += 1
        return todo.copy()

    def list(self):
        return [todo.copy() for todo in self._todos.values()]

    def complete(self, todo_id):
        todo = self._todos.get(todo_id)
        if todo is None:
            return None
        todo["completed"] = True
        return todo.copy()

    def delete(self, todo_id):
        if todo_id not in self._todos:
            return False
        del self._todos[todo_id]
        return True


store = TodoStore()
