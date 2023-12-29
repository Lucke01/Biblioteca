from django.urls import path
from catalogo import views
from django.views.generic import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url = '/catalogo/',permanent = True))
]