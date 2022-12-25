from django.urls import path, include
from . import views


from django.urls import include, path

app_name = "accounts"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # path('', include('django.contrib.auth.urls')),
    
    
]




