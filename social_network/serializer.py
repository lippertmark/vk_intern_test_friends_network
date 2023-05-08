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
    
'''    def create(self, validated_data):
        from_user_data = validated_data.pop('from_user')
        to_user_data = validated_data.pop('to_user')
        from_user, _ = User.objects.get(**from_user_data)
        to_user, _ = User.objects.get(**to_user_data)
        friend_request = FriendRequests.objects.create(from_user=from_user, to_user=to_user, **validated_data)
        return friend_request'''
        
class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'
        