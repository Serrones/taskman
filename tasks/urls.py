from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/home', views.home, name='home'),
    path('tasks/create', views.create_task, name='create_task'),
    path('<int:tarefa_id>/', views.task_detail, name='task_detail'),
    path('users/create', views.create_user, name='create_user'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/login', views.login_user, name='login_user'),
    path('users/logout', views.logout_user, name='logout_user'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
]
