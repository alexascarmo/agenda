# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Evento


def titulo_evento(request, titulo):
    evento = Evento.objects.get(titulo=titulo)
    return HttpResponse('O local do evento é: {} e na data {}'.format(evento.local, evento.data_evento))
    #return HttpResponse('O local do evento é: {}'.format(evento.local))

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos' :evento}
    return render(request, 'agenda.html', dados)

    #Código para buscar um determinado evento usando request e response
    #evento = Evento.objects.get(id=1)
    #response = {'evento': evento}
    #return render(request, 'agenda.html', response)