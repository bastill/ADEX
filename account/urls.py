from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login,logout,logout_then_login,
    password_change,password_change_done,
    password_reset,password_reset_done,
    password_reset_confirm,password_reset_complete
)



urlpatterns = [
    # Authentication Urls (Predefined Django Views)
    url(r'^auth/login/$', login, {'template_name':'account/authentication/login.html'}, name='login'),
    url(r'^auth/logout/$', logout, {'template_name':'account/authentication/logged_out.html'},  name='logout'),
    url(r'^auth/logout_then_login/$', logout_then_login, name='logout_then_login'),
    url(r'^auth/password-change/$', password_change, name='password_change'),
    url(r'^auth/password-change/done/$', password_change_done, name='password_change_done'),
    url(r'^auth/reset-password/$', views.password_reset, name='password_reset'),
    url(r'^auth/password-reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^auth/password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm, name='password_reset_confirm'),

    # SignUp  Urls (Customs views)
    url(r'^auth/signup/$', views.register, name='signup')
]
