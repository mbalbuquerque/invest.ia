from django.urls import path
from . import views

app_name = "carteira"

urlpatterns = [
    path(
        "",
        views.minha_carteira,
        name="minha_carteira",
    ),
    path(
        "novo/",
        views.cadastrar_investimento,
        name="cadastrar",
    ),
    path(
        "<int:pk>/editar/",
        views.editar_investimento,
        name="editar",
    ),
    path(
        "<int:pk>/excluir/",
        views.excluir_investimento,
        name="excluir",
    ),
]


from django.urls import path
from . import views

app_name = "carteira"

urlpatterns = [
    path(
        "",
        views.minha_carteira,
        name="minha_carteira",
    ),

    path(
        "raio-x/",
        views.raio_x_carteira,
        name="raio_x",
    ),

    path(
        "novo/",
        views.cadastrar_investimento,
        name="cadastrar",
    ),

    path(
        "<int:pk>/editar/",
        views.editar_investimento,
        name="editar",
    ),

    path(
        "<int:pk>/excluir/",
        views.excluir_investimento,
        name="excluir",
    ),
]
