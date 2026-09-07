# -*- coding: utf-8 -*-
"""Enregistrement de la famille Inter (polices vectorielles embarquées)."""

import os

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts"
)

_FONTS = {
    "Inter-Light": "Inter-Light.ttf",
    "Inter-Regular": "Inter-Regular.ttf",
    "Inter-Italic": "Inter-Italic.ttf",
    "Inter-Medium": "Inter-Medium.ttf",
    "Inter-SemiBold": "Inter-SemiBold.ttf",
    "Inter-Bold": "Inter-Bold.ttf",
}

_registered = False


def register_fonts() -> None:
    """Enregistre les TTF auprès de reportlab (opération idempotente)."""
    global _registered
    if _registered:
        return

    missing = []
    for name, filename in _FONTS.items():
        path = os.path.join(FONT_DIR, filename)
        if not os.path.exists(path):
            missing.append(filename)
            continue
        pdfmetrics.registerFont(TTFont(name, path))

    if missing:
        raise RuntimeError(
            "Polices introuvables dans %s : %s. Lancez tools/fetch_fonts.py."
            % (FONT_DIR, ", ".join(missing))
        )

    # Liaisons gras / italique pour les balises <b> et <i> du paragraphe.
    pdfmetrics.registerFontFamily(
        "Inter-Regular",
        normal="Inter-Regular",
        bold="Inter-Bold",
        italic="Inter-Italic",
        boldItalic="Inter-Bold",
    )
    _registered = True
