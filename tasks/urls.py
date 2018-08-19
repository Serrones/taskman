from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tarefa_id>/', views.detail, name='detail'),
    path('create', views.create_task, name='create')
]
