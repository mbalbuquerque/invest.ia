from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from .models import ProgressoEducacional

def aula_concluida(usuario, codigo):
    return ProgressoEducacional.objects.filter(
        usuario=usuario,
        aula=codigo,
        concluida=True,
    ).exists()


@login_required
def inicio(request):

    trilhas = [
        {
            "numero": 1,
            "titulo": "Dinheiro e escolhas",
            "descricao": "Entenda como nossas escolhas afetam a vida financeira.",
            "status": "disponivel",
            "url": "educacao:dinheiro_escolhas",
            "codigo": "dinheiro_e_escolhas",
        },
        {
            "numero": 2,
            "titulo": "Orçamento",
            "descricao": "Aprenda a organizar receitas, despesas e prioridades.",
            "status": "bloqueado",
            "url": "educacao:orcamento",
            "codigo": "orcamento",
        },
        {
            "numero": 3,
            "titulo": "Consumo consciente",
            "descricao": "Aprenda a diferenciar necessidade, desejo e impulso.",
            "status": "bloqueado",
            "url": "educacao:consumo_consciente",
            "codigo": "consumo_consciente",
        },
        {
            "numero": 4,
            "titulo": "Crédito e juros",
            "descricao": "Entenda cartão, parcelamento, empréstimos e juros.",
            "status": "bloqueado",
            "url": "educacao:credito_juros",
            "codigo": "credito_juros",
        },
        {
            "numero": 5,
            "titulo": "Dívidas",
            "descricao": "Aprenda como prevenir e organizar situações de endividamento.",
            "status": "bloqueado",
            "url": "educacao:dividas",
            "codigo": "dividas",
        },
        {
            "numero": 6,
            "titulo": "Reserva de emergência",
            "descricao": "Entenda por que proteção financeira vem antes do longo prazo.",
            "status": "bloqueado",
            "url": "educacao:reserva_emergencia",
            "codigo": "reserva_emergencia",
        },
        {
        "numero": 7,
        "titulo": "Primeiros investimentos",
        "descricao": "Conheça risco, liquidez, prazo e rentabilidade.",
        "status": "bloqueado",
        "url": "educacao:primeiros_investimentos",
        "codigo": "primeiros_investimentos",
        },

    ]

    concluidas = ProgressoEducacional.objects.filter(
        usuario=request.user,
        concluida=True,
    ).values_list(
        "aula",
        flat=True,
    )

    concluidas = set(concluidas)

    total_aulas = len(trilhas)

    total_concluidas = sum(
        1
        for trilha in trilhas
        if trilha["codigo"] in concluidas
    )

    percentual = int(
        (total_concluidas / total_aulas) * 100
    )

    for indice, trilha in enumerate(trilhas):

        trilha["concluida"] = (
            trilha["codigo"] in concluidas
        )

        if indice == 0:
            trilha["status"] = "disponivel"

        elif trilhas[indice - 1]["concluida"]:
            trilha["status"] = "disponivel"

        else:
            trilha["status"] = "bloqueado"

    return render(
        request,
        "educacao/inicio.html",
        {
            "trilhas": trilhas,
            "total_aulas": total_aulas,
            "total_concluidas": total_concluidas,
            "percentual": percentual,
        },
    )


@login_required
def dinheiro_escolhas(request):

    resultado = None

    if request.method == "POST":

        resposta = request.POST.get("resposta")

        if resposta == "B":

            resultado = "correta"

            ProgressoEducacional.objects.update_or_create(
                usuario=request.user,
                aula="dinheiro_e_escolhas",
                defaults={
                    "concluida": True
                },
            )

        else:
            resultado = "incorreta"

    progresso = ProgressoEducacional.objects.filter(
        usuario=request.user,
        aula="dinheiro_e_escolhas",
        concluida=True,
    ).exists()

    return render(
        request,
        "educacao/dinheiro_escolhas.html",
        {
            "resultado": resultado,
            "progresso": progresso,
        },
    )

@login_required

def orcamento(request):

    if not aula_concluida(
        request.user,
        "dinheiro_e_escolhas"
    ):
        return redirect("educacao:inicio")

    

    resultado = None

    if request.method == "POST":

        resposta = request.POST.get("resposta")

        if resposta == "C":

            resultado = "correta"

            ProgressoEducacional.objects.update_or_create(
                usuario=request.user,
                aula="orcamento",
                defaults={
                    "concluida": True
                },
            )

        else:
            resultado = "incorreta"

    progresso = ProgressoEducacional.objects.filter(
        usuario=request.user,
        aula="orcamento",
        concluida=True,
    ).exists()

    return render(
        request,
        "educacao/orcamento.html",
        {
            "resultado": resultado,
            "progresso": progresso,
        },
    )

