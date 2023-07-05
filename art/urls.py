# art/urls.py

from django.urls import path
from . import views

app_name = 'art'

urlpatterns = [
    # /art/create/
    path('create/', views.create_art, name='create_art'),
    
    # /art/
    path('', views.art_index, name = 'art_index'),

    # /art/1/
    path('<int:art_pk>/', views.art_detail, name='art_detail'),

    # /art/1/update/
    path('<int:art_pk>/update', views.update_art, name='update_art'),

    # /art/1/delete/
    path('<int:art_pk>/delete', views.delete_art, name='delete_art'),

    # /art/1/comments/create'
    path('<int:art_pk>/comments/create', views.create_comment, name='create_comment'),

    # /art/1/comments/1/delete/
    path('<int:art_pk>/comments/<int:comment_pk>/delete', views.delete_comment, name ='delete_comment'),

    # /art/1/like/
    path('<int:art_pk>/like/', views.like_art, name='like_art'),

    # /art/1/clipping/
    path('<int:art_pk>/clipping/', views.clipping_art, name='clipping_art'),
]
