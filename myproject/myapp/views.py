from django.shortcuts import render

# Create your views here.
login = request.POST.get('login')
password = request.POST.get('password')

account = authenticate(login=login, password=password)