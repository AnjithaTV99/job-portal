from django import forms
from myapp.models import Category,Job
from django.forms import Select

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        # exclude = ('salary')
        fields = '__all__'
        widgets = {
            'category':Select(attrs={
                'class': "form-select",
                
                
                }),
        }

