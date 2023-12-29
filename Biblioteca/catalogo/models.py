from django.db import models
from django.urls import reverse

# Create your models here.
class Genero(models.Model):
    #modelo del genero del item
    nombre = models.CharField(max_length = 200, help_text = "Ingrese el nombre del genero (p.ej: Accion, Supervivencia,etc)")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p.ej: sitio de administracion)
        """
        return self.name
    

class Juego(models.Model):
    titulo = models.CharField(max_length = 200)
     # ForeignKey, ya que un juego tiene una sola marca, pero la misma marca puede haber desarrollado muchos juegos.
    marca = models.ForeignKey('Marca',on_delete = models.SET_NULL , null = True) 

    sumario = models.TextField(max_length = 1000, help_text = 'Ingrese una descripcion del juego')

    genero = models.ManyToManyField(Genero, help_text='Seleccione un genero para este juego')
    
    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):

        return reverse('detalle del juego',args =[str(self.id)])
    
class Marca (models.Model):
    nombre_empresa = models.CharField(max_length = 200)
    desarrolladores = models.CharField(max_length = 200)
    año_de_salida = models.DateField(null = True, blank = True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de una empresa.
        """
        return reverse('marca-detalle', args=[str(self.id)])
    
    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.nombre_empresa, self.desarrolladores)