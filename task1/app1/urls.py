from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('page1/', views.app1page1, name = "app1page1"),
    path('page2/', views.app1page2, name = "app1page2"),
]