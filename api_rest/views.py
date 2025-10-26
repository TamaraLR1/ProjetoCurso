from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer

# ----------------------------------------------------------------------
# VIEWS PARA ALUNO 
# ----------------------------------------------------------------------

@api_view(['GET', 'POST'])
def aluno_list_create(request):
    """
    GET: Lista todos os alunos. POST: Cria um novo aluno.
    """
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def aluno_detail_update_delete(request, pk):
    """
    GET: Detalha. PUT: Atualiza. DELETE: Deleta.
    """
    try:
        aluno = Aluno.objects.get(aluno_id=pk)
    except Aluno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------
# VIEWS PARA CURSO
# ----------------------------------------------------------------------

@api_view(['GET', 'POST'])
def curso_list_create(request):
    """
    GET: Lista todos os cursos. POST: Cria um novo curso.
    """
    if request.method == 'GET':
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def curso_detail_update_delete(request, pk):
    """
    GET: Detalha. PUT: Atualiza. DELETE: Deleta.
    """
    try:
        curso = Curso.objects.get(curso_id=pk)
    except Curso.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = CursoSerializer(curso)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------
# VIEWS PARA MATRICULA (COM PATCH INCLUÍDO)
# ----------------------------------------------------------------------

@api_view(['GET', 'POST'])
def matricula_list_create(request):
    """
    GET: Lista todas as matrículas. POST: Cria uma nova matrícula.
    """
    if request.method == 'GET':
        matriculas = Matricula.objects.all()
        serializer = MatriculaSerializer(matriculas, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MatriculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE']) # PATCH ADICIONADO AQUI
def matricula_detail_update_delete(request, pk):
    """
    GET: Detalha. PUT: Atualiza tudo. PATCH: Atualiza parcial. DELETE: Deleta.
    """
    try:
        matricula = Matricula.objects.get(id=pk) 
    except Matricula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = MatriculaSerializer(matricula)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # PUT requer todos os campos
        serializer = MatriculaSerializer(matricula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        # PATCH: partial=True permite enviar apenas os campos que serão alterados
        serializer = MatriculaSerializer(matricula, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        matricula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)