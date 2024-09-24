from django.contrib import admin
from cars.models import Car, Brand, CarInventory

class BrandAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')

class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('cars_count', 'cars_value', 'created_at')
    search_fields = ('created_at',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(CarInventory, CarInventoryAdmin)


