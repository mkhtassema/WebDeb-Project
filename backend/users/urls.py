from django.urls import path
from .views import match

urlpatterns = [
    path('mathc/<int:user_id>/', match)
]