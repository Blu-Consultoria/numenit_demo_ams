from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.http import JsonResponse
import json

# Create your views here.

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