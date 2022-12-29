from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from todo.models import Task

User=get_user_model()

class Command(BaseCommand):
    help = "Add five tasks with each run"

    def __init__(self, *args, **kwargs) -> None:
        super(Command,self).__init__(*args, **kwargs)
        self.faker=Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.faker.email(), password="T@123456")
        for _ in range(5):
            Task.objects.create(author=user, title=self.faker.text(),status=self.faker.boolean(chance_of_getting_true=50))
        print(f"create five task for user : {user.email} & password : T@123456")
