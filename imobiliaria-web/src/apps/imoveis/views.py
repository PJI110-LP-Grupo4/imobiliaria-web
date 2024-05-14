from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.imoveis.models import Imovel
from apps.imoveis.forms import ImovelForms


def index(request):
    imoveis = Imovel.objects.order_by("disponivel", "titulo")
    return render(request, "imoveis/index.html", {"cards": imoveis})


def imovel(request, imovel_id):
    imovel = Imovel.objects.get(id=imovel_id)
    return render(request, "imoveis/imovel.html", {"imovel": imovel})


def meus_imoveis(request):
    imoveis = Imovel.objects.order_by("disponivel", "titulo")
    return render(request, "imoveis/meus_imoveis.html", {"cards": imoveis})


def novo_imovel(request):
    form = ImovelForms
    if request.method == "GET":
        return render(request, "imoveis/novo_imovel.html", {"form": form})

    form = ImovelForms(request.POST, request.FILES)
    if form.is_valid():
        imovel = form.save()
        messages.success(request, "Imóvel cadastrado com sucesso.")
        return redirect("imovel", imovel_id=imovel.id)


def editar_imovel(request, imovel_id):
    form = ImovelForms
    imovel = Imovel.objects.get(id=imovel_id)
    if request.method == "GET":
        form = ImovelForms(instance=imovel)
        return render(
            request,
            "imoveis/editar_imovel.html",
            {"form": form, "imovel_id": imovel_id},
        )

    form = ImovelForms(request.POST, request.FILES, instance=imovel)
    if form.is_valid():
        form.save()
        messages.success(request, "Imóvel editado com sucesso.")
        return redirect("imovel", imovel_id=imovel_id)
