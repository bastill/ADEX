from django.contrib import admin
from . models import  UserActivation


class  UserActivationAdmin(admin.ModelAdmin):

    list_display = ['username', 'email', 'phone_num', 't_and_c', 'date_created', 'status']
    list_filter = ['email', 'phone_num']
    search_fields = ['phone_num']


admin.site.register(UserActivation, UserActivationAdmin)