# -*- coding: utf-8 -*-
"""Briques de mise en page réutilisables (flowables reportlab).

Chaque brique est autonome : elle calcule sa hauteur, se dessine et respecte
la charte définie dans theme.py.
"""

import os

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    Flowable,
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from theme import (
    ACCENT,
    BODY,
    CONTENT_WIDTH,
    DANGER,
    FONT,
    FONT_BOLD,
    FONT_ITALIC,
    FONT_LIGHT,
    FONT_MEDIUM,
    FONT_SEMI,
    INFO,
    INK,
    MUTED,
    NAVY,
    PANEL,
    PANEL_ALT,
    RULE,
    RULE_SOFT,
    SEVERITY,
    STATUS,
    STEEL,
    SUCCESS,
    WARNING,
    WHITE,
    FS_BODY,
    FS_H1,
    FS_H2,
    FS_H3,
    FS_MICRO,
    FS_SMALL,
    LEADING_BODY,
    LEADING_SMALL,
    rgba,
)

# --------------------------------------------------------------------------- #
# Styles de paragraphe
# --------------------------------------------------------------------------- #


def _style(name, **kw):
    base = dict(
        fontName=FONT,
        fontSize=FS_BODY,
        leading=LEADING_BODY,
        textColor=BODY,
        alignment=TA_JUSTIFY,
        spaceBefore=0,
        spaceAfter=0,
    )
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "body": _style("body", spaceAfter=6),
    "body_tight": _style("body_tight", spaceAfter=0),
    "lead": _style(
        "lead",
        fontName=FONT_LIGHT,
        fontSize=11.4,
        leading=17.4,
        textColor=INK,
        spaceAfter=8,
    ),
    "bullet": _style("bullet", alignment=TA_LEFT, spaceAfter=3.2),
    "bullet_sub": _style(
        "bullet_sub", alignment=TA_LEFT, fontSize=FS_SMALL, leading=LEADING_SMALL,
        textColor=MUTED, spaceAfter=2,
    ),
    "h2": _style(
        "h2", fontName=FONT_SEMI, fontSize=FS_H2, leading=16, textColor=NAVY,
        alignment=TA_LEFT, spaceBefore=10, spaceAfter=4.5,
    ),
    "h3": _style(
        "h3", fontName=FONT_MEDIUM, fontSize=FS_H3, leading=14, textColor=INK,
        alignment=TA_LEFT, spaceBefore=7, spaceAfter=3,
    ),
    "table_head": _style(
        "table_head", fontName=FONT_SEMI, fontSize=7.8, leading=10.4,
        textColor=WHITE, alignment=TA_LEFT,
    ),
    "table_cell": _style(
        "table_cell", fontName=FONT, fontSize=FS_SMALL, leading=LEADING_SMALL,
        textColor=INK, alignment=TA_LEFT,
    ),
    "table_cell_r": _style(
        "table_cell_r", fontName=FONT, fontSize=FS_SMALL, leading=LEADING_SMALL,
        textColor=INK, alignment=TA_RIGHT,
    ),
    "table_total": _style(
        "table_total", fontName=FONT_SEMI, fontSize=FS_SMALL, leading=LEADING_SMALL,
        textColor=NAVY, alignment=TA_LEFT,
    ),
    "table_total_r": _style(
        "table_total_r", fontName=FONT_SEMI, fontSize=FS_SMALL, leading=LEADING_SMALL,
        textColor=NAVY, alignment=TA_RIGHT,
    ),
    "caption": _style(
        "caption", fontName=FONT_ITALIC, fontSize=FS_MICRO, leading=10,
        textColor=MUTED, alignment=TA_LEFT, spaceBefore=3.5, spaceAfter=8,
    ),
    "callout_title": _style(
        "callout_title", fontName=FONT_SEMI, fontSize=9, leading=12.4,
        textColor=NAVY, alignment=TA_LEFT, spaceAfter=2,
    ),
    "callout_body": _style(
        "callout_body", fontName=FONT, fontSize=FS_SMALL + 0.4, leading=13.4,
        textColor=BODY, alignment=TA_JUSTIFY, spaceAfter=0,
    ),
    "kpi_value": _style(
        "kpi_value", fontName=FONT_BOLD, fontSize=17, leading=20, textColor=NAVY,
        alignment=TA_LEFT,
    ),
    "kpi_label": _style(
        "kpi_label", fontName=FONT_SEMI, fontSize=FS_MICRO, leading=9.6,
        textColor=MUTED, alignment=TA_LEFT, spaceAfter=2.5,
    ),
    "kpi_note": _style(
        "kpi_note", fontName=FONT, fontSize=7.0, leading=9.6, textColor=MUTED,
        alignment=TA_LEFT, spaceBefore=2,
    ),
    "quote": _style(
        "quote", fontName=FONT_LIGHT, fontSize=11, leading=16.5, textColor=NAVY,
        alignment=TA_LEFT,
    ),
    "quote_author": _style(
        "quote_author", fontName=FONT_MEDIUM, fontSize=FS_MICRO, leading=10,
        textColor=MUTED, alignment=TA_LEFT, spaceBefore=5,
    ),
    "tl_date": _style(
        "tl_date", fontName=FONT_SEMI, fontSize=FS_MICRO, leading=10,
        textColor=STEEL, alignment=TA_LEFT,
    ),
    "tl_title": _style(
        "tl_title", fontName=FONT_MEDIUM, fontSize=9.4, leading=12.6,
        textColor=INK, alignment=TA_LEFT, spaceAfter=1,
    ),
    "tl_text": _style(
        "tl_text", fontName=FONT, fontSize=FS_SMALL, leading=LEADING_SMALL,
        textColor=MUTED, alignment=TA_LEFT,
    ),
    "gantt_label": _style(
        "gantt_label", fontName=FONT_MEDIUM, fontSize=7.8, leading=10.4,
        textColor=INK, alignment=TA_LEFT,
    ),
    "gantt_axis": _style(
        "gantt_axis", fontName=FONT, fontSize=6.6, leading=8.6, textColor=MUTED,
        alignment=TA_CENTER,
    ),
}

