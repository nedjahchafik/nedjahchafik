# -*- coding: utf-8 -*-
"""Moteur de génération du PDF A4 : gabarits de page, en-têtes, pieds de page,
page de garde, sommaire et pagination « Page X / Y ».
"""

import os

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

from components import S, AccentBar, HRule, Pill, paragraph
from fonts import register_fonts
from theme import (
    ACCENT,
    BODY,
    CONTENT_WIDTH,
    FONT,
    FONT_BOLD,
    FONT_LIGHT,
    FONT_MEDIUM,
    FONT_SEMI,
    FOOTER_BASELINE,
    HEADER_BASELINE,
    INK,
    MARGIN_BOTTOM,
    MARGIN_LEFT,
    MARGIN_RIGHT,
    MARGIN_TOP,
    MUTED,
    NAVY,
    NAVY_DEEP,
    PAGE_HEIGHT,
    PAGE_WIDTH,
    PANEL,
    RULE,
    RULE_SOFT,
    STEEL,
    WHITE,
    FS_MICRO,
    FS_SMALL,
    rgba,
)


# --------------------------------------------------------------------------- #
# Utilitaires de dessin
# --------------------------------------------------------------------------- #


def draw_tracked(c, text, x, y, font=FONT_SEMI, size=7.4, tracking=0.85,
                 color=MUTED, align="left", width=None):
    """Texte en capitales espacées (letter-spacing), aligné à gauche/droite."""
    c.saveState()
    c.setFont(font, size)
    c.setFillColor(color)
    chars = list(text)
    widths = [stringWidth(ch, font, size) for ch in chars]
    total = sum(widths) + tracking * max(0, len(chars) - 1)
    if align == "right" and width is not None:
        x = x + width - total
    elif align == "center" and width is not None:
        x = x + (width - total) / 2.0
    cx = x
    for ch, w in zip(chars, widths):
        c.drawString(cx, y, ch)
        cx += w + tracking
    c.restoreState()
    return total


class SetSection(Flowable):
    """Flowable invisible : informe l'en-tête du titre de section courant."""

    def __init__(self, label):
        Flowable.__init__(self)
        self.label = label
        self.height = 0
        self.width = 0

    def wrap(self, availWidth, availHeight):
        return (0, 0)

    def draw(self):
        self.canv._current_section = self.label


# --------------------------------------------------------------------------- #
# Canvas paginé (Page X / Y)
# --------------------------------------------------------------------------- #


class NumberedCanvas(pdfcanvas.Canvas):
    """Deux passes : le total de pages est connu avant d'écrire les pieds."""

    def __init__(self, *args, **kwargs):
        pdfcanvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []
        self.doc_meta = {}

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved_page_states)
        for i, state in enumerate(self._saved_page_states, start=1):
            self.__dict__.update(state)
            self._draw_page_number(i, total)
            pdfcanvas.Canvas.showPage(self)
        pdfcanvas.Canvas.save(self)

    def _draw_page_number(self, index, total):
        if index == 1:                      # pas de folio sur la page de garde
            return
        label = "Page %d / %d" % (index, total)
        c = self
        c.saveState()
        c.setFont(FONT_MEDIUM, FS_MICRO + 0.2)
        c.setFillColor(MUTED)
        c.drawRightString(PAGE_WIDTH - MARGIN_RIGHT, FOOTER_BASELINE, label)
        c.restoreState()


# --------------------------------------------------------------------------- #
# Décor des pages
# --------------------------------------------------------------------------- #


