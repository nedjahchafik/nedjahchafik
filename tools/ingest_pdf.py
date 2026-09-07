#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyse un PDF source déposé dans sources/ et en extrait la matière première.

Produit, dans sources/extract/<nom>/ :
    page-NN.png        rendu de chaque page (150 dpi) — pour lecture visuelle
    page-NN.txt        texte brut de chaque page
    img-NN-MM.png      images embarquées (logos, photos…)
    analyse.md         synthèse : géométrie, polices, hiérarchie typographique,
                       blocs détectés (titres, listes, tableaux approximatifs)

Usage :
    python3 tools/ingest_pdf.py [chemin/vers/fichier.pdf]
    (sans argument : prend le premier PDF trouvé dans sources/)
"""

import glob
import os
import re
import sys

import fitz  # PyMuPDF

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SOURCES = os.path.join(ROOT, "sources")


def pick_pdf(arg=None):
    if arg:
        return arg
    cands = sorted(glob.glob(os.path.join(SOURCES, "*.pdf")))
    cands += sorted(glob.glob(os.path.join(SOURCES, "**", "*.pdf"),
                              recursive=True))
    if not cands:
        sys.exit("[erreur] aucun PDF dans sources/ — déposez-le d'abord.")
    return cands[0]


def main():
    path = pick_pdf(sys.argv[1] if len(sys.argv) > 1 else None)
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", os.path.splitext(
        os.path.basename(path))[0])
    out = os.path.join(SOURCES, "extract", name)
    os.makedirs(out, exist_ok=True)

    doc = fitz.open(path)
    lines = []
    lines.append("# Analyse de `%s`" % os.path.basename(path))
    lines.append("")
    lines.append("- Pages : %d" % len(doc))
    lines.append("- Métadonnées : %s" % {k: v for k, v in doc.metadata.items()
                                         if v})
    lines.append("")

    for i, page in enumerate(doc, start=1):
        rect = page.rect
        lines.append("## Page %d — %.0f × %.0f pt (%.0f × %.0f mm)" % (
            i, rect.width, rect.height, rect.width / 72 * 25.4,
            rect.height / 72 * 25.4))
        lines.append("")

        # rendu visuel
        pix = page.get_pixmap(dpi=150)
        pix.save(os.path.join(out, "page-%02d.png" % i))

        # texte
        text = page.get_text("text")
        with open(os.path.join(out, "page-%02d.txt" % i), "w",
                  encoding="utf-8") as fh:
            fh.write(text)

        # hiérarchie typographique (tailles de police)
        sizes = {}
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    txt = span["text"].strip()
                    if not txt:
                        continue
                    key = (round(span["size"], 1), span["font"])
                    sizes.setdefault(key, []).append(txt)
        if sizes:
            lines.append("### Hiérarchie typographique")
            lines.append("")
            for (size, font), texts in sorted(sizes.items(), reverse=True)[:8]:
                sample = " | ".join(t[:40] for t in texts[:3])
                lines.append("- **%.1f pt** `%s` : %s" % (size, font, sample))
            lines.append("")

        # images embarquées
        imgs = page.get_images(full=True)
        if imgs:
            lines.append("### Images embarquées : %d" % len(imgs))
            lines.append("")
            for j, img in enumerate(imgs, start=1):
                xref = img[0]
                try:
                    base = doc.extract_image(xref)
                    ext = base["ext"]
                    fn = "img-%02d-%02d.%s" % (i, j, ext)
                    with open(os.path.join(out, fn), "wb") as fh:
                        fh.write(base["image"])
                    lines.append("- `%s` (%d × %d, %d Ko)" % (
                        fn, base["width"], base["height"],
                        len(base["image"]) // 1024))
                except Exception as exc:
                    lines.append("- image %d illisible : %s" % (j, exc))
            lines.append("")

        # texte brut (extrait)
        lines.append("### Texte brut")
        lines.append("")
        lines.append("```")
        lines.append(text.strip() or "(aucun texte — page probablement "
                                     "matérielle/scannée)")
        lines.append("```")
        lines.append("")

    report = os.path.join(out, "analyse.md")
    with open(report, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    doc.close()
    print("[ok] extraction terminée : %s" % out)
    print("[ok] rapport : %s" % report)


if __name__ == "__main__":
    main()
