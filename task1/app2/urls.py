from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('page1/', views.app2page1, name = 'app2page1'),
]