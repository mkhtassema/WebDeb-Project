from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer

@api_view(['POST'])
def create_review(request):
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_review(request, pk):
    try:
        review = Review.objects.get(id=pk)

        if review.user != request.user:
            return Response({"error": "not allowed"}, status=403)

        serializer = ReviewSerializer(review, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    except Review.DoesNotExist:
        return Response({"error": "not found"}, status=404)

@api_view(['DELETE'])
def delete_review(request, pk):
    try:
        review = Review.objects.get(id=pk)

        if review.user != request.user:
            return Response({"error": "not allowed"}, status=403)

        review.delete()
        return Response({"message": "deleted"})

    except Review.DoesNotExist:
        return Response({"error": "not found"}, status=404)