"""Garde-fous de connexion.

La SIGB est un outil interne : toutes les pages exigent une connexion
(sauf connexion, déconnexion, robots.txt et l'identification admin), et
toutes les réponses portent ``X-Robots-Tag: noindex, nofollow``.
"""
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse


class ConnexionRequiseMiddleware:
    """Exige une connexion partout + anti-indexation systématique.

    Exemptions : pages de connexion/déconnexion, robots.txt, identification
    admin, fichiers statiques (dev). Le header ``X-Robots-Tag`` est ajouté
    à chaque réponse, connecté ou non.
    """

    EXEMPTIONS_PREFIXES = ("/admin/login", "/static/")

    def __init__(self, get_response):
        self.get_response = get_response

    def _exempt(self):
        return {
            reverse("accounts:login"),
            reverse("accounts:logout"),
            reverse("robots"),
            "/admin/logout/",
        }

    def __call__(self, request):
        if (
            not request.user.is_authenticated
            and request.path not in self._exempt()
            and not request.path.startswith(self.EXEMPTIONS_PREFIXES)
        ):
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        reponse = self.get_response(request)
        reponse["X-Robots-Tag"] = "noindex, nofollow"
        return reponse


class ForcePasswordChangeMiddleware:
    """Impose le changement de mot de passe quand le compte l'exige."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        utilisateur = getattr(request, "user", None)
        if getattr(utilisateur, "is_authenticated", False) and getattr(
            utilisateur, "force_password_change", False
        ):
            autorises = {
                reverse("accounts:password_change"),
                reverse("accounts:password_change_done"),
                reverse("accounts:logout"),
            }
            if request.path not in autorises and not request.path.startswith("/admin/"):
                return redirect("accounts:password_change")
        return self.get_response(request)
