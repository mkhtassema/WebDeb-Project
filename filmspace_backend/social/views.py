from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Poll, Vote
from .serializers import PollSerializer, VoteSerializer


class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]
    queryset = Poll.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cast_vote(request):
    poll_id = request.data.get('poll')
    movie_id = request.data.get('selected_movie')

    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        return Response({'error': 'Poll not found'}, status=404)

    vote, created = Vote.objects.update_or_create(
        user=request.user,
        poll=poll,
        defaults={'selected_movie_id': movie_id}
    )
    serializer = VoteSerializer(vote)
    return Response(serializer.data, status=201 if created else 200)
