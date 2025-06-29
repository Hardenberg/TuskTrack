# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('auditor', 'Auditor'),
        ('manager', 'Manager'),
        ('viewer', 'Viewer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
