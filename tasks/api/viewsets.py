from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializer import TaskSerializer
from tasks.models import Task
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user.id)
        
        status = self.request.query_params.get("status", None)
        
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset