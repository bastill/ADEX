from django.contrib import admin
from . models import TaskModel
# Register your models here.

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'task_title', 'description', 'date_created', 'due_date']
    list_filter = ['user', 'task_title', 'due_date']




admin.site.register(TaskModel, TaskModelAdmin)
    
