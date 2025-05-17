from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Cliente

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'tipo', 'cliente', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('tipo', 'cliente', 'telefone', 'cpf', 'data_inicio', 'data_fim')}),
    )

admin.site.register(Cliente)