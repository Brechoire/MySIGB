from django.test import TestCase, Client

from accounts.models import Compte


def _connecte(username="lecteur", staff=False):
    compte = Compte.objects.create_user(username=username)
    compte.force_password_change = False
    compte.is_staff = staff
    compte.save()
    client = Client()
    client.force_login(compte)
    return client


class AccesRestreintTest(TestCase):
    def test_accueil_anonyme_redirige_connexion(self):
        reponse = Client().get("/")
        self.assertRedirects(reponse, "/comptes/connexion/?next=/")

    def test_suivi_anonyme_redirige_connexion(self):
        reponse = Client().get("/suivi/")
        self.assertRedirects(reponse, "/comptes/connexion/?next=/suivi/")

    def test_connexion_reste_publique(self):
        reponse = Client().get("/comptes/connexion/")
        self.assertEqual(reponse.status_code, 200)

    def test_admin_login_reste_public(self):
        reponse = Client().get("/admin/login/")
        self.assertEqual(reponse.status_code, 200)

    def test_robots_public_et_interdit_tout(self):
        reponse = Client().get("/robots.txt")
        self.assertEqual(reponse.status_code, 200)
        self.assertIn("Disallow: /", reponse.content.decode())

    def test_entete_anti_indexation(self):
        reponse = Client().get("/comptes/connexion/")
        self.assertEqual(reponse["X-Robots-Tag"], "noindex, nofollow")


class CompteDetailTest(TestCase):
    def test_anonyme_redirige_vers_connexion(self):
        reponse = Client().get("/comptes/jdupont/")
        self.assertRedirects(reponse, "/comptes/connexion/?next=/comptes/jdupont/")

    def test_non_staff_redirige(self):
        client = _connecte(username="lecteur")
        reponse = client.get("/comptes/jdupont/")
        self.assertEqual(reponse.status_code, 302)

    def test_staff_voit_toutes_les_informations(self):
        Compte.objects.create_user(
            username="jdupont", first_name="Jeanne", last_name="Dupont",
            langue="fr", legacy_userid=7, legacy_rights=16,
        )
        client = _connecte(username="chef", staff=True)
        reponse = client.get("/comptes/jdupont/")
        self.assertEqual(reponse.status_code, 200)
        contenu = reponse.content.decode()
        for attendu in ["jdupont", "Jeanne", "Dupont", "7", "16", "Pagination", "Catalogage"]:
            self.assertIn(attendu, contenu)
        self.assertContains(reponse, "<table>")
        self.assertContains(reponse, "<caption>Catalogage</caption>", html=True)

    def test_detail_ne_montre_jamais_le_mot_de_passe(self):
        cible = Compte.objects.create_user(username="jdupont", password="Secret123!")
        client = _connecte(username="chef", staff=True)
        reponse = client.get("/comptes/jdupont/")
        self.assertNotContains(reponse, cible.password)

    def test_detail_inexistant_repond_404(self):
        client = _connecte(username="chef", staff=True)
        reponse = client.get("/comptes/inconnu/")
        self.assertEqual(reponse.status_code, 404)