CALLOUT_COLORS = {
    "info": INFO,
    "success": SUCCESS,
    "warning": WARNING,
    "danger": DANGER,
    "neutral": MUTED,
    "accent": ACCENT,
}


# --------------------------------------------------------------------------- #
# Primitives graphiques
# --------------------------------------------------------------------------- #


class Pill(Flowable):
    """Pastille / étiquette arrondie (statut, niveau de risque, tag)."""

    def __init__(self, text, bg=NAVY, fg=WHITE, font=FONT_SEMI, size=6.9,
                 padx=4.6, pady=2.2, radius=5.6, outline=None):
        Flowable.__init__(self)
        self.text = text
        self.bg = bg
        self.fg = fg
        self.font = font
        self.size = size
        self.padx = padx
        self.pady = pady
        self.radius = radius
        self.outline = outline
        self._w = stringWidth(text, font, size) + 2 * padx
        self._h = size + 2 * pady

    def wrap(self, availWidth, availHeight):
        return (self._w, self._h)

    def draw(self):
        c = self.canv
        c.saveState()
        if self.bg is not None:
            c.setFillColor(self.bg)
            c.roundRect(0, 0, self._w, self._h, self.radius, stroke=0, fill=1)
        if self.outline is not None:
            c.setStrokeColor(self.outline)
            c.setLineWidth(0.6)
            c.roundRect(0, 0, self._w, self._h, self.radius, stroke=1, fill=0)
        c.setFillColor(self.fg)
        c.setFont(self.font, self.size)
        c.drawString(self.padx, self.pady + (self.size * 0.24), self.text)
        c.restoreState()


class HRule(Flowable):
    """Filet horizontal."""

    def __init__(self, width=None, thickness=0.7, color=RULE, space_before=2,
                 space_after=6):
        Flowable.__init__(self)
        self.width = width
        self.thickness = thickness
        self.color = color
        self.space_before = space_before
        self.space_after = space_after

    def wrap(self, availWidth, availHeight):
        self._w = self.width or availWidth
        return (self._w, self.thickness + self.space_before + self.space_after)

    def split(self, availWidth, availHeight):
        return []

    def draw(self):
        self.canv.saveState()
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        y = self.space_after + self.thickness / 2.0
        self.canv.line(0, y, self._w, y)
        self.canv.restoreState()


