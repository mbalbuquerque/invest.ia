from django import forms

from .models import PerfilInvestidor


class PerfilInvestidorForm(forms.ModelForm):

    OBJETIVOS = [
        ("RESERVA", "Formar reserva de segurança"),
        ("RENDA", "Gerar renda"),
        ("PATRIMONIO", "Construir patrimônio"),
        ("APOSENTADORIA", "Planejar aposentadoria"),
        ("OBJETIVO_ESPECIFICO", "Alcançar um objetivo específico"),
    ]

    objetivo = forms.ChoiceField(
        choices=OBJETIVOS,
        widget=forms.RadioSelect,
        label="Qual é seu principal objetivo financeiro?",
    )

    horizonte_anos = forms.ChoiceField(
        choices=[
            (1, "Até 1 ano"),
            (3, "De 1 a 3 anos"),
            (5, "De 3 a 5 anos"),
            (10, "Mais de 5 anos"),
        ],
        widget=forms.RadioSelect,
        label="Qual é o seu horizonte de investimento?",
    )

    conhecimento = forms.ChoiceField(
        choices=[
            (5, "Estou começando agora"),
            (15, "Conheço os produtos mais comuns"),
            (25, "Já invisto e acompanho meus investimentos"),
            (35, "Tenho boa experiência com diferentes classes de ativos"),
        ],
        widget=forms.RadioSelect,
        label="Como você avalia seu conhecimento sobre investimentos?",
    )

    tolerancia_risco = forms.ChoiceField(
        choices=[
            (5, "Prefiro preservar meu patrimônio, mesmo com menor retorno"),
            (15, "Aceito pequenas oscilações"),
            (25, "Aceito oscilações relevantes buscando maior retorno"),
            (35, "Tenho alta tolerância a volatilidade"),
        ],
        widget=forms.RadioSelect,
        label="Como você reage às oscilações da carteira?",
    )

    capacidade_perda = forms.ChoiceField(
        choices=[
            (5, "Uma perda temporária me afetaria muito"),
            (15, "Tenho alguma capacidade de suportar perdas"),
            (20, "Consigo manter os investimentos durante quedas"),
            (30, "Tenho capacidade financeira para suportar perdas relevantes"),
        ],
        widget=forms.RadioSelect,
        label="Qual é sua capacidade financeira para suportar perdas temporárias?",
    )

    class Meta:
        model = PerfilInvestidor
        fields = [
            "objetivo",
            "horizonte_anos",
            "conhecimento",
            "tolerancia_risco",
            "capacidade_perda",
        ]