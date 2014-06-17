from django.contrib import admin
from django import forms
from user import models as user_models
#from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = user_models.CareGrooveUser
        fields = ('name', 'email', 'password')



'''
class UserLoginProfileForm(forms.ModelForm):
    class Meta:
        model = UserLoginProfile
        fields = ('mobileNumber', )
'''

"""
class UserForm(forms.ModelForm):
    """ """A form for creating new users. Includes all the required
    fields, plus a repeated password.""" """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'username', )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
"""