class SectionTitle(Flowable):
    """Titre de section numéroté : numéro en accent + libellé + filet."""

    def __init__(self, number, text, width=None):
        Flowable.__init__(self)
        self.number = number
        self.text = text
        self.width = width or CONTENT_WIDTH
        self._h = 26

    def wrap(self, availWidth, availHeight):
        self._w = min(self.width, availWidth)
        return (self._w, self._h)

    def split(self, availWidth, availHeight):
        return []

    def draw(self):
        c = self.canv
        c.saveState()
        # Numéro
        c.setFillColor(ACCENT)
        c.setFont(FONT_BOLD, 19)
        c.drawString(0, 8.5, self.number)
        num_w = stringWidth(self.number, FONT_BOLD, 19)
        # Filet vertical séparateur
        x = num_w + 7
        c.setStrokeColor(RULE)
        c.setLineWidth(0.8)
        c.line(x, 4, x, 21)
        # Intitulé
        c.setFillColor(NAVY)
        c.setFont(FONT_SEMI, FS_H1)
        c.drawString(x + 8, 8, self.text)
        # Filet bas
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.6)
        c.line(0, 0, self._w, 0)
        c.restoreState()


class AccentBar(Flowable):
    """Petit rectangle d'accent (décor de titre, séparateur visuel)."""

    def __init__(self, width=18 * mm, height=2.4, color=ACCENT, space_after=6):
        Flowable.__init__(self)
        self._w = width
        self._h = height
        self.color = color
        self.space_after = space_after

    def wrap(self, availWidth, availHeight):
        return (self._w, self._h + self.space_after)

    def split(self, availWidth, availHeight):
        return []

    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(self.color)
        self.canv.rect(0, self.space_after, self._w, self._h, stroke=0, fill=1)
        self.canv.restoreState()


# --------------------------------------------------------------------------- #
# Compositeurs
# --------------------------------------------------------------------------- #


def paragraph(text, style="body"):
    return Paragraph(text, S[style])


def rich_bullets(items, bullet_char="\u2013", indent=9):
    """Liste à puces ; chaque item peut être une chaîne ou un dict
    {"text": ..., "sub": [...]}."""
    flows = []
    for it in items:
        if isinstance(it, dict):
            main = Paragraph(
                it.get("text", ""), S["bullet"]
            )
            flows.append(ListItem(main, leftIndent=indent, value=bullet_char))
            for sub in it.get("sub", []) or []:
                flows.append(
                    ListItem(
                        Paragraph(sub, S["bullet_sub"]),
                        leftIndent=indent + 10,
                        value="\u00b7",
                    )
                )
        else:
            flows.append(ListItem(Paragraph(it, S["bullet"]), leftIndent=indent,
                                  value=bullet_char))
    return ListFlowable(
        flows,
        bulletType="bullet",
        start=bullet_char,
        leftIndent=indent,
        bulletFontName=FONT_MEDIUM,
        bulletFontSize=8.6,
        bulletColor=STEEL,
        bulletOffsetY=-0.4,
        spaceBefore=1,
        spaceAfter=7,
    )


def rich_numbers(items, indent=12):
    flows = [ListItem(Paragraph(it, S["bullet"]), leftIndent=indent)
             for it in items]
    return ListFlowable(
        flows,
        bulletType="1",
        bulletFormat="%s.",
        leftIndent=indent,
        bulletFontName=FONT_SEMI,
        bulletFontSize=8.6,
        bulletColor=NAVY,
        spaceBefore=1,
        spaceAfter=7,
    )


def callout(kind="info", title=None, text=None, items=None):
    """Encadré : filet coloré à gauche, fond panneau, titre + corps."""
    color = CALLOUT_COLORS.get(kind, INFO)
    inner = []
    if title:
        st = ParagraphStyle(
            "co_t", parent=S["callout_title"], textColor=color
        )
        inner.append(Paragraph(title, st))
    if text:
        inner.append(Paragraph(text, S["callout_body"]))
    if items:
        inner.append(Spacer(1, 2))
        inner.append(rich_bullets(items, indent=8))

    tbl = Table([[inner]], colWidths=[CONTENT_WIDTH])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PANEL),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, color),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8.5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return KeepTogether([Spacer(1, 3), tbl, Spacer(1, 8)])


