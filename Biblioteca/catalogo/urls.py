from django.urls import path,re_path
from catalogo import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('juegos/',views.JuegoListView.as_view(), name = "juegos"),
    path('juego/<int:pk>', views.JuegoDetailView.as_view(), name ='juego-detalle'),
    #re_path(r'^juego/(?P<pk>\d+)$', views.JuegoDetailView.as_view(), name='juego-detail'),
    path('marca/',views.MarcaListView.as_view(),name = 'Marca'),
    path('marca/<int:pk>', views.MarcaDetailView.as_view(), name = 'Marca-detalle')
]   