BROKER_URL = "redis://nikai.io:6379/0"
CELERY_RESULT_BACKEND = "redis://nikai.io:6379/2"

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'celery_demo.task1',
    'celery_demo.task2',
)
