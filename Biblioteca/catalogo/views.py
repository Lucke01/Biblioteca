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
    
#importamos generic para poder tener disponible la vista generica en lista 
from django.views import generic

class JuegoListView(generic.ListView):
    model = Juego
    template_name = 'juegos_list.html'
    paginate_by = 5

    
class JuegoDetailView(generic.DetailView):
    model = Juego


class MarcaListView(generic.ListView):
    model = Marca
    template_name = 'base_generic.html'
class GeneroListView(generic.ListView):
    model = Genero
    

class MarcaDetailView(generic.DetailView):
    model = Marca