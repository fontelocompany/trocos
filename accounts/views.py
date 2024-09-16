from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Account, Institutions

# Create your views here.
def index(request): 
    context = {'output' : "home dashboard"}
    return render(request, 'dash/index.html', context)

def AddAccount(request):
    if request.method == 'POST':
        family = request.POST.get('family'),
        name = request.POST.get('name')
        account_type = request.POST.get('account_type')

        balance = request.POST.get('balance')
        currency = request.POST.get('currency')

        institution = request.POST.get('institution')
        is_active = request.POST.get('active')

        new_account = Account(
            family=family,
            name=name,
            account_type=account_type,
            balance=balance,
            currency=currency,
            institution=institution,
            is_active=is_active
        )

        new_account.save()

        return redirect('index')
    
def EditAccount():
    pass

def DelAccount():
    pass