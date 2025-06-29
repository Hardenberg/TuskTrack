from django.urls import path
from . import views

urlpatterns = [
    path('/', views.dashboard, name='actions-dashboard'),
    path('/list/', views.actions_list, name='actions-list'),
    path('/actions/new/', views.actions_create, name='actions-create'),
]
