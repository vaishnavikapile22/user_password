from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import LoginHistory, RegisterHistory
from django.contrib.auth import logout
from django.shortcuts import redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            LoginHistory.objects.create(user=user)
            return redirect('dashboard')  # Redirect to dashboard or any valid page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'error': 'Username already exists'})
            else:
                user = User.objects.create_user(username=username, password=password)
                LoginHistory.objects.create(user=user)
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard or any valid page
        else:
            return render(request, 'register.html', {'error': 'Please provide username and password'})
    else:
        return render(request, 'register.html')

def history_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        login_history = LoginHistory.objects.all()
        register_history = RegisterHistory.objects.all()
        return render(request, 'history.html', {'login_history': login_history, 'register_history': register_history})
    else:
        return render(request, 'access_denied.html')
    


def logout_view(request):
    # Perform logout operations here
    logout(request)
    # Redirect to a specific page after logout
    return redirect('login') 

def dashboard_view(request):
    # Your logic for the dashboard view goes here
    return render(request, 'dashboard.html')    
