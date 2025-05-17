from django.shortcuts import render, get_object_or_404, redirect
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def reports_view(request):
    return render(request, 'dashboard/reports.html')

@login_required
def tasks_view(request):
    return render(request, 'dashboard/tasks.html')

@login_required
def role_based_dashboard_view(request):
    user = request.user
    
    if user.is_superuser:
        # Admin general dashboard
        return render(request, 'dashboard/dashboard.html')
    elif user.is_staff:
        # Client admin dashboard
        return render(request, 'dashboard/dashboard.html')
    else:
        # Regular client user dashboard
        return render(request, 'dashboard/dashboard.html')
    
@login_required
def users_view(request):
    # Check user permissions
    if request.user.is_superuser:
        # Superusers can see all users
        users = CustomUser.objects.all()
    elif request.user.is_staff:
        # Staff can see non-superusers
        users = CustomUser.objects.filter(is_superuser=False)
    else:
        # Regular users can only see themselves
        users = CustomUser.objects.filter(id=request.user.id)
        
    return render(request, 'dashboard/users.html', {'users': users})

@login_required
def settings_view(request):
    return render(request, 'dashboard/settings.html')

@login_required
def user_create_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = CustomUserCreationForm()
    return render(request, 'dashboard/user_form.html', {'form': form})

@login_required
def user_edit_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard/users.html')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'dashboard/user_form.html', {'form': form})

@login_required
def user_delete_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('dashboard/users.html')
    return render(request, 'dashboard/user_confirm_delete.html', {'user': user})