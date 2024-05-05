from django.urls import path
from apps.imoveis.views import index, imovel, meus_imoveis, editar_imovel, novo_imovel

urlpatterns = [
    path("", index, name="index"),
    path("imovel/<int:imovel_id>", imovel, name="imovel"),
    path("meus-imoveis", meus_imoveis, name="meus_imoveis"),
    path("novo-imovel", novo_imovel, name="novo_imovel"),
    path("editar-imovel/<int:imovel_id>", editar_imovel, name="editar_imovel"),
]
