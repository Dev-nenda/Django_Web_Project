from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # /home/
    path('', views.home, name='home' ),
    #/search/
    path('search/', views.search, name='search')
]
