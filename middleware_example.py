from fastapi import FastAPI, Request
import time

app = FastAPI()

@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    print(f"Path: {request.url.path} - Request processing time: {end_time - start_time}")
    return response