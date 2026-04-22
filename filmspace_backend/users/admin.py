from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'unique_user_id', 'personality_type', 'coins', 'level')
    search_fields = ('user__username', 'unique_user_id')
    list_filter = ('personality_type', 'level')

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'
