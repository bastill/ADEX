from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token    
from . import views


urlpatterns = [
    url(r'^(?P<token>[-\w]+)/tasks/(?P<id>\d+)/$',views.TaskDetailView.as_view(), name='task_detail'),
    url(r'^(?P<token>[-\w]+)/tasks/$', views.TaskListView.as_view(), name='task_list'),
    url(r'^token-auth/(?P<token>[-\w]+)/$', views.UserAuthToken.as_view(), name='token-auth'),
]