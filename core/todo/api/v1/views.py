# from rest_framework.decorators import action
# from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from django.views.decorators.vary import vary_on_cookie
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from todo.api.v1.serializers import TaskSerializer
from todo.models import Task
import requests


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = {'category':["exact","in"], 'author':["exact"],'status':["exact"]}
    # filterset_class = PostFilters
    # search_fields = ["title", "content"]
    # ordering_fields = ["published_date"]
    # pagination_class = DefaultPagination


class GetWeather(viewsets.ViewSet):
    # With cookie: cache requested url for each user for 2 hours
    @method_decorator(cache_page(20*60))
    @method_decorator(vary_on_cookie)
    def list(self, request, format=None):
        API_key = "5ad0e4cf5c414c0c903104202223112"
        url = f"http://api.weatherapi.com/v1/current.json?key={API_key}&q=32.661343,51.680374&aqi=yes"
        content = requests.get(url).json()
        return Response(content)

# class CategoryModelViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()
