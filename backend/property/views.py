from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Residency
# Create your views here.

def index(request, id):
    items = Car.objects.filter(owner=request.user)
    context = {'output' : "property page"}
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

        return redirect('property-home')
    
def EditCar(request, id):
    item = get_object_or_404(Car, id=id)
    pass

def DelCar(request, id):
    item = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('property-home')

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

        return redirect('property-home')
    
def EditResidency():
    pass

def DelResidency(request, id):
    item = get_object_or_404(Residency, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('property-home')