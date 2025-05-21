from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm, LoginForm

@csrf_protect
def log(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'authreg/login.html', {'form': form})
    form = LoginForm()
    return render(request, 'authreg/login.html', {'form': form})

def reg(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        return render(request, 'authreg/registration.html', {'form': form})
    form = RegisterForm()
    return render(request, 'authreg/registration.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')