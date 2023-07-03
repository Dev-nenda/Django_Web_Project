# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # /accounts/signup/
    path('signup/', views.signup, name='signup'),
    
]
