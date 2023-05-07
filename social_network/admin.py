from django.contrib import admin


from social_network.models import User, FriendRequests, Friends

admin.register(User)
admin.register(FriendRequests)
admin.register(Friends)