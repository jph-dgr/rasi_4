from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, HistoriaClinica, Adenda
from .forms import PacienteForm, HistoriaClinicaForm, AdendaForm

def inicio(request):
    return render(request, 'gestionPacientes\templates\inicio.html')

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'gestionPacientes/lista_pacientes.html', {'pacientes': pacientes})

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'gestionPacientes/paciente_form.html', {'form': form})

def lista_historias_clinicas(request):
    historias = HistoriaClinica.objects.all()
    return render(request, 'gestionPacientes/lista_historias_clinicas.html', {'historias': historias})

def crear_historia_clinica(request):
    if request.method == 'POST':
        form = HistoriaClinicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_historias_clinicas')
    else:
        form = HistoriaClinicaForm()
    return render(request, 'gestionPacientes/historia_clinica_form.html', {'form': form})

def buscar_historia_clinica(request):
    id = request.GET.get('id', None)
    historia = None
    if id:
        historia = get_object_or_404(HistoriaClinica, pk=id)
    return render(request, 'gestionPacientes/detalle_historia_clinica.html', {'historia': historia})

def detalle_historia_clinica(request, id):
    historia = get_object_or_404(HistoriaClinica, pk=id)
    return render(request, 'gestionPacientes/detalle_historia_clinica.html', {'historia': historia})

def crear_adenda(request):
    if request.method == 'POST':
        form = AdendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguna_url_después_de_crear')  # Reemplaza con la URL adecuada
    else:
        form = AdendaForm()
    return render(request, 'gestionPacientes/crear_adenda.html', {'form': form})

def ver_adendas(request):
    id_historia_clinica = request.GET.get('id_historia_clinica')
    adendas = Adenda.objects.filter(historia_clinica_id=id_historia_clinica) if id_historia_clinica else []
    return render(request, 'gestionPacientes/ver_adendas.html', {'adendas': adendas})
