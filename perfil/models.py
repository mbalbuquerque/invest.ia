from django.conf import settings
from django.db import models


class PerfilInvestidor(models.Model):
    CLASSIFICACOES = [
        ("CONSERVADOR", "Conservador"),
        ("MODERADO", "Moderado"),
        ("ARROJADO", "Arrojado"),
    ]

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil_investidor",
    )

    score = models.PositiveIntegerField(default=0)

    classificacao = models.CharField(
        max_length=20,
        choices=CLASSIFICACOES,
        blank=True,
    )

    objetivo = models.CharField(max_length=100, blank=True)
    horizonte_anos = models.PositiveIntegerField(default=1)
    conhecimento = models.PositiveIntegerField(default=0)
    tolerancia_risco = models.PositiveIntegerField(default=0)
    capacidade_perda = models.PositiveIntegerField(default=0)

    atualizado_em = models.DateTimeField(auto_now=True)

    def calcular_score(self):
        score = (
            self.conhecimento
            + self.tolerancia_risco
            + self.capacidade_perda
        )

        score = max(0, min(score, 100))

        if score <= 33:
            classificacao = "CONSERVADOR"
        elif score <= 66:
            classificacao = "MODERADO"
        else:
            classificacao = "ARROJADO"

        self.score = score
        self.classificacao = classificacao

        return score

    def save(self, *args, **kwargs):
        self.calcular_score()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.usuario} - {self.get_classificacao_display()}"