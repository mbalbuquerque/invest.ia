from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import LoginForm
from . import views


app_name = "accounts"


urlpatterns = [
    path(
        "cadastro/",
        views.cadastro,
        name="cadastro",
    ),

    path(
        "entrar/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),

    path(
        "sair/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]