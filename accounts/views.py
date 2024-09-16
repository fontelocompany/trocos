from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): 
    context = {'output' : "home dashboard"}
    return render(request, 'dash/index.html', context)