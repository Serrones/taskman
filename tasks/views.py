from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Tarefa

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
