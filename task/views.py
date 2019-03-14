from django.shortcuts import render
from . forms import TaskModelForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def post_task(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.user = request.user
            return HttpResponse("Sucess")

    else:
        form = TaskModelForm()

    return render(request, 'task/base.html', {'form':form})