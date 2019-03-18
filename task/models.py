from django.db import models
from django.contrib.auth.models import User


class TaskModel(models.Model):
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    task_title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=400, blank=False)
    due_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

