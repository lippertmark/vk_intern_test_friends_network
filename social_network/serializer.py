from rest_framework import serializers
from social_network.models import User, FriendRequests, Friends


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FriendRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequests
        fields = '__all__'
        
class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'
        