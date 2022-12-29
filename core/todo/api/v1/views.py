from rest_framework.permissions import (
    IsAuthenticated,
)
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from todo.api.v1.serializers import TaskSerializer
from todo.models import Task


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


# class CategoryModelViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CategorySerializer
#     queryset = Category.objects.all()