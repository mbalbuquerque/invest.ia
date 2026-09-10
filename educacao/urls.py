from django.urls import path
from . import views

app_name = "educacao"

urlpatterns = [
    path("", views.inicio, name="inicio"),

    path(
        "dinheiro-e-escolhas/",
        views.dinheiro_escolhas,
        name="dinheiro_escolhas",
    ),

    path(
        "orcamento/",
        views.orcamento,
        name="orcamento",
    ),

    path(
        "consumo-consciente/",
        views.consumo_consciente,
        name="consumo_consciente",
    ),

    path(
        "credito-e-juros/",
        views.credito_juros,
        name="credito_juros",
    ),

    path(
        "dividas/",
        views.dividas,
        name="dividas",
    ),

    path(
        "reserva-de-emergencia/",
        views.reserva_emergencia,
        name="reserva_emergencia",
    ),
    path(
        "primeiros-investimentos/",
        views.primeiros_investimentos,
        name="primeiros_investimentos",
),

]