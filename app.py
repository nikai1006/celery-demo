# from tasks import add
from celery_demo import task1, task2

task1.add.delay(3, 4)
task2.multiply.delay(4, 6)
print("end..........")
# if __name__ == '__main__':
#     print("taskt start")
#     result = add.delay(3, 4)
#     print("task end")
#     print(result)
