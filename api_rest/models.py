# api_rest/models.py
from django.db import models
from datetime import datetime
from django.db.models import Max
from django.core.exceptions import ValidationError

# --- Opções para o campo 'situacao' ---
SITUACAO_MATRICULA = (
    ('M', 'Matriculado'),
    ('T', 'Trancado'),
    ('C', 'Concluído'),
    ('E', 'Evadido'),
)

# --- 1. Classe Aluno ---
class Aluno(models.Model):
    aluno_id = models.CharField(primary_key=True, max_length=100, default='')
    aluno_nome = models.CharField(max_length=150, default='')
    aluno_CPF = models.CharField(max_length=14, default='')
    aluno_data_nascimento = models.CharField(default='') # MANTIDO como CharField
    
    # Função __str__ para exibir todos os dados do aluno com a data formatada
    def __str__(self):
        data_formatada = self.aluno_data_nascimento
        try:
            # Tenta converter a string (ex: '2000-12-31') para um objeto datetime
            data_obj = datetime.strptime(self.aluno_data_nascimento, '%Y-%m-%d')
            # Formata o objeto datetime para o formato brasileiro (DD/MM/YYYY)
            data_formatada = data_obj.strftime('%d/%m/%Y')
        except (ValueError, TypeError):
            # Se a string estiver vazia ou com formato incorreto
            data_formatada = self.aluno_data_nascimento if self.aluno_data_nascimento else 'N/A'
        
        return (
            f'ID: {self.aluno_id} | Nome: {self.aluno_nome} | '
            f'CPF: {self.aluno_CPF} | Data Nasc.: {data_formatada}'
        )

# --- 2. Classe Curso ---
class Curso(models.Model):
    curso_id = models.CharField(primary_key=True, max_length=100, default='')
    nome_curso = models.CharField(max_length=100, unique=True, null=False)
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'ID: {self.curso_id} | Código: {self.codigo} - {self.nome_curso}'


# --- 3. Classe Matricula ---
class Matricula(models.Model):
    # Relacionamentos
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    
    # Outros Atributos
    data_matricula = models.DateField(auto_now_add=True) # Este é um DateField
    situacao = models.CharField(
        max_length=1,
        choices=SITUACAO_MATRICULA,
        default='M'
    )

    # Função __str__ (ATUALIZADA com data de matrícula formatada)
    def __str__(self):
        # Gera o número da matrícula a partir do ID sequencial do Django (id + 999)
        numero_matricula = self.id + 999 if self.id else 'N/A'
        
        # Formata o DateField (self.data_matricula) diretamente
        # Nota: O Django garante que self.data_matricula seja um objeto Date se o modelo foi salvo
        data_formatada_matricula = self.data_matricula.strftime('%d/%m/%Y')
        
        return (
            f'Nº {numero_matricula} | Aluno: {self.aluno.aluno_nome} | '
            f'Curso: {self.curso.nome_curso} | Data Matrícula: {data_formatada_matricula}'
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('aluno', 'curso')