from django.contrib import admin
from .models import * #importamos todos los models
# Register your models here.


admin.site.register(Genero)
admin.site.register(Juego)
admin.site.register(Marca)
admin.site.register(Instancia_juego)

