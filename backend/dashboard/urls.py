from django.urls import path
from . import views

urlpatterns = [
    path('', views.role_based_dashboard_view, name='dashboard'),
    path('reports/', views.reports_view, name='reports'),
    path('users/', views.users_view, name='users'),
    path('users/novo/', views.user_create_view, name='user_create'),
    path('users/<int:pk>/editar/', views.user_edit_view, name='user_edit'),
    path('users/<int:pk>/excluir/', views.user_delete_view, name='user_delete'),
    path('settings/', views.settings_view, name='settings'),
]