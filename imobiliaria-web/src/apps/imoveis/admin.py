from django.contrib import admin
from apps.imoveis.models import Imovel


class ListarImoveis(admin.ModelAdmin):
    list_display = ("id", "titulo", "oferta_venda", "oferta_locacao", "disponivel")
    list_display_links = ("id", "titulo")
    search_fields = ("titulo", "oferta_venda", "oferta_locacao", "disponivel")
    list_editable = ("disponivel",)
    list_per_page = 20


admin.site.register(Imovel, ListarImoveis)
