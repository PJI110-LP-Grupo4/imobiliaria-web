from django.db import models

# Create your models here.
class Usuario(models.Model):
    STATUS_CHOICES = [
        (1,'Feminino'),
        (2,'Masculino'),
        (3,'Não Informar')
        
    ]
    nome = models.CharField(max_length=100, null=False)
    sobrenome = models.CharField(max_length=100, null=False)
    data = models.DateField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=False)