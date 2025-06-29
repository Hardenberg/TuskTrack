from django.db import models
from django.conf import settings

class Audit(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('planned', 'Geplant'),
        ('running', 'Laufend'),
        ('done', 'Abgeschlossen')
    ])

    def __str__(self):
        return self.title