"""Comptes de connexion MySIGB.

Reprise de la table PMB ``users`` (comptes professionnels : bibliothécaires
et comptes techniques comme ``pmb_api``). À ne pas confondre avec la table
PMB ``comptes`` (comptes *financiers* des lecteurs), qui fera l'objet d'une
autre app.

Règles de reprise (sécurité + RGPD) :
- les colonnes ``pwd`` et ``user_digest`` de PMB ne sont JAMAIS importées ;
- tout compte importé reçoit un mot de passe inutilisable
  (``set_unusable_password()``) et ``force_password_change=True`` ;
- le premier super-compte est créé par ``createsuperuser`` (secret jamais
  commité), la réinitialisation se fait par l'admin.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Compte(AbstractUser):
    """Compte de connexion (un par agent ou compte technique).

    USERNAME_FIELD reste ``username`` pour profiter de tout le système
    d'authentification Django (hashage, sessions, admin, permissions).
    """

    username = models.CharField(
        "nom d'utilisateur",
        max_length=100,
        unique=True,
        help_text="Identifiant de connexion. Reprend PMB users.username (varchar 100).",
    )
    first_name = models.CharField(
        "prénom",
        max_length=150,
        blank=True,
        help_text="Reprend PMB users.prenom (varchar 30, élargi au standard Django).",
    )
    last_name = models.CharField(
        "nom",
        max_length=150,
        blank=True,
        help_text="Reprend PMB users.nom (varchar 30, élargi au standard Django).",
    )
    langue = models.CharField(
        "langue",
        max_length=10,
        default="fr",
        help_text="Langue de l'agent. Reprend PMB users.user_lang (ex. 'fr_FR' → 'fr').",
    )
    legacy_userid = models.PositiveIntegerField(
        "référence PMB",
        null=True,
        blank=True,
        unique=True,
        help_text="PMB users.userid d'origine (traçabilité de la reprise, jamais réutilisé comme clé).",
    )
    legacy_rights = models.IntegerField(
        "droits PMB bruts",
        default=0,
        help_text="Bitmask PMB users.rights conservé pour audit. SANS EFFET : les droits effectifs sont les groupes/permissions Django.",
    )
    force_password_change = models.BooleanField(
        "changement de mot de passe imposé",
        default=True,
        help_text="Vrai après import ou réinitialisation admin : l'agent doit changer son mot de passe à la prochaine connexion.",
    )

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "compte"
        verbose_name_plural = "comptes"

    def __str__(self) -> str:
        return self.username


class Preferences(models.Model):
    """Préférences de travail et défauts de catalogage d'un compte.

    Reprend les colonnes de paramétrage de PMB ``users`` (affichage et
    valeurs par défaut à la création de notices). Aucune donnée sensible.
    """

    compte = models.OneToOneField(
        Compte,
        on_delete=models.CASCADE,
        related_name="preferences",
        verbose_name="compte",
        help_text="Compte propriétaire de ces préférences.",
    )
    nb_per_page_search = models.PositiveIntegerField(
        "résultats par page (recherche)", default=4,
        help_text="Reprend PMB users.nb_per_page_search.",
    )
    nb_per_page_select = models.PositiveIntegerField(
        "résultats par page (sélection)", default=10,
        help_text="Reprend PMB users.nb_per_page_select.",
    )
    nb_per_page_gestion = models.PositiveIntegerField(
        "résultats par page (gestion)", default=20,
        help_text="Reprend PMB users.nb_per_page_gestion.",
    )
    param_popup_ticket = models.BooleanField(
        "ticket en fenêtre surgissante", default=False,
        help_text="Reprend PMB users.param_popup_ticket.",
    )
    param_sounds = models.BooleanField("sons", default=True, help_text="Reprend PMB users.param_sounds.")
    param_rfid_activate = models.BooleanField(
        "RFID activée", default=True, help_text="Reprend PMB users.param_rfid_activate.",
    )
    param_chat_activate = models.BooleanField(
        "chat activé", default=False, help_text="Reprend PMB users.param_chat_activate.",
    )
    param_licence = models.BooleanField(
        "licence acceptée", default=False, help_text="Reprend PMB users.param_licence.",
    )
    deflt_notice_statut = models.PositiveIntegerField(
        "statut de notice par défaut", default=1,
        help_text="Reprend PMB users.deflt_notice_statut.",
    )
    deflt_notice_statut_analysis = models.PositiveIntegerField(
        "statut de dépouillement par défaut", default=0,
        help_text="Reprend PMB users.deflt_notice_statut_analysis.",
    )
    deflt_integration_notice_statut = models.PositiveIntegerField(
        "statut d'intégration par défaut", default=1,
        help_text="Reprend PMB users.deflt_integration_notice_statut.",
    )
    xmlta_indexation_lang = models.CharField(
        "langue d'indexation", max_length=20, blank=True, default="",
        help_text="Reprend PMB users.xmlta_indexation_lang.",
    )
    deflt_docs_type = models.PositiveIntegerField(
        "type de document par défaut", default=1,
        help_text="Reprend PMB users.deflt_docs_type.",
    )
    deflt_serials_docs_type = models.PositiveIntegerField(
        "type de périodique par défaut", default=1,
        help_text="Reprend PMB users.deflt_serials_docs_type.",
    )
    deflt_lenders = models.PositiveIntegerField(
        "prêteur par défaut", default=0, help_text="Reprend PMB users.deflt_lenders.",
    )
    deflt_styles = models.CharField(
        "feuille de style par défaut", max_length=20, default="default",
        help_text="Reprend PMB users.deflt_styles.",
    )
    deflt_docs_statut = models.PositiveIntegerField(
        "statut d'exemplaire par défaut", default=0,
        help_text="Reprend PMB users.deflt_docs_statut.",
    )
    deflt_docs_codestat = models.PositiveIntegerField(
        "code statistique par défaut", default=0,
        help_text="Reprend PMB users.deflt_docs_codestat.",
    )
    value_deflt_lang = models.CharField(
        "langue de catalogage", max_length=20, blank=True, default="fre",
        help_text="Reprend PMB users.value_deflt_lang.",
    )
    value_deflt_fonction = models.CharField(
        "fonction d'auteur par défaut", max_length=20, blank=True, default="070",
        help_text="Reprend PMB users.value_deflt_fonction (070 = auteur).",
    )
    value_deflt_relation = models.CharField(
        "relation par défaut", max_length=20, blank=True, default="a",
        help_text="Reprend PMB users.value_deflt_relation.",
    )
    value_deflt_relation_serial = models.CharField(
        "relation de périodique par défaut", max_length=20, blank=True, default="",
        help_text="Reprend PMB users.value_deflt_relation_serial.",
    )

    class Meta:
        verbose_name = "préférences"
        verbose_name_plural = "préférences"

    def __str__(self) -> str:
        return f"Préférences de {self.compte}"


@receiver(post_save, sender=Compte)
def creer_preferences(sender, instance, created, **kwargs):
    """Crée le jeu de préférences par défaut à la création du compte."""
    if created:
        Preferences.objects.create(compte=instance)
