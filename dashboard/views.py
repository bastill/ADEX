from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import UserActivation
from task.forms import TaskModelForm


@login_required
def dashboard(request):
    form = TaskModelForm()
    all_users = UserActivation.objects.all()
    if request.user.is_staff:          
       return render(request, 'dashboard/user_dashboard/all_users.html', {
        'section':'users',
        'all_users' : all_users
    })

    else:
         return render(request, 'task/base.html', {
            'section':'post-task',
            'form':form
        })


    


@login_required
def pending_users(request):
    pending_users = UserActivation.pending.all()
    return render(request, 'dashboard/user_dashboard/pending_users.html', {
        'section':'pending',
        'pending_users':pending_users
    })


@login_required
def approved_users(request):
    approved_users = UserActivation.approve.all()
    return render(request, 'dashboard/user_dashboard/approved_users.html', {
        'section':'approved',
        'approved_users' : approved_users
    })