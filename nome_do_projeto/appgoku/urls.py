from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('start-strength/', views.start_strength_training, name='start_strength'),
    path('start-cardio/', views.start_cardio, name='start_cardio'),
    path('track-progress/', views.track_progress, name='track_progress'),
]