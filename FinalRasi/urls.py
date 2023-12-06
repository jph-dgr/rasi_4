from django.contrib import admin
from django.urls import path, include
from gestionPacientes import views as gestionPacientes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestionPacientes/', include('gestionPacientes.urls')),
    path('', gestionPacientes_views.inicio, name='inicio'),  # URL raíz
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]
