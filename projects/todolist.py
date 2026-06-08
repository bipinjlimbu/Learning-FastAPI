from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
todos = []

class TodoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    
@app.post("/todos")
def create_todo_item(todo: TodoItem):
    todos.append(todo)
    return {"message": "Todo item created successfully", "todo": todo}

@app.get("/todos")
def get_todo_items():
    return {"todos": todos}

@app.get("/todos/{todo_id}")
def get_todo_item(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo item not found"}

@app.put("/todos/{todo_id}")
def update_todo_item(todo_id: int, updated_todo: TodoItem):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "Todo item updated successfully", "todo": updated_todo}
    return {"message": "Todo item not found"}

@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[index]
            return {"message": "Todo item deleted successfully"}
    return {"message": "Todo item not found"}