
from datetime import date
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Investimento


User = get_user_model()


class CarteiraSegurancaTests(TestCase):

    def setUp(self):
        self.usuario1 = User.objects.create_user(
            username="investidor1",
            email="investidor1@teste.com",
            password="SenhaTeste@123",
        )

        self.usuario2 = User.objects.create_user(
            username="investidor2",
            email="investidor2@teste.com",
            password="SenhaTeste@456",
        )

        self.investimento = Investimento.objects.create(
            usuario=self.usuario1,
            nome="Tesouro Teste",
            categoria="RENDA_FIXA",
            quantidade=Decimal("1000"),
            preco_medio=Decimal("35"),
            data_aplicacao=date(2026, 10, 8),
        )

    def test_carteira_exige_login(self):
        resposta = self.client.get(
            reverse("carteira:minha_carteira")
        )
        self.assertEqual(resposta.status_code, 302)

    def test_usuario_visualiza_propria_carteira(self):
        self.client.force_login(self.usuario1)

        resposta = self.client.get(
            reverse("carteira:minha_carteira")
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Tesouro Teste")

    def test_usuario_nao_visualiza_carteira_alheia(self):
        self.client.force_login(self.usuario2)

        resposta = self.client.get(
            reverse("carteira:minha_carteira")
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertNotContains(resposta, "Tesouro Teste")

    def test_usuario_nao_edita_investimento_alheio(self):
        self.client.force_login(self.usuario2)

        resposta = self.client.post(
            reverse(
                "carteira:editar",
                args=[self.investimento.pk],
            ),
            {
                "nome": "Alterado indevidamente",
                "categoria": "ACOES",
                "quantidade": "10",
                "preco_medio": "50",
                "data_aplicacao": "2026-10-08",
            },
        )

        self.assertEqual(resposta.status_code, 404)

        self.investimento.refresh_from_db()
        self.assertEqual(
            self.investimento.nome,
            "Tesouro Teste",
        )

    def test_usuario_nao_exclui_investimento_alheio(self):
        self.client.force_login(self.usuario2)

        resposta = self.client.post(
            reverse(
                "carteira:excluir",
                args=[self.investimento.pk],
            )
        )

        self.assertEqual(resposta.status_code, 404)

        self.assertTrue(
            Investimento.objects.filter(
                pk=self.investimento.pk
            ).exists()
        )

    def test_exclusao_nao_permite_get(self):
        self.client.force_login(self.usuario1)

        resposta = self.client.get(
            reverse(
                "carteira:excluir",
                args=[self.investimento.pk],
            )
        )

        self.assertEqual(resposta.status_code, 405)

        self.assertTrue(
            Investimento.objects.filter(
                pk=self.investimento.pk
            ).exists()
        )

    def test_proprietario_pode_editar(self):
        self.client.force_login(self.usuario1)

        resposta = self.client.post(
            reverse(
                "carteira:editar",
                args=[self.investimento.pk],
            ),
            {
                "nome": "Tesouro Atualizado",
                "categoria": "RENDA_FIXA",
                "quantidade": "1000",
                "preco_medio": "40",
                "data_aplicacao": "2026-10-08",
            },
        )

        self.assertEqual(resposta.status_code, 302)

        self.investimento.refresh_from_db()

        self.assertEqual(
            self.investimento.preco_medio,
            Decimal("40"),
        )

    def test_proprietario_pode_excluir(self):
        self.client.force_login(self.usuario1)

        resposta = self.client.post(
            reverse(
                "carteira:excluir",
                args=[self.investimento.pk],
            )
        )

        self.assertEqual(resposta.status_code, 302)

        self.assertFalse(
            Investimento.objects.filter(
                pk=self.investimento.pk
            ).exists()
        )

class RaioXCarteiraTests(TestCase):

    def setUp(self):
        self.usuario1 = User.objects.create_user(
            username="raiox_usuario1",
            email="raiox1@teste.com",
            password="SenhaTeste@123",
        )

        self.usuario2 = User.objects.create_user(
            username="raiox_usuario2",
            email="raiox2@teste.com",
            password="SenhaTeste@456",
        )

        self.url = reverse("carteira:raio_x")

    def criar_investimento(
        self,
        usuario,
        nome,
        categoria,
        quantidade,
        preco_medio,
    ):
        return Investimento.objects.create(
            usuario=usuario,
            nome=nome,
            categoria=categoria,
            quantidade=Decimal(str(quantidade)),
            preco_medio=Decimal(str(preco_medio)),
            data_aplicacao=date(2026, 10, 8),
        )

    def test_distribuicao_por_categoria(self):
        self.criar_investimento(
            self.usuario1,
            "Tesouro",
            "RENDA_FIXA",
            60,
            100,
        )

        self.criar_investimento(
            self.usuario1,
            "Acao Teste",
            "ACOES",
            40,
            100,
        )

        self.client.force_login(self.usuario1)

        resposta = self.client.get(self.url)

        self.assertEqual(resposta.status_code, 200)

        self.assertEqual(
            resposta.context["total_investido"],
            Decimal("10000"),
        )

        distribuicao = {
            item["categoria"]: item["percentual"]
            for item in resposta.context["distribuicao"]
        }

        self.assertEqual(
            distribuicao["Renda Fixa"],
            Decimal("60.00"),
        )

        self.assertEqual(
            distribuicao["Ações"],
            Decimal("40.00"),
        )

    def test_maior_concentracao(self):
        self.criar_investimento(
            self.usuario1,
            "Tesouro Principal",
            "RENDA_FIXA",
            70,
            100,
        )

        self.criar_investimento(
            self.usuario1,
            "Acao Secundaria",
            "ACOES",
            30,
            100,
        )

        self.client.force_login(self.usuario1)

        resposta = self.client.get(self.url)

        self.assertEqual(
            resposta.context["maior_categoria"]["categoria"],
            "Renda Fixa",
        )

        self.assertEqual(
            resposta.context["maior_ativo"].nome,
            "Tesouro Principal",
        )

        self.assertEqual(
            resposta.context["percentual_maior_ativo"],
            Decimal("70.00"),
        )

    def test_isolamento_entre_usuarios(self):
        self.criar_investimento(
            self.usuario1,
            "Investimento Privado",
            "RENDA_FIXA",
            100,
            100,
        )

        self.client.force_login(self.usuario2)

        resposta = self.client.get(self.url)

        self.assertEqual(resposta.status_code, 200)

        self.assertEqual(
            resposta.context["total_investido"],
            Decimal("0.00"),
        )

        self.assertEqual(
            resposta.context["quantidade_ativos"],
            0,
        )

        self.assertNotContains(
            resposta,
            "Investimento Privado",
        )

    def test_carteira_vazia(self):
        self.client.force_login(self.usuario1)

        resposta = self.client.get(self.url)

        self.assertEqual(resposta.status_code, 200)

        self.assertEqual(
            resposta.context["total_investido"],
            Decimal("0.00"),
        )

        self.assertEqual(
            resposta.context["quantidade_ativos"],
            0,
        )

        self.assertEqual(
            resposta.context["quantidade_categorias"],
            0,
        )

        self.assertEqual(
            resposta.context["distribuicao"],
            [],
        )

        self.assertIsNone(
            resposta.context["maior_categoria"],
        )

        self.assertIsNone(
            resposta.context["maior_ativo"],
        )

    def test_raio_x_exige_autenticacao(self):
        resposta = self.client.get(self.url)

        self.assertEqual(resposta.status_code, 302)
