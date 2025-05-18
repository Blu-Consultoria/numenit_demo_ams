from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.http import JsonResponse
import json


# Rotas de Login

# Realiza login no backend e retorna mensagem para o next.js
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": True, "message": "Login bem-sucedido"})
        else:
            return JsonResponse({"success": False, "error": "Credenciais inválidas"}, status=401)
    return JsonResponse({"error": "Método não permitido"}, status=405)

# Realiza logout no backend e retorna mensagem para o next.js
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return JsonResponse({"success": True, "message": "Logout bem-sucedido"})

# Verifica a existência da sessão e retorna seus dados
def session_status(request):
    if request.user.is_authenticated:
        user = request.user
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.username,
        }
        return JsonResponse({"authenticated": True, "user": user_data})
    else:
        return JsonResponse({"authenticated": False, "user": None})
    
# Autenticação de permissão
def check_permission(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            "success": False,
            "error": "Usuário não está autenticado"
        }, status=401)
    
    permissions_data = {
        "is_authenticated": True,
        "is_staff": user.is_staff,
        "is_superuser": user.is_superuser,
        "permissions": list(user.get_all_permissions())
    }
    
    return JsonResponse({
        "success": True,
        "permissions": permissions_data
    })


# ---------------------------------------------------------------------------------

# Rotas de dashboard
