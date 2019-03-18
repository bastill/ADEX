from django.shortcuts import render, redirect
from . forms import TaskModelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def post_task(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            sub_message = "Task Has been posted successfully"
            messages.success(request,sub_message)
            return redirect('/dashboard/task/')
            

    else:
        form = TaskModelForm()

    return render(request, 'task/base.html', {
        'form':form,
        'section':'post-task'
    })