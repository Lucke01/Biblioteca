from django.shortcuts import render
from .models import *
from django.http import Http404
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
    context_object_name = "juego_list"
    queryset = Juego.objects.filter(titulo__icontains = 'age')[:5] #consigue los 5 juegos que el titulo contenga 'age'
    template_name = 'juegos_list.html'

    def get_context_data(self, **kwargs):
        # Llame primero a la implementación base para obtener un contexto.
        context = super(JuegoListView, self).get_context_data(**kwargs)
        # Obtenga el blog del id y agréguelo al contexto.
        context['juego_list'] = Juego.objects.all()
        return context
    
class JuegoDetailView(generic.DetailView):
    model = Juego
    
    def juego_detail_list(request,pk):
        try:
            juego_id = Juego.objects.get(pk=pk)
        except Juego.DoesNotExist:
            raise Http404("el juego que busca no existe")
        
        
        return render(request, 'catalogo/juegos_detalle.html', context={'juego_id':juego_id})
