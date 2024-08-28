from django import forms
from cars.models import Car
import re
    
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
    
    def clean_proprietario(self):
        proprietario = self.cleaned_data.get('proprietario')
        print(proprietario)
        regex = r'\b[A-Za-z ã]{1,150}\b'
        if re.fullmatch(regex, proprietario):
            return proprietario.title()
        else:
            self.add_error('proprietario', 'insira somente letras e espaços')
    