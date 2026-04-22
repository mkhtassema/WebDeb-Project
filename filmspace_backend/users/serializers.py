from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    user_id = serializers.UUIDField(source='unique_user_id', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user_id', 'username', 'email', 'coins', 'level', 'personality_type', 'bio', 'favorite_genre', 'taste_dna', 'created_at']
        read_only_fields = ['coins', 'level', 'created_at']