@login_required
def consumo_consciente(request):

    if not aula_concluida(
        request.user,
        "orcamento"
    ):
        return redirect("educacao:inicio")

    resultado = None

    if request.method == "POST":

        resposta = request.POST.get("resposta")

        if resposta == "B":

            resultado = "correta"

            ProgressoEducacional.objects.update_or_create(
                usuario=request.user,
                aula="consumo_consciente",
                defaults={
                    "concluida": True
                },
            )

        else:
            resultado = "incorreta"

    progresso = ProgressoEducacional.objects.filter(
        usuario=request.user,
        aula="consumo_consciente",
        concluida=True,
    ).exists()

    return render(
        request,
        "educacao/consumo_consciente.html",
        {
            "resultado": resultado,
            "progresso": progresso,
        },
    )

@login_required
def credito_juros(request):

    if not aula_concluida(
        request.user,
        "consumo_consciente"
    ):
        return redirect("educacao:inicio")

    resultado = None

    if request.method == "POST":

        resposta = request.POST.get("resposta")

        if resposta == "C":

            resultado = "correta"

            ProgressoEducacional.objects.update_or_create(
                usuario=request.user,
                aula="credito_juros",
                defaults={
                    "concluida": True
                },
            )

        else:
            resultado = "incorreta"

    progresso = ProgressoEducacional.objects.filter(
        usuario=request.user,
        aula="credito_juros",
        concluida=True,
    ).exists()

    return render(
        request,
        "educacao/credito_juros.html",
        {
            "resultado": resultado,
            "progresso": progresso,
        },
    )

@login_required
def dividas(request):

    if not aula_concluida(
        request.user,
        "credito_juros"
    ):
        return redirect("educacao:inicio")

    resultado = None
    simulacao = None

    if request.method == "POST":

        acao = request.POST.get("acao")

        # =====================================
        # QUIZ
        # =====================================

        if acao == "quiz":

            resposta = request.POST.get("resposta")

            if resposta == "B":

                resultado = "correta"

                ProgressoEducacional.objects.update_or_create(
                    usuario=request.user,
                    aula="dividas",
                    defaults={
                        "concluida": True
                    },
                )

            else:
                resultado = "incorreta"

        # =====================================
        # SIMULADOR
        # =====================================

        elif acao == "simular":

            try:

                divida = float(
                    request.POST.get(
                        "valor_divida",
                        "0"
                    ).replace(",", ".")
                )

                juros = float(
                    request.POST.get(
                        "juros",
                        "0"
                    ).replace(",", ".")
                )

                pagamento = float(
                    request.POST.get(
                        "pagamento",
                        "0"
                    ).replace(",", ".")
                )

                saldo = divida
                total_pago = 0
                meses = 0

                taxa = juros / 100

                if (
                    divida > 0
                    and pagamento > 0
                    and juros >= 0
                ):

                    while saldo > 0 and meses < 600:

                        juros_mes = saldo * taxa
                        saldo += juros_mes

                        valor_pago = min(
                            pagamento,
                            saldo
                        )

                        saldo -= valor_pago
                        total_pago += valor_pago
                        meses += 1

                        if pagamento <= juros_mes:
                            break

                    if saldo <= 0:

                        simulacao = {
                            "status": "quitada",
                            "meses": meses,
                            "total_pago": total_pago,
                            "juros_total": (
                                total_pago - divida
                            ),
                        }

                    else:

                        simulacao = {
                            "status": "nao_quita",
                        }

            except ValueError:

                simulacao = {
                    "status": "erro",
                }

    progresso = ProgressoEducacional.objects.filter(
        usuario=request.user,
        aula="dividas",
        concluida=True,
    ).exists()

    return render(
        request,
        "educacao/dividas.html",
        {
            "resultado": resultado,
            "simulacao": simulacao,
            "progresso": progresso,
        },
    )

@login_required

def reserva_emergencia(request):

    if not aula_concluida(
        request.user,
        "dividas"
    ):
        return redirect("educacao:inicio")

    resultado = None

    if request.method == "POST":

        resposta = request.POST.get("resposta")

        if resposta == "B":

            resultado = "correta"

            ProgressoEducacional.objects.update_or_create(
                usuario=request.user,
                aula="reserva_emergencia",
                defaults={
                    "concluida": True
                },
            )

        else:
            resultado = "incorreta"

    progresso = ProgressoEducacional.objects.filter(
        usuario=request.user,
        aula="reserva_emergencia",
        concluida=True,
    ).exists()

    return render(
        request,
        "educacao/reserva_emergencia.html",
        {
            "resultado": resultado,
            "progresso": progresso,
        },
    )

@login_required

def primeiros_investimentos(request):

    if not aula_concluida(
        request.user,
        "reserva_emergencia"
    ):
        return redirect("educacao:inicio")

    resultado = None

    if request.method == "POST":

        resposta = request.POST.get("resposta")

        if resposta == "C":

            resultado = "correta"

            ProgressoEducacional.objects.update_or_create(
                usuario=request.user,
                aula="primeiros_investimentos",
                defaults={
                    "concluida": True
                },
            )

        else:
            resultado = "incorreta"

    progresso = ProgressoEducacional.objects.filter(
        usuario=request.user,
        aula="primeiros_investimentos",
        concluida=True,
    ).exists()

    return render(
        request,
        "educacao/primeiros_investimentos.html",
        {
            "resultado": resultado,
            "progresso": progresso,
        },
    )   