from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_user(name: str):
    return {"message": f"Hello, {name}!"}