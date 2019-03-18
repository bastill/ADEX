from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from task.forms import TaskModelForm
from django.utils import timezone



@login_required
def dashboard(request):
    
    all_users = UserProfile.objects.all()
    if request.user.is_staff:          
       return render(request, 'dashboard/user_dashboard/all_users.html', {
        'section':'users',
        'all_users' : all_users
    })

    else:
        form = TaskModelForm()
        return render(request, 'task/base.html', {
            'section':'post-task',
            'form':form
        })



@staff_member_required
@login_required
def pending_users(request):
    pending_users = UserProfile.pending.all()
    return render(request, 'dashboard/user_dashboard/pending_users.html', {
        'section':'pending',
        'pending_users':pending_users
    })


@staff_member_required
@login_required
def approved_users(request):
    approved_users = UserProfile.approved.all()
    return render(request, 'dashboard/user_dashboard/approved_users.html', {
        'section':'approved',
        'approved_users' : approved_users
    })


@staff_member_required
@login_required
def activate_users(request, username):
     
    activate_user = get_object_or_404(UserProfile, user__username=username)
    if activate_user.status == True:
        messages.success(request, 'User account is already activated')

    else:
        activate_user.status = True 
        activate_user. date_activated = timezone.now()
        activate_user.save()
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        sub_message = "{} account have been approved".format(activate_user.user.username)
        messages.success(request, sub_message)
        

    #storage = messages.get_messages(request)
    #pending_users = UserProfile.pending.all()

    return redirect('/dashboard/pending-users/')
    
    '''
    render(request, 'dashboard/user_dashboard/pending_users.html', {
        'section':'pending',
        'pending_users':pending_users,
        'messages':storage
    })
'''