from django.urls import path, include
from accounts.api.v1 import views


from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path("signup/", views.RegistrationApiView.as_view(), name="registration"),
    path('', include('django.contrib.auth.urls')),
]
