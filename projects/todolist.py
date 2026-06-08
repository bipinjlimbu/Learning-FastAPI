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