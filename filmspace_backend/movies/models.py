from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'),
        ('horror', 'Horror'), ('romance', 'Romance'), ('sci-fi', 'Sci-Fi'),
        ('thriller', 'Thriller'), ('animation', 'Animation'), ('documentary', 'Documentary'),
        ('fantasy', 'Fantasy'),
    ]
    MOOD_CHOICES = [
        ('happy', 'Happy'), ('sad', 'Sad'), ('excited', 'Excited'),
        ('anxious', 'Anxious'), ('relaxed', 'Relaxed'), ('angry', 'Angry'),
        ('inspired', 'Inspired'), ('lonely', 'Lonely'), ('romantic', 'Romantic'),
        ('adventurous', 'Adventurous'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    rating = models.FloatField(default=0.0)
    year = models.IntegerField(default=2020)
    director = models.CharField(max_length=100, blank=True)
    poster_url = models.URLField(blank=True, default='')
    watch_url = models.URLField(blank=True, default='')
    keywords = models.TextField(blank=True, help_text='Comma separated keywords')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