def kpi_cards(items, cols=None):
    """Bandeau d'indicateurs clés (valeur + libellé + note), cartes séparées."""
    n = cols or len(items)
    gap = 3.2 * mm
    card_w = (CONTENT_WIDTH - gap * (n - 1)) / float(n)

    row, colw = [], []
    for i, it in enumerate(items):
        inner = [
            Paragraph(str(it.get("label", "")).upper(), S["kpi_label"]),
            Paragraph(str(it.get("value", "")), S["kpi_value"]),
        ]
        if it.get("note"):
            inner.append(Paragraph(it["note"], S["kpi_note"]))
        row.append(inner)
        colw.append(card_w)
        if i < n - 1:
            row.append("")
            colw.append(gap)

    tbl = Table([row], colWidths=colw, hAlign="LEFT")
    st = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]
    for i in range(n):
        col = 2 * i
        st += [
            ("BACKGROUND", (col, 0), (col, 0), PANEL),
            ("LINEABOVE", (col, 0), (col, 0), 2.2, NAVY),
            ("LEFTPADDING", (col, 0), (col, 0), 9),
            ("RIGHTPADDING", (col, 0), (col, 0), 9),
            ("TOPPADDING", (col, 0), (col, 0), 8),
            ("BOTTOMPADDING", (col, 0), (col, 0), 9),
        ]
    tbl.setStyle(TableStyle(st))
    return KeepTogether([Spacer(1, 2), tbl, Spacer(1, 9)])


def data_table(headers, rows, widths=None, aligns=None, caption=None,
               zebra=True, total_row=False, chips=None, header_bg=NAVY,
               font_size=FS_SMALL):
    """Tableau institutionnel : en-tête navy répété, zébrage, filets discrets.

    chips : dict {index_colonne: {"valeur": couleur}} → pastilles colorées.
    total_row : la dernière ligne est mise en forme comme un total.
    """
    aligns = aligns or ["left"] * len(headers)
    widths = widths or [CONTENT_WIDTH / float(len(headers))] * len(headers)
    scale = CONTENT_WIDTH / float(sum(widths))
    widths = [w * scale for w in widths]

    data = [[Paragraph(str(h).upper(), S["table_head"]) for h in headers]]
    body_rows = rows[:]
    total = None
    if total_row and body_rows:
        total = body_rows.pop()

    for r, row in enumerate(body_rows):
        line = []
        for c, val in enumerate(row):
            chip_color = None
            if chips and c in chips and isinstance(val, str):
                chip_color = chips[c].get(val.strip().lower())
            if chip_color is not None:
                line.append(Pill(val, bg=rgba(chip_color, 0.12), fg=chip_color,
                                 outline=rgba(chip_color, 0.45), size=6.8))
            else:
                style = "table_cell_r" if aligns[c] == "right" else (
                    "table_cell" if aligns[c] != "center" else "table_cell")
                st = ParagraphStyle(
                    "tc_%d_%d" % (r, c), parent=S[style], fontSize=font_size,
                    alignment=TA_RIGHT if aligns[c] == "right" else (
                        TA_CENTER if aligns[c] == "center" else TA_LEFT),
                )
                line.append(Paragraph(str(val), st))
        data.append(line)

    if total is not None:
        line = []
        for c, val in enumerate(total):
            key = "table_total_r" if aligns[c] == "right" else "table_total"
            line.append(Paragraph(str(val), S[key]))
        data.append(line)

    st = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, 0), 6.5),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6.5),
        ("TOPPADDING", (0, 1), (-1, -1), 5.6),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5.6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, RULE_SOFT),
        ("LINEBELOW", (0, -1), (-1, -1), 0.9, NAVY),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, NAVY),
    ]
    if zebra:
        for r in range(1, len(data) - (1 if total is not None else 0)):
            if r % 2 == 0:
                st.append(("BACKGROUND", (0, r), (-1, r), PANEL_ALT))
    if total is not None:
        st.append(("BACKGROUND", (0, len(data) - 1), (-1, len(data) - 1), PANEL))
        st.append(("LINEABOVE", (0, len(data) - 1), (-1, len(data) - 1), 0.9, NAVY))

    tbl = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    tbl.setStyle(TableStyle(st))

    out = [Spacer(1, 2), tbl]
    if caption:
        out.append(Paragraph(caption, S["caption"]))
    else:
        out.append(Spacer(1, 9))
    return KeepTogether(out) if len(rows) <= 8 else _keep_header(tbl, out, caption)


