from django.db import models


# Create your models here.

class Projeto(models.Model):
    id_projeto = models.CharField(max_length=50, unique=True, blank=True)
    nome = models.CharField(max_length=100, verbose_name="Nome do Projeto")
    descricao = models.TextField(blank=True, verbose_name="Descrição do Projeto")
    horas_alocacao_gerente = models.PositiveIntegerField(default=0, verbose_name="Horas de Alocação do Gerente")
    data_inicio = models.DateField(verbose_name="Data início contrato")
    data_fim = models.DateField(null=True, blank=True, verbose_name="Data fim contrato")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='projetos')
    
    def save(self, *args, **kwargs):
        if not self.id_projeto:
            # Generate a unique ID if not provided
            last_project = Projeto.objects.order_by('-id').first()
            next_id = 1 if not last_project else last_project.id + 1
            self.id_projeto = f"PRJ{next_id:04d}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nome} ({self.id_projeto})"

class Recurso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    tipo = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)
    projeto = models.ForeignKey(Projeto, on_delete=models.SET_NULL, null=True, blank=True, related_name='recursos')
    
    def __str__(self):
        return self.nome

class Chamado(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('critica', 'Crítica'),
    ]
    
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em Andamento'),
        ('pendente', 'Pendente'),
        ('resolvido', 'Resolvido'),
        ('fechado', 'Fechado'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='aberto')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='chamados')
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='chamados')
    atribuido_para = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='chamados_atribuidos')
    
    def __str__(self):
        return self.titulo
    
