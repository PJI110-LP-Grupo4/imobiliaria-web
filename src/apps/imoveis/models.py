from django.db import models
from django.contrib.auth.models import User


class Imovel(models.Model):
    titulo = models.CharField(max_length=25, null=False, blank=False)
    resumo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=300, null=False, blank=False)
    oferta_venda = models.BooleanField(default=False)
    oferta_locacao = models.BooleanField(default=False)
    disponivel = models.BooleanField(default=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )
