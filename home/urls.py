from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # /home/
    path('', views.home, name='home' )
]
