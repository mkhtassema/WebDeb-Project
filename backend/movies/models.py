from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    mood_tags = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Poll(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question

class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.movie.title} - {self.votes}"
