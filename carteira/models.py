from decimal import Decimal

from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator


class Investimento(models.Model):

    CATEGORIAS = [
        ("RENDA_FIXA", "Renda Fixa"),
        ("ACOES", "Ações"),
        ("FIIS", "Fundos Imobiliários"),
        ("ETFS", "ETFs"),
        ("FUNDOS", "Fundos de Investimento"),
        ("CRIPTO", "Criptoativos"),
        ("OUTROS", "Outros"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="investimentos",
    )

    nome = models.CharField(
        max_length=150,
    )

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
    )

    quantidade = models.DecimalField(
        max_digits=18,
        decimal_places=8,
        validators=[
            MinValueValidator(Decimal("0.00000001"))
        ],
    )

    preco_medio = models.DecimalField(
        max_digits=18,
        decimal_places=8,
        validators=[
            MinValueValidator(Decimal("0.00000001"))
        ],
    )

    data_aplicacao = models.DateField()

    observacoes = models.TextField(
        blank=True,
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
    )

    @property
    def valor_investido(self):
        return self.quantidade * self.preco_medio

    class Meta:
        ordering = ["-data_aplicacao", "-criado_em"]
        verbose_name = "Investimento"
        verbose_name_plural = "Investimentos"

    def __str__(self):
        return f"{self.nome} - {self.usuario}"