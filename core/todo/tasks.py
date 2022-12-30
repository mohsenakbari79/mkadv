
from celery import shared_task
from time import sleep



@shared_task
def RemoveTask():
    from todo.models import Task
    try:
        Task.objects.filter(status=True).delete()
    except Exception as e :
        print(e)
    print("remove all  task status true")
