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

# Realiza logout no backend e retorna mensagem para o next.js
@csrf_exempt
def logout_view(request):
    logout(request)
    if request.headers.get('content-type') == 'application/json':
        return JsonResponse({"success": True, "message": "Logout realizado com sucesso", "redirect": "/"})
    else:
        return redirect('/')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'users/login.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {
        'user': request.user
    })
    