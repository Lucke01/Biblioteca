from django.shortcuts import render
from .models import *
# Create your views here.


#view index
def index(request): 
    #generar contadores de algunos objetos principales
    num_juego = Juego.objects.all().count() #contar la cantidad de juegos que tenemos
    num_intancia = Instancia_juego.objects.all().count() #contar las intancias de juegos que tenemos
    #cantidad de juegos (status = 'a')
    num_intancia_disponible = Instancia_juego.objects.filter(status__exact = 'a').count()
    num_marca = Marca.objects.count()
    
    #renderizamos el template
    
    return render(request, 'index.html',context={
        'num_juego':num_juego,
        'num_intancia':num_intancia,
        'num_instancia_disponible':num_intancia_disponible,
        'num_marca':num_marca,
    })