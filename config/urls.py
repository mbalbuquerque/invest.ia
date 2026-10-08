from django.contrib import admin
from django.urls import include, path

from accounts.views import dashboard


urlpatterns = [
    # Administração
    path("admin/", admin.site.urls),

    # Autenticação e cadastro
    path("conta/", include("accounts.urls")),

    # Página inicial
    path("", include("core.urls")),

    # Dashboard
    path("app/", dashboard, name="dashboard"),

    # Perfil financeiro
    path("perfil/", include("perfil.urls")),

    # Educação financeira
    path("aprender/", include("educacao.urls")),

    # Carteira de investimentos
    path("carteira/", include("carteira.urls")),
]