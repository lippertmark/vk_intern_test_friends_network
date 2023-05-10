from django.contrib import admin
from django.urls import path, include
from social_network import views

urlpatterns = [
    path('users', view=views.user),
    path('friend_requests/<int:id>', view=views.friend_requests),
    path('friend_requests', view=views.send_request),
    #path('reject_request/', view=views.reject_request),
]
'''
user:
-id
-username
friend_request:
-
friend:
-
'''