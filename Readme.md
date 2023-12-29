1) CREO PROYECTO Y APP
1.1) Python -m django startproject + nombre del proyecto

1.2)cd nombre del proyecto

1.3) creamos app : Python manage.py startapp + Nombre de la app

1.4) ponemos la app en Biblioteca/settings.py

1.5) ponemos la app en Biblioteca/urls.py // path('nombreapp/', include(('nombreapp.urls', 'Nombreapp'),namespace='nombreapp'))

1.6) creamos en la app: urls.py y ponemos: from django.urls import path
from catalogo import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url = '/catalogo/',permanent = True))
]

2) Creamos los modelos y los campos 
2.1) migramos con: Python manage.py makemigrations
2.2) luego python manage.py migrate

///////////////////////////////////  COMMIT -- PROYECTO/APP/ MODELS////////////////////////////

3) Registro de los modelos en catalogo/admin.py

///////////////////// commit -- correccion de errores////////////

4) Creacion de un SUPERUSER
