from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.http import JsonResponse
import json


# Rotas de Login

@ensure_csrf_cookie
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({"success": True, "message": "Login bem-sucedido"})
            response["Access-Control-Allow-Credentials"] = "true"
            return response
        else:
            return JsonResponse({"success": False, "error": "Credenciais inválidas"}, status=401)
    return JsonResponse({"error": "Método não permitido"}, status=405)

@csrf_exempt
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        response = JsonResponse({"success": True, "message": "Logout successful"})
        response.delete_cookie('sessionid', path='/', samesite='None', secure=True)
        response["Access-Control-Allow-Credentials"] = "true"
        return response
    return JsonResponse({"success": True, "message": "Already logged out"})

@ensure_csrf_cookie
@csrf_exempt
def session_status(request):
    if request.user.is_authenticated:
        user = request.user
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.username,
        }
        response = JsonResponse({"authenticated": True, "user": user_data})
        response["Access-Control-Allow-Credentials"] = "true"
        return response
    else:
        return JsonResponse({"authenticated": False, "user": None})

@csrf_exempt
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
    
    response = JsonResponse({
        "success": True,
        "permissions": permissions_data
    })
    response["Access-Control-Allow-Credentials"] = "true"
    return response

@ensure_csrf_cookie
def csrf_token(request):
    return JsonResponse({"csrfToken": "set"})
