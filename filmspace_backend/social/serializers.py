from rest_framework import serializers
from .models import Poll, Vote
from movies.serializers import MovieSerializer


class VoteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Vote
        fields = ['id', 'user', 'username', 'poll', 'selected_movie', 'created_at']
        read_only_fields = ['user', 'created_at']


class PollSerializer(serializers.ModelSerializer):
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    movie_options_details = MovieSerializer(source='movie_options', many=True, read_only=True)
    votes = VoteSerializer(many=True, read_only=True)
    vote_count = serializers.IntegerField(source='votes.count', read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'question', 'created_by', 'created_by_username', 'movie_options', 'movie_options_details', 'votes', 'vote_count', 'created_at', 'is_active']
        read_only_fields = ['created_by', 'created_at']
