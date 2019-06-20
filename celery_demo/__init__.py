from celery import Celery

app = Celery('demo')
# 通过Celery实例加载配置模块
app.config_from_object('celery_demo.celeryconfig')
