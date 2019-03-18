from django.contrib import admin
from . models import  UserProfile


class  UserProfileAdmin(admin.ModelAdmin):

    list_display = ['user',  'phone_number', 't_and_c', 'date_activated','status']
    list_filter = ['user', 'phone_number', 'date_activated','status']
    search_fields = ['phone_number','user']


admin.site.register(UserProfile, UserProfileAdmin)