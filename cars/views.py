from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import  CarModelForm
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView,UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.

#FUNÇÃO DE VER CARROS e Classe based views
#def cars_view(request):
#    cars = Car.objects.all().order_by('model')     ##USANDO FUNÇÃO PARA REPRESENTAR NOSSA VIEW DE CARROS
#    search = request.GET.get('search')
#    if search:
#        cars = cars.filter(brand__nome__icontains=search).order_by('brand__nome')
#    return render(request, 'cars.html', {'cars': cars})
class CarsView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('brand__nome')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search).order_by('brand__nome')
           
        return cars


#FUNÇÃO DA HOME
class HomeViews(TemplateView):
    template_name = 'home.html'

#FUNÇÃO DE NOVOS CARROS
#Criando Carros
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.id})

#Mostrando os detalhes de cada carro
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


#deletando o carro escolhido atraves do ID ou PK
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = reverse_lazy('cars_list')

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.id})










        