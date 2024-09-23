from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Institutions

# Create your views here.
def index(request): 
    context = {'user' : request.user}
    return render(request, 'dash/index.html', context)

def AccountsHome(request):  
    accounts = Account.objects.filter(owner=request.user)
    return render(request, 'dash/accounts.html', {'accounts': accounts})

def AddAccount(request):
    if request.method == 'POST':
        family = 1
        name = request.POST.get('name')
        account_type = request.POST.get('account_type')

        balance = request.POST.get('balance')
        currency = request.POST.get('currency')

        institution = request.POST.get('institution')
        is_active = True

        new_account = Account(
            family=request.user.family,
            owner=request.user,
            name=name,
            account_type=account_type,
            balance=balance,
            currency=currency,
            institution=institution,
            is_active=is_active
        )

        new_account.save()

        return redirect('accounts-home')
    
def DetailAccount(request, id):
    item = get_object_or_404(Account, id=id)
    return item

def EditAccount(request, id):
    pass

def DelAccount(request, id):
    item = get_object_or_404(Account, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('dash-home')