from django.http import HttpResponse
from django.shortcuts import render

# Pages with info
def index(request):
    return render(request, 'dash/settings.html', {'user' : request.user})

def inflation(request):
    output = "inflation page"
    return render(request, 'dash/inflation.html', output)

def fx(request):
    output = "fx page"
    return render(request, 'dash/fx.html', output)