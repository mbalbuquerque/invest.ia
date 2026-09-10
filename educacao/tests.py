from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from educacao.models import ProgressoEducacional


class EducacaoTests(TestCase):

    def setUp(self):
        self.usuario1 = User.objects.create_user(
            username="usuario1",
            email="usuario1@teste.com",
            password="Teste@12345",
        )

        self.usuario2 = User.objects.create_user(
            username="usuario2",
            email="usuario2@teste.com",
            password="Teste@12345",
        )

    def test_usuario_nao_autenticado_nao_acessa_educacao(self):
        response = self.client.get(
            reverse("educacao:inicio")
        )

        self.assertEqual(response.status_code, 302)

        self.assertIn(
            reverse("accounts:login"),
            response.url,
        )

    def test_usuario_nao_pode_pular_etapas(self):
        self.client.login(
            username="usuario1",
            password="Teste@12345",
        )

        response = self.client.get(
            reverse("educacao:orcamento")
        )

        self.assertRedirects(
            response,
            reverse("educacao:inicio"),
        )

    def test_resposta_correta_conclui_primeira_aula(self):
        self.client.login(
            username="usuario1",
            password="Teste@12345",
        )

        response = self.client.post(
            reverse("educacao:dinheiro_escolhas"),
            {
                "resposta": "B",
            },
        )

        self.assertEqual(response.status_code, 200)

        progresso = ProgressoEducacional.objects.filter(
            usuario=self.usuario1,
            aula="dinheiro_e_escolhas",
            concluida=True,
        ).exists()

        self.assertTrue(progresso)

    def test_resposta_errada_nao_conclui_primeira_aula(self):
        self.client.login(
            username="usuario1",
            password="Teste@12345",
        )

        response = self.client.post(
            reverse("educacao:dinheiro_escolhas"),
            {
                "resposta": "A",
            },
        )

        self.assertEqual(response.status_code, 200)

        progresso = ProgressoEducacional.objects.filter(
            usuario=self.usuario1,
            aula="dinheiro_e_escolhas",
            concluida=True,
        ).exists()

        self.assertFalse(progresso)

    def test_progresso_de_um_usuario_nao_libera_outro(self):
        ProgressoEducacional.objects.create(
            usuario=self.usuario1,
            aula="dinheiro_e_escolhas",
            concluida=True,
        )

        self.client.login(
            username="usuario2",
            password="Teste@12345",
        )

        response = self.client.get(
            reverse("educacao:orcamento")
        )

        self.assertRedirects(
            response,
            reverse("educacao:inicio"),
        )