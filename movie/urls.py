# movie/urls.py

from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    # /movie/create/
    path('create/', views.create_movie, name='create_movie'),
    
    # /movie/
    path('', views.movie_index, name= 'movie_index'),

    # /movie/1/
    path('<int:movie_pk>/', views.movie_detail, name= 'movie_detail'),

    # /movie/1/update/
    path('<int:movie_pk>/update/', views.update_movie, name='update_movie'),

    # /movie/1/delete/
    path('<int:movie_pk>/delete', views.delete_movie, name='delete_movie'),

    # /movie/1/expert_reviews/create/
    path('<int:movie_pk>/expert_reviews/create/', views.create_expert_review, name='create_expert_review'),

    # /movie/1/exeprt_reviews/1/delete/
    path('<int:movie_pk>/expert_reviews/<int:expert_review_pk>/delete/', views.delete_expert_review, name='delete_expert_review'),

    # /movie/1/general_reviews/create/
    path('<int:movie_pk>/general_reviews/create/', views.create_general_review, name='create_general_review'),

    # /movie/1/exeprt_reviews/1/delete/
    path('<int:movie_pk>/general_reviews/<int:general_review_pk>/delete/', views.delete_general_review, name='delete_general_review'),

    # /movie/1/like/
    path('<int:movie_pk>/like/', views.like_movie, name='like_movie')
]