def _keep_header(tbl, out, caption):
    """Pour les tableaux longs : on laisse reportlab paginer (en-tête répété)."""
    flows = [Spacer(1, 2), tbl]
    if caption:
        flows.append(Paragraph(caption, S["caption"]))
    else:
        flows.append(Spacer(1, 9))
    return flows


class TimelineFlow(Flowable):
    """Frise chronologique verticale mesurée précisément.

    Colonnes : [date + pastille de statut] [rail + point] [titre + texte].
    Le rail et les points sont alignés sur la première ligne de chaque jalon,
    quelle que soit la hauteur réelle des paragraphes.
    """

    DATE_W = 26 * mm
    RAIL_W = 10 * mm
    PAD = 4.0            # respiration verticale autour de chaque jalon
    DOT_R = 3.2

    def __init__(self, items, first_index=0, last_index=None):
        Flowable.__init__(self)
        self.all_items = items
        self.first_index = first_index
        self.last_index = last_index if last_index is not None \
            else len(items) - 1
        self.items = items[self.first_index:self.last_index + 1]
        self._rows = None

    # -- mesure -------------------------------------------------------------
    def _prepare(self, availWidth):
        text_w = availWidth - self.DATE_W - self.RAIL_W
        rows = []
        for idx, it in enumerate(self.items):
            status = (it.get("status") or "").strip().lower()
            color = STATUS.get(status, STEEL)
            date_p = Paragraph(str(it.get("date", "")), S["tl_date"])
            _, date_h = date_p.wrap(self.DATE_W, 10000)
            pill = None
            if status:
                pill = Pill(status.capitalize(), bg=rgba(color, 0.12),
                            fg=color, outline=rgba(color, 0.4), size=6.4)
                pill.wrap(availWidth, 10000)
            left_h = date_h + (pill._h + 3.5 if pill else 0)

            title_p = Paragraph(str(it.get("title", "")), S["tl_title"])
            _, title_h = title_p.wrap(text_w, 10000)
            text_p = None
            text_h = 0
            if it.get("text"):
                text_p = Paragraph(it["text"], S["tl_text"])
                _, text_h = text_p.wrap(text_w, 10000)
                text_h += 1.5
            right_h = title_h + text_h

            rows.append({
                "date_p": date_p, "date_h": date_h, "pill": pill,
                "color": color, "title_p": title_p, "title_h": title_h,
                "text_p": text_p, "text_h": text_h,
                "h": max(left_h, right_h, 14) + 2 * self.PAD,
            })
        self._text_w = text_w
        return rows

    def wrap(self, availWidth, availHeight):
        self._rows = self._prepare(availWidth)
        self._w = availWidth
        self._h = sum(r["h"] for r in self._rows)
        return (self._w, self._h)

    def split(self, availWidth, availHeight):
        if self._rows is None:
            self.wrap(availWidth, availHeight)
        # Nombre de jalons qui tiennent dans la hauteur disponible.
        acc, count = 0.0, 0
        for r in self._rows:
            if acc + r["h"] > availHeight and count > 0:
                break
            acc += r["h"]
            count += 1
        if count <= 0 or count >= len(self.items):
            return []
        head = TimelineFlow(self.all_items, self.first_index,
                            self.first_index + count - 1)
        tail = TimelineFlow(self.all_items, self.first_index + count,
                            self.last_index)
        return [head, tail]

    # -- dessin -------------------------------------------------------------
    def draw(self):
        if self._rows is None:
            self.wrap(self._w, 10000)
        c = self.canv
        c.saveState()
        rail_x = self.DATE_W + self.RAIL_W / 2.0 - 1.0
        text_x = self.DATE_W + self.RAIL_W
        y = self._h                                   # bord haut

        for i, r in enumerate(self._rows):
            top = y
            bottom = y - r["h"]
            dot_y = top - self.PAD - 4.6

            # rail vertical (segments au-dessus / au-dessous du point)
            c.setStrokeColor(RULE)
            c.setLineWidth(1.15)
            if i > 0 or self.first_index > 0:
                c.line(rail_x, top, rail_x, dot_y + self.DOT_R + 1.6)
            if i < len(self._rows) - 1 or self.last_index < len(self.all_items) - 1:
                c.line(rail_x, dot_y - self.DOT_R - 1.6, rail_x, bottom)

            # point
            c.setFillColor(WHITE)
            c.setStrokeColor(r["color"])
            c.setLineWidth(1.5)
            c.circle(rail_x, dot_y, self.DOT_R, stroke=1, fill=1)
            c.setFillColor(r["color"])
            c.circle(rail_x, dot_y, 1.45, stroke=0, fill=1)

            # colonne gauche : date puis pastille de statut
            r["date_p"].drawOn(c, 0, top - self.PAD - r["date_h"])
            if r["pill"] is not None:
                r["pill"].drawOn(c, 0,
                                 top - self.PAD - r["date_h"] - 3.5 -
                                 r["pill"]._h)

            # colonne droite : titre puis description
            r["title_p"].drawOn(c, text_x, top - self.PAD - r["title_h"])
            if r["text_p"] is not None:
                r["text_p"].drawOn(c, text_x,
                                   top - self.PAD - r["title_h"] - 1.5 -
                                   r["text_h"] + 1.5)
            y = bottom

        c.restoreState()


