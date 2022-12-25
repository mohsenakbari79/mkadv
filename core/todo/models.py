from django.db import models

# Create your models here.

class Task(models.Model):
    """
    this is a class to define posts for blog app
    """
    author = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title