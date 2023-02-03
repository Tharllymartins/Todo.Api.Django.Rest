from django.db import models
from django.contrib.auth.models import User
import uuid


class Task(models.Model):
    task_status = [
        (0, "To do"),
        (1, "Doing"),
        (2, "Done")
    ]
    
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete="CASCADE")
    status = models.IntegerField(default=0, choices=task_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
