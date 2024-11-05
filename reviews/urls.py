from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createReview, name='review_create'),
    path('update/<str:pk>/', views.updateReview, name='review_update'),
    path('delete/<str:pk>/', views.deleteReview, name='review_delete'),
]
