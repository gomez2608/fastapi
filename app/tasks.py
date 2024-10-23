# app/tasks.py
from app.celery_app import celery_app

@celery_app.task
def add(a: int, b: int):
    return a + b
