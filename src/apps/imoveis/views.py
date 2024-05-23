from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.imoveis.models import Imovel
from apps.imoveis.forms import ImovelForms
from helpers.error_helper import tratar_errors


def index(request):
    imoveis = Imovel.objects.order_by("disponivel", "titulo")
    return render(request, "imoveis/index.html", {"cards": imoveis})


def imovel(request, imovel_id):
    imovel = get_object_or_404(Imovel, pk=imovel_id)
    return render(request, "imoveis/imovel.html", {"imovel": imovel})


def meus_imoveis(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Você precisa estar logado visualizar seus imóveis")
        return redirect("entrar")

    imoveis = Imovel.objects.filter(usuario=request.user).order_by(
        "disponivel",
        "titulo",
    )
    return render(request, "imoveis/meus_imoveis.html", {"cards": imoveis})


def novo_imovel(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Você precisa estar logado cadastrar imóveis")
        return redirect("entrar")

    form = ImovelForms

    if request.method == "POST":
        form = ImovelForms(request.POST, request.FILES)
        if form.is_valid():
            imovel = form.save(commit=False)
            imovel.usuario = request.user
            imovel.save()
            messages.success(request, "Imóvel cadastrado com sucesso.")
            return redirect("imovel", imovel_id=imovel.id)
        else:
            tratar_errors(form, request)
    return render(request, "imoveis/novo_imovel.html", {"form": form})


def editar_imovel(request, imovel_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Você precisa estar logado editar seus imóveis")
        return redirect("entrar")

    imovel = Imovel.objects.filter(id=imovel_id).first()
    if not (imovel):
        messages.warning(request, "O imóvel que você quer editar não existe mais")
        return redirect("index")

    form = ImovelForms(instance=imovel)

    if request.method == "POST":
        form = ImovelForms(request.POST, request.FILES, instance=imovel)
        if form.is_valid():
            form.save()
            messages.success(request, "Imóvel editado com sucesso.")
            return redirect("imovel", imovel_id=imovel_id)
        else:
            tratar_errors(form, request)

    return render(
        request,
        "imoveis/editar_imovel.html",
        {
            "form": form,
            "imovel_id": imovel_id,
        },
    )
