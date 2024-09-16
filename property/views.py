from django.http import HttpResponse
from django.shortcuts import render, redirect   
from .models import Car, Residency
# Create your views here.

def index(request): 
    context = {'output':"property page"}
    return render(request, 'dash/property.html', context)

def SaveCar(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        make = request.POST.get('make')
        model = request.POST.get('model')

        odometer_value = request.POST.get('odometer_value')
        odometer_unit = request.POST.get('odometer_unit')

        new_car = Car(
            year=year,
            make=make,
            model=model,
            odometer_value=odometer_value,
            odometer_unit=odometer_unit
        )
        new_car.save()

        return redirect('index')
    
def EditCar():
    pass

def DelCar():
    pass

def SaveResidency(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        name = request.POST.get('name')
        year_built = request.POST.get('year_built')
        address = request.POST.get('address')

        area_value = request.POST.get('area_value')
        area_unit = request.POST.get('area_unit')

        new_residency = Residency(
            type=type,
            name=name,
            year_built=year_built,
            address=address,
            area_value=area_value,
            area_unit=area_unit,
        )
        new_residency.save()

        return redirect('index')
    
def EditResidency():
    pass

def DelResidency():
    pass