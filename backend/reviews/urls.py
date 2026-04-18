from django.urls import path
from .views import create_review, review_list, update_review, delete_review

urlpatterns = [
    path('reviews/', review_list),
    path('reviews/create/', create_review),
    path('reviews/<int:pk>/update/', update_review),
    path('reviews/<nt:pk>/delete/', delete_review),
]