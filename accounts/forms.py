# account/forms.py
from django import forms

from django.contrib.auth.forms import UsercreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UsercreationForm):
    
    phone_number = forms.CharField(max_length= 11)

    class Meta:
        model = get_user_model()
        fields = ('username',)