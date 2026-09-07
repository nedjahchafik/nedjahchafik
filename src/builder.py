# -*- coding: utf-8 -*-
"""Assembleur : transforme un dictionnaire de contenu en story reportlab,
puis produit le PDF A4 final.

Point d'entrée : build_pdf(data, output_path)
"""

import os
import re

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    CondPageBreak,
    Flowable,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from components import (
    S,
    AccentBar,
    HRule,
    SectionTitle,
    callout,
    data_table,
    figure,
    gantt,
    kpi_cards,
    paragraph,
    quote,
    rich_bullets,
    rich_numbers,
    severity_legend,
    signature_blocks,
    tag_row,
    timeline,
)
from engine import (
    NumberedCanvas,
    ProjectDocument,
    SetSection,
    TocHeading,
    build_toc,
    draw_tracked,
)
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
    INK,
    MARGIN_LEFT,
    MUTED,
    NAVY,
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
# Flowables spécifiques à la page de garde
# --------------------------------------------------------------------------- #


class TrackedText(Flowable):
    """Ligne de texte en capitales espacées (kicker, libellés de cartouche)."""

    def __init__(self, text, font=FONT_SEMI, size=8, tracking=1.4, color=ACCENT,
                 space_after=2, align="left"):
        Flowable.__init__(self)
        self.text = text or ""
        self.font = font
        self.size = size
        self.tracking = tracking
        self.color = color
        self.space_after = space_after
        self.align = align

    def wrap(self, availWidth, availHeight):
        self._w = availWidth
        chars = list(self.text)
        self._tw = (sum(stringWidth(c, self.font, self.size) for c in chars) +
                    self.tracking * max(0, len(chars) - 1))
        return (availWidth, self.size + self.space_after)

    def split(self, availWidth, availHeight):
        return []

    def draw(self):
        draw_tracked(self.canv, self.text, 0, self.space_after, font=self.font,
                     size=self.size, tracking=self.tracking, color=self.color,
                     align=self.align, width=self._w)


def _cover_title_style():
    return ParagraphStyle(
        "cover_title", fontName=FONT_BOLD, fontSize=29, leading=33.5,
        textColor=NAVY, alignment=0, spaceAfter=0,
    )


def _cover_sub_style():
    return ParagraphStyle(
        "cover_sub", fontName=FONT_LIGHT, fontSize=12.6, leading=17.4,
        textColor=MUTED, alignment=0, spaceAfter=0,
    )


def _cover_abstract_style():
    return ParagraphStyle(
        "cover_abs", fontName=FONT, fontSize=9.4, leading=14.4, textColor=BODY,
        alignment=4, spaceAfter=0,
    )


def meta_grid(rows, cols=2):
    """Cartouche de métadonnées de la page de garde (libellé / valeur)."""
    cells = []
    for chunk_start in range(0, len(rows), cols):
        line = []
        for label, value in rows[chunk_start:chunk_start + cols]:
            block = [
                Paragraph(str(label).upper(), S["kpi_label"]),
                Paragraph(str(value), ParagraphStyle(
                    "mv", fontName=FONT_MEDIUM, fontSize=9.2, leading=12.4,
                    textColor=INK)),
            ]
            line.append(block)
        while len(line) < cols:
            line.append("")
        cells.append(line)

    gap = 8 * mm
    w = (CONTENT_WIDTH - gap * (cols - 1)) / float(cols)
    colw = []
    for i in range(cols):
        colw.append(w)
        if i < cols - 1:
            colw.append(gap)

    # Intercale les gouttières dans les données
    data = []
    for line in cells:
        row = []
        for i, cell in enumerate(line):
            row.append(cell)
            if i < cols - 1:
                row.append("")
        data.append(row)

    tbl = Table(data, colWidths=colw, hAlign="LEFT")
    st = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEABOVE", (0, 0), (-1, 0), 0.7, RULE),
    ]
    tbl.setStyle(TableStyle(st))
    return tbl


# --------------------------------------------------------------------------- #
# Rendu des blocs de contenu
# --------------------------------------------------------------------------- #


