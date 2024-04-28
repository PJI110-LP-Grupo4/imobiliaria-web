from django.db import models


class Imovel(models.Model):
    titulo = models.CharField(max_length=25, null=False, blank=False)
    resumo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=250, null=False, blank=False)
    oferta_venda = models.BooleanField(default=False)
    oferta_locacao = models.BooleanField(default=False)
