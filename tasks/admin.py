from django.contrib import admin

from .models import Tarefa, Marcador, TarefaParcial, Usuario


class TarefaAdmin(admin.ModelAdmin):
    fields = ['tarefa', 'usuario', 'descricao']
    list_display = (
                    'tarefa',
                    'usuario',
                    'data_abertura',
                    'tarefa_tempo_total',
                    'marcador',
                    'arquivado')

class MarcadorAdmin(admin.ModelAdmin):
    fields = ['marcador', 'cor']

class TarefaParcialAdmin(admin.ModelAdmin):
    fields = ['tarefa', 'inicio_tarefa', 'final_tarefa']

class UsuarioAdmin(admin.ModelAdmin):
    fields = ['login', 'email']


admin.site.register(Tarefa, TarefaAdmin)
admin.site.register(Marcador, MarcadorAdmin)
admin.site.register(TarefaParcial, TarefaParcialAdmin)
admin.site.register(Usuario, UsuarioAdmin)
