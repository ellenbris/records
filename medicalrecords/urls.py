from django.urls import path
from . import views

# user goes to home page, take to views.index
urlpatterns = [
    path('', views.index, name = 'index')
]