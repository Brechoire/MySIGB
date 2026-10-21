import tempfile
from pathlib import Path

from django.contrib.auth import get_user_model
from django.test import TestCase, Client, override_settings

from changelog.services import list_plans, get_plan, rendre_markdown


def _client_connecte():
    """Client authentifié (la SIGB exige une connexion partout)."""
    compte = get_user_model().objects.create_user(username="lecteur")
    compte.force_password_change = False
    compte.save()
    client = Client()
    client.force_login(compte)
    return client


def _creer_plan(dossier: Path, nom: str, titre: str) -> Path:
    plan_dir = dossier / nom
    plan_dir.mkdir(parents=True)
    (plan_dir / "plan.md").write_text(f"# {titre}\n\n## Demande\n\nTest.\n", encoding="utf-8")
    return plan_dir


class ServiceListPlansTest(TestCase):
    def test_retourne_plans_tries(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            _creer_plan(base, "002-deuxieme", "Deuxième")
            _creer_plan(base, "001-premier", "Premier")
            plans = list_plans(base_dir=base)
            self.assertEqual([p["nom"] for p in plans], ["001-premier", "002-deuxieme"])
            self.assertEqual(plans[0]["numero"], "001")
            self.assertEqual(plans[0]["titre"], "Premier")

    def test_dossier_vide_retourne_liste_vide(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(list_plans(base_dir=Path(tmp)), [])


class ServiceGetPlanTest(TestCase):
    def test_retrouve_par_numero_court(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            _creer_plan(base, "001-premier", "Premier")
            plan = get_plan("001", base_dir=base)
            self.assertIsNotNone(plan)
            self.assertEqual(plan["titre"], "Premier")

    def test_rejette_traversee_de_chemin(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            _creer_plan(base, "001-premier", "Premier")
            self.assertIsNone(get_plan("../secrets", base_dir=base))
            self.assertIsNone(get_plan("../../etc/passwd", base_dir=base))
            self.assertIsNone(get_plan("999-inexistant", base_dir=base))


class ChangelogVuesTest(TestCase):
    def test_index_repond_200_avec_liste(self):
        with tempfile.TemporaryDirectory() as tmp:
            with override_settings(BASE_DIR=Path(tmp)):
                _creer_plan(Path(tmp) / "workflow", "001-premier", "Premier suivi")
                reponse = _client_connecte().get("/suivi/")
            self.assertEqual(reponse.status_code, 200)
            self.assertContains(reponse, "Premier suivi")

    def test_detail_repond_200(self):
        with tempfile.TemporaryDirectory() as tmp:
            _creer_plan(Path(tmp) / "workflow", "001-premier", "Premier suivi")
            with override_settings(BASE_DIR=Path(tmp)):
                reponse = _client_connecte().get("/suivi/001-premier/")
            self.assertEqual(reponse.status_code, 200)
            self.assertContains(reponse, "Premier suivi")

    def test_detail_inexistant_repond_404(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "workflow").mkdir(parents=True, exist_ok=True)
            with override_settings(BASE_DIR=Path(tmp)):
                reponse = _client_connecte().get("/suivi/999-inexistant/")
            self.assertEqual(reponse.status_code, 404)


class ServiceRendreMarkdownTest(TestCase):
    def test_convertit_titre_et_section(self):
        html = rendre_markdown("# Bonjour\n\n## Demande\n\nTest.\n")
        self.assertIn("<h1>Bonjour</h1>", html)
        self.assertIn("<h2>Demande</h2>", html)

    def test_texte_vide_retourne_chaine_vide(self):
        self.assertEqual(rendre_markdown(""), "")


class ChangelogMarkdownVuesTest(TestCase):
    def test_detail_rend_markdown_interprete(self):
        with tempfile.TemporaryDirectory() as tmp:
            _creer_plan(Path(tmp) / "workflow", "001-premier", "Premier suivi")
            with override_settings(BASE_DIR=Path(tmp)):
                reponse = _client_connecte().get("/suivi/001-premier/")
            self.assertEqual(reponse.status_code, 200)
            self.assertContains(reponse, "<h2>Demande</h2>", html=True)

    def test_pied_de_page_contient_lien_suivi(self):
        reponse = _client_connecte().get("/")
        self.assertEqual(reponse.status_code, 200)
        contenu = reponse.content.decode()
        self.assertIn("<footer", contenu)
        self.assertIn("/suivi/", contenu)
