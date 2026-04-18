from django.urls import path
from .views import (
    movie_list,
    emotion_movies,
    create_poll,
    add_option,
    vote,
    poll_detail
)

urlpatterns = [
    path('movies/', movie_list),
    path('emotion/', emotion_movies),

    path('poll/create/', create_poll),
    path('poll/add-option/', add_option),
    path('poll/vote/', vote),
    path('poll/<int:poll_id>/', poll_detail),
]