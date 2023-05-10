from django.shortcuts import render
from social_network.models import User, FriendRequests, Friends
from social_network.serializer import UserSerializer, FriendRequestsSerializer, FriendsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import typing



@api_view(['GET', 'POST'])
def user(request: Request) -> Response:
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def send_request(request: Request) -> Response:
    if request.method == 'POST':
        serializer = FriendRequestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT'])
def friend_requests(request: Request, id: int) -> Response:
    
    try:
        friend_request = FriendRequests.objects.get(pk=id)
    except FriendRequests.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = FriendRequestsSerializer(friend_request)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        #friend_request.request_status = request.data['request_status']
        #if friend_request.request_status == "PENDING":
        serializer = FriendRequestsSerializer(friend_request, data=request.data, partial=True)
        # TODO добавить функционал добавления в друзья
        if serializer.is_valid():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
            print('smth')
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_of_requests(request: Request, user_id:int):
    pass

@api_view(['GET'])
def list_of_friends(request: Request, user_id:int):
    pass

@api_view(['GET', 'DELETE'])
def friendship_status(request: Request, user_id:int, other_user_id:int):
    try:
        friend = Friends.objects.get(user1=user_id, user2=other_user_id)
    except FriendRequests.DoesNotExist:
        return 