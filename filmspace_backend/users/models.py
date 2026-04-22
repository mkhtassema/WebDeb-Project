import uuid
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    PERSONALITY_CHOICES = [
        ('explorer', 'The Explorer'),
        ('romantic', 'The Romantic'),
        ('thinker', 'The Thinker'),
        ('thrill-seeker', 'The Thrill-Seeker'),
        ('empath', 'The Empath'),
        ('humorist', 'The Humorist'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    unique_user_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    coins = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    personality_type = models.CharField(max_length=50, choices=PERSONALITY_CHOICES, blank=True)
    bio = models.TextField(blank=True)
    favorite_genre = models.CharField(max_length=50, blank=True)
    taste_dna = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def add_coins(self, amount):
        self.coins += amount
        self.level = 1 + self.coins // 50
        self.save()
