"""Vues de connexion (habillage FR des vues d'authentification Django)."""
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, render

from accounts.models import Compte, Preferences


class MotDePasseChangeView(PasswordChangeView):
    """Changement de mot de passe qui lève le forçage une fois réussi."""

    def form_valid(self, form):
        reponse = super().form_valid(form)
        self.request.user.force_password_change = False
        self.request.user.save(update_fields=["force_password_change"])
        return reponse


@staff_member_required
def detail(request, username):
    """Fiche d'un compte (staff uniquement). N'affiche aucun secret."""
    compte = get_object_or_404(Compte, username=username)
    prefs, _ = Preferences.objects.get_or_create(compte=compte)
    groupes = {
        "Pagination": ("nb_per_page_search", "nb_per_page_select", "nb_per_page_gestion"),
        "Affichage": (
            "param_popup_ticket", "param_sounds", "param_rfid_activate",
            "param_chat_activate", "param_licence",
        ),
        "Catalogage": (
            "deflt_notice_statut", "deflt_notice_statut_analysis",
            "deflt_integration_notice_statut", "xmlta_indexation_lang",
            "deflt_docs_type", "deflt_serials_docs_type", "deflt_lenders",
            "deflt_styles", "deflt_docs_statut", "deflt_docs_codestat",
            "value_deflt_lang", "value_deflt_fonction", "value_deflt_relation",
            "value_deflt_relation_serial",
        ),
    }
    sections = [
        (titre, [(Preferences._meta.get_field(n).verbose_name, getattr(prefs, n)) for n in noms])
        for titre, noms in groupes.items()
    ]
    return render(request, "accounts/detail.html", {"compte": compte, "sections": sections})
