from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = "redis://nikai.io:6379/0"
CELERY_RESULT_BACKEND = "redis://nikai.io:6379/2"

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'celery_demo.task1',
    'celery_demo.task2',
)

# 调度配置
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_demo.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (23, 43)
    },
    'task2': {
        'task': 'celery_demo.task2.multiply',
        'schedule': crontab(hour=1, minute=3),
        'args': (9, 22)
    }
}
