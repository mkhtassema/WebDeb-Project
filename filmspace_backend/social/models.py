from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Poll(models.Model):
    question = models.CharField(max_length=300)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='polls')
    movie_options = models.ManyToManyField(Movie, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='votes')
    selected_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'poll')

    def __str__(self):
        return f'{self.user.username} voted on {self.poll.question}'
