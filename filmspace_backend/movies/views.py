import random
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from .models import Movie, Review, Favorite
from .serializers import MovieSerializer, ReviewSerializer, FavoriteSerializer
from users.models import UserProfile


MOOD_KEYWORD_MAP = {
    'happy': ['comedy', 'fun', 'joy', 'laugh', 'uplifting', 'cheerful'],
    'sad': ['drama', 'emotional', 'grief', 'tears', 'loss', 'melancholy'],
    'excited': ['action', 'adventure', 'thrilling', 'explosive', 'epic'],
    'anxious': ['thriller', 'suspense', 'mystery', 'tense', 'psychological'],
    'relaxed': ['animation', 'family', 'light', 'calm', 'peaceful'],
    'angry': ['action', 'revenge', 'fight', 'intense', 'power'],
    'inspired': ['documentary', 'biography', 'motivation', 'success', 'journey'],
    'lonely': ['romance', 'connection', 'friendship', 'warmth', 'bond'],
    'romantic': ['romance', 'love', 'passion', 'date', 'chemistry'],
    'adventurous': ['adventure', 'explore', 'quest', 'discovery', 'fantasy'],
}

EMOTION_KEYWORD_MAP = {
    'sad': 'sad', 'unhappy': 'sad', 'depressed': 'sad', 'cry': 'sad', 'down': 'sad',
    'happy': 'happy', 'joy': 'happy', 'great': 'happy', 'wonderful': 'happy', 'good': 'happy',
    'excited': 'excited', 'thrilled': 'excited', 'energetic': 'excited', 'pumped': 'excited',
    'anxious': 'anxious', 'nervous': 'anxious', 'worried': 'anxious', 'stressed': 'anxious',
    'relax': 'relaxed', 'tired': 'relaxed', 'calm': 'relaxed', 'peaceful': 'relaxed',
    'angry': 'angry', 'mad': 'angry', 'furious': 'angry', 'frustrated': 'angry',
    'inspired': 'inspired', 'motivated': 'inspired', 'creative': 'inspired',
    'lonely': 'lonely', 'alone': 'lonely', 'isolated': 'lonely',
    'love': 'romantic', 'romantic': 'romantic', 'crush': 'romantic',
    'adventure': 'adventurous', 'bored': 'adventurous', 'explore': 'adventurous',
}

PERSONALITY_MAP = {
    'a': 'explorer', 'b': 'romantic', 'c': 'thinker',
    'd': 'thrill-seeker', 'e': 'empath', 'f': 'humorist',
}


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    movies = Movie.objects.all()
    mood = request.query_params.get('mood')
    genre = request.query_params.get('genre')
    search = request.query_params.get('search')

    if mood:
        movies = movies.filter(mood=mood)
    if genre:
        movies = movies.filter(genre=genre)
    if search:
        movies = movies.filter(Q(title__icontains=search) | Q(description__icontains=search))

    serializer = MovieSerializer(movies, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=404)
    serializer = MovieSerializer(movie, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def random_movie(request):
    movies = Movie.objects.all()
    if not movies.exists():
        return Response({'error': 'No movies available'}, status=404)
    movie = random.choice(list(movies))
    serializer = MovieSerializer(movie, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def emotion_recommend(request):
    text = request.data.get('text', '').lower()
    detected_mood = 'happy'
    for keyword, mood in EMOTION_KEYWORD_MAP.items():
        if keyword in text:
            detected_mood = mood
            break

    movies = Movie.objects.filter(mood=detected_mood)
    if not movies.exists():
        movies = Movie.objects.all()
    movie = random.choice(list(movies))
    serializer = MovieSerializer(movie, context={'request': request})
    return Response({'detected_mood': detected_mood, 'movie': serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def personality_test(request):
    answers = request.data.get('answers', {})
    personality_scores = {p: 0 for p in PERSONALITY_MAP.values()}

    for q, answer in answers.items():
        personality = PERSONALITY_MAP.get(answer.lower())
        if personality:
            personality_scores[personality] += 1

    personality_type = max(personality_scores, key=personality_scores.get)

    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    profile.personality_type = personality_type
    profile.taste_dna = personality_scores
    profile.save()

    genre_map = {
        'explorer': 'adventure', 'romantic': 'romance', 'thinker': 'sci-fi',
        'thrill-seeker': 'thriller', 'empath': 'drama', 'humorist': 'comedy',
    }
    recommended_genre = genre_map.get(personality_type, 'drama')
    movies = Movie.objects.filter(genre=recommended_genre)[:5]
    serializer = MovieSerializer(movies, many=True, context={'request': request})
    return Response({
        'personality_type': personality_type,
        'taste_dna': personality_scores,
        'recommended_movies': serializer.data,
    })


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Review.objects.all()
        movie_id = self.request.query_params.get('movie')
        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        profile.add_coins(5)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def favorites(request):
    if request.method == 'GET':
        favs = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favs, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        movie_id = request.data.get('movie')
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=404)
        fav, created = Favorite.objects.get_or_create(user=request.user, movie=movie)
        if created:
            return Response({'status': 'added'}, status=201)
        return Response({'status': 'already exists'})

    elif request.method == 'DELETE':
        movie_id = request.data.get('movie')
        Favorite.objects.filter(user=request.user, movie_id=movie_id).delete()
        return Response({'status': 'removed'})
