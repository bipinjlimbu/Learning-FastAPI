from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: dict):
    return {
        "message": "User created successfully",
        "user": user
    }
    
@app.get("/users/")
def get_users():
    return {
        "status": "success",
        "message": "Users retrieved successfully",
        "data": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }
    
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id == 1:
        return {"id": 1, "name": "Alice"}
    elif user_id == 2:
        return {"id": 2, "name": "Bob"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")  