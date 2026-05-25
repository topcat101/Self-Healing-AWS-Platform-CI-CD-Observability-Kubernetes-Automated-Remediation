from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({
        "message": "Self-Healing AWS Platform API",
        "status": "running"
    })


def health(request):
    return JsonResponse({
        "status": "healthy"
    })


def version(request):
    return JsonResponse({
        "version": "1.0.0",
        "environment": "local"
    })