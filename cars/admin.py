from django.contrib import admin
from cars.models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
    


