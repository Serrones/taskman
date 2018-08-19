from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Tarefa, Usuario, Marcador

def index(request):
    latest_question_list = Tarefa.objects.order_by('data_abertura')[:5]
    template = loader.get_template('tasks/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'tasks/index.html', context)


def detail(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)
    return render(request, 'tasks/detail.html', {'tarefa': tarefa})


def create_task(request):
    if request.method == 'POST':
        user = Usuario.objects.filter(login=request.user).first()
        marcador = get_object_or_404(Marcador, pk=request.POST['marcador'])
        tarefa = Tarefa(
                    tarefa=request.POST['tarefa'],
                    descricao=request.POST['descricao'],
                    usuario=user,
                    marcador=marcador)
        tarefa.save()
        return render(request, 'tasks/detail.html', {'tarefa': tarefa})
    else:
        tarefa = Tarefa(),
        marcadores = Marcador.objects.all()
        return render(request, 'tasks/create.html', {'tarefa': tarefa, 'marcadores': marcadores})
