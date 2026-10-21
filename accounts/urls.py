from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView
from django.urls import path, reverse_lazy

from accounts.views import MotDePasseChangeView, detail

app_name = "accounts"

urlpatterns = [
    path("connexion/", LoginView.as_view(template_name="accounts/connexion.html"), name="login"),
    path("deconnexion/", LogoutView.as_view(template_name="accounts/deconnexion.html"), name="logout"),
    path(
        "mot-de-passe/",
        MotDePasseChangeView.as_view(
            template_name="accounts/mot_de_passe.html",
            success_url=reverse_lazy("accounts:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "mot-de-passe/termine/",
        PasswordChangeDoneView.as_view(template_name="accounts/mot_de_passe_termine.html"),
        name="password_change_done",
    ),
    path("<str:username>/", detail, name="detail"),
]
