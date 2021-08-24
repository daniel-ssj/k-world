from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-400 text-gray-300 rounded-l',
                'placeholder': 'username',
            }
        )
    )

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-gray-400 text-gray-300 rounded-l mt-1',
                'placeholder': 'password',
            }
        )
    )

    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
           attrs={
                'class': 'bg-gray-400 text-gray-300 rounded-l mt-1',
                'placeholder': 'confirm password',
            }
        )
    )
