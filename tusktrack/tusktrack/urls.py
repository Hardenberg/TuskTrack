from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from users.forms import CustomAuthForm

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            authentication_form=CustomAuthForm
        ),
        name='login'
    ),
    
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),

    path('audits', include('audits.urls')),
    path('actions', include('actions.urls'))
]