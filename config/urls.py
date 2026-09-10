from django.contrib import admin
from django.urls import include, path

from accounts.views import dashboard


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "conta/",
        include("accounts.urls"),
    ),

    path(
        "",
        include("core.urls"),
    ),
    
    path(
    "app/",
    dashboard,
    name="dashboard",
),
    path(
    "perfil/",
    include("perfil.urls"),
),

path("aprender/", include("educacao.urls")),


]