def timeline(items):
    """Frise verticale : jalon, date, description, statut."""
    return KeepTogether([Spacer(1, 2), TimelineFlow(items), Spacer(1, 7)]) \
        if len(items) <= 4 else \
        [Spacer(1, 2), TimelineFlow(items), Spacer(1, 7)]


def gantt(items, months, width=None):
    """Diagramme de Gantt simplifié : une ligne par lot, barres colorées.

    months : liste de libellés de colonnes (ex. ["T1", "T2", "T3", "T4"]).
    items  : [{"label", "start", "end", "status"}] — start/end = index de
             colonne (0-based, end exclusif accepté comme index de fin).
    """
    width = width or CONTENT_WIDTH
    label_w = 46 * mm
    n = len(months)
    grid_w = width - label_w
    col_w = grid_w / float(n)
    row_h = 8.6 * mm

    header = [Paragraph("", S["gantt_label"])]
    for m in months:
        header.append(Paragraph(str(m).upper(), S["gantt_axis"]))

    data = [header]
    styles = [
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, NAVY),
        ("TOPPADDING", (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
        ("LEFTPADDING", (0, 1), (0, -1), 0),
    ]
    for c in range(1, n + 1):
        styles.append(("LINEBEFORE", (c, 1), (c, -1), 0.35, RULE_SOFT))
    styles.append(("LINEAFTER", (n, 1), (n, -1), 0.35, RULE_SOFT))

    for i, it in enumerate(items, start=1):
        data.append([Paragraph(str(it.get("label", "")), S["gantt_label"])] +
                    [""] * n)
        color = STATUS.get((it.get("status") or "").strip().lower(), STEEL)
        s = int(it.get("start", 0))
        e = int(it.get("end", s + 1))
        styles.append(("SPAN", (1 + s, i), (min(e, n), i)))
        styles.append(("BACKGROUND", (1 + s, i), (min(e, n), i), color))
        styles.append(("TOPPADDING", (1 + s, i), (min(e, n), i), 5.2))
        styles.append(("BOTTOMPADDING", (1 + s, i), (min(e, n), i), 5.2))
        if i % 2 == 0:
            for c in range(0, n + 1):
                if not (1 + s <= c <= min(e, n)):
                    styles.append(("BACKGROUND", (c, i), (c, i), PANEL_ALT))

    tbl = Table(data, colWidths=[label_w] + [col_w] * n, rowHeights=[7 * mm] +
                [row_h] * len(items), hAlign="LEFT")
    tbl.setStyle(TableStyle(styles))
    return KeepTogether([Spacer(1, 2), tbl, Spacer(1, 9)])


def quote(text, author=None):
    inner = [Paragraph("\u201c%s\u201d" % text, S["quote"])]
    if author:
        inner.append(Paragraph(author, S["quote_author"]))
    tbl = Table([[inner]], colWidths=[CONTENT_WIDTH])
    tbl.setStyle(TableStyle([
        ("LINEBEFORE", (0, 0), (0, -1), 2, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return KeepTogether([Spacer(1, 3), tbl, Spacer(1, 9)])


def two_columns(left_blocks, right_blocks, ratio=0.5, gap=7 * mm):
    lw = (CONTENT_WIDTH - gap) * ratio
    rw = (CONTENT_WIDTH - gap) - lw
    tbl = Table([[left_blocks, right_blocks]], colWidths=[lw, gap, rw],
                hAlign="LEFT")
    tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("SPAN", (1, 0), (1, 0)),
    ]))
    # La colonne du milieu sert uniquement de gouttière.
    tbl._argW = [lw, gap, rw]
    tbl._ncols = 3
    return tbl


def figure(path, caption=None, max_width=None, max_height=95 * mm):
    max_width = max_width or CONTENT_WIDTH
    if not os.path.exists(path):
        return callout("warning", "Visuel indisponible",
                       "Fichier introuvable : %s" % os.path.basename(path))
    img = Image(path)
    iw, ih = img.imageWidth, img.imageHeight
    scale = min(max_width / float(iw), max_height / float(ih))
    img.drawWidth = iw * scale
    img.drawHeight = ih * scale
    img.hAlign = "CENTER"
    out = [Spacer(1, 3), img]
    if caption:
        out.append(Paragraph(caption, S["caption"]))
    else:
        out.append(Spacer(1, 8))
    return KeepTogether(out)


def signature_blocks(items, cols=None):
    """Cartouches de signature (validation officielle)."""
    n = cols or len(items)
    gap = 5 * mm
    w = (CONTENT_WIDTH - gap * (n - 1)) / float(n)
    cells = []
    for it in items:
        inner = [
            Paragraph(str(it.get("role", "")).upper(), S["kpi_label"]),
            Paragraph(str(it.get("name", "")).replace("\n", "<br/>"),
                      S["tl_title"]),
            Spacer(1, 15 * mm),
            Paragraph("Date et signature", S["kpi_note"]),
        ]
        cells.append(inner)
    tbl = Table([cells], colWidths=[w] * n, hAlign="LEFT")
    tbl.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.6, RULE),
        ("INNERGRID", (0, 0), (-1, -1), 0.6, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("BACKGROUND", (0, 0), (-1, -1), WHITE),
    ]))
    return KeepTogether([Spacer(1, 4), tbl, Spacer(1, 8)])


