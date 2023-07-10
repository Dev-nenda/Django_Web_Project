# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # /accounts/signup/
    path('signup/', views.signup, name='signup'),

    # /accounts/login/
    path('login/', views.login, name='login'),

    # /accounts/logout/
    path('logout/', views.logout, name= 'logout'),

    # /accounts/nenda/
    path('<str:username>/', views.profile, name='profile'),

    # /accounts/nenda/follow/
    path('<str:username>/follow/', views.follow, name='follow'),

    # accounts/nenda/followers/
    path('<str:username>/followers/', views.followers, name='followers'),

    # /accounts/nenda/followings/
    path('<str:username>/followings/', views.followings, name='followings'),

]
