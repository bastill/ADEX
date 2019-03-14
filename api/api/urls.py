from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^task/$', views.TaskListView.as_view(), name='task_list'),
    url(r'^token-auth/(?P<token>[-\w]+)', views.AuthTokenView.as_view(), name='token-auth'),
    url(r'^task/(?P<pk>\d+)/$',views.TaskDetailView.as_view(), name='task_detail'),
       
]