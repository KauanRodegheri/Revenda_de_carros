from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm
# Create your views here.

#FUNÇÃO DE VER CARROS
def view_cars(request):
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    else:
        cars = Car.objects.all().order_by('brand__nome')

    return render(
        request,
        'cars.html',      #PRECISA SER O ARQUIVO HTML
        {'cars': cars}    #PRECISA SER UM DICIONARIO
        )

#FUNÇÃO DA HOME
def home_views(request):
    return render(
        request,
        'home.html',
    )

#FUNÇÃO DE NOVOS CARROS
def new_car_views(request):
    new_car_form = CarForm()
    return render (
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )
