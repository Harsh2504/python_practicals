from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'bg-transparent border border-gray-600 text-green-500 w-full p-2 mt-4',
        'placeholder': 'Enter your email...',
        'required': True,
    }))
