from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Poll, PollOption
from .serializers import MovieSerializer, PollSerializer
import random

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def emotion_movies(request):
    text = request.data.get('text', '').lower()

    if not text:
        return Response({"error": "text is required"}, status=400)

    if any(word in text for word in ['sad', 'lost', 'cry', 'alone']):
        movies = Movie.objects.filter(genre__icontains='drama')
    elif any(word in text for word in ['love', 'romantic', 'relationship']):
        movies = Movie.objects.filter(genre__icontains='romance')
    elif any(word in text for word in ['space', 'future', 'ai', 'robot']):
        movies = Movie.objects.filter(genre__icontains='sci')
    else:
        movies = Movie.objects.all()

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def random_movie(request):
    movies = Movie.objects.all()

    if not movies:
        return Response({"error": "No movies found"}, status=404)

    movie = random.choice(movies)
    return Response(MovieSerializer(movie).data)


@api_view(['POST'])
def create_poll(request):
    poll = Poll.objects.create(
        creator=request.user,
        question=request.data.get('question')
    )

    return Response({
        "id": poll.id,
        "question": poll.question
    })

@api_view(['POST'])
def add_option(request):
    poll_id = request.data.get('poll_id')
    movie_id = request.data.get('movie_id')

    try:
        poll = Poll.objects.get(id=poll_id)
        movie = Movie.objects.get(id=movie_id)

        option = PollOption.objects.create(
            poll=poll,
            movie=movie
        )

        return Response({
            "message": "option added",
            "option_id": option.id
        })

    except Poll.DoesNotExist:
        return Response({"error": "Poll not found"}, status=404)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=404)


@api_view(['POST'])
def vote(request):
    option_id = request.data.get('option_id')

    try:
        option = PollOption.objects.get(id=option_id)
        option.votes += 1
        option.save()

        return Response({
            "message": "vote added",
            "votes": option.votes
        })

    except PollOption.DoesNotExist:
        return Response({"error": "Option not found"}, status=404)


@api_view(['GET'])
def poll_detail(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    except Poll.DoesNotExist:
        return Response({"error": "Poll not found"}, status=404)

@api_view(['GET'])
def poll_list(request):
    polls = Poll.objects()
    result = []

    for poll in polls:
        options = PollOption.objects.filter(poll=poll)

        winner = None
        if options:
            winner = max(options, key=lambda x: x.votes).movie.title

        result.append({
            "id": poll.id,
            "question": poll.question,
            "options": [
                {"movie": opt.movie.title, "votes": opt.votes}
                for opt in options
            ],
            "winner": winner
        })

    return Response(result)