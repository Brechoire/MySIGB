from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Compte


def index(request):
    """Page d'accueil : présentation + liste des comptes enregistrés."""
    comptes = Compte.objects.order_by("username")
    return render(request, "home/index.html", {"comptes": comptes})


def robots(request):
    """robots.txt : outil interne, indexation interdite partout."""
    return HttpResponse("User-agent: *\nDisallow: /\n", content_type="text/plain")
