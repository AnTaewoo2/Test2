from todo import TodoStore


def test_create_assigns_id_and_defaults_completed():
    store = TodoStore()

    assert store.create("Buy milk") == {
        "id": 1,
        "title": "Buy milk",
        "completed": False,
    }


def test_list_returns_created_todos():
    store = TodoStore()
    store.create("Buy milk")

    assert store.list() == [
        {"id": 1, "title": "Buy milk", "completed": False}
    ]


def test_complete_marks_todo_completed():
    store = TodoStore()
    store.create("Buy milk")

    assert store.complete(1) == {
        "id": 1,
        "title": "Buy milk",
        "completed": True,
    }


def test_delete_removes_todo():
    store = TodoStore()
    store.create("Buy milk")

    assert store.delete(1)
    assert store.list() == []
