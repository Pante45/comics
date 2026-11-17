from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('comic/<int:comic_id>/', views.detalle_comic, name='detalle_comic'),
    path('comic/<int:comic_id>/reservar/', views.reservar_comic, name='reservar_comic'),
]