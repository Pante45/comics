
import re

from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'correo', 'rut', 'cantidad']

        labels = {
            'nombre': 'Nombre completo',
            'correo': 'Correo electrónico',
            'rut': 'RUT',
            'cantidad': 'Cantidad de ejemplares',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre completo'
            }),
            'correo': forms.EmailInput(attrs={
                'placeholder': 'ejemplo@correo.cl'
            }),
            'rut': forms.TextInput(attrs={
                'placeholder': '12.345.678-5'
            }),
            'cantidad': forms.NumberInput(attrs={
                'min': 1,
                'max': 3
            }),
        }

    def clean_rut(self):
        rut = self.cleaned_data['rut'].strip().upper()

        if not re.fullmatch(r'\d{1,2}\.\d{3}\.\d{3}-[\dK]', rut):
            raise forms.ValidationError(
                'Ingresa el RUT con formato válido. Ejemplo: 12.345.678-5'
            )

        numero, digito = rut.replace('.', '').split('-')

        suma = 0
        multiplicador = 2

        for cifra in reversed(numero):
            suma += int(cifra) * multiplicador
            multiplicador = 2 if multiplicador == 7 else multiplicador + 1

        resultado = 11 - (suma % 11)

        if resultado == 11:
            verificador = '0'
        elif resultado == 10:
            verificador = 'K'
        else:
            verificador = str(resultado)

        if digito != verificador:
            raise forms.ValidationError(
                'El dígito verificador del RUT es incorrecto.'
            )

        return rut

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']

        if cantidad < 1 or cantidad > 3:
            raise forms.ValidationError(
                'Solo puedes reservar entre 1 y 3 ejemplares.'
            )

        return cantidad
