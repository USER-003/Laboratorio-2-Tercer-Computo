from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'  # Puedes especificar los campos si no quieres todos

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        # Aquí puedes personalizar los campos si es necesario
