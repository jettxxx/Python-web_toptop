from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "post"
urlpatterns = [
    path('post/', views.post, name='post'),
    path('createPost/', views.createPage, name='create'),
    path('user_details/<usr_id>', views.user_details, name='user_details'),
    path('createPost/', views.createPage, name='user_details'),
    path('getPost/', views.getPost, name='getPost'),
    path('deletePost/<str:pk>/', views.deletePost, name='deletePost'),
    path('updatePost/<str:pk>/', views.updatePost, name='updatePost'),
    path('editPost/<str:pk>/', views.editPost, name='editPost')
]
