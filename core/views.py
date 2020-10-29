# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.models import Evento

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

    #Código para buscar um determinado evento usando request e response
    #evento = Evento.objects.get(id=1)
    #response = {'evento': evento}
    #return render(request, 'agenda.html', response)

def titulo_evento(request, titulo):
    evento = Evento.objects.get(titulo=titulo)
    return HttpResponse('O local do evento é: {} e na data {}'.format(evento.local, evento.data_evento))
    #return HttpResponse('O local do evento é: {}'.format(evento.local))
