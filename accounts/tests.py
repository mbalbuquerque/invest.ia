from django.test import TestCase
from django.urls import reverse

from accounts.models import User


class AccountsTests(TestCase):

    def setUp(self):
        self.usuario = User.objects.create_user(
            username="teste",
            email="teste@investai.local",
            password="Teste@12345",
        )

    def test_login_com_credenciais_corretas(self):
        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "teste",
                "password": "Teste@12345",
            },
        )

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            str(self.client.session["_auth_user_id"]),
            str(self.usuario.pk),
        )

    def test_login_com_senha_errada(self):
        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": "teste",
                "password": "senha-errada",
            },
        )

        self.assertEqual(response.status_code, 200)

        self.assertNotIn(
            "_auth_user_id",
            self.client.session,
        )

    def test_dashboard_exige_login(self):
        response = self.client.get(
            reverse("dashboard")
        )

        self.assertEqual(
            response.status_code,
            302,
        )

        self.assertIn(
            reverse("accounts:login"),
            response.url,
        )

    def test_dashboard_abre_para_usuario_logado(self):
        self.client.login(
            username="teste",
            password="Teste@12345",
        )

        response = self.client.get(
            reverse("dashboard")
        )

        self.assertEqual(
            response.status_code,
            200,
        )

    def test_email_nao_pode_ser_duplicado(self):
        with self.assertRaises(Exception):
            User.objects.create_user(
                username="outro",
                email="teste@investai.local",
                password="Outra@12345",
            )