# jobs/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'block border border-gray-300 p-2 w-full rounded mb-4',
        'placeholder': 'Email',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block border border-gray-300 p-2 w-full rounded mb-4',
                'placeholder': 'Username',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'block border border-gray-300 p-2 w-full rounded mb-4',
                'placeholder': 'Password',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'block border border-gray-300 p-2 w-full rounded mb-4',
                'placeholder': 'Confirm Password',
            }),
           
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'block border border-gray-300 p-2 w-full rounded mb-4',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block border border-gray-300 p-2 w-full rounded mb-4',
        'placeholder': 'Password',
    }))
