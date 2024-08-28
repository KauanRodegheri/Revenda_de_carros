"""https://docs.djangoproject.com/en/5.0/topics/http/urls/"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import *  #view do app cars
from usuarios.views import * #view do app usuarios



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeViews.as_view(), name='home_views'),
    #CRUD
    path('cars/', CarsView.as_view(), name='cars_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name= 'car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='delete_car'),
    path('new_car', NewCarView.as_view(), name='new_cars'),
    #LOGIN
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)