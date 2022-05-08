from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "post"
urlpatterns = [
    path('post/', views.post, name='post'),
    path('createPost/', views.createPage, name='create')
]
