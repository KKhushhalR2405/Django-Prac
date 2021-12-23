from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    re_path(r'^page1/', views.page1, name = "page1"),
    re_path(r'^page2/', views.page2, name = "page2"),
]