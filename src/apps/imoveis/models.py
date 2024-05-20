from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False, unique=True)


ESTADOS = [
    ("SP", "São Paulo"),
    ("RJ", "Rio de Janeiro"),
    ("DF", "Distrito Federal"),
    ("MG", "Minas Gerais"),
]


class Cidade(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, choices=ESTADOS, default="")


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
    categoria = models.ForeignKey(
        to=Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="categoria",
    )

class Anunciar(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False)
    telefone = models.CharField(max_length=25, null=False, blank=False)
    email = models.CharField(max_length=25, null=False, blank=False)
    cep = models.CharField(max_length=25, null=False, blank=False)
    endereco = models.CharField(max_length=25, null=False, blank=False)
    complemento = models.CharField(max_length=25, null=False, blank=False)
    bairro = models.CharField(max_length=25, null=False, blank=False)
    cidade = models.CharField(max_length=25, null=False, blank=False)
    estado = models.CharField(max_length=25, null=False, blank=False)
    finalidade = models.CharField(max_length=25, null=False, blank=False)
    tipo = models.CharField(max_length=25, null=False, blank=False)
    valor_venda = models.FloatField(max_length=25, null=False, blank=False)
    valor_locacao = models.FloatField(max_length=25, null=False, blank=False)
    qtd_quartos = models.IntegerField(null=False, blank=False)
    qtd_suites = models.IntegerField(null=False, blank=False)
    qtd_banheiros = models.IntegerField(null=False, blank=False)
    qtd_vagas = models.IntegerField(null=False, blank=False)
    obs = models.TextField(null=False, blank=False)
    imagem_imovel = models.ImageField(null=False, blank=False)


class recuperar_senha(models.Model):
    email = models.CharField(max_length=25, null=False, blank=False)


class atualiza_dados(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False)
    email = models.CharField(max_length=25, null=False, blank=False)
    celular = models.CharField(max_length=12, null=False, blank=False)
    data_nasc = models.DateField(max_length=25, null=False, blank=False)
    cpf_cnpj = models.CharField(max_length=25, null=False, blank=False)
    cep = models.CharField(max_length=12, null=False, blank=False)
    endereco = models.CharField(max_length=25, null=False, blank=False)
    bairro = models.CharField(max_length=25, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    email = models.CharField(max_length=25, null=False, blank=False)
    senha = models.CharField(max_length=10, null=False, blank=False)
    confirme_senha = models.CharField(max_length=10, null=False, blank=False)

class detalhe_imoveis(models.Model):
    valor_venda = models.CharField(max_length=25, null=False, blank=False)
    valor_aluguel = models.CharField(max_length=25, null=False, blank=False)
    condominio = models.CharField(max_length=25, null=False, blank=False)
    tipo_imovel = models.CharField(max_length=25, null=False, blank=False)
    qtd_quartos = models.CharField(max_length=25, null=False, blank=False)
    qtd_banheiros = models.CharField(max_length=25, null=False, blank=False)
    qtd_vagas = models.CharField(max_length=25, null=False, blank=False)
    metragem = models.CharField(max_length=25, null=False, blank=False)
    descrição = models.TextField(null=False, blank=False)

class meus_imoveis(models.Model):
    FINALIDADE_CHOICES = [
        (1, 'Comprar'),
        (2, 'Alugar')
    ]

    TIPOIMOVEL_CHOICES = [

        (1, 'Casa'),
        (2, 'Apartamento'),
        (3, 'Kit-net'),
        (4, 'Quarto')
    ]

    BAIRRO_CHOICES = [

        (1, 'Cecap'),
        (2, 'Ubirama'),
        (3, 'Itamaraty'),
        (4, 'Principe'),
        (4, 'Cruzeiro'),
        (4, 'Caju'),
        (4, 'Antonieta')
    ]

    finalidade_imovel = models.IntegerField(choices=FINALIDADE_CHOICES, null=False, blank=False) 
    tipo_imovel = models.IntegerField(choices=TIPOIMOVEL_CHOICES, null=False, blank=False) 
    bairro = models.IntegerField(choices=BAIRRO_CHOICES, null=False, blank=False) 
    imagem_imovel = models.ImageField(null=False, blank=False)

class login(models.Model):
    email = models.CharField(max_length=25, null=False, blank=False)
    senha = models.CharField(max_length=25, null=False, blank=False)


class contato(models.Model):
    nome = models.CharField(max_length=25, null=False, blank=False)
    email = models.CharField(max_length=25, null=False, blank=False)
    celular = models.CharField(max_length=12, null=False, blank=False)
    observacao = models.TextField(max_length=25, null=False, blank=False)   

