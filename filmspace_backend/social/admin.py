from django.contrib import admin
from .models import Poll, Vote


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_by', 'vote_count', 'is_active', 'created_at')
    search_fields = ('question', 'created_by__username')
    list_filter = ('is_active',)

    def vote_count(self, obj):
        return obj.votes.count()
    vote_count.short_description = 'Votes'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'poll', 'selected_movie', 'created_at')
    search_fields = ('user__username', 'poll__question')
