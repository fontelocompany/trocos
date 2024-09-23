from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Families


def login_view(request): 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, 
                            username=email, 
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('dash-home')
        else:
            messages.error(request, "Invalid email or password")
    elif request.user.is_authenticated:
        return redirect('dash-home')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# onboarding, first time init app
def onboarding(request):
    context = {'page':'onboading start'}
    return render(request, 'onboarding/index.html', context)

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'onboarding/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'onboarding/signup.html')

        family = Families(
            name=email + ' family',
        )
        
        family.save()
        user = User.objects.create_user(email=email, password=password1, family=family)
        login(request, user)
        return redirect('dash')  # Replace 'home' with your home page URL name

    return render(request, 'onboarding/signup.html')

# Settings Pages
def SettingsHome(request):
    output = 'settings home'
    return render(request, 'settings/index.html', output)

def UserSettings(request):
    output = 'users settings'
    return render(request, 'settings/user.html', output)

def FamilySettings(request):
    output = 'family settings'
    return render(request, 'settings/family.html', output)

def UtilSettings(request):
    output = 'util settings'
    return render(request, 'settings/util.html', output)
