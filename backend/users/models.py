from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    level = models.CharField(max_length=50, default="Beginner")

class TasteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    drama = models.IntegerField(default=0)
    scifi = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')