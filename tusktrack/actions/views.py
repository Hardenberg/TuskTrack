from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'actions/actions_dashboard.html')

@login_required
def actions_list(request):
    return render(request, 'actions/actions_list.html')

@login_required
def actions_create(request):
    return render(request, 'actions/actions_create.html')