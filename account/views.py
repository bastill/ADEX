from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import SignUpForm
from . models import UserProfile


def register(request):
    
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            cd = signup_form.cleaned_data
            new_user = User.objects.create(
                username = cd['username'],
                email   = cd['email']
            )
            new_user.set_password(cd['password'])
            new_user.is_active = False
            new_user.save()
            new_profile = UserProfile.objects.create(
                user = new_user,
                phone_number = cd['phone_number'],
                t_and_c = cd['t_and_c']
            )
            new_profile.save()
            
            return render(request, 'account/authentication/register_done.html', {
                'email':new_user.email
            })

    else:
        signup_form = SignUpForm()

    return render(request, 'account/authentication/signup.html', {
        'form':signup_form,
    })


def password_reset(request):

    return render(request, 'account/authentication/password-recovery.html', {})