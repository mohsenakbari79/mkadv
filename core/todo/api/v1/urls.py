from todo.api.v1 import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'task', views.TaskModelViewSet)

app_name = "api-v1"
urlpatterns = router.urls