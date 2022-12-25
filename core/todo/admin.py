from django.contrib import admin
from todo.models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "status",
        "created_date",
    ]


admin.site.register(Task,TaskAdmin)