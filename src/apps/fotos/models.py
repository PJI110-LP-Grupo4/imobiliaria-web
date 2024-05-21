from django.db import models
from apps.imoveis.models import Imovel


class Foto(models.Model):
    id_imovel = models.ForeignKey(
        to=Imovel,
        on_delete=models.CASCADE,
    )
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    ordem = models.IntegerField
