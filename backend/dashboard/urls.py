from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('reports/', views.reports_view, name='reports'),
    path('users/', views.users_view, name='users'),
    path('settings/', views.settings_view, name='settings'),
]