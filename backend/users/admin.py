from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cliente

# Para o CustomUser, herdamos de UserAdmin para aproveitar funcionalidades do Django
class CustomUserAdmin(UserAdmin):
    # Campos extras para exibir e editar
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('tipo', 'data_inicio', 'data_fim', 'telefone', 'cpf')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações adicionais', {'fields': ('tipo', 'telefone', 'cpf')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'tipo', 'is_staff']
    search_fields = ['username', 'email', 'cpf']

# Registrar o CustomUser com o admin customizado
admin.site.register(CustomUser, CustomUserAdmin)

# Registrar Cliente no admin, permitindo edição simples
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome_cliente', 'id_cliente', 'telefone', 'email', 'responsavel', 'segmento']
    search_fields = ['nome_cliente', 'id_cliente', 'email']