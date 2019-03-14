from django.shortcuts import render
from . forms import SignUpForm,EmailForm


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = form.save(commit=True)
            new_user.save()
            return render(request, 'account/authentication/register_done.html', {})

    else:
        form = SignUpForm()
        

    return render(request, 'account/authentication/signup.html', {'form':form})



def password_reset(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            # send mail
            pass
    
    else:
        form = EmailForm()    

    return render(request, 'account/authentication/password-recovery.html', {'form':form})