from django.conf import settings
from django.db import models


class ProgressoEducacional(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="progresso_educacional",
    )

    aula = models.CharField(
        max_length=100
    )

    concluida = models.BooleanField(
        default=False
    )

    atualizado_em = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = (
            "usuario",
            "aula",
        )

    def __str__(self):
        return f"{self.usuario} - {self.aula}"