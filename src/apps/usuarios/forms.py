from django import forms


class EntrarForms(forms.Form):
    email_usuario = forms.CharField(
        label="E-mail de cadastro",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: contato@imobiliariaweb.com.br",
            }
        ),
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        ),
    )
