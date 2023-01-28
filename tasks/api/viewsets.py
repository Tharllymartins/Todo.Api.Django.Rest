from rest_framework.viewsets import ModelViewSet
from .serializer import TaskSerializer
from tasks.models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        queryset = Task.objects.all()
        
        status = self.request.query_params.get("status", None)
        
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset