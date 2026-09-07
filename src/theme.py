# -*- coding: utf-8 -*-
"""Charte graphique « Corporate sobre » — présentation officielle de projet, A4.

Toutes les constantes de style sont centralisées ici : couleurs, typographie,
géométrie de page. Modifier ce fichier suffit à re-thémer l'ensemble du PDF.
"""

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# --------------------------------------------------------------------------- #
# Géométrie de page (A4 portrait)
# --------------------------------------------------------------------------- #
PAGE_WIDTH, PAGE_HEIGHT = A4                      # 210 x 297 mm
MARGIN_LEFT = 20 * mm
MARGIN_RIGHT = 20 * mm
MARGIN_TOP = 24 * mm                              # bandeau d'en-tête inclus
MARGIN_BOTTOM = 20 * mm                           # pied de page inclus
CONTENT_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT

HEADER_BASELINE = PAGE_HEIGHT - 14 * mm           # ligne de base de l'en-tête
FOOTER_BASELINE = 11 * mm                         # ligne de base du pied de page

# --------------------------------------------------------------------------- #
# Palette
# --------------------------------------------------------------------------- #
NAVY = HexColor("#44449F")        # couleur primaire : indigo de la marque
NAVY_DEEP = HexColor("#2E2E7C")   # dégradé / aplats sombres
STEEL = HexColor("#5B5BC0")       # accent (liens, filets actifs)
ACCENT = HexColor("#C9A227")      # accent secondaire sobre (or institutionnel)
INK = HexColor("#26263A")         # corps de texte
BODY = HexColor("#3A3A4C")        # corps de texte secondaire
MUTED = HexColor("#6C6C82")       # mentions, légendes
RULE = HexColor("#D6D6E8")        # filets de séparation
RULE_SOFT = HexColor("#E7E7F3")   # filets discrets
PANEL = HexColor("#F4F4FB")       # fonds de blocs
PANEL_ALT = HexColor("#ECECF6")   # zébrage de tableaux / encadrés lavande
WHITE = HexColor("#FFFFFF")

SUCCESS = HexColor("#2F7D5D")
WARNING = HexColor("#B27A16")
DANGER = HexColor("#A8352B")
INFO = HexColor("#44449F")

SEVERITY = {
    "critique": DANGER,
    "élevé": HexColor("#C4622D"),
    "moyen": WARNING,
    "faible": SUCCESS,
}

STATUS = {
    "terminé": SUCCESS,
    "en cours": STEEL,
    "planifié": MUTED,
    "à risque": WARNING,
    "bloqué": DANGER,
}


def rgba(color: Color, alpha: float) -> Color:
    """Version translucide d'une couleur (utile pour les aplats légers)."""
    return Color(color.red, color.green, color.blue, alpha=alpha)


# --------------------------------------------------------------------------- #
# Typographie
# --------------------------------------------------------------------------- #
FONT_LIGHT = "Inter-Light"
FONT = "Inter-Regular"
FONT_ITALIC = "Inter-Italic"
FONT_MEDIUM = "Inter-Medium"
FONT_SEMI = "Inter-SemiBold"
FONT_BOLD = "Inter-Bold"

FONT_FAMILY = {
    "light": FONT_LIGHT,
    "regular": FONT,
    "italic": FONT_ITALIC,
    "medium": FONT_MEDIUM,
    "semi": FONT_SEMI,
    "bold": FONT_BOLD,
}

# Échelle typographique (pt)
FS_COVER_KICKER = 9
FS_COVER_TITLE = 30
FS_COVER_SUB = 12.5
FS_H1 = 17
FS_H2 = 12.5
FS_H3 = 10.5
FS_BODY = 9.6
FS_SMALL = 8.4
FS_MICRO = 7.2

LEADING_BODY = 14.6
LEADING_SMALL = 12.2