def _cover_background(c, doc):
    """Page de garde : liseré supérieur, aplats et bandeau inférieur navy."""
    meta = getattr(doc, "meta", {})
    c.saveState()

    # Bandeau supérieur fin + filet
    c.setFillColor(NAVY)
    c.rect(0, PAGE_HEIGHT - 6 * mm, PAGE_WIDTH, 6 * mm, stroke=0, fill=1)
    c.setFillColor(ACCENT)
    c.rect(0, PAGE_HEIGHT - 7.6 * mm, PAGE_WIDTH, 1.6 * mm, stroke=0, fill=1)

    # Identification de l'organisme (sous le bandeau)
    org = meta.get("organization", "")
    dept = meta.get("department", "")
    if org:
        draw_tracked(c, org.upper(), MARGIN_LEFT, PAGE_HEIGHT - 17 * mm,
                     font=FONT_BOLD, size=9.2, tracking=1.15, color=NAVY)
    if dept:
        draw_tracked(c, dept.upper(), MARGIN_LEFT, PAGE_HEIGHT - 22.5 * mm,
                     font=FONT_MEDIUM, size=7.4, tracking=0.95, color=MUTED)

    # Filet de séparation haut
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.line(MARGIN_LEFT, PAGE_HEIGHT - 28 * mm, PAGE_WIDTH - MARGIN_RIGHT,
           PAGE_HEIGHT - 28 * mm)

    # Logo éventuel (coin supérieur droit)
    logo = meta.get("logo_path")
    if logo and os.path.exists(logo):
        try:
            c.drawImage(logo, PAGE_WIDTH - MARGIN_RIGHT - 34 * mm,
                        PAGE_HEIGHT - 26 * mm, width=34 * mm, height=17 * mm,
                        preserveAspectRatio=True, mask="auto")
        except Exception:
            pass

    # Bandeau inférieur navy
    band_h = 30 * mm
    c.setFillColor(NAVY)
    c.rect(0, 0, PAGE_WIDTH, band_h, stroke=0, fill=1)
    c.setFillColor(ACCENT)
    c.rect(0, band_h, PAGE_WIDTH, 1.2 * mm, stroke=0, fill=1)

    # Mentions du bandeau
    left_items = [
        (meta.get("footer_left") or org, FONT_MEDIUM, 8.2, 0.7),
        (meta.get("footer_right") or meta.get("location", ""), FONT, 7.4, 0.7),
    ]
    y = band_h - 12 * mm
    for text, font, size, tracking in left_items:
        if text:
            draw_tracked(c, str(text).upper(), MARGIN_LEFT, y, font=font,
                         size=size, tracking=tracking, color=rgba(WHITE, 0.92))
            y -= 5.6 * mm

    # Cartouche référence / version / date (côté droit du bandeau)
    fields = []
    if meta.get("reference"):
        fields.append(("Réf.", meta["reference"]))
    if meta.get("version"):
        fields.append(("Version", meta["version"]))
    if meta.get("date"):
        fields.append(("Date", meta["date"]))
    ry = band_h - 10.5 * mm
    for label, value in fields:
        draw_tracked(c, label.upper(), PAGE_WIDTH - MARGIN_RIGHT - 62 * mm, ry,
                     font=FONT_MEDIUM, size=6.4, tracking=0.8,
                     color=rgba(WHITE, 0.55))
        c.setFont(FONT_SEMI, 8)
        c.setFillColor(WHITE)
        c.drawRightString(PAGE_WIDTH - MARGIN_RIGHT, ry - 0.4 * mm, str(value))
        ry -= 6.4 * mm

    c.restoreState()


def _body_background(c, doc):
    """Pages courantes : en-tête (projet / section) et pied de page."""
    meta = getattr(doc, "meta", {})
    section = getattr(c, "_current_section", None)
    if section is None:
        section = meta.get("short_title", "")
    c.saveState()

    # --- En-tête -----------------------------------------------------------
    header_y = PAGE_HEIGHT - 15.5 * mm
    title = meta.get("short_title") or meta.get("title", "")
    draw_tracked(c, str(title).upper(), MARGIN_LEFT, header_y,
                 font=FONT_SEMI, size=7.2, tracking=0.95, color=NAVY)
    if section and section != title:
        c.setFont(FONT, FS_MICRO + 0.2)
        c.setFillColor(MUTED)
        c.drawRightString(PAGE_WIDTH - MARGIN_RIGHT, header_y, section)

    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.line(MARGIN_LEFT, header_y - 3.4 * mm, PAGE_WIDTH - MARGIN_RIGHT,
           header_y - 3.4 * mm)
    # Amorce colorée du filet (accent)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1.8)
    c.line(MARGIN_LEFT, header_y - 3.4 * mm, MARGIN_LEFT + 16 * mm,
           header_y - 3.4 * mm)

    # --- Pied de page ------------------------------------------------------
    footer_y = FOOTER_BASELINE
    c.setStrokeColor(RULE)
    c.setLineWidth(0.7)
    c.line(MARGIN_LEFT, footer_y + 4.6 * mm, PAGE_WIDTH - MARGIN_RIGHT,
           footer_y + 4.6 * mm)

    left = meta.get("footer_left") or meta.get("organization", "")
    if left:
        c.setFont(FONT, FS_MICRO)
        c.setFillColor(MUTED)
        c.drawString(MARGIN_LEFT, footer_y, str(left))

    mid = meta.get("classification")
    if mid:
        draw_tracked(c, str(mid).upper(), MARGIN_LEFT, footer_y,
                     font=FONT_SEMI, size=6.4, tracking=0.85, color=ACCENT,
                     align="center", width=CONTENT_WIDTH)

    ref = meta.get("reference")
    if ref:
        c.setFont(FONT, FS_MICRO)
        c.setFillColor(MUTED)
        # Le folio « Page X / Y » est ajouté par NumberedCanvas (2e passe).
        c.drawRightString(PAGE_WIDTH - MARGIN_RIGHT - 26 * mm, footer_y,
                          str(ref))

    c.restoreState()


