from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): 
    output = "home dashboard"
    return render(request, 'dash/index.html', output)