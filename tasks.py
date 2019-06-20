import time

from celery import Celery

broker = "redis://nikai.io:6379/0"
backend = "redis://nikai.io:6379/2"
app = Celery('nikai_task', broker=broker, backend=backend)


@app.task
def add(x, y):
    print("enter the function")
    time.sleep(3)
    return x + y