from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(): 
    output = "property page"
    return render('dash/property.html', output)