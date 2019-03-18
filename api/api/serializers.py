from rest_framework import serializers
from task.models import TaskModel


class TaskModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskModel
        fields = ['task_title', 'description', 'due_date']