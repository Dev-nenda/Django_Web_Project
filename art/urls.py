# accounts/urls.py

from django.urls import path
from . import views

appname = 'art'

urlpatterns = [
    # '/art/create/
    path('create/', views.create_art, name='create_art'),
]
