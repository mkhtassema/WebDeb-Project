from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'polls', views.PollViewSet, basename='poll')

urlpatterns = [
    path('polls/vote/', views.cast_vote, name='cast-vote'),
    path('', include(router.urls)),
]
