from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'audits/index.html')

@login_required
def audit_list(request):
    return render(request, 'audits/audit_list.html')

@login_required
def audit_create(request):
    return render(request, 'audits/audit_create.html')