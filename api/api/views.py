from task.models import TaskModel
from . serializers import TaskModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.http import HttpResponse


def authenticate_usertoken_status(token):
    try:
        user_token = Token.objects.get(key=token)
        return user_token.user
            
    except Token.DoesNotExist:
        return None


class  UserAuthToken(APIView):

    def get(self, request, token):
      user =  authenticate_usertoken_status(token)
      if user == None:
        return Response({
            'authentication_failed':'Sorry token does not exist.',
        })
      
      else:
        return Response({
            'username':user.username,
            'email':user.email,
            'authenticated': True,
            'Session':'Inactivate'
        })


class TaskListView(APIView):
   

    def get(self, request, token):
        user =  authenticate_usertoken_status(token)
        if user == None:
            return Response({'Invalid_token':'Sorry token does not exist.'})

        else:
            task = TaskModel.objects.filter(user__username=user.username)
            serializer = TaskModelSerializer(task, many=True)
            return Response(serializer.data)



class TaskDetailView(APIView):

    def get(self, request, token, id):
        user =  authenticate_usertoken_status(token)
        if user == None:
            return Response({'Invalid_token':'Sorry token does not exist.'})

        else:    
            try:
                detail_task = TaskModel.objects.get(id=pk)
                serializer = TaskModelSerializer(detail_task)
                return Response(serializer.data)

            except TaskModel.DoesNotExist:
                return Response({'Empty_Task':'Sorry empty value found at index'})


