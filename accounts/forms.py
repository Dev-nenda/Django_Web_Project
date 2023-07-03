# account/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    
    phone_number = forms.CharField(max_length= 11)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone_number',)