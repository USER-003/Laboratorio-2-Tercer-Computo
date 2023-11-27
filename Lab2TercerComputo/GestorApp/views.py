from django.shortcuts import render, redirect
from .formularios.registerform import NewUserForm
from .formularios.loginform import LoginForm
from django.http import HttpResponseRedirect
from .models import Productos, Proveedores
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'  # Puedes especificar los campos si no quieres todos

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        # Aquí puedes personalizar los campos si es necesario



def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        return HttpResponseRedirect("/")
    else:
        formulario = NewUserForm()
        return render(request, "Reg_user.html", {"form": formulario})

def iniciar_sesion(request):
    user = None
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def index(request):
    
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    es_admin = request.user.is_staff
    if es_estudiante or es_admin:
        return render(request, 'index.html', {'user': request.user, 'es_estudiante': es_estudiante,'es_admin':es_admin})

@login_required(login_url='login')
def agregar_proveedor(request):
    es_admin = request.user.is_staff
    if request.method == 'POST':
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']

        proveedor = Proveedores(nombre=nombre, telefono=telefono)
        proveedor.save()
        return render(request, 'agregar_prove.html',{'user': request.user,'es_admin':es_admin})
    else:
        return render(request, 'agregar_prove.html',{'user': request.user,'es_admin':es_admin} )

def listado_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'listado_proveedores.html', {'proveedores': proveedores})


@login_required(login_url='login')
def agregar_producto(request):
    es_admin = request.user.is_staff
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'agregar_producto.html', {'form': form, 'user': request.user,'es_admin':es_admin} )
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form, 'user': request.user,'es_admin':es_admin} )

def listado_productos(request):
    productos = Productos.objects.all()
    return render(request, 'listado_producto.html', {'productos': productos})