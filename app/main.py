# app/main.py
from fastapi import FastAPI
from app.celery_app import celery_app
from app.tasks import add

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with Celery and Nginx!"}

@app.get("/add/{a}/{b}")
async def add_numbers(a: int, b: int):
    task = add.delay(a, b)  # Run the task asynchronously
    return {"task_id": task.id, "status": "Task submitted!"}

@app.get("/task/{task_id}")
async def get_task_status(task_id: str):
    task = celery_app.AsyncResult(task_id)
    return {"task_id": task.id, "status": task.status, "result": task.result}
