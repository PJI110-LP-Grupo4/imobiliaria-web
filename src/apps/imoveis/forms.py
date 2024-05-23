from django import forms
from apps.imoveis.models import Imovel


class ImovelForms(forms.ModelForm):
    class Meta:
        model = Imovel
        exclude = [
            "usuario",
        ]
        labels = {
            "foto_capa": "Foto de Capa",
            "titulo": "Título",
            "resumo": "Resumo",
            "descricao": "Descrição",
            "oferta_venda": "Oferta de Venda",
            "oferta_locacao": "Oferta de Locação",
            "disponivel": "Disponível no Imobiliária Web",
            "foto_capa": "Foto de Capa",
            "link_contato": "Link para Contato",
            "informacoes_contato": "Informações de Contato",
            "cidade": "Cidade",
            "endereco": "Endereço",
            "coordenas_geograficas": "Coordenadas Geográficas",
            "categoria": "Categoria do Imóvel",
            "valor_locacao": "Valor Final para Locação",
            "valor_venda": "Valor de Venda",
            "quantidade_suites": "Quantidade de Suítes",
            "quantidade_quartos": "Quantidade de Quartos",
            "quantidade_banheiros": "Quantidade de Banheiros",
            "quantidade_vagas_garagem": "Quantidade de Vagas na Garagem",
            "metragem_imovel": "Metragem do Imóvel (m²)",
        }
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: Casa no Jardim Saúde, próximo a USP",
                }
            ),
            "resumo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: Casa recém reformada. Suíte com ar condicionado e mais dois quartos.",
                }
            ),
            "descricao": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: Casa em tons pasteis, mobiliada, churrasqueira, sem tarifas de condomínio, interfone.",
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
            "link_contato": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: https://wa.me/qr/codeWApp ",
                    "aria-label": "Username",
                    "aria-describedby": "basic-addon1",
                }
            ),
            "informacoes_contato": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: Você pode entrar em contato através do e-mail contato@imobiliariaweb.com.br",
                }
            ),
            "cidade": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "endereco": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: Rua das Flores, 53, Próximo ao Supermercado BoaCompra",
                }
            ),
            "coordenas_geograficas": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: -22.60121403915666, -48.786334703151375",
                }
            ),
            "categoria": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "valor_locacao": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 1020,00",
                }
            ),
            "valor_venda": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 100123,00",
                }
            ),
            "quantidade_suites": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 1",
                }
            ),
            "quantidade_quartos": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 2",
                }
            ),
            "quantidade_banheiros": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 2",
                }
            ),
            "quantidade_vagas_garagem": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 2",
                }
            ),
            "metragem_imovel": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: 82",
                }
            ),
        }
