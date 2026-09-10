from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CadastroForm


def cadastro(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CadastroForm()

    return render(
        request,
        "accounts/cadastro.html",
        {"form": form},
    )


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")