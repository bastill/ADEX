from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='index'),
    url(r'^approved-users/$', views.dashboard, name='approved_users'),
    url(r'^pending-users/$', views.pending_users, name='pending_users'),
    url(r'^all-users/$', views.approved_users, name='all_users'),
    url(r'^task/', include('task.urls')),
]

#just testing