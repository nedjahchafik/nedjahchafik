# -*- coding: utf-8 -*-
"""Contenu de DÉMONSTRATION — sert de modèle de mise en page.

Ce fichier illustre toutes les briques disponibles (encadrés, indicateurs,
tableaux, frise, Gantt, signatures…). Remplacez-le par le contenu réel du
document à mettre en page, ou dupliquez-le vers src/content.py.

Le schéma de données est documenté en fin de fichier.
"""

from theme import DANGER, SEVERITY, STATUS, SUCCESS, WARNING, STEEL

DOCUMENT = {
    "meta": {
        "kicker": "Présentation officielle de projet",
        "title": "Programme de modernisation<br/>des services numériques",
        "subtitle": "Refonte du socle applicatif et dématérialisation "
                    "des procédures usagers",
        "abstract":
            "Ce document présente les objectifs, le périmètre, la gouvernance, "
            "le calendrier et l'enveloppe budgétaire du programme de "
            "modernisation des services numériques, soumis à validation du "
            "comité de pilotage pour la période 2026-2027.",
        "organization": "Direction des Systèmes d'Information",
        "department": "Pôle Transformation & Innovation",
        "client": "Comité de direction générale",
        "sponsor": "Direction générale",
        "author": "Nedjah Chafik",
        "location": "Oran, Algérie",
        "date": "7 septembre 2026",
        "version": "1.0",
        "reference": "DSI-PRO-2026-014",
        "classification": "Diffusion restreinte",
        "short_title": "Modernisation des services numériques",
        "footer_left": "Direction des Systèmes d'Information",
        "footer_right": "Oran — Algérie",
        "toc_title": "Sommaire",
        "toc_note": None,
    },

    "toc": True,

    "sections": [
        # ------------------------------------------------------------------ #
        {
            "number": "01",
            "title": "Résumé exécutif",
            "intro":
                "Le programme vise à remplacer un socle applicatif vieillissant "
                "par une plateforme modulaire, à dématérialiser les principales "
                "procédures usagers et à fiabiliser la donnée de pilotage, pour "
                "un budget maîtrisé de 4,85 M€ sur vingt mois.",
            "blocks": [
                {"type": "kpis", "items": [
                    {"label": "Budget global", "value": "4,85 M€",
                     "note": "dont 12 % de provision pour aléas"},
                    {"label": "Durée", "value": "20 mois",
                     "note": "janvier 2026 → août 2027"},
                    {"label": "Procédures dématérialisées", "value": "18",
                     "note": "sur 24 procédures cibles"},
                    {"label": "Gain de délai attendu", "value": "−42 %",
                     "note": "traitement moyen des dossiers"},
                ]},
                {"type": "p", "text":
                    "Trois enjeux structurent l'intervention : la "
                    "<b>continuité de service</b> pendant la migration, "
                    "l'<b>adhésion des agents</b> aux nouveaux outils et la "
                    "<b>maîtrise des coûts</b> dans un contexte de tension sur "
                    "les ressources internes. Le programme est découpé en cinq "
                    "lots autonomes, chacun livré avec ses critères "
                    "d'acceptation et sa revue de qualité."},
                {"type": "callout", "style": "success",
                 "title": "Décision attendue du comité de pilotage",
                 "text":
                     "Validation du périmètre du lot 3 (dématérialisation des "
                     "procédures usagers) et déblocage de la première tranche "
                     "de financement, soit 1,20 M€ au titre de l'exercice 2026."},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "02",
            "title": "Contexte et enjeux",
            "blocks": [
                {"type": "p", "text":
                    "Le système d'information historique repose sur des "
                    "applications développées entre 2004 et 2011, sans "
                    "documentation exploitable et avec une couverture de tests "
                    "inférieure à 20 %. Chaque évolution corrective mobilise en "
                    "moyenne onze jours ouvrés, contre trois jours pour les "
                    "référentiels du marché."},
                {"type": "h2", "text": "Diagnostic partagé"},
                {"type": "bullets", "items": [
                    {"text": "<b>Dette technique</b> estimée à 1 400 jours-hommes "
                             "de remise à niveau",
                     "sub": ["Obsolescence de deux socles middleware",
                             "Absence d'annuaire de services transversal"]},
                    "<b>Parcours usagers fragmentés</b> : 62 % des dossiers "
                    "nécessitent une ressaisie manuelle",
                    "<b>Pilotage limité</b> : les indicateurs de performance "
                    "sont produits manuellement, avec un délai de consolidation "
                    "de quinze jours",
                    "<b>Conformité</b> : mise à niveau requise au regard de la "
                    "réglementation sur la protection des données personnelles",
                ]},
                {"type": "quote",
                 "text": "La modernisation n'est pas un projet informatique : "
                         "c'est la condition de la continuité du service rendu "
                         "à l'usager dans les cinq prochaines années.",
                 "author": "Note de cadrage de la direction générale, mars 2026"},
                {"type": "h2", "text": "Opportunités identifiées"},
                {"type": "numbers", "items": [
                    "Mutualiser les briques communes (authentification, "
                    "gestion documentaire, notifications) entre six directions.",
                    "Réduire de 38 % le coût de maintenance corrective annuel.",
                    "Ouvrir un portail usagers unique, accessible sur mobile.",
                    "Fiabiliser la donnée de pilotage par un référentiel unique.",
                ]},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "03",
            "title": "Objectifs et livrables",
            "blocks": [
                {"type": "p", "text":
                    "Les objectifs sont formulés selon le principe SMART et "
                    "rattachés à un indicateur de résultat mesurable à la "
                    "recette de chaque lot."},
                {"type": "table",
                 "caption": "Tableau 1 — Objectifs, livrables associés et critères "
                            "d'acceptation.",
                 "headers": ["Objectif", "Livrable principal",
                             "Indicateur de résultat", "Échéance"],
                 "widths": [30, 26, 30, 14],
                 "aligns": ["left", "left", "left", "center"],
                 "rows": [
                     ["Sécuriser le socle", "Plateforme modulaire v1",
                      "Disponibilité ≥ 99,5 %", "T2 2026"],
                     ["Unifier l'accès", "SSO et annuaire unique",
                      "100 % des agents fédérés", "T3 2026"],
                     ["Dématérialiser", "Portail usagers",
                      "18 procédures en ligne", "T1 2027"],
                     ["Fiabiliser la donnée", "Entrepôt de pilotage",
                      "Consolidation ≤ 24 h", "T2 2027"],
                     ["Accompagner le changement", "Dispositif de formation",
                      "≥ 90 % des agents formés", "T3 2027"],
                 ]},
                {"type": "callout", "style": "info",
                 "title": "Hors périmètre",
                 "items": [
                     "Renouvellement du parc matériel des agences",
                     "Refonte du système de paie et de la gestion des ressources "
                     "humaines",
                     "Migration des archives antérieures à 2010",
                 ]},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "04",
            "title": "Périmètre et architecture cible",
            "blocks": [
                {"type": "two_columns", "ratio": 0.5,
                 "left": [
                     {"type": "h2", "text": "Périmètre fonctionnel"},
                     {"type": "bullets", "items": [
                         "Gestion de la relation usagers",
                         "Instruction administrative des dossiers",
                         "Gestion électronique documentaire",
                         "Pilotage et tableaux de bord",
                         "Portail self-service et notifications",
                     ]},
                 ],
                 "right": [
                     {"type": "h2", "text": "Principes d'architecture"},
                     {"type": "bullets", "items": [
                         "Services modulaires à API contractuelle",
                         "Authentification fédérée et habilitations fines",
                         "Réversibilité et absence de verrou propriétaire",
                         "Exploitation en environnement souverain",
                         "Journalisation et traçabilité complètes",
                     ]},
                 ]},
                {"type": "spacer", "h": 2},
                {"type": "h2", "text": "Lots du programme"},
                {"type": "tags", "items": [
                    "Lot 1 — Socle technique", "Lot 2 — Identité",
                    "Lot 3 — Portail usagers", "Lot 4 — Décisionnel",
                    "Lot 5 — Conduite du changement",
                ]},
                {"type": "callout", "style": "warning",
                 "title": "Point de vigilance",
                 "text": "Le lot 3 dépend de la livraison du lot 2 ; tout "
                         "glissement supérieur à trois semaines sur l'annuaire "
                         "d'identité répercutera mécaniquement le calendrier "
                         "du portail usagers."},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "05",
            "title": "Gouvernance et organisation",
            "blocks": [
                {"type": "p", "text":
                    "La gouvernance repose sur trois instances : un comité "
                    "stratégique semestriel, un comité de pilotage mensuel et un "
                    "comité technique hebdomadaire. Une cellule de conduite du "
                    "changement est rattachée directement au chef de projet."},
                {"type": "table",
                 "caption": "Tableau 2 — Instances de gouvernance, composition "
                            "et fréquence.",
                 "headers": ["Instance", "Présidence", "Composition",
                             "Fréquence"],
                 "widths": [24, 24, 36, 16],
                 "aligns": ["left", "left", "left", "center"],
                 "rows": [
                     ["Comité stratégique", "Direction générale",
                      "Directeurs métiers, DSI, contrôle de gestion",
                      "Semestrielle"],
                     ["Comité de pilotage", "Directeur de programme",
                      "Chefs de lot, représentants métiers, achats",
                      "Mensuelle"],
                     ["Comité technique", "Architecte en chef",
                      "Référents techniques, exploitation, sécurité",
                      "Hebdomadaire"],
                     ["Cellule changement", "Responsable accompagnement",
                      "Référents métiers, formation, communication",
                      "Bimensuelle"],
                 ]},
                {"type": "h2", "text": "Équipe projet"},
                {"type": "table",
                 "headers": ["Rôle", "Titulaire", "Affectation", "Charge"],
                 "widths": [30, 28, 26, 16],
                 "aligns": ["left", "left", "left", "right"],
                 "rows": [
                     ["Directeur de programme", "Nedjah Chafik",
                      "DSI — Transformation", "100 %"],
                     ["Architecte en chef", "À désigner", "DSI — Études",
                      "80 %"],
                     ["Chef de lot Portail", "À désigner", "Prestataire",
                      "100 %"],
                     ["Responsable sécurité", "À désigner", "DSI — RSSI",
                      "40 %"],
                     ["Responsable accompagnement", "À désigner",
                      "Ressources humaines", "60 %"],
                     ["Contrôleur de gestion", "À désigner", "Finance",
                      "20 %"],
                 ]},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "06",
            "title": "Calendrier et jalons",
            "blocks": [
                {"type": "p", "text":
                    "Le calendrier s'articule sur huit trimestres. Les jalons "
                    "marqués « Terminé » ont fait l'objet d'une recette "
                    "contradictoire signée."},
                {"type": "gantt",
                 "months": ["T1 26", "T2 26", "T3 26", "T4 26", "T1 27",
                            "T2 27", "T3 27", "T4 27"],
                 "items": [
                     {"label": "Lot 1 — Socle technique", "start": 0, "end": 2,
                      "status": "Terminé"},
                     {"label": "Lot 2 — Identité fédérée", "start": 1, "end": 3,
                      "status": "En cours"},
                     {"label": "Lot 3 — Portail usagers", "start": 3, "end": 5,
                      "status": "Planifié"},
                     {"label": "Lot 4 — Décisionnel", "start": 4, "end": 6,
                      "status": "Planifié"},
                     {"label": "Lot 5 — Conduite du changement", "start": 2,
                      "end": 7, "status": "En cours"},
                 ]},
                {"type": "h2", "text": "Jalons de décision"},
                {"type": "timeline", "items": [
                     {"date": "15 janv. 2026", "status": "Terminé",
                      "title": "Cadrage et validation du dossier d'opportunité",
                      "text": "Comité stratégique — avis favorable à "
                              "l'unanimité."},
                     {"date": "30 mars 2026", "status": "Terminé",
                      "title": "Choix du titulaire du lot 1",
                      "text": "Consultation en trois temps, six candidats "
                              "auditionnés."},
                     {"date": "30 juin 2026", "status": "En cours",
                      "title": "Mise en service du socle technique",
                      "text": "Recette de stabilité sur trente jours glissants."},
                     {"date": "15 sept. 2026", "status": "À risque",
                      "title": "Ouverture du portail en version pilote",
                      "text": "Périmètre limité à trois procédures et deux "
                              "agences."},
                     {"date": "30 juin 2027", "status": "Planifié",
                      "title": "Bascule générale et décommissionnement",
                      "text": "Arrêt progressif des applications historiques."},
                ]},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "07",
            "title": "Budget et financement",
            "blocks": [
                {"type": "p", "text":
                    "L'enveloppe présentée couvre les charges de "
                    "prestations, les licences, l'infrastructure et les "
                    "actions d'accompagnement. Elle inclut une provision pour "
                    "aléas de 12 %, conforme aux pratiques de l'organisme pour "
                    "les programmes pluriannuels."},
                {"type": "table",
                 "caption": "Tableau 3 — Décomposition de l'enveloppe budgétaire "
                            "(en milliers d'euros, hors taxes).",
                 "headers": ["Poste", "2026", "2027", "Total", "Part"],
                 "widths": [40, 15, 15, 16, 14],
                 "aligns": ["left", "right", "right", "right", "right"],
                 "rows": [
                     ["Prestations de réalisation", "1 480", "1 210", "2 690",
                      "55,5 %"],
                     ["Licences et souscriptions", "210", "245", "455", "9,4 %"],
                     ["Infrastructure et hébergement", "325", "290", "615",
                      "12,7 %"],
                     ["Accompagnement et formation", "140", "180", "320",
                      "6,6 %"],
                     ["Assistance à maîtrise d'ouvrage", "95", "90", "185",
                      "3,8 %"],
                     ["Provision pour aléas (12 %)", "340", "245", "585",
                      "12,0 %"],
                     ["<b>Total du programme</b>", "<b>2 590</b>", "<b>2 260</b>",
                      "<b>4 850</b>", "<b>100 %</b>"],
                 ],
                 "total_row": True},
                {"type": "kpis", "items": [
                    {"label": "Tranche 2026", "value": "2,59 M€",
                     "note": "engagement demandé : 1,20 M€"},
                    {"label": "Tranche 2027", "value": "2,26 M€",
                     "note": "conditionnelle au jalon de juin 2027"},
                    {"label": "Coût récurrent annuel", "value": "310 K€",
                     "note": "à partir de 2028, hors projets"},
                ]},
                {"type": "callout", "style": "neutral",
                 "title": "Hypothèses de chiffrage",
                 "text":
                     "Les montants sont établis sur la base des bordereaux de "
                     "prix unitaires du titulaire retenu, indexés à hauteur de "
                     "2,1 % pour 2027. Toute évolution du périmètre fera "
                     "l'objet d'un avenant soumis au comité de pilotage."},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "08",
            "title": "Risques et plan de mitigation",
            "blocks": [
                {"type": "risk_legend"},
                {"type": "table",
                 "caption": "Tableau 4 — Registre des risques majeurs au "
                            "31 août 2026.",
                 "headers": ["Risque", "Criticité", "Impact", "Mitigation",
                             "Pilote"],
                 "widths": [25, 11, 22, 28, 14],
                 "aligns": ["left", "center", "left", "left", "left"],
                 "chips": {
                     1: {"critique": SEVERITY["critique"],
                         "élevé": SEVERITY["élevé"],
                         "moyen": SEVERITY["moyen"],
                         "faible": SEVERITY["faible"]},
                 },
                 "rows": [
                     ["Indisponibilité des référents métiers", "Élevé",
                      "Retard de recette jusqu'à 6 semaines",
                      "Plan de charge validé et suppléants désignés",
                      "DSI"],
                     ["Dérive du périmètre fonctionnel", "Critique",
                      "Surcoût estimé à 420 K€",
                      "Comité de changement, gel du périmètre par lot",
                      "Programme"],
                     ["Reprise de données incomplète", "Moyen",
                      "Anomalies en production",
                      "Double campagne de recette et réversibilité",
                      "Lot 1"],
                     ["Adoption insuffisante des outils", "Moyen",
                      "Retour aux pratiques manuelles",
                      "Dispositif de formation et référents de proximité",
                      "RH"],
                     ["Dépendance à un sous-traitant unique", "Élevé",
                      "Perte de maîtrise technique",
                      "Transfert de compétences et documentation exigée",
                      "Achats"],
                     ["Cybersécurité et conformité des données", "Faible",
                      "Notification et suspension de traitement",
                      "Homologation sécurité et audits trimestriels",
                      "RSSI"],
                 ]},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "09",
            "title": "Indicateurs de performance",
            "blocks": [
                {"type": "p", "text":
                    "Les indicateurs ci-dessous sont relevés mensuellement et "
                    "présentés en comité de pilotage. Les valeurs cibles sont "
                    "appréciées à la date de mise en service de chaque lot."},
                {"type": "table",
                 "caption": "Tableau 5 — Tableau de bord du programme.",
                 "headers": ["Indicateur", "Référence", "Cible 2027",
                             "Valeur actuelle"],
                 "widths": [40, 18, 18, 24],
                 "aligns": ["left", "right", "right", "right"],
                 "rows": [
                     ["Délai moyen de traitement d'un dossier", "11,4 j",
                      "6,6 j", "9,8 j"],
                     ["Taux de dématérialisation des procédures", "8 %",
                      "75 %", "21 %"],
                     ["Disponibilité de la plateforme", "97,1 %", "99,5 %",
                      "98,6 %"],
                     ["Taux de satisfaction usagers", "62 %", "85 %", "71 %"],
                     ["Coût de maintenance corrective annuel", "740 K€",
                      "460 K€", "690 K€"],
                     ["Part des agents formés", "0 %", "90 %", "34 %"],
                 ]},
            ],
        },

        # ------------------------------------------------------------------ #
        {
            "number": "10",
            "title": "Prochaines étapes",
            "blocks": [
                {"type": "numbers", "items": [
                    "Validation du présent dossier par le comité de pilotage "
                    "(séance du 22 septembre 2026).",
                    "Notification de la tranche ferme 2026 au titulaire du "
                    "lot 2 (octobre 2026).",
                    "Lancement de la conception détaillée du portail usagers "
                    "et des ateliers métiers associés (novembre 2026).",
                    "Premier point d'avancement trimestriel et actualisation du "
                    "registre des risques (décembre 2026).",
                ]},
                {"type": "callout", "style": "info",
                 "title": "Documents joints au dossier",
                 "items": [
                     "Annexe A — Dossier d'architecture technique cible",
                     "Annexe B — Bordereaux de prix unitaires et détail du "
                     "chiffrage",
                     "Annexe C — Registre des risques complet (28 entrées)",
                     "Annexe D — Plan de conduite du changement et de formation",
                 ]},
            ],
        },
    ],

    "closing": {
        "number": "11",
        "title": "Validation et signatures",
        "blocks": [
            {"type": "p", "text":
                "Les signatures ci-dessous valent approbation du périmètre, du "
                "calendrier et de l'enveloppe budgétaire présentés dans ce "
                "document, ainsi qu'autorisation d'engager la tranche ferme de "
                "l'exercice 2026."},
            {"type": "signatures", "items": [
                {"role": "Préparé par", "name": "Nedjah Chafik\nDirecteur de "
                                               "programme"},
                {"role": "Vérifié par", "name": "Contrôle de gestion\nPôle "
                                               "Finance"},
                {"role": "Approuvé par", "name": "Direction générale\nComité de "
                                                "pilotage"},
            ]},
            {"type": "rule", "thickness": 0.7, "space_after": 8},
            {"type": "callout", "style": "neutral",
             "title": None,
             "text":
                 "Référence DSI-PRO-2026-014 — version 1.0 — diffusé le "
                 "7 septembre 2026. Document classé « diffusion restreinte » : "
                 "toute reproduction ou communication à un tiers non autorisé "
                 "est soumise à l'accord préalable de la direction des systèmes "
                 "d'information."},
        ],
    },
}


# --------------------------------------------------------------------------- #
# Schéma de données — référence rapide
# --------------------------------------------------------------------------- #
# DOCUMENT = {
#   "meta": {kicker, title, subtitle, abstract, organization, department,
#            client, sponsor, author, location, date, version, reference,
#            classification, short_title, footer_left, footer_right,
#            logo_path (optionnel), cover_fields (optionnel)},
#   "toc": True/False,
#   "sections": [
#       {"number": "01", "title": "...", "intro": "...", "new_page": True,
#        "blocks": [ ... ]}
#   ],
#   "closing": {"number": "11", "title": "...", "blocks": [...]},
# }
#
# Blocs disponibles :
#   {"type":"p","text":"..."}                paragraphe justifié (HTML limité :
#                                            <b>, <i>, <br/>, <font color>)
#   {"type":"lead","text":"..."}             chapeau de section
#   {"type":"h2","text":"..."}               sous-titre (alimente le sommaire)
#   {"type":"h3","text":"..."}               inter-titre
#   {"type":"bullets","items":["...", {"text":"...", "sub":["..."]}]}
#   {"type":"numbers","items":["..."]}
#   {"type":"callout","style":"info|success|warning|danger|neutral|accent",
#    "title":"...", "text":"...", "items":[...]}
#   {"type":"kpis","items":[{"label","value","note"}]}
#   {"type":"table","headers":[...],"rows":[[...]],"widths":[...],
#    "aligns":["left|right|center"],"caption":"...","total_row":True,
#    "chips":{col:{"valeur":COULEUR}}}
#   {"type":"timeline","items":[{"date","title","text","status"}]}
#   {"type":"gantt","months":[...],"items":[{"label","start","end","status"}]}
#   {"type":"quote","text":"...","author":"..."}
#   {"type":"tags","items":[...]}
#   {"type":"two_columns","left":[blocs],"right":[blocs],"ratio":0.5}
#   {"type":"figure","path":"...","caption":"..."}
#   {"type":"signatures","items":[{"role","name"}]}
#   {"type":"risk_legend"} / {"type":"rule"} / {"type":"spacer","h":mm}
#   {"type":"pagebreak"} / {"type":"keep_with_next","h":mm}
