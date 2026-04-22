from django.contrib import admin
from .models import Movie, Review, Favorite


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'mood', 'rating', 'year', 'director')
    search_fields = ('title', 'director', 'keywords')
    list_filter = ('genre', 'mood', 'year')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'rating', 'created_at')
    search_fields = ('user__username', 'movie__title')
    list_filter = ('rating',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'created_at')
    search_fields = ('user__username', 'movie__title')
