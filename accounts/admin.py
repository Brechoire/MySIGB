"""Administration des comptes.

La page de changement de mot de passe de l'admin impose un nouveau
changement à la prochaine connexion (hygiène après réinitialisation).
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Compte, Preferences


class PreferencesInline(admin.StackedInline):
    """Préférences modifiables depuis la fiche du compte."""

    model = Preferences
    can_delete = False
    verbose_name = "préférences"
    verbose_name_plural = "préférences"


@admin.register(Compte)
class CompteAdmin(UserAdmin):
    """Gestion des comptes de connexion (création, réinitialisation)."""

    fieldsets = UserAdmin.fieldsets + (
        ("Reprise PMB", {"fields": ("legacy_userid", "legacy_rights", "langue", "force_password_change")}),
    )
    inlines = [PreferencesInline]

    def save_model(self, request, obj, form, change):
        if change:
            ancien = Compte.objects.get(pk=obj.pk)
            if ancien.password != obj.password:
                obj.force_password_change = True
        super().save_model(request, obj, form, change)
