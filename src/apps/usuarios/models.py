from django.db import models

# Create your models here.
class Usuario(models.Model):
    STATUS_CHOICES = [
        (1, 'Comprador'),
        (2, 'Vendedor')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=10, null=False, blank=False)
    confirme_senha = models.CharField(max_length=10, null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=False)