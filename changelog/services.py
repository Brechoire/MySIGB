import re
from pathlib import Path

import markdown as _markdown
from django.conf import settings

NOM_PLAN_VALIDE = re.compile(r"^[0-9]{3}-[a-z0-9-]+$")
NUMERO_COURT_VALIDE = re.compile(r"^[0-9]{3}$")


def _dossier_workflow(base_dir=None) -> Path:
    if base_dir is not None:
        return _normaliser_base(base_dir)
    return Path(settings.BASE_DIR) / "workflow"


def _normaliser_base(base_dir) -> Path:
    chemin = Path(base_dir)
    # Les tests service passent directement le dossier contenant les plans,
    # les vues passent BASE_DIR (qui contient un sous-dossier workflow/).
    if (chemin / "workflow").is_dir():
        return chemin / "workflow"
    return chemin


def _lire_titre(fichier: Path, defaut: str) -> str:
    try:
        for ligne in fichier.read_text(encoding="utf-8").splitlines():
            if ligne.startswith("# "):
                return ligne[2:].strip() or defaut
    except OSError:
        pass
    return defaut


def rendre_markdown(texte: str) -> str:
    if not texte or not texte.strip():
        return ""
    return _markdown.markdown(texte, extensions=["fenced_code", "tables"])


def list_plans(base_dir=None) -> list[dict]:
    dossier = _dossier_workflow(base_dir) if base_dir is None else _normaliser_base(base_dir)
    if not dossier.is_dir():
        return []
    plans = []
    for entree in sorted(dossier.iterdir()):
        if not entree.is_dir() or not NOM_PLAN_VALIDE.match(entree.name):
            continue
        fichier = entree / "plan.md"
        plans.append(
            {
                "numero": entree.name[:3],
                "nom": entree.name,
                "titre": _lire_titre(fichier, entree.name) if fichier.is_file() else entree.name,
                "chemin": entree,
            }
        )
    return plans


def get_plan(numero: str, base_dir=None) -> dict | None:
    if not isinstance(numero, str):
        return None
    numero = numero.strip()
    dossier = _dossier_workflow(base_dir) if base_dir is None else _normaliser_base(base_dir)
    candidat: Path | None = None
    if NOM_PLAN_VALIDE.match(numero):
        candidat = dossier / numero
    elif NUMERO_COURT_VALIDE.match(numero):
        trouves = sorted(dossier.glob(f"{numero}-*")) if dossier.is_dir() else []
        if len(trouves) == 1 and trouves[0].is_dir():
            candidat = trouves[0]
        else:
            return None
    else:
        return None
    try:
        resolu = candidat.resolve()
        racine = dossier.resolve()
    except OSError:
        return None
    if not resolu.is_relative_to(racine) or not resolu.is_dir():
        return None
    fichier = resolu / "plan.md"
    contenu = ""
    if fichier.is_file():
        try:
            contenu = fichier.read_text(encoding="utf-8")
        except OSError:
            contenu = ""
    return {
        "numero": resolu.name[:3],
        "nom": resolu.name,
        "titre": _lire_titre(fichier, resolu.name) if fichier.is_file() else resolu.name,
        "contenu": contenu,
        "chemin": resolu,
    }
