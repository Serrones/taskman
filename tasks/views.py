from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template import loader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Tarefa, Marcador


def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tasks:home'))

        else:
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/tasks')


def index(request):
    return render(request, 'tasks/index.html')

@login_required
def home(request):
    latest_tasks = Tarefa.objects.order_by('-data_abertura')[:5]
    context = {
        'latest_tasks': latest_tasks,
    }
    return render(request, 'tasks/home.html', context)

@login_required
def task_detail(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    return render(request, 'tasks/detail.html', {'tarefa': tarefa})

@login_required
def user_detail(request, user_id):
    usuario = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'usuario': usuario})

@login_required
def create_task(request):
    if request.method == 'POST':
        user = User.objects.filter(username=request.user).first()
        marcador = get_object_or_404(Marcador, pk=request.POST['marcador'])
        tarefa = Tarefa(
                    tarefa=request.POST['tarefa'],
                    descricao=request.POST['descricao'],
                    usuario=user,
                    marcador=marcador)
        tarefa.save()
        return HttpResponseRedirect(reverse('tasks:task_detail', args=(tarefa.id,)))
    else:
        tarefa = Tarefa()
        marcadores = Marcador.objects.all()
        return render(request, 'tasks/create.html', {'tarefa': tarefa, 'marcadores': marcadores})


def create_user(request):
    if request.method == 'POST':
        if request.POST['email'] == request.POST['conf_email'] and request.POST['password'] == request.POST['conf_password']:
            usuario = User(username=request.POST['username'],
                            email=request.POST['email'])
            usuario.set_password(request.POST['password'])
            usuario.save()
            return HttpResponseRedirect(reverse('tasks:login_user'))
        else:
            usuario = User()
            return render(request, 'users/create.html', {'usuario': usuario})
    else:
        usuario = User()
        return render(request, 'users/create.html', {'usuario': usuario})
