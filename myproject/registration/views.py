from django.shortcuts import render

def index(request):
    return render(request, 'registration/index.html')

def welcome(request):
    return render(request, 'registration/welcome.html')

def registration(request):
    return render(request, 'registration/registration.html')