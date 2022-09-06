from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','categorias','precio']
        labels = {
            'nombre': 'Nombre del producto',
            'categorias': 'Categoria que pertenece el producto',
            
            'precio': 'Precio correspondido',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese nombre del producto',
                    'id': 'nombre'
                }
            ),
              'categorias': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la categoria que pertenece su alimento',
                    'id': 'categorias'
                }
            ),
               '''imagen': forms.(
                attrs = {
                    'class':'form-TextInput',
                    'placeholder':'Ingrese imagen del producto',
                    'id': 'imagen'
                }
            ),'''
               'precio': forms.Textarea(
                attrs = {
                    'class':'form-TextInput',
                    'placeholder':'Ingrese precio del producto',
                    'id': 'precio'
                }
            )
        }
