from django.urls import path
from . import views

urlpatterns = [
    # URLs para Aluno
    path('alunos/', views.aluno_list_create, name='aluno-list-create'),
    path('alunos/<str:pk>/', views.aluno_detail_update_delete, name='aluno-detail-update-delete'),
    
    # URLs para Curso
    path('cursos/', views.curso_list_create, name='curso-list-create'),
    path('cursos/<str:pk>/', views.curso_detail_update_delete, name='curso-detail-update-delete'),
    
    # URLs para Matrícula
    # A PK da matrícula é um inteiro (ID), mas usamos 'str:pk' para simplificar o URLconf
    path('matriculas/', views.matricula_list_create, name='matricula-list-create'),
    path('matriculas/<int:pk>/', views.matricula_detail_update_delete, name='matricula-detail-update-delete'),
]