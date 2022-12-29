from django.urls import path,include
# from . import views

app_name = "todo"


urlpatterns = [
    path('api/v1/',include('todo.api.v1.urls')),
    
]
# urlpatterns = [
#     path('',views.TaskListView.as_view(),name="task-list"),
#     path('create/',views.TaskCreateView.as_view(),name="task-create"),
#     path('<int:pk>/edit/',views.TaskEditView.as_view(),name="task-edit"),
#     path('<int:pk>/delete/',views.TaskDeleteView.as_view(),name="task-delete"),
#     path('<int:pk>/complate/',views.TaskComplete.as_view(),name="task-complate")
# ]
