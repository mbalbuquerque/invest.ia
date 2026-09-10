from django.urls import path

from . import views


app_name = "perfil"


urlpatterns = [
    path(
        "avaliacao/",
        views.avaliacao,
        name="avaliacao",
    ),

    path(
        "resultado/",
        views.resultado,
        name="resultado",
    ),
]