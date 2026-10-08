
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import InvestimentoForm
from .models import Investimento


# =====================================================
# MINHA CARTEIRA
# =====================================================

@login_required
def minha_carteira(request):
    investimentos = Investimento.objects.filter(
        usuario=request.user
    )

    total_investido = sum(
        (item.valor_investido for item in investimentos),
        Decimal("0.00"),
    )

    return render(
        request,
        "carteira/minha_carteira.html",
        {
            "investimentos": investimentos,
            "total_investido": total_investido,
        },
    )


# =====================================================
# RAIO-X DA CARTEIRA + PLOTLY
# =====================================================

@login_required
def raio_x_carteira(request):

    investimentos = list(
        Investimento.objects.filter(
            usuario=request.user
        )
    )

    total_investido = sum(
        (item.valor_investido for item in investimentos),
        Decimal("0.00"),
    )

    quantidade_ativos = len(investimentos)

    categorias = dict(Investimento.CATEGORIAS)
    totais_categoria = {}

    for investimento in investimentos:
        categoria = investimento.categoria

        totais_categoria[categoria] = (
            totais_categoria.get(categoria, Decimal("0"))
            + investimento.valor_investido
        )

    distribuicao = []

    for codigo, valor in totais_categoria.items():

        percentual = (
            valor / total_investido * Decimal("100")
            if total_investido > 0
            else Decimal("0")
        )

        distribuicao.append({
            "categoria": categorias.get(codigo, codigo),
            "valor": valor,
            "percentual": round(percentual, 2),
        })

    distribuicao.sort(
        key=lambda item: item["valor"],
        reverse=True,
    )

    quantidade_categorias = len(distribuicao)

    maior_categoria = (
        distribuicao[0]
        if distribuicao
        else None
    )

    maior_ativo = (
        max(
            investimentos,
            key=lambda item: item.valor_investido,
        )
        if investimentos
        else None
    )

    percentual_maior_ativo = Decimal("0")

    if maior_ativo and total_investido > 0:
        percentual_maior_ativo = round(
            maior_ativo.valor_investido
            / total_investido
            * Decimal("100"),
            2,
        )

    # =====================================================
    # DADOS DOS GRÁFICOS INTERATIVOS
    # =====================================================

    distribuicao_grafico = [
        {
            "categoria": item["categoria"],
            "valor": float(item["valor"]),
            "percentual": float(item["percentual"]),
        }
        for item in distribuicao
    ]

    ativos_grafico = [
        {
            "id": investimento.pk,
            "nome": investimento.nome,
            "categoria": categorias.get(
                investimento.categoria,
                investimento.categoria,
            ),
            "valor": float(investimento.valor_investido),
            "quantidade": str(investimento.quantidade),
            "preco_medio": str(investimento.preco_medio),
        }
        for investimento in investimentos
    ]

    ativos_grafico.sort(
        key=lambda item: item["valor"],
        reverse=True,
    )

    return render(
        request,
        "carteira/raio_x.html",
        {
            "total_investido": total_investido,
            "quantidade_ativos": quantidade_ativos,
            "quantidade_categorias": quantidade_categorias,
            "distribuicao": distribuicao,
            "maior_categoria": maior_categoria,
            "maior_ativo": maior_ativo,
            "percentual_maior_ativo": percentual_maior_ativo,
            "distribuicao_grafico": distribuicao_grafico,
            "ativos_grafico": ativos_grafico,
        },
    )


# =====================================================
# CADASTRAR INVESTIMENTO
# =====================================================

@login_required
def cadastrar_investimento(request):

    if request.method == "POST":
        form = InvestimentoForm(request.POST)

        if form.is_valid():
            investimento = form.save(commit=False)
            investimento.usuario = request.user
            investimento.save()

            return redirect("carteira:minha_carteira")

    else:
        form = InvestimentoForm()

    return render(
        request,
        "carteira/form_investimento.html",
        {
            "form": form,
            "titulo": "Adicionar investimento",
        },
    )


# =====================================================
# EDITAR INVESTIMENTO
# =====================================================

@login_required
def editar_investimento(request, pk):

    investimento = get_object_or_404(
        Investimento,
        pk=pk,
        usuario=request.user,
    )

    if request.method == "POST":

        form = InvestimentoForm(
            request.POST,
            instance=investimento,
        )

        if form.is_valid():
            form.save()
            return redirect("carteira:minha_carteira")

    else:
        form = InvestimentoForm(
            instance=investimento
        )

    return render(
        request,
        "carteira/form_investimento.html",
        {
            "form": form,
            "titulo": "Editar investimento",
        },
    )


# =====================================================
# EXCLUIR INVESTIMENTO
# =====================================================

@login_required
@require_POST
def excluir_investimento(request, pk):

    investimento = get_object_or_404(
        Investimento,
        pk=pk,
        usuario=request.user,
    )

    investimento.delete()

    return redirect("carteira:minha_carteira")
