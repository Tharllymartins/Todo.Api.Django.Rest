from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializer
from tasks.models import Task


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer