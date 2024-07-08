from django.db import models
from django.contrib.auth.models import User


CATEGORIAS = [
    ("Casa", "Casa"),
    ("Apartamento", "Apartamento"),
    ("Chácara", "Chácara"),
    ("Pensão", "Pensão"),
    ("Salão de Festas", "Salão de Festas"),
]

CIDADES = [
    ("3506003", "Bauru"),
    ("3506003", "Botucatu"),
    ("3526803", "Lençóis Paulista"),
]


class Imovel(models.Model):
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    titulo = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    resumo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(max_length=300, null=False, blank=False)
    oferta_venda = models.BooleanField(default=False)
    oferta_locacao = models.BooleanField(default=False)
    disponivel = models.BooleanField(default=False)
    foto_capa = models.ImageField(upload_to="fotos/%Y/%m/%d/", null=False)
    link_contato = models.CharField(max_length=100)
    informacoes_contato = models.TextField(max_length=300)
    cidade = models.CharField(max_length=100, choices=CIDADES, default="")
    endereco = models.CharField(max_length=100)
    coordenas_geograficas = models.CharField(max_length=100, null=True)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default="")
    valor_locacao = models.FloatField(null=True)
    valor_venda = models.FloatField(null=True)
    quantidade_suites = models.IntegerField(null=True)
    quantidade_quartos = models.IntegerField(null=True)
    quantidade_banheiros = models.IntegerField(null=True)
    quantidade_vagas_garagem = models.IntegerField(null=True)
    metragem_imovel = models.IntegerField(null=True)
