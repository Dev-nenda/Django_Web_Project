# accounts/urls.py

from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # /account/signup/
    path('signup/', views.signup, name='signup'),

    # /account/login/
    path('login/', views.login, name='login'),

    # /account/logout/
    path('logout/', views.logout, name= 'logout'),


    path('set_general_permission/', views.set_general_permission, name='set_general_permission'),

    # /account/nenda/
    path('<str:username>/', views.profile, name='profile'),

    # /account/nenda/follow/
    path('<str:username>/follow/', views.follow, name='follow'),

    # account/nenda/followers/
    path('<str:username>/followers/', views.followers, name='followers'),

    # /account/nenda/followings/
    path('<str:username>/followings/', views.followings, name='followings'),

    #/account/nenda/delete/
    path('<str:username>/delete/', views.delete, name='delete'),

    #/account/nenda/update/
    path('<str:username>/update/', views.update, name='update'),

    path('<str:username>/password/', views.change_password, name='change_password')
   
]
