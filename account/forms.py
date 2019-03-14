from re import findall
from django import forms
from . models import UserActivation

class SignUpForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    password_2 = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = UserActivation
        fields = ['username', 'email', 'phone_num', 't_and_c', 'password', 'password_2']

    def clean_password(self):
        cd = self.cleaned_data
        if findall('[^A-Za-z0-9]', cd['password']) and any(x.isupper() for x in cd['password']):
            return cd['password']

        else:
            raise forms.ValdationError("Password must contain a special symbol and a captial letter.")
        

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password_2']

  

class EmailForm(forms.Form):
    email = forms.EmailField(max_length=40, required=True)