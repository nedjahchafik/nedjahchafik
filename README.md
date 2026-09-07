# nedjahchafik

Moteur de mise en page **A4** pour présentations officielles de projet :
à partir d'un contenu structuré (dictionnaire Python), il produit un PDF
institutionnel complet — page de garde, sommaire paginé, sections numérotées,
tableaux, encadrés, indicateurs, Gantt, frise de jalons, registre des risques
et page de signatures.

## Rendu

Charte « corporate sobre » : marine `#14243D`, accent or vieilli `#B08A3E`,
typographie **Inter** (graisses 300 → 700, embarquée dans le PDF), format A4
portrait, en-têtes et pieds de page avec folio « Page X / Y ».

## Structure

```
assets/fonts/     polices Inter (TTF, générées par tools/fetch_fonts.py)
src/theme.py      charte graphique : couleurs, géométrie de page, typographie
src/fonts.py      enregistrement des polices auprès de reportlab
src/components.py briques de mise en page (encadrés, tableaux, Gantt, frise…)
src/engine.py     gabarits A4 : page de garde, en-têtes/pieds, sommaire, folios
src/builder.py    assembleur contenu → story → PDF (+ métadonnées)
src/content.py    ◀ CONTENU DU DOCUMENT (à remplacer par le contenu réel)
src/content_demo.py  contenu de démonstration / modèle de référence
src/build.py      point d'entrée en ligne de commande
tools/            régénération des polices
livrables/        sorties PDF + aperçus PNG de contrôle — non versionné
```

## Utilisation

```bash
# dépendances (environnement virtuel recommandé)
pip install reportlab fonttools brotli pillow pypdf pymupdf

# génération du PDF (+ aperçus PNG de contrôle)
python src/build.py                     # utilise src/content.py
python src/build.py -c content_demo     # module de contenu alternatif
python src/build.py -o livrables/doc.pdf --preview
```

## Ajouter / modifier le contenu

Tout le document est décrit par le dictionnaire `DOCUMENT` d'un module de
contenu :

- `meta` : kicker, titre, sous-titre, résumé, organisation, auteur, date,
  version, référence, classification, pieds de page, logo optionnel ;
- `sections` : liste de sections numérotées, chacune avec `intro` et `blocks` ;
- `closing` : page finale de validation / signatures.

Blocs disponibles dans `blocks` : `p`, `lead`, `h2`, `h3`, `bullets`,
`numbers`, `callout`, `kpis`, `table` (avec pastilles de statut et ligne de
total), `timeline`, `gantt`, `quote`, `tags`, `two_columns`, `figure`,
`signatures`, `risk_legend`, `rule`, `spacer`, `pagebreak`.

Le schéma détaillé, avec exemples, est commenté en fin de
`src/content_demo.py`.

## Polices

Les TTF Inter sont versionnés dans `assets/fonts/`. Pour les régénérer :

```bash
cd tools && npm install @fontsource/inter
python3 fetch_fonts.py
```
