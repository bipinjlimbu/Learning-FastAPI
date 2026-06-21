from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_user():
    return {"message": "Hello, World!"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}