def render_block(block):
    """Retourne un flowable ou une liste de flowables pour un bloc donné."""
    kind = block.get("type", "p")

    if kind == "p":
        style = block.get("style", "body")
        return Paragraph(block.get("text", ""), S.get(style, S["body"]))

    if kind == "lead":
        return Paragraph(block.get("text", ""), S["lead"])

    if kind == "h2":
        return Paragraph(block.get("text", ""), S["h2"])

    if kind == "h3":
        return Paragraph(block.get("text", ""), S["h3"])

    if kind == "bullets":
        return rich_bullets(block.get("items", []))

    if kind == "numbers":
        return rich_numbers(block.get("items", []))

    if kind == "callout":
        return callout(kind=block.get("style", block.get("kind", "info")),
                       title=block.get("title"), text=block.get("text"),
                       items=block.get("items"))

    if kind == "kpis":
        return kpi_cards(block.get("items", []), cols=block.get("cols"))

    if kind == "table":
        chips = {}
        for col, mapping in (block.get("chips") or {}).items():
            chips[int(col)] = {str(k).strip().lower(): v
                               for k, v in mapping.items()}
        res = data_table(
            headers=block.get("headers", []),
            rows=block.get("rows", []),
            widths=block.get("widths"),
            aligns=block.get("aligns"),
            caption=block.get("caption"),
            zebra=block.get("zebra", True),
            total_row=block.get("total_row", False),
            chips=chips or None,
            font_size=block.get("font_size", FS_SMALL),
        )
        return res

    if kind == "timeline":
        return timeline(block.get("items", []))

    if kind == "gantt":
        return gantt(block.get("items", []), block.get("months", []))

    if kind == "quote":
        return quote(block.get("text", ""), block.get("author"))

    if kind == "tags":
        return tag_row(block.get("items", []), color=block.get("color", STEEL))

    if kind == "figure":
        return figure(block.get("path"), caption=block.get("caption"))

    if kind == "signatures":
        return signature_blocks(block.get("items", []), cols=block.get("cols"))

    if kind == "rule":
        return HRule(thickness=block.get("thickness", 0.7),
                     color=block.get("color", RULE),
                     space_after=block.get("space_after", 7))

    if kind == "spacer":
        return Spacer(1, block.get("h", 5) * mm)

    if kind == "pagebreak":
        return PageBreak()

    if kind == "keep_with_next":
        return CondPageBreak(block.get("h", 60) * mm)

    if kind == "two_columns":
        left = [render_block(b) for b in block.get("left", [])]
        right = [render_block(b) for b in block.get("right", [])]
        ratio = block.get("ratio", 0.5)
        gap = block.get("gap", 7) * mm
        lw = (CONTENT_WIDTH - gap) * ratio
        rw = (CONTENT_WIDTH - gap) - lw
        tbl = Table([[left, "", right]], colWidths=[lw, gap, rw], hAlign="LEFT")
        tbl.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ]))
        return tbl

    if kind == "risk_legend":
        return KeepTogether([
            TrackedText("Échelle de criticité", font=FONT_SEMI, size=6.8,
                        tracking=0.9, color=MUTED, space_after=4),
            severity_legend(),
            Spacer(1, 9),
        ])

    raise ValueError("Type de bloc inconnu : %r" % kind)


def flatten(items):
    out = []
    for it in items:
        if isinstance(it, (list, tuple)):
            out.extend(flatten(it))
        elif it is not None:
            out.append(it)
    return out


# --------------------------------------------------------------------------- #
# Page de garde
# --------------------------------------------------------------------------- #


def cover_story(meta):
    story = []
    story.append(Spacer(1, 14 * mm))

    kicker = meta.get("kicker", "Présentation officielle de projet")
    if kicker:
        story.append(TrackedText(kicker.upper(), font=FONT_SEMI, size=8.2,
                                 tracking=1.7, color=ACCENT, space_after=3))
        story.append(Spacer(1, 6 * mm))

    title = meta.get("title", "")
    story.append(Paragraph(title, _cover_title_style()))
    story.append(Spacer(1, 4.5 * mm))
    story.append(AccentBar(width=24 * mm, height=2.6, color=ACCENT,
                           space_after=5))

    if meta.get("subtitle"):
        story.append(Paragraph(meta["subtitle"], _cover_sub_style()))
        story.append(Spacer(1, 7 * mm))

    if meta.get("abstract"):
        abs_tbl = Table([[Paragraph(meta["abstract"], _cover_abstract_style())]],
                        colWidths=[CONTENT_WIDTH], hAlign="LEFT")
        abs_tbl.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PANEL),
            ("LINEBEFORE", (0, 0), (0, -1), 2.4, NAVY),
            ("LEFTPADDING", (0, 0), (-1, -1), 11),
            ("RIGHTPADDING", (0, 0), (-1, -1), 11),
            ("TOPPADDING", (0, 0), (-1, -1), 9),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]))
        story.append(Spacer(1, 3 * mm))
        story.append(abs_tbl)

    story.append(Spacer(1, 12 * mm))

    fields = meta.get("cover_fields") or []
    if not fields:
        fields = _default_cover_fields(meta)
    story.append(meta_grid(fields, cols=meta.get("cover_cols", 2)))

    return flatten(story)


