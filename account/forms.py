from re import findall
from django.contrib.auth.models import User
from account.models import UserProfile
from django import forms



class SignUpForm(forms.Form):
    username = forms.CharField(max_length=40, required=True)
    email    = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=14)
    password = forms.CharField(min_length=8, max_length=25, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)
    t_and_c  = forms.BooleanField(required=True)
    
    
    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])

        except User.DoesNotExist:
            return self.cleaned_data['username']
            
        else:
            raise forms.ValidationError('Sorry this username is already taken.')
       


    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])

        except User.DoesNotExist:
            return self.cleaned_data['email']
            
        else:
            raise forms.ValidationError('Sorry this email id is already taken.')
        
        

    '''
    def clean_password(self):
        cd = self.cleaned_data
        if findall('[^A-Za-z0-9]', cd['password']) and any(x.isupper() for x in cd['password']):
            raise forms.ValidationError("Please password must contain a symbol,digit,and a uppercase letter")
           
        
        return self.cleaned_data['password']
    '''     


    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Passwords don't match.")

        return self.cleaned_data['password2']


    def clean_phone_number(self):
        try:
            int(self.cleaned_data['phone_number'])

        except ValueError:
            raise forms.ValidationError("Sorry phone number must contain only digits")

        if len(self.cleaned_data['phone_number']) > 14 :
            raise forms.ValidationError("Sorry phone number is incorrect")
        try:
            UserProfile.objects.get(phone_number=self.cleaned_data['phone_number'])

        except UserProfile.DoesNotExist:
            return self.cleaned_data['phone_number']
            
        else:
            raise forms.ValidationError("Sorry phone number is already in use.")

        



class EmailForm(forms.Form):
    email = forms.EmailField(max_length=40, required=True)