def tag_row(items, color=STEEL):
    pills = [Pill(t, bg=rgba(color, 0.10), fg=color, outline=rgba(color, 0.35),
                  size=7) for t in items]
    # Disposition en une ligne, avec retour géré par un tableau dynamique.
    widths = [p._w + 3 for p in pills]
    total = sum(widths)
    if total <= CONTENT_WIDTH:
        tbl = Table([pills], colWidths=widths, hAlign="LEFT")
        tbl.setStyle(TableStyle([
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))
        return KeepTogether([Spacer(1, 2), tbl, Spacer(1, 9)])
    return KeepTogether([Spacer(1, 2)] + pills + [Spacer(1, 9)])


def severity_legend(mapping=None):
    mapping = mapping or SEVERITY
    pills = [Pill(k.capitalize(), bg=rgba(v, 0.12), fg=v, outline=rgba(v, 0.45),
                  size=6.8) for k, v in mapping.items()]
    widths = [p._w + 8 for p in pills]
    tbl = Table([pills], colWidths=widths, hAlign="LEFT")
    tbl.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return tbl


__all__ = [
    "S", "Pill", "HRule", "SectionTitle", "AccentBar", "paragraph",
    "rich_bullets", "rich_numbers", "callout", "kpi_cards", "data_table",
    "timeline", "gantt", "quote", "two_columns", "figure",
    "signature_blocks", "tag_row", "severity_legend",
    "Paragraph", "Spacer", "PageBreak", "KeepTogether", "Table", "TableStyle",
]
