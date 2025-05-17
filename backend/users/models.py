from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.CharField(max_length=50, unique=True, blank=True)
    nome_cliente = models.CharField(max_length=100)
    identificacao = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    responsavel = models.CharField(max_length=100)
    segmento = models.CharField(max_length=50)
    endereco = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id_cliente:
            last = Cliente.objects.order_by('-id').first()
            next_id = 1 if not last else last.id + 1
            self.id_cliente = f"CLI{next_id:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_cliente} ({self.id_cliente})"

class CustomUser(AbstractUser):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True, related_name="usuarios")
    tipo = models.CharField(max_length=20, choices=[("admin", "Admin"), ("tecnico", "Técnico"), ("usuario", "Usuário")])
    telefone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_inicio = models.DateField(auto_now_add=True)
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.tipo})"