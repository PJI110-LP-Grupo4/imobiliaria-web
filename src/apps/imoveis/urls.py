from django.urls import path
from apps.imoveis.views import index

urlpatterns = [
    path("", index, name="index"),
]
