from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TasteProfile

@api_view(['POST'])
def test_result(request):
    user = request.user
    data = request.data

    profile, created = TasteProfile.objects.get_or_create(user=user)

    profile.drama += int(data.get("drama", 0))
    profile.scifi += int(data.get("scifi", 0))
    profile.romance += int(data.get("romance", 0))

    profile.save()

    return Response({
        "message": "Test saved",
        "drama": profile.drama,
        "scifi": profile.scifi,
        "romance": profile.romance
    })


@api_view(['GET'])
def match(request, user_id):
    try:
        user1_profile = TasteProfile.objects.get(user=request.user)
        user2_profile = TasteProfile.objects.get(user_id=user_id)

        def similarity(a, b):
            if a == 0 and b == 0:
                return 100
            return max(0, 100 - abs(a - b))

        drama_match = similarity(user1_profile.drama, user2_profile.drama)
        scifi_match = similarity(user1_profile.scifi, user2_profile.scifi)
        romance_match = similarity(user1_profile.romance, user2_profile.romance)

        final_match = int((drama_match + scifi_match + romance_match) / 3)

        return Response({
            "user_id": user_id,
            "match_percent": final_match,
            "details": {
                "drama": drama_match,
                "scifi": scifi_match,
                "romance": romance_match
            }
        })

    except TasteProfile.DoesNotExist:
        return Response({"error": "TasteProfile not found"}, status=404)