def _default_cover_fields(meta):
    fields = []
    mapping = [
        ("Maître d'ouvrage", "client"),
        ("Porteur du projet", "sponsor"),
        ("Chef de projet", "author"),
        ("Direction / Département", "department"),
        ("Date de diffusion", "date"),
        ("Version", "version"),
        ("Référence", "reference"),
        ("Classification", "classification"),
    ]
    for label, key in mapping:
        if meta.get(key):
            fields.append((label, meta[key]))
    return fields


# --------------------------------------------------------------------------- #
# Construction complète
# --------------------------------------------------------------------------- #


def build_story(data):
    meta = data.get("meta", {})
    story = []

    # --- Page de garde -----------------------------------------------------
    story += cover_story(meta)
    story.append(NextPageTemplate("Body"))
    story.append(PageBreak())

    # --- Sommaire ----------------------------------------------------------
    if data.get("toc", True):
        story.append(SetSection(meta.get("toc_title", "Sommaire")))
        story.append(TocHeading(data.get("toc_title", "Sommaire")))
        story.append(Spacer(1, 9))
        story.append(build_toc())
        if data.get("toc_note"):
            story.append(Spacer(1, 8))
            story.append(callout("neutral", None, data["toc_note"]))
        story.append(PageBreak())

    # --- Sections ----------------------------------------------------------
    for i, section in enumerate(data.get("sections", [])):
        if section.get("new_page", True) and i > 0:
            story.append(PageBreak())
        number = section.get("number")
        if number is None:
            number = "%02d" % (i + 1)
        title = section.get("title", "")
        story.append(SetSection("%s  %s" % (number, title) if number else title))
        story.append(SectionTitle(str(number), title))
        story.append(Spacer(1, 4.5 * mm))

        if section.get("intro"):
            story.append(Paragraph(section["intro"], S["lead"]))
            story.append(Spacer(1, 2))

        for block in section.get("blocks", []):
            story.append(render_block(block))

    # --- Page finale (mentions / validation) -------------------------------
    closing = data.get("closing")
    if closing:
        if closing.get("new_page", True):
            story.append(PageBreak())
        story.append(SetSection(closing.get("title", "Validation")))
        story.append(SectionTitle(closing.get("number", ""),
                                  closing.get("title", "Validation")))
        story.append(Spacer(1, 4.5 * mm))
        for block in closing.get("blocks", []):
            story.append(render_block(block))

    return flatten(story)


def build_pdf(data, output_path):
    """Génère le PDF ; renvoie le chemin écrit."""
    register_fonts()
    out_dir = os.path.dirname(os.path.abspath(output_path))
    if out_dir and not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    meta = dict(data.get("meta", {}))
    doc = ProjectDocument(output_path, meta=meta)
    story = build_story(data)

    doc.multiBuild(story, canvasmaker=NumberedCanvas)

    _set_metadata(output_path, meta)
    return output_path


def _set_metadata(path, meta):
    """Renseigne les métadonnées du PDF (titre, auteur, sujet, référence)."""
    try:
        from pypdf import PdfReader, PdfWriter

        reader = PdfReader(path)
        writer = PdfWriter(clone_from=reader)
        title = meta.get("title", "") or ""
        title = re.sub(r"<[^>]+>", " ", title)
        title = re.sub(r"\s+", " ", title).strip()
        if meta.get("subtitle"):
            title = "%s — %s" % (title, meta["subtitle"])
        writer.add_metadata({
            "/Title": title,
            "/Author": meta.get("author") or meta.get("organization", ""),
            "/Subject": meta.get("classification", "") or title,
            "/Keywords": meta.get("reference", ""),
            "/Creator": "Arena — moteur de mise en page A4",
            "/Producer": "ReportLab / moteur de mise en page A4",
        })
        with open(path, "wb") as fh:
            writer.write(fh)
    except Exception as exc:                       # non bloquant
        print("[warn] métadonnées PDF non mises à jour : %s" % exc)


__all__ = ["build_pdf", "build_story", "render_block", "cover_story",
           "meta_grid", "TrackedText"]
