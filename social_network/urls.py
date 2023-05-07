from django.contrib import admin
from django.urls import path, include
from social_network import views

urlpatterns = [
    path('user/', view=views.user),
    
    
]
