from django.contrib import admin
from .models import Projeto, Recurso, Chamado

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'id_projeto', 'cliente', 'data_inicio', 'data_fim']
    search_fields = ['nome', 'id_projeto']

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'disponivel', 'projeto']
    list_filter = ['disponivel', 'tipo']

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'prioridade', 'status', 'cliente', 'projeto', 'atribuido_para']
    list_filter = ['prioridade', 'status']
    search_fields = ['titulo', 'cliente__nome_cliente', 'projeto__nome']
