from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import login
from .models import Objetivo, NivelAtividade, Dieta 

from nutri.models import Objetivo

def index(request):
    return render(request,'paginas/home.html')


def UserLogin(request):
    if request.method == 'POST':
        nome = request.POST.get('username')
        senha = request.POST.get('password')
        check = auth.authenticate(request, username=nome, password=senha)
        if check is not None:
            login(request, check)
            return redirect('home')
        else:
            messages.info(request, 'Login invalido.')
            return render(request,'paginas/login.html')
    return render(request,'paginas/login.html')

def Tela_tmb(request):
    objetivo = Objetivo.objects.all()
    return render(request, 'paginas/tela_tmb.html', {'objetivo': objetivo})