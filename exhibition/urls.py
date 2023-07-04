# exhibition/urls/py

from django.urls import path
from . import views


app_name = 'exhibition'

urlpatterns = [
    #/exhibition/create/
    path('create/', views.create_exhibition, name='create_exhibition'),

    # /exhibition/
    path('', views.exhibition_index, name='exhibition_index'),

    # /exhibition/1/
    path('<int:exhibition_pk>/', views.exhibition_detail, name='exhibition_detail'),

    # /exhibition/1/update/
    path('<int:exhibition_pk>/update/', views.update_exhibition, name='update_exhibition'),

    # /exhibition/1/delete/
    path('<int:exhibition_pk>/1/delete/', views.delete_exhibition, name='delete_exhibition'),

    # /exhibition/1/expert_reviews/create/
    path('<int:exhibition_pk>/expert_reviews/create/', views.create_expert_review, name='create_expert_review'),

    # /exhibiton/1/expert_reviews/delete/
    path('<int:exhibition_pk>/expert_reviews/<int:expert_reviews_pk>/delete/', views.delete_expert_review, name='delete_expert_review'),

    # /exhibition/1/general_reviews/create/
    path('<int:exhibition_pk>/general_reviews/create/', views.create_general_review, name='create_general_review'),
    
    # /exhibiton/1/general_reviews/delete/
    path('<int:exhibition_pk>/general_reviews/<int:general_reviews_pk>/delete/', views.delete_general_review, name='delete_general_review'),

    # /exhibition/1/like/
    path('<int:exhibition_pk>/like/', views.like_exhibition, name='like_exhibition')


]
