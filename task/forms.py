from django import forms
from . models import TaskModel


class TaskModelForm(forms.ModelForm):

    class Meta:
        model = TaskModel
        fields = ['task_title', 'description', 'due_date']