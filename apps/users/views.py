from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

def user_profile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        return render(request, 'users/user_profile.html', {'profile': profile})
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the name of your login URL pattern