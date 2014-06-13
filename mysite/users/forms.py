from django import forms
from users.models import UserLoginProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')

class UserLoginProfileForm(forms.ModelForm):
    class Meta:
        model = UserLoginProfile
        fields = ('mobileNumber',)
