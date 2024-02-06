from django import forms
from myapp.models import Category
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','password','first_name','last_name','email']





