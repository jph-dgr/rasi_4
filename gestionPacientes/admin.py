from django.contrib import admin
from .models import Paciente, HistoriaClinica

admin.site.register(Paciente)
admin.site.register(HistoriaClinica)
