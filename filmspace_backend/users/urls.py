from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login, name='login'),
    path('auth/logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/coins/', views.update_coins, name='update-coins'),
    path('match/<uuid:user_id>/', views.match_users, name='match-users'),
]
