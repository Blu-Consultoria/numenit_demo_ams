from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def reports_view(request):
    return render(request, 'dashboard/reports.html')

@login_required
def users_view(request):
    return render(request, 'dashboard/users.html')

@login_required
def settings_view(request):
    return render(request, 'dashboard/settings.html')
