from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import  CarModelForm
from django.views.generic import ListView, TemplateView
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
class HomeViews(TemplateView):
    template_name = 'home.html'


#FUNÇÃO DE NOVOS CARROS
def new_car_views(request):
    if request.method == "POST":
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render (
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )
