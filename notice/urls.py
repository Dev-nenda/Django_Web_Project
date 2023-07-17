from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
     # notice/create/
    path('create/', views.create_notice, name='create_notice'),

    
    # /notice/
    path('', views.notice_index, name='notice_index'),

    # /notice/1/
    path('<int:notice_pk>/', views.notice_detail, name='notice_detail'),

    # /notice/1/update
    path('<int:notice_pk>/update', views.update_notice, name='update_notice'),

    # /notice/1/delete
    path('<int:notice_pk>/delete/', views.delete_notice, name = 'delete_notice'),

]
