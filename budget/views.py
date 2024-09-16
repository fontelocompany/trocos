from django.shortcuts import render

# Create your views here.
def index():
    output = 'budget home'
    return render('dash/budget.html', output)