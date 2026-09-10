from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class CadastroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "seuemail@exemplo.com",
                "autocomplete": "email",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escolha um nome de usuário",
                    "autocomplete": "username",
                }
            ),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Usuário",
                "autocomplete": "username",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Senha",
                "autocomplete": "current-password",
            }
        )
    )