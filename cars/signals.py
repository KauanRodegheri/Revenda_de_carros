from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInventory
from gemini_api.client import get_car_ai_bio


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']
    #para adiocionar no BD
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()



@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()

@receiver(pre_save, sender=Car)
def car_bio(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = get_car_ai_bio(
            model = instance.model,
            brand = instance.brand,
            year = instance.model_year
        )
    







