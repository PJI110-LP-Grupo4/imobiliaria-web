from django.shortcuts import render
from apps.imoveis.models import Imovel


def index(request):
    imoveis = Imovel.objects.order_by("titulo")
    return render(request, "shared/bem-vindo.html", {"cards": imoveis})
