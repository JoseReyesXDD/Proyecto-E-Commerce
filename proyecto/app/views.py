from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .models import Producto
from .models import Ubicacion

# Create your views here.
def add_usuario(request):
    User.objects.create_user('rodrigo123', 'prieto@gmail.com', 'megustanloswawis123')
    return HttpResponse('Datos guardados')

def update_email(response):
    u = User.objects.get(username= 'rodrigo123')
    u.email = 'prietokun123@gmail.com'
    u.save()
    return HttpResponse('Se actualizo el correo')

def authenticate_user(response):
    n = response.POST.get("username")
    passw = response.POST.get("password")
    user = authenticate(response, username=n, password=passw)
    if user is not None:
        login(response, user)
        return HttpResponse('Usuario autenticado')
    else:
        return HttpResponse('No se encontro')
    
def logout_view(request):
    logout(request)
    return HttpResponse('Usuario deslogueado')

def index(request):
    return render(request, 'index.html')

def productos(request):
    return render(request, 'productos.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        categoria = request.POST.get('categoria')
        nuevo_producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria
        )
    return render(request, 'agregar_productos.html')

def borrar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('lista_productos') 

def modificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.categoria = request.POST.get('categoria')
        producto.save()
        return redirect('lista_productos') 
    return render(request, 'modificar_productos.html', {'producto': producto})

def mapa(request):
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')  
    if lat is not None and lon is not None:
        Ubicacion.objects.create(lat=lat, lon=lon)
        return render(request, 'mapa.html', {'lat': lat, 'lon': lon})
    else:
        return render(request, 'mapa.html', {'error': 'Nulo'})

# def guardar_ubicacion(request):
#     if request.method == 'POST':
#          lat = request.POST.get('lat')
#          lon = request.POST.get('lon')  
#          nueva_ubicacion = Ubicacion.objects.create(
#             lat = float(lat),
#             lon = float(lon),
#         )
#     return render(request, 'mapa.html')
