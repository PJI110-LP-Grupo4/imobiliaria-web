from django.shortcuts import render, redirect
from apps.usuarios.forms import EntrarForms  # , CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def entrar(request):
    form = EntrarForms()
    if request.method == "GET":
        return render(request, "usuarios/entrar.html", {"form": form})

    form = EntrarForms(request.POST)
    if form.is_valid():
        user_email = form["email_usuario"].value()
        senha = form["senha"].value()

        user = User.objects.filter(email=user_email).first()
        if user:
            usuario = auth.authenticate(request, username=user.username, password=senha)
            if usuario:
                auth.login(request, usuario)
                messages.success(request, "Login efetuado com sucesso")
                return redirect("index")

        messages.warning(request, "Erro ao entrar no sistema")
        return redirect("entrar")
 