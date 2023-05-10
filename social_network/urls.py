from django.contrib import admin
from django.urls import path, include
from social_network import views

urlpatterns = [
    path('users', view=views.user),
    path('friend_requests/<int:id>', view=views.friend_requests),
    path('friend_requests', view=views.send_request),
    path('users/<int:user_id>/friend_requests', view=views.list_of_requests),
    path('users/<int:user_id>/friends', view=views.list_of_friends),
    path('users/<int:user_id>/friends/<int:other_user_id>', view=views.friendship_status),  # тут два GET and DELETE
]
