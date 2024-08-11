"""https://docs.djangoproject.com/en/5.0/topics/http/urls/"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import *
from usuarios.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', view_cars, name='cars_list'),
    path('register/', register_view, name='register'),
    path('', HomeViews.as_view(), name='home_views'),
    path('new_car', new_car_form, name='new_cars')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)