from django.urls import path,include
# from . import views
from todo.api.v1 import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/task', views.TaskModelViewSet)

app_name = "todo"
urlpatterns = router.urls
# urlpatterns = [
#     path('',views.TaskListView.as_view(),name="task-list"),
#     path('create/',views.TaskCreateView.as_view(),name="task-create"),
#     path('<int:pk>/edit/',views.TaskEditView.as_view(),name="task-edit"),
#     path('<int:pk>/delete/',views.TaskDeleteView.as_view(),name="task-delete"),
#     path('<int:pk>/complate/',views.TaskComplete.as_view(),name="task-complate")
# ]
