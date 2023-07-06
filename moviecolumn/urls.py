from django.urls import path
from . import views

app_name ='moviecolumn'

urlpatterns = [
    # /moviecolumn/create/
    path('create/', views.create_moviecolumn, name='create_moviecolumn'),
    
    # /moviecolumn/
    path('', views.moviecolumn_index, name='moviecolumn_index'),

    # /moviecolumn/1/
    path('<int:moviecolumn_pk>/', views.moviecolumn_detail, name='moviecolumn_detail'),

    # /moviecolumn/1/update
    path('<int:moviecolumn_pk>/update', views.update_moviecolumn, name='update_moviecolumn'),

    # /moviecolumn/1/delete
    path('<int:moviecolumn_pk>/delete/', views.delete_moviecolumn, name = 'delete_moviecolumn'),

    # /moviecolumn/1/comments/create
    path('<int:moviecolumn_pk>/comments/create', views.create_comment, name='create_comments'),

    # /moviecolumn/1/comments/1/delete/
    path('<int:moviecolumn>/comments/<int:comment_pk>/delete', views.delete_comment, name='delete_comment'),

    # /moviecolumn/1/like/
    path('<int:moviecolum_pk>/like/', views.like_moviecolumn, name='like_moviecolumn'),

    # /moviecolumn/1/clipping/
    path('<int:moviecolumn_pk>/clipping/', views.clipping_moviecolumn, name='clipping_moviecolumn')
]
