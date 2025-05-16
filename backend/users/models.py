from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    tipo = models.CharField(max_length=20, choices=[("admin", "Admin"),  ('cliente', "Cliente")])