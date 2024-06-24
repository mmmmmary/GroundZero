from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, ObraForm, CustomUserCreationForm
from .models import Obra
from cart.models import CartItem
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def home(request):
    return render(request, 'Myapp/home.html')

def nosotros(request):
    return render(request, 'Myapp/Nosotros.html')

def galeria(request):
    obra = Obra.objects.all()
    data = {
        'obra': obra
    }
    return render(request, 'Myapp/galeria.html', data)

def artistas(request):
    return render(request, 'Myapp/artistas.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Enviado"
        else:
            data["form"] = formulario 

    return render(request, 'Myapp/contacto.html', data)

@permission_required('Myapp.add_obra')
def agregar_producto(request):

    data = {
        'form' : ObraForm()
    }

    if request.method == 'POST':
        formulario = ObraForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Obra Agregada"
        else:
            data["form"] = formulario

    return render(request, 'Myapp/obras/agregar.html', data)

@permission_required('Myapp.view_obra')
def listar_productos(request):

    obras = Obra.objects.all()

    data = {

        'obras': obras
    }
    
    return render(request, 'Myapp/obras/listar.html', data)

@permission_required('Myapp.change_obra')
def modificar_productos(request, id):

    obra = get_object_or_404(Obra, id=id)

    data = {

        'form' : ObraForm(instance=obra)
    }

    if request.method == 'POST':
        formulario = ObraForm(data=request.POST, instance=obra, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to=listar_productos)
        else:
            data["form"] = formulario

    return render(request, 'Myapp/obras/modificar.html' )

@permission_required('Myapp.delete_obra')
def eliminar_productos(request, id):
    obra = get_object_or_404(Obra, id=id)
    obra.delete()
    return redirect(to="listar_productos")

def registro(request):

    data ={

        'form' : CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario  = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            
            return redirect(to="home")

        else:
            data['form'] = formulario
    return render(request, 'registration/registro.html', data)

def product_detail(request, product_id):
    obra = get_object_or_404(Obra, id=product_id)
    return render(request, 'myapp/product_detail.html', {'obra': obra})
