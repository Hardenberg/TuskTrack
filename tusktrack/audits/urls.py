from django.urls import path
from . import views

urlpatterns = [
    path('/', views.dashboard, name='audit-dashboard'),
    path('/list/', views.audit_list, name='audit-list'),
    path('/audit/new/', views.audit_create, name='audit-create'),
]
