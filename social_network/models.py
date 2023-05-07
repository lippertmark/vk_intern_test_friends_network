from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.username


class FriendRequests(models.Model):
    REQUEST_TYPE = [
        ("PENDING", "PENDING"),
        ("ACCEPTED", "ACCEPTED"),
        ("REJECTED", "REJECTED"),
    ]
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_request_from_user")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friend_request_to_user")
    request_status = models.CharField(max_length=255, choices=REQUEST_TYPE)
    created_at = models.DateTimeField(auto_now=True)

class Friends(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends_from_user")
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="friends_to_user")
    created_at = models.DateTimeField(auto_now=True)