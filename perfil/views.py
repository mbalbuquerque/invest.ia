from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PerfilInvestidorForm
from .models import PerfilInvestidor


@login_required
def avaliacao(request):

    perfil, _ = PerfilInvestidor.objects.get_or_create(
        usuario=request.user
    )

    if request.method == "POST":

        form = PerfilInvestidorForm(
            request.POST,
            instance=perfil,
        )

        if form.is_valid():
            perfil = form.save(commit=False)

            perfil.conhecimento = int(
                form.cleaned_data["conhecimento"]
            )

            perfil.tolerancia_risco = int(
                form.cleaned_data["tolerancia_risco"]
            )

            perfil.capacidade_perda = int(
                form.cleaned_data["capacidade_perda"]
            )

            perfil.horizonte_anos = int(
                form.cleaned_data["horizonte_anos"]
            )

            perfil.usuario = request.user
            perfil.save()

            return redirect("perfil:resultado")

    else:
        form = PerfilInvestidorForm(instance=perfil)

    return render(
        request,
        "perfil/avaliacao.html",
        {
            "form": form,
        },
    )


@login_required
def resultado(request):

    perfil = PerfilInvestidor.objects.get(
        usuario=request.user
    )

    return render(
        request,
        "perfil/resultado.html",
        {
            "perfil": perfil,
        },
    )