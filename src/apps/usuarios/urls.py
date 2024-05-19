from django.urls import path

from apps.usuarios.views import entrar #, cadastro, logout

urlpatterns = [
    path("entrar", entrar, name="entrar"),
#    path("cadastro", cadastro, name="cadastro"),
#    path("logout", logout, name="logout"),
]
