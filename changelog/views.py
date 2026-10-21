from django.http import Http404
from django.shortcuts import render

from .services import get_plan, list_plans, rendre_markdown


def index(request):
    plans = list_plans()
    dernier = plans[-1] if plans else None
    return render(request, "changelog/index.html", {"plans": plans, "dernier": dernier})


def detail(request, numero: str):
    plan = get_plan(numero)
    if plan is None:
        raise Http404("Plan introuvable")
    plan["contenu_html"] = rendre_markdown(plan.get("contenu", ""))
    return render(request, "changelog/detail.html", {"plan": plan})
