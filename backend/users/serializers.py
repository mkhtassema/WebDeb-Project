from rest_framework import serializers
from .models import UserProfile, TasteProfile, Follow

class UserProfileSerializer(serializers.ModelSerialize):
    class Meta:
        model = UserProfile
        fields = '__all__'

class TasteProfileSerializer(serializers.ModelSerialize):
    class Meta:
        model = TasteProfile
        fields = '__all__'

class FollowSerializer(serializers.ModelSerialize):
    class Meta:
        model = Follow
        fields = '__all__'