from django.shortcuts import get_object_or_404
from rest_framework import generics
from task.models import TaskModel
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authtoken.models import Token


class  TaskListView(generics.ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer



class AuthTokenView(APIView):
    
    def get(self, request,token):
        try:
            user_token = Token.objects.get(key=token)
            content = {'success':'Welcome, adex'}

        except Token.DoesNotExist:
            content = {'message':'Authentication token is invalid '} 
           
        return Response(content)
