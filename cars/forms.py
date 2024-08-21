from django import forms
from cars.models import Car

    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor minimo é de R$20.000')
        else:
            return value
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year > 2025 or factory_year < 1940:
            self.add_error('factory_year', 'Adicione um ano valido')
        else:
            return int(factory_year)
    
    