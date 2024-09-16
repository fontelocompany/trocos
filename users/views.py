from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request): 
    output = "login page"
    return render(request, 'login.html', output)

def onboarding(request):
    output = 'onboarding'
    return render(request, 'onboarding/index.html', output)

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
