from django.contrib import admin
from .models import Proveedores, Productos

admin.site.register(Productos)
admin.site.register(Proveedores)
