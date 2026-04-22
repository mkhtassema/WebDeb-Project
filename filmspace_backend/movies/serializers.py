from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Review, Favorite


class MovieSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.favorited_by.filter(user=request.user).exists()
        return False

    def get_review_count(self, obj):
        return obj.reviews.count()


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'username', 'movie', 'text', 'rating', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']


class FavoriteSerializer(serializers.ModelSerializer):
    movie_details = MovieSerializer(source='movie', read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'movie', 'movie_details', 'created_at']
        read_only_fields = ['created_at']