# --------------------------------------------------------------------------- #
# Gabarit de document
# --------------------------------------------------------------------------- #


class ProjectDocument(BaseDocTemplate):
    """Document A4 : gabarit « Cover » puis gabarit « Body »."""

    def __init__(self, filename, meta=None, **kwargs):
        self.meta = meta or {}
        BaseDocTemplate.__init__(
            self,
            filename,
            pagesize=(PAGE_WIDTH, PAGE_HEIGHT),
            leftMargin=MARGIN_LEFT,
            rightMargin=MARGIN_RIGHT,
            topMargin=MARGIN_TOP,
            bottomMargin=MARGIN_BOTTOM,
            title=self.meta.get("title", "Présentation de projet"),
            author=self.meta.get("author") or self.meta.get("organization", ""),
            subject=self.meta.get("subtitle", ""),
            creator="Arena — générateur de documents A4",
            **kwargs
        )

        cover_frame = Frame(
            MARGIN_LEFT, 30 * mm + 14 * mm,
            CONTENT_WIDTH, PAGE_HEIGHT - 28 * mm - 44 * mm - 14 * mm,
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
            id="cover",
        )
        body_frame = Frame(
            MARGIN_LEFT, MARGIN_BOTTOM,
            CONTENT_WIDTH, PAGE_HEIGHT - MARGIN_TOP - MARGIN_BOTTOM,
            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
            id="body",
        )

        self.addPageTemplates([
            PageTemplate(id="Cover", frames=[cover_frame],
                         onPage=_cover_background),
            # Le décor des pages courantes est peint *après* le contenu
            # (onPageEnd) afin que l'en-tête affiche la section réellement
            # entamée sur la page, et non celle de la page précédente.
            PageTemplate(id="Body", frames=[body_frame],
                         onPageEnd=_body_background),
        ])
        self._toc_entries = []

    # -- Sommaire -----------------------------------------------------------
    def afterFlowable(self, flowable):
        """Alimente la table des matières (niveau 0 : sections, 1 : sous-titres)."""
        from components import SectionTitle

        if isinstance(flowable, SectionTitle):
            label = flowable.text
            if flowable.number:
                label = "%s \u2002\u2013\u2002 %s" % (flowable.number, flowable.text)
            self.notify("TOCEntry", (0, label, self.page))
        elif isinstance(flowable, Paragraph):
            if flowable.style.name == "h2":
                self.notify("TOCEntry", (1, flowable.getPlainText(), self.page))


class TocHeading(Flowable):
    """Titre « Sommaire » de la page de table des matières."""

    def __init__(self, text="Sommaire"):
        Flowable.__init__(self)
        self.text = text

    def wrap(self, availWidth, availHeight):
        return (availWidth, 22)

    def split(self, availWidth, availHeight):
        return []

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFillColor(NAVY)
        c.setFont(FONT_SEMI, 16)
        c.drawString(0, 6, self.text)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.6)
        c.line(0, 0, availWidth if False else CONTENT_WIDTH, 0)
        c.setFillColor(ACCENT)
        c.rect(0, 0, 16 * mm, 1.6, stroke=0, fill=1)
        c.restoreState()


def build_toc():
    """Table des matières stylée (2 niveaux, points de conduite)."""
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            name="TOC1", fontName=FONT_SEMI, fontSize=9.6, leading=17,
            textColor=NAVY, leftIndent=0, firstLineIndent=0,
            spaceBefore=5, spaceAfter=0,
        ),
        ParagraphStyle(
            name="TOC2", fontName=FONT, fontSize=8.8, leading=14.6,
            textColor=BODY, leftIndent=12, firstLineIndent=0,
            spaceBefore=0, spaceAfter=0,
        ),
    ]
    toc.dotsMinLevel = 0
    return toc


__all__ = [
    "ProjectDocument", "NumberedCanvas", "SetSection", "TocHeading",
    "build_toc", "draw_tracked",
]
