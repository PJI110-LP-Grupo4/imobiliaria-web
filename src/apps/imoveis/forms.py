from django import forms
from apps.imoveis.models import Imovel


class ImovelForms(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = [
            "usuario",
        ]
        labels = {
            "titulo": "Título",
            "resumo": "Resumo",
            "descricao": "Descrição",
            "oferta_venda": "Venda",
            "oferta_locacao": "Locação",
            "disponivel": "Disponível",
            "foto_capa": "Foto de Capa",
        }
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Título de Exibição",
                }
            ),
            "resumo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Resumo Breve",
                }
            ),
            "descricao": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descrição Completa",
                }
            ),
            "oferta_venda": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "oferta_locacao": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "disponivel": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "foto_capa": forms.FileInput(
                attrs={
                    "class": "form-control",
                },
            ),
        }
