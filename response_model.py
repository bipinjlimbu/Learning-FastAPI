from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    email: str
    password: str
    name: str
    age: int
    
class UserResponse(BaseModel):
    email: str
    name: str
    age: int
    
@app.get("/users", response_model=UserResponse)
def get_users():
    return {
        "email": "bipin@gmail.com",
        "password": "securepassword",
        "name": "Bipin",
        "age": 30
    }