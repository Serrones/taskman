from django.db import models

class Tarefa(models.Model):
    def __str__(self):
        return self.tarefa
    # colunas
    tarefa = models.CharField(max_length=50)
    descricao = models.TextField()
    data_abertura = models.DateField(auto_now_add=True)
    data_encerramento = models.DateField(null=True, blank=True)
    tarefa_tempo_total =models.TimeField(null=True, blank=True)
    arquivado = models.BooleanField(default=False)
    # ForeignKey
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    marcador = models.ForeignKey('Marcador', on_delete=models.CASCADE)

class Marcador(models.Model):
    def __str__(self):
        return self.marcador
    # colunas
    marcador = models.CharField(max_length=50)
    cor = models.CharField(max_length=7)

class TarefaParcial(models.Model):
    def __str__(self):
        return self.inicio_tarefa
    # colunas
    inicio_tarefa = models.DateField(auto_now_add=True)
    final_tarefa = models.DateField(null=True, blank=True)
    # relacionamentos m:n com Tarefa
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)


class Usuario(models.Model):
    def __str__(self):
        return self.login
    # colunas
    login = models.CharField(max_length=25)
    senha = models.CharField(max_length=32)
    email = models.CharField(max_length=50)
