#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Régénère assets/fonts/ (famille Inter) depuis le paquet npm @fontsource/inter.

Usage :
    cd tools && npm install @fontsource/inter     # une seule fois
    python3 fetch_fonts.py

Les woff2 sont décompressés en TTF via fontTools (+ brotli).
"""

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = HERE
FONTS_OUT = os.path.join(os.path.dirname(TOOLS), "assets", "fonts")

WANTED = {
    "inter-latin-300-normal.woff2": "Inter-Light.ttf",
    "inter-latin-400-normal.woff2": "Inter-Regular.ttf",
    "inter-latin-400-italic.woff2": "Inter-Italic.ttf",
    "inter-latin-500-normal.woff2": "Inter-Medium.ttf",
    "inter-latin-600-normal.woff2": "Inter-SemiBold.ttf",
    "inter-latin-700-normal.woff2": "Inter-Bold.ttf",
}


def main():
    src = os.path.join(TOOLS, "node_modules", "@fontsource", "inter", "files")
    if not os.path.isdir(src):
        print("[info] installation de @fontsource/inter …")
        subprocess.check_call(["npm", "install", "--silent",
                               "@fontsource/inter"], cwd=TOOLS)
    os.makedirs(FONTS_OUT, exist_ok=True)

    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        print("[erreur] fontTools manquant : pip install fonttools brotli")
        return 1

    for woff, ttf in WANTED.items():
        path = os.path.join(src, woff)
        if not os.path.exists(path):
            print("[warn] absent : %s" % woff)
            continue
        font = TTFont(path)
        font.flavor = None
        out = os.path.join(FONTS_OUT, ttf)
        font.save(out)
        print("[ok] %s (%d Ko)" % (ttf, os.path.getsize(out) // 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
