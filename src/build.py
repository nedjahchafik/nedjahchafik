#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Point d'entrée : génère le PDF A4 à partir d'un module de contenu.

Usage :
    python src/build.py                          # utilise src/content.py
    python src/build.py -c content_demo          # module src/content_demo.py
    python src/build.py -o build/mon-doc.pdf     # chemin de sortie explicite
"""

import argparse
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from builder import build_pdf          # noqa: E402


def slugify(text):
    import re as _re
    import unicodedata
    text = _re.sub(r"<[^>]+>", " ", text or "")      # retire les balises HTML
    text = _re.sub(r"\s+", " ", text).strip()
    # translittère les accents (nom de fichier ASCII sûr)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    out = []
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_":
            out.append("-")
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "document"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Générateur de présentation A4")
    ap.add_argument("-c", "--content", default="content",
                    help="module Python (dans src/) contenant DOCUMENT")
    ap.add_argument("-o", "--output", default=None,
                    help="chemin du PDF de sortie")
    ap.add_argument("--preview", action="store_true",
                    help="exporte aussi un aperçu PNG de chaque page")
    args = ap.parse_args(argv)

    module = importlib.import_module(args.content)
    data = module.DOCUMENT

    if args.output:
        out = args.output
    else:
        name = slugify(data.get("meta", {}).get("title", "document"))
        out = os.path.join(ROOT, "livrables", "%s.pdf" % name)

    build_pdf(data, out)
    size_kb = os.path.getsize(out) / 1024.0
    print("[ok] PDF généré : %s (%.0f Ko)" % (out, size_kb))

    if args.preview:
        try:
            import fitz                       # PyMuPDF

            prev_dir = os.path.join(os.path.dirname(out), "apercus")
            os.makedirs(prev_dir, exist_ok=True)
            doc = fitz.open(out)
            for i, page in enumerate(doc, start=1):
                pix = page.get_pixmap(dpi=110)
                p = os.path.join(prev_dir, "page-%02d.png" % i)
                pix.save(p)
            print("[ok] aperçus PNG : %s (%d pages)" % (prev_dir, len(doc)))
            doc.close()
        except Exception as exc:
            print("[warn] aperçu indisponible : %s" % exc)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
