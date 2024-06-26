from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name','last_name','email','username','password1','password2',
        ]
