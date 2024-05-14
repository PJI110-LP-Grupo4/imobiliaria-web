from django import forms
from apps.imoveis.models import Imovel


class ImovelForms(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = [
            "usuario",
        ]
        labels = {
            "titulo": "Título:",
            "resumo": "Resumo:",
            "descricao": "Descrição:",
            "oferta_venda": "Para Venda:",
            "oferta_locacao": "Para Locação:",
            "disponivel": "Disponível:",
        }
