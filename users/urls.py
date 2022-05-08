from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('create/',views.create,name='create'),
    path('', views.home, name="home")
]
