from django.shortcuts import render
from social_network.models import User, FriendRequests, Friends
from social_network.serializer import UserSerializer, FriendRequestsSerializer, FriendsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
import typing
import json


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
        if request.data['request_status'] == 'ACCEPTED':
            Friends.objects.create(user1=friend_request.from_user, user2 = friend_request.to_user)
            #Friends.objects.create(user1=friend_request.to_user, user2 = friend_request.from_user)
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
def list_of_requests(request: Request, user_id:int)->Response:
    if request.method == 'GET':
        friends_sended = FriendRequests.objects.filter(from_user=user_id, )
        friends_received = FriendRequests.objects.filter(to_user=user_id)
        friends_sended_serializer = FriendRequestsSerializer(friends_sended, many=True)
        friends_received_serializer = FriendRequestsSerializer(friends_received, many=True)
        response = {
            "sended":friends_sended_serializer.data,
            "received":friends_received_serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def list_of_friends(request: Request, user_id:int) -> Response:
    if request.method == 'GET':
        friends_user1 = Friends.objects.filter(user1=user_id)
        friends_user2 = Friends.objects.filter(user2=user_id)
        friends = friends_user1 | friends_user2
        serializer = FriendsSerializer(friends, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



        
    
    

@api_view(['GET', 'DELETE'])
def friendship_status(request: Request, user_id:int, other_user_id:int):
    try:
        user_1 = User.objects.get(user_id)
        user_2 = User.objects.get(other_user_id)
        friend = Friends.objects.get(user1=user_1, user2=user_2)
    except Friends.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass