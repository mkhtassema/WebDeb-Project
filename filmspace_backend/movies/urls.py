from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet, basename='review')

urlpatterns = [
    path('movies/', views.movie_list, name='movie-list'),
    path('movies/random/', views.random_movie, name='random-movie'),
    path('movies/<int:pk>/', views.movie_detail, name='movie-detail'),
    path('emotion/', views.emotion_recommend, name='emotion-recommend'),
    path('test/', views.personality_test, name='personality-test'),
    path('favorites/', views.favorites, name='favorites'),
    path('', include(router.urls)),
]
