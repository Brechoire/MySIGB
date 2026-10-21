from django.test import TestCase, Client

from accounts.models import Compte


def _client_connecte():
    compte = Compte.objects.create_user(username="lecteur")
    compte.force_password_change = False
    compte.save()
    client = Client()
    client.force_login(compte)
    return client


class AccueilUtilisateursTest(TestCase):
    def test_accueil_liste_les_comptes(self):
        Compte.objects.create_user(username="jdupont", first_name="Jeanne", last_name="Dupont")
        Compte.objects.create_user(username="pmb_api")
        reponse = _client_connecte().get("/")
        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, "jdupont")
        self.assertContains(reponse, "pmb_api")
        self.assertContains(reponse, "Jeanne")
        self.assertContains(reponse, "<table")

    def test_accueil_sans_autre_compte_affiche_un_message(self):
        # Seul le visiteur connecté existe : il se voit lui-même listé.
        reponse = _client_connecte().get("/")
        self.assertEqual(reponse.status_code, 200)
        self.assertContains(reponse, "lecteur")

    def test_noms_cliquables_vers_les_fiches(self):
        Compte.objects.create_user(username="jdupont")
        reponse = _client_connecte().get("/")
        self.assertContains(reponse, 'href="/comptes/jdupont/"')
