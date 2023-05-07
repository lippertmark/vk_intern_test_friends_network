from django.shortcuts import render
from social_network.models import User, FriendRequests, Friends
from social_network.serializer import UserSerializer, FriendRequestsSerializer, FriendsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status



@api_view(['GET'])
def user(request: Request) -> Response:
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
