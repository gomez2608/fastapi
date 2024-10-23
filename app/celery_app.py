# app/celery_app.py
from celery import Celery

def create_celery():
    celery = Celery(
        __name__,
        broker="redis://redis:6379/0",
        backend="redis://redis:6379/0",
    )
    return celery

celery_app = create_celery()
