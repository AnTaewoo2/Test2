const TODOS_URL = "/api/todos";
const TODO_URL_PREFIX = "/api/todos/";
const COMPLETE_URL_SUFFIX = "/complete";

const todoForm = document.getElementById("todo-form");
const todoInput = document.getElementById("todo-input");
const todoList = document.getElementById("todo-list");
const errorArea = document.getElementById("error");

function showError(message) {
  errorArea.textContent = message;
}

function clearError() {
  errorArea.textContent = "";
}

async function request(url, options) {
  const response = await fetch(url, options);
  const text = await response.text();
  let data = null;

  if (text) {
    try {
      data = JSON.parse(text);
    } catch (error) {
      data = text;
    }
  }

  if (!response.ok) {
    const message =
      (data && typeof data === "object" && (data.error || data.detail)) ||
      (typeof data === "string" && data) ||
      `Request failed with status ${response.status}`;
    throw new Error(message);
  }

  return data;
}

function renderTodos(todos) {
  todoList.replaceChildren();

  todos.forEach((todo) => {
    const item = document.createElement("li");
    const title = document.createElement("span");
    const completeButton = document.createElement("button");
    const deleteButton = document.createElement("button");

    title.textContent = todo.completed
      ? `${todo.title} (completed)`
      : todo.title;
    item.dataset.completed = String(todo.completed);

    completeButton.type = "button";
    completeButton.textContent = todo.completed ? "Completed" : "Complete";
    completeButton.disabled = todo.completed;
    completeButton.addEventListener("click", async () => {
      try {
        clearError();
        await request(`${TODO_URL_PREFIX}${todo.id}${COMPLETE_URL_SUFFIX}`, {
          method: "POST",
        });
        await loadTodos();
      } catch (error) {
        showError(error.message);
      }
    });

    deleteButton.type = "button";
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", async () => {
      try {
        clearError();
        await request(`${TODO_URL_PREFIX}${todo.id}`, {
          method: "DELETE",
        });
        await loadTodos();
      } catch (error) {
        showError(error.message);
      }
    });

    item.append(title, completeButton, deleteButton);
    todoList.appendChild(item);
  });
}

async function loadTodos() {
  try {
    const data = await request(TODOS_URL, { method: "GET" });
    const todos = Array.isArray(data) ? data : data.todos || [];
    renderTodos(todos);
    clearError();
  } catch (error) {
    showError(error.message);
  }
}

todoForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const title = todoInput.value.trim();
  if (!title) {
    return;
  }

  try {
    clearError();
    await request(TODOS_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ title }),
    });
    todoInput.value = "";
    await loadTodos();
  } catch (error) {
    showError(error.message);
  }
});

loadTodos();
