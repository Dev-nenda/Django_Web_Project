from django.urls import path
from . import views

app_name ='moviecolumn'

urlpatterns = [
    # /moviecolumn/create/
    path('create/', views.create_moviecolumn, name='create_moviecolumn')
    
]
