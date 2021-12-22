from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('contactme', views.contact, name="contact"),
]