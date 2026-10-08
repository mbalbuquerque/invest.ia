from django import forms
from .models import Investimento


class InvestimentoForm(forms.ModelForm):

    class Meta:
        model = Investimento

        fields = [
            "nome",
            "categoria",
            "quantidade",
            "preco_medio",
            "data_aplicacao",
            "observacoes",
        ]

        widgets = {
            "nome": forms.TextInput(
                attrs={"placeholder": "Ex.: Tesouro IPCA+"}
            ),
            "quantidade": forms.NumberInput(
                attrs={"step": "0.00000001", "min": "0.00000001"}
            ),
            "preco_medio": forms.NumberInput(
                attrs={"step": "0.00000001", "min": "0.00000001"}
            ),
            "data_aplicacao": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d",
            ),
            "observacoes": forms.Textarea(
                attrs={"rows": 3}
            ),
        }