# Generated by Django 5.0.6 on 2024-08-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='proprietario',
            field=models.CharField(max_length=150, null=True),
        ),
    ]