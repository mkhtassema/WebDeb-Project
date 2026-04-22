from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserProfile
from .serializers import UserProfileSerializer, UserSerializer
from movies.models import Favorite


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)
    UserProfile.objects.create(user=user)

    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data,
    }, status=201)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'}, status=401)

    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data,
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
    except Exception:
        pass
    return Response({'message': 'Logged out successfully'})


@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def profile(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'GET':
        serializer = UserProfileSerializer(profile, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_coins(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    amount = request.data.get('amount', 0)
    profile.add_coins(amount)
    return Response({'coins': profile.coins, 'level': profile.level})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def match_users(request, user_id):
    try:
        other_profile = UserProfile.objects.select_related('user').get(unique_user_id=user_id)
        other_user = other_profile.user
    except UserProfile.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    my_favs = set(Favorite.objects.filter(user=request.user).values_list('movie_id', flat=True))
    their_favs = set(Favorite.objects.filter(user=other_user).values_list('movie_id', flat=True))

    if not my_favs and not their_favs:
        score = 0
    else:
        union = my_favs | their_favs
        intersection = my_favs & their_favs
        score = int((len(intersection) / len(union)) * 100) if union else 0

    my_profile, _ = UserProfile.objects.get_or_create(user=request.user)
    their_profile, _ = UserProfile.objects.get_or_create(user=other_user)

    personality_bonus = 10 if my_profile.personality_type == their_profile.personality_type else 0
    final_score = min(100, score + personality_bonus)

    return Response({
        'user': other_user.username,
        'user_id': str(other_profile.unique_user_id),
        'compatibility_score': final_score,
        'shared_movies': len(my_favs & their_favs),
        'my_personality': my_profile.personality_type,
        'their_personality': their_profile.personality_type,
    })
