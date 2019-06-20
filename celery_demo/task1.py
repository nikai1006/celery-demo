import time

from celery_demo import app


@app.task
def add(x, y):
    time.sleep(3)
    return x + y
