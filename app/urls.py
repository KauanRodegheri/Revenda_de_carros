"""https://docs.djangoproject.com/en/5.0/topics/http/urls/"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import *  #view do app cars
from usuarios.views import * #view do app usuarios



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', CarsView.as_view(), name='cars_list'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', HomeViews.as_view(), name='home_views'),
    path('new_car', NewCarView.as_view(), name='new_cars')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)