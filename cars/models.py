from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome



class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    proprietario = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.model