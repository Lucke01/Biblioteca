from django.urls import path,re_path
from catalogo import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('juegos/',views.JuegoListView.as_view(), name = "juegos"),
    #path('juegos/<int:pk>', views.JuegoDetailView.as_view(), name ='juegos_detalle'),
    re_path(r'^juegos/(?P<pk>\d+)$', views.JuegoDetailView.as_view(), name='juegos-detail'), #tengo un error aca pero weno
]   