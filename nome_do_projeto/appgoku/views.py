from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'appgoku/home.html')

def start_strength_training(request):
    # Simulated strength training start
    messages.success(request, "🏋️ Treino de Força iniciado! Vamos aumentar seu poder de luta!")
    return redirect('home')

def start_cardio(request):
    # Simulated cardio training start
    messages.success(request, "🏃 Corrida iniciada! Transformando-se em Super Saiyajin!")
    return redirect('home')

def track_progress(request):
    # Simulated progress tracking
    progress_data = {
        'strength_level': 75,
        'cardio_endurance': 65,
        'power_level': 'Super Saiyajin Nível 1'
    }
    return JsonResponse(progress_data)