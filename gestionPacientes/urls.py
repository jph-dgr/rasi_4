from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('crear_paciente/', views.crear_paciente, name='crear_paciente'),
    path('historias_clinicas/', views.lista_historias_clinicas, name='lista_historias_clinicas'),
    path('crear_historia_clinica/', views.crear_historia_clinica, name='crear_historia_clinica'),
    path('buscar_historia_clinica/', views.buscar_historia_clinica, name='buscar_historia_clinica'),
    path('historia_clinica/<int:id>/', views.detalle_historia_clinica, name='detalle_historia_clinica'),
    path('adendas/crear/', views.crear_adenda, name='crear_adenda'),
    path('ver_adendas/', views.ver_adendas, name='ver_adendas'),


]

