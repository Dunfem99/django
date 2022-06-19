from django.urls import URLPattern, path

from . import views

URLPattern = [
    path('', views.home, name='home')
]