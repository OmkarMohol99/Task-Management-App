from django.db import models
from django.contrib.auth.models import User

class TaskManagementModel(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

    def __str__(self):
        return f'{self.task_name}'
