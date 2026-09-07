# -*- coding: utf-8 -*-
"""CONTENU DÉFINITIF — « L'Âme des Nations, à travers le regard de son Président ».

Reconstruction intégrale du document source scanné (36 pages, concept d'émission
internationale de Hana Ghezzar Bouakkaz) dans la trame officielle A4.
Texte repris fidèlement ; coquilles typographiques du scan corrigées.
"""

import os

IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   os.pardir, "assets", "img")


def img(name):
    return os.path.normpath(os.path.join(IMG, name))


DOCUMENT = {
    "meta": {
        "kicker": "Concept d'émission internationale",
        "title": "L'Âme des Nations",
        "subtitle": "À travers le regard de son Président",
        "abstract":
            "« Les nations ne se résument pas à leurs frontières. "
            "Elles vivent dans leur histoire, leur culture, leurs valeurs "
            "et dans les femmes et les hommes qui les incarnent. »",
        "organization": "Hana Ghezzar Bouakkaz",
        "department": "Journaliste audiovisuelle, productrice "
                      "et conceptrice d'émissions",
        "author": "Hana Ghezzar Bouakkaz",
        "location": "Alger, Algérie",
        "date": "Septembre 2026",
        "version": "1.0",
        "reference": "HGB-ADN-2026",
        "classification": "Dossier de présentation",
        "short_title": "L'Âme des Nations",
        "footer_left": "Hana Ghezzar Bouakkaz — création & production",
        "footer_right": "hanabouakkaz@outlook.com",
        "toc_title": "Sommaire",
        "cover_fields": [
            ("Créatrice", "Hana Ghezzar Bouakkaz"),
            ("Format", "Collection documentaire de prestige"),
            ("Durée", "52 minutes par épisode"),
            ("Diffusion", "Chaînes, plateformes & médias internationaux"),
            ("Contact", "hanabouakkaz@outlook.com"),
            ("Téléphone", "+213 (0) 660 769 763"),
        ],
    },

    "toc": True,

    "sections": [
        # ================================================================== #
        {
            "number": "01",
            "title": "Concept d'émission internationale",
            "blocks": [
                {"type": "h2", "text": "Présentation"},
                {"type": "lead", "text":
                    "Et si, pour une fois, un chef d'État ne parlait ni de "
                    "politique, ni d'élections, ni de conflits…<br/>"
                    "Et s'il racontait simplement son pays ?"},
                {"type": "box_grid", "cols": 3, "items": [
                    "Son histoire.", "Son peuple.", "Ses traditions.",
                    "Ses paysages.", "Ses valeurs.", "Son patrimoine.",
                ]},
                {"type": "p", "text":
                    "<b>Et surtout ce qui fait battre le cœur de sa nation.</b>"},
                {"type": "p", "text":
                    "<b>Le Président, Premier Ambassadeur de sa Nation</b> est "
                    "un concept inédit qui invite les chefs d'État à quitter le "
                    "cadre traditionnel des entretiens politiques pour partager "
                    "une conversation profondément humaine, culturelle et "
                    "patrimoniale."},
                {"type": "p", "text":
                    "Loin des questions d'actualité, cette émission offre un "
                    "espace rare où chaque Président devient le narrateur de "
                    "son pays."},
                {"type": "p", "text":
                    "Car avant d'être un responsable politique, il est aussi le "
                    "premier représentant de son peuple, de son identité et de "
                    "son héritage."},
                {"type": "p", "text":
                    "À travers une rencontre élégante, sincère et intemporelle, "
                    "le téléspectateur découvre une nation non pas à travers "
                    "les chiffres ou les décisions gouvernementales, mais à "
                    "travers le regard de celui qui en incarne l'histoire, les "
                    "valeurs et les aspirations."},
                {"type": "quote", "text":
                    "Cette émission ne cherche pas à commenter l'actualité. "
                    "Elle cherche à raconter les nations."},

                {"type": "h2", "text": "Une autre façon de raconter le monde"},
                {"type": "callout", "style": "info",
                 "title": "Le constat",
                 "text":
                     "Aujourd'hui, les chefs d'État sont sollicités "
                     "quotidiennement pour répondre aux questions politiques, "
                     "économiques ou diplomatiques. Ils sont rarement invités "
                     "à raconter ce qui fait la beauté de leur pays."},
                {"type": "h3", "text": "Ce qu'ils pourraient partager"},
                {"type": "bullets", "items": [
                    "Leur culture.",
                    "Leurs souvenirs.",
                    "Leurs traditions.",
                    "Les femmes et les hommes qui font vivre leur nation.",
                ]},
                {"type": "p", "text":
                    "Cette émission leur offre cette possibilité.<br/>"
                    "Le Président ne vient pas défendre une politique.<br/>"
                    "Il vient partager une identité.<br/>"
                    "Il devient, le temps d'une rencontre, le premier "
                    "ambassadeur de son pays."},

                {"type": "h2", "text": "L'esprit de l'émission"},
                {"type": "p", "text":
                    "Cette émission repose sur une conviction simple :"},
                {"type": "quote", "text":
                    "Les peuples se rapprochent davantage lorsqu'ils "
                    "apprennent à se connaître."},
                {"type": "p", "text":
                    "La diplomatie culturelle est aujourd'hui l'un des plus "
                    "puissants instruments de dialogue entre les nations."},
                {"type": "p", "text":
                    "À travers cette émission, chaque rencontre devient une "
                    "invitation à découvrir un pays dans ce qu'il possède de "
                    "plus précieux : <b>son âme.</b>"},

                {"type": "h2", "text": "Déroulé de l'émission"},
                {"type": "h3", "text":
                     "Première partie — Une conversation avec le Président"},
                {"type": "p", "text":
                    "La rencontre débute dans un lieu choisi personnellement "
                    "par le chef d'État. Il ne s'agit pas nécessairement d'un "
                    "bureau officiel. Ce peut être :"},
                {"type": "box_grid", "cols": 2, "items": [
                    "Le jardin du palais présidentiel,", "Une bibliothèque,",
                    "Un musée,", "Un théâtre,",
                    "Une résidence historique,", "Une place emblématique,",
                    "Une forêt,", "Un monument national,",
                    "Une ferme présidentielle,",
                    "Ou tout autre lieu qu'il estime représenter "
                    "l'identité de son pays.",
                ]},
                {"type": "p", "text":
                    "Le décor devient déjà un premier message.<br/>"
                    "La conversation est construite autour de l'identité du "
                    "pays.<br/>Les questions ne sont jamais politiques.<br/>"
                    "Elles sont universelles."},
                {"type": "h3", "text": "Les questions universelles"},
                {"type": "p", "text": "Par exemple :"},
                {"type": "box_grid", "cols": 1, "align": "left", "items": [
                    "Quel est votre premier souvenir lorsque vous pensez à "
                    "votre pays ?",
                    "Quel paysage représente le mieux votre nation ?",
                    "Quelle tradition souhaiteriez-vous transmettre au monde ?",
                    "Quelle musique raconte votre peuple ?",
                    "Quel plat devrait goûter chaque visiteur ?",
                    "Quelle valeur caractérise le mieux vos concitoyens ?",
                    "Quelle personnalité historique incarne votre nation ?",
                    "Quel lieu faut-il absolument découvrir ?",
                    "Quel mot de votre langue est impossible à traduire ?",
                    "Si votre pays était une émotion… laquelle serait-elle ?",
                ]},
                {"type": "p", "text":
                    "À travers ces questions, le Président raconte son pays "
                    "avec ses propres mots."},

                {"type": "h3", "text":
                     "Deuxième partie — Le Président devient le guide "
                     "de son pays"},
                {"type": "p", "text":
                    "La conversation laisse place à l'immersion. Le chef "
                    "d'État choisit lui-même une activité permettant de "
                    "découvrir son pays autrement. Par exemple :"},
                {"type": "bullets", "items": [
                    "Visiter un site classé au patrimoine mondial de "
                    "l'UNESCO ;",
                    "Rencontrer des artisans ;",
                    "Assister à une cérémonie traditionnelle ;",
                    "Parcourir un quartier historique ;",
                    "Embarquer sur un bateau traditionnel ;",
                    "Visiter un musée ;",
                    "Découvrir un atelier d'art ;",
                    "Rencontrer de jeunes chercheurs ;",
                    "Partager un repas traditionnel ;",
                    "Assister à une répétition d'un orchestre ;",
                    "Découvrir un marché historique ;",
                    "Rencontrer des étudiants ;",
                    "Ou toute autre expérience qu'il juge représentative de "
                    "son pays.",
                ]},
                {"type": "p", "text":
                    "Le Président ne répond plus uniquement à des questions. "
                    "Il fait découvrir ce qu'il aime.<br/>Cette immersion "
                    "permet au téléspectateur de découvrir une nation à "
                    "travers le regard de son premier représentant."},

                {"type": "h3", "text":
                     "Troisième partie — Une rencontre choisie par "
                     "le Président"},
                {"type": "p", "text":
                    "Avant de conclure, le Président transmet symboliquement "
                    "le relais. Il choisit lui-même une personnalité qui, "
                    "selon lui, incarne l'esprit de son pays. Cette personne "
                    "peut être :"},
                {"type": "bullets", "items": [
                    "Un scientifique,", "Un artiste,", "Un sportif,",
                    "Un enseignant,", "Un chef cuisinier,", "Un artisan,",
                    "Un médecin,", "Un entrepreneur,", "Un écrivain,",
                    "Un agriculteur,", "Un jeune talent,",
                    "Ou toute autre personnalité inspirante.",
                ]},
                {"type": "p", "text":
                    "Cette rencontre prolonge naturellement la conversation. "
                    "Elle permet de découvrir les femmes et les hommes qui "
                    "contribuent chaque jour au rayonnement de leur nation. "
                    "À travers leur parcours, leur engagement et leur passion, "
                    "ils donnent un visage humain aux valeurs évoquées par le "
                    "Président."},

                {"type": "h2", "text": "Une identité éditoriale unique"},
                {"type": "callout", "style": "info",
                 "title": "Cette émission ne raconte pas les chefs d'État.",
                 "items": [
                     "Elle raconte les nations.",
                     "Elle ne cherche pas à recueillir des déclarations "
                     "politiques.",
                     "Elle révèle ce qui unit les peuples.",
                     "Elle ne montre pas seulement le pouvoir.",
                     "Elle montre l'héritage.",
                     "Elle ne filme pas uniquement des institutions.",
                     "Elle raconte des histoires.",
                 ],
                 "text":
                     "Chaque épisode devient un voyage diplomatique, culturel "
                     "et humain où le Président est invité à partager ce qui "
                     "fait la singularité de son pays et ce qu'il souhaite "
                     "transmettre au monde."},
                {"type": "h3", "text": "Une empreinte internationale"},
                {"type": "p", "text":
                    "Chaque chef d'État répond aux mêmes grandes questions."},
                {"type": "p", "text":
                    "Ce fil conducteur crée une collection unique de "
                    "témoignages où les dirigeants du monde entier racontent "
                    "leur pays avec leurs mots, leur sensibilité et leur "
                    "histoire."},
                {"type": "p", "text":
                    "Au fil des épisodes, se dessine une mosaïque des cultures "
                    "du monde, révélant que, malgré leurs différences, les "
                    "nations partagent des aspirations communes : la "
                    "transmission, la mémoire, la culture, la paix et le "
                    "dialogue."},

                {"type": "h2", "text": "Signature de l'émission"},
                {"type": "p", "text": "Chaque épisode s'ouvre sur cette phrase :"},
                {"type": "quote", "text":
                    "Derrière chaque nation se cache une histoire. "
                    "Aujourd'hui, c'est son premier ambassadeur qui nous la "
                    "raconte."},
                {"type": "p", "text": "Et se conclut par ces mots :"},
                {"type": "quote", "text":
                    "Parce que les plus belles relations entre les peuples "
                    "naissent d'abord de la connaissance, du respect et du "
                    "dialogue."},
                {"type": "p", "text":
                    "Cette émission est une invitation adressée aux chefs "
                    "d'État du monde entier : non pas pour parler de pouvoir, "
                    "mais pour raconter ce qu'aucun traité ne peut décrire "
                    "pleinement — l'âme de leur nation."},
            ],
        },

        # ================================================================== #
        {
            "number": "02",
            "title": "Note d'intention",
            "blocks": [
                {"type": "p", "text":
                    "Il existe des milliers d'émissions qui interrogent les "
                    "chefs d'État sur l'actualité, la politique ou les grands "
                    "enjeux internationaux."},
                {"type": "p", "text":
                    "Très peu leur offrent la possibilité de raconter ce qui "
                    "ne figure dans aucun traité, aucun discours officiel et "
                    "aucun communiqué diplomatique : <b>l'âme de leur nation.</b>"},
                {"type": "p", "text":
                    "<b>L'Âme des Nations</b> est née d'une conviction "
                    "profonde : les peuples se rapprochent durablement "
                    "lorsqu'ils apprennent à se connaître, à découvrir leurs "
                    "cultures, leurs histoires, leurs traditions et les "
                    "valeurs qui les unissent au-delà des frontières."},
                {"type": "p", "text":
                    "À une époque où les relations internationales sont "
                    "souvent racontées à travers les crises, les conflits ou "
                    "les équilibres géopolitiques, cette émission propose un "
                    "regard différent : celui de la rencontre, du dialogue et "
                    "de la diplomatie culturelle."},
                {"type": "p", "text":
                    "Le Président n'y est pas invité comme un acteur de "
                    "l'actualité politique. Il y est accueilli comme le "
                    "premier ambassadeur de sa nation."},
                {"type": "p", "text":
                    "À travers une conversation élégante, intime et "
                    "intemporelle, il partage ce qui fait battre le cœur de "
                    "son pays : son histoire, son patrimoine, ses paysages, "
                    "sa culture, ses traditions, les femmes et les hommes qui "
                    "l'inspirent, les souvenirs qui l'ont façonné, ainsi que "
                    "les valeurs qu'il souhaite transmettre aux générations "
                    "futures."},
                {"type": "p", "text":
                    "Mais cette rencontre ne se limite pas à un entretien. "
                    "Le Président devient également le guide de son propre "
                    "pays. Il ouvre les portes d'un lieu qui lui est cher, "
                    "invite à découvrir une tradition, un savoir-faire, un "
                    "site emblématique, une expérience ou une rencontre qu'il "
                    "estime représentative de l'identité nationale."},
                {"type": "p", "text":
                    "Le téléspectateur découvre ainsi une nation non pas "
                    "comme un simple territoire, mais comme une histoire "
                    "vivante racontée par celui qui l'incarne."},
                {"type": "p", "text":
                    "L'émission se poursuit ensuite par une rencontre avec "
                    "une personnalité choisie par le Président lui-même : un "
                    "scientifique, un artiste, un enseignant, un entrepreneur, "
                    "un artisan, un sportif ou toute autre femme ou homme "
                    "dont le parcours témoigne de la richesse humaine de son "
                    "pays."},
                {"type": "p", "text":
                    "À travers cette transmission symbolique, le Président "
                    "confie son pays à celles et ceux qui le font rayonner au "
                    "quotidien."},
                {"type": "p", "text":
                    "<b>L'Âme des Nations</b> n'est pas une émission "
                    "politique. Ce n'est pas davantage une émission de "
                    "voyage. C'est une collection internationale de "
                    "rencontres consacrée aux identités nationales, au "
                    "dialogue interculturel et à la diplomatie des peuples."},
                {"type": "p", "text":
                    "Elle invite les dirigeants du monde à raconter leur "
                    "nation avec leurs propres mots, dans un esprit de "
                    "respect, d'ouverture et de compréhension mutuelle."},
                {"type": "p", "text":
                    "Chaque épisode devient ainsi une passerelle entre les "
                    "cultures, une invitation au voyage et une célébration de "
                    "la diversité des civilisations."},
                {"type": "p", "text":
                    "À travers cette collection, je souhaite offrir au public "
                    "un regard rare sur les chefs d'État : non plus seulement "
                    "comme des décideurs, mais comme les gardiens d'une "
                    "mémoire collective, les témoins d'un héritage et les "
                    "premiers ambassadeurs de leur peuple."},
                {"type": "quote", "text":
                    "Parce qu'au-delà des frontières, des langues et des "
                    "institutions, chaque nation possède une âme. "
                    "Et chaque âme mérite d'être racontée."},
            ],
        },

        # ================================================================== #
        {
            "number": "03",
            "title": "Objectifs",
            "blocks": [
                {"type": "quote", "text":
                    "Raconter les nations, c'est préserver leur mémoire et "
                    "rapprocher les peuples."},
                {"type": "p", "text":
                    "<b>L'Âme des Nations</b> poursuit une ambition simple "
                    "mais essentielle : contribuer, à travers le langage "
                    "universel de la culture, à une meilleure connaissance "
                    "des peuples et à un dialogue durable entre les nations."},
                {"type": "p", "text":
                    "À une époque où les relations internationales sont "
                    "souvent perçues à travers le prisme de l'actualité "
                    "politique, des enjeux géostratégiques ou des crises, "
                    "cette collection propose un regard complémentaire : "
                    "celui de l'identité, du patrimoine, de la mémoire et des "
                    "valeurs qui fondent chaque nation."},
                {"type": "p", "text":
                    "Son objectif est de mettre en lumière ce qui rapproche "
                    "les peuples autant que ce qui fait leur singularité, en "
                    "offrant aux chefs d'État un espace inédit où ils peuvent "
                    "partager, avec authenticité, l'histoire, la culture et "
                    "l'héritage de leur pays."},
                {"type": "p", "text":
                    "Au-delà de la découverte d'une destination, <b>L'Âme des "
                    "Nations</b> souhaite constituer une véritable mémoire "
                    "audiovisuelle des identités nationales. À travers les "
                    "témoignages de celles et ceux qui incarnent leur pays au "
                    "plus haut niveau, cette collection ambitionne de "
                    "préserver et de transmettre aux générations futures un "
                    "patrimoine immatériel d'une valeur exceptionnelle : "
                    "<i>le récit vivant des nations, raconté par leurs "
                    "premiers ambassadeurs.</i>"},
                {"type": "p", "text":
                    "Cette démarche s'inscrit pleinement dans les principes "
                    "du dialogue interculturel, de la diplomatie culturelle "
                    "et du respect mutuel, en favorisant une meilleure "
                    "compréhension entre les peuples, loin des stéréotypes et "
                    "des perceptions réductrices."},
                {"type": "p", "text":
                    "En révélant les histoires, les traditions, les "
                    "savoir-faire, les paysages, les expressions artistiques "
                    "et les femmes et les hommes qui façonnent l'identité "
                    "d'un pays, chaque épisode devient une invitation à la "
                    "découverte, à l'écoute et à la rencontre."},
                {"type": "p", "text":
                    "Parce que mieux connaître une nation, c'est déjà "
                    "construire un pont vers elle."},
                {"type": "p", "text":
                    "Et parce que les plus belles relations entre les peuples "
                    "naissent toujours de la connaissance, du respect et du "
                    "dialogue."},
            ],
        },

        # ================================================================== #
        {
            "number": "04",
            "title": "Pourquoi cette série est différente ?",
            "blocks": [
                {"type": "p", "text":
                    "À une époque où les dirigeants s'expriment surtout à "
                    "travers l'actualité, <b>L'Âme des Nations</b> propose une "
                    "approche résolument différente : <i>révéler la dimension "
                    "humaine qui éclaire l'exercice de la plus haute "
                    "responsabilité.</i>"},
                {"type": "p", "text":
                    "Chaque rencontre dépasse l'interview classique : elle "
                    "invite le chef d'État à partager l'histoire, les valeurs, "
                    "les traditions et la vision qui façonnent son pays."},
                {"type": "p", "text":
                    "Par son traitement cinématographique, le rythme et la "
                    "qualité des échanges, la série offre une immersion rare "
                    "au cœur des civilisations, chaque épisode constituant un "
                    "dialogue entre peuples, fondé sur le respect et la "
                    "découverte."},
                {"type": "p", "text":
                    "Plus qu'une série d'entretiens, c'est une collection de "
                    "témoignages d'exception destinée à traverser le temps, "
                    "une mémoire audiovisuelle portée par la voix des plus "
                    "hauts représentants des États."},
                {"type": "p", "text":
                    "À la croisée de la diplomatie, de la culture et du "
                    "documentaire de prestige, la série propose un regard "
                    "inédit sur les femmes et les hommes qui incarnent leur "
                    "pays."},
            ],
        },

        # ================================================================== #
        {
            "number": "05",
            "title": "Architecture éditoriale",
            "blocks": [
                {"type": "callout", "style": "info", "title": None,
                 "text":
                     "<b>L'Âme des Nations – À travers le regard de son "
                     "Président</b> est une collection internationale de "
                     "documentaires de prestige, conçue pour révéler "
                     "l'identité profonde des nations à travers le regard de "
                     "leur premier ambassadeur : <b>le Chef de l'État.</b><br/>"
                     "Chaque épisode constitue une rencontre unique, mêlant "
                     "entretien, immersion culturelle et découverte "
                     "patrimoniale, dans une réalisation cinématographique "
                     "soignée, pensée pour une diffusion internationale.<br/>"
                     "D'une durée d'environ 52 minutes, le programme "
                     "s'articule autour de trois temps forts, complémentaires "
                     "et indissociables."},
                {"type": "kpis", "items": [
                    {"label": "Durée d'un épisode", "value": "52 min",
                     "note": "format documentaire de prestige"},
                    {"label": "Temps forts", "value": "3",
                     "note": "complémentaires et indissociables"},
                    {"label": "Vocation", "value": "Internationale",
                     "note": "chaînes, plateformes & médias internationaux"},
                ]},
                {"type": "h3", "text":
                     "Première partie — Une conversation avec le Président"},
                {"type": "p", "text":
                    "L'émission s'ouvre sur un entretien exclusif avec le "
                    "Chef de l'État, dans un lieu qu'il aura lui-même choisi "
                    "pour sa portée symbolique ou historique."},
                {"type": "p", "text":
                    "Loin du cadre institutionnel habituel, cette "
                    "conversation invite le Président à partager un regard "
                    "personnel sur son pays. Il y évoque son histoire, son "
                    "patrimoine, ses paysages, ses traditions, les valeurs de "
                    "son peuple, ainsi que les souvenirs et les références "
                    "qui ont façonné son attachement à sa nation."},
                {"type": "p", "text":
                    "À travers des questions universelles, intemporelles et "
                    "résolument non politiques, le téléspectateur découvre "
                    "une autre manière de connaître un pays : <i>par la voix "
                    "de celui qui en incarne l'identité.</i>"},
                {"type": "h3", "text":
                     "Deuxième partie — Une immersion au cœur de la nation"},
                {"type": "p", "text":
                    "L'entretien laisse place à une expérience vivante."},
                {"type": "p", "text":
                    "Le Président invite l'émission à découvrir un lieu, une "
                    "tradition, un savoir-faire, un site patrimonial ou une "
                    "activité qu'il considère représentatif de son pays."},
                {"type": "p", "text":
                    "Cette immersion peut conduire le téléspectateur au cœur "
                    "d'un site classé au patrimoine mondial, d'un atelier "
                    "d'artisan, d'un marché traditionnel, d'un espace "
                    "naturel remarquable, d'un musée, d'une institution "
                    "culturelle ou de tout autre lieu emblématique choisi par "
                    "le Chef de l'État."},
                {"type": "p", "text":
                    "Cette séquence donne à voir la nation dans toute son "
                    "authenticité et permet d'illustrer, par l'image, les "
                    "valeurs évoquées au cours de l'entretien."},
                {"type": "h3", "text": "Troisième partie — La transmission"},
                {"type": "p", "text":
                    "En conclusion, le Président désigne une personnalité "
                    "qui, selon lui, incarne l'esprit de son pays et "
                    "contribue à son rayonnement."},
                {"type": "p", "text":
                    "Scientifique, artiste, enseignant, entrepreneur, "
                    "artisan, sportif, chercheur ou jeune talent, cette "
                    "rencontre offre un prolongement naturel au récit "
                    "présidentiel."},
                {"type": "p", "text":
                    "Elle met en lumière celles et ceux qui, par leur "
                    "engagement, leur créativité ou leur excellence, "
                    "participent chaque jour au développement, à la "
                    "transmission et à l'influence de leur nation."},
                {"type": "p", "text":
                    "Cette transmission symbolique rappelle que l'identité "
                    "d'un pays ne repose pas uniquement sur ses institutions, "
                    "mais également sur les femmes et les hommes qui la font "
                    "vivre."},
                {"type": "h3", "text": "Une réalisation à vocation internationale"},
                {"type": "p", "text":
                    "Pensée comme une collection documentaire de prestige, "
                    "L'Âme des Nations privilégie une écriture "
                    "cinématographique, des images immersives, une narration "
                    "sobre et élégante, ainsi qu'une identité visuelle "
                    "intemporelle."},
                {"type": "p", "text":
                    "Chaque épisode suit une même architecture éditoriale, "
                    "garantissant une cohérence d'ensemble tout en laissant "
                    "à chaque nation la liberté d'exprimer ce qui fait sa "
                    "singularité."},
                {"type": "p", "text":
                    "Cette approche permet de constituer, au fil des "
                    "rencontres, une collection internationale unique, où "
                    "chaque Chef d'État raconte son pays avec sa propre "
                    "sensibilité, offrant au public une mosaïque des cultures "
                    "du monde et une invitation permanente au dialogue entre "
                    "les peuples."},
            ],
        },

        # ================================================================== #
        {
            "number": "06",
            "title": "Le public visé",
            "blocks": [
                {"type": "h2", "text": "Une collection à vocation universelle"},
                {"type": "p", "text":
                    "Par son approche universelle, <b>L'Âme des Nations</b> "
                    "s'adresse à un public international, sensible aux enjeux "
                    "culturels, patrimoniaux et humains qui façonnent les "
                    "identités des peuples."},
                {"type": "p", "text":
                    "L'émission s'adresse à toutes celles et ceux qui "
                    "souhaitent découvrir les nations autrement, à travers "
                    "leur histoire, leurs traditions, leurs valeurs, leur "
                    "patrimoine et les femmes et les hommes qui les incarnent."},
                {"type": "p", "text":
                    "Conçue pour une diffusion sur les chaînes de télévision, "
                    "les plateformes numériques et les médias internationaux, "
                    "cette collection s'adresse notamment :"},
                {"type": "bullets", "items": [
                    "Au <b>grand public</b>, curieux de mieux comprendre les "
                    "cultures du monde ;",
                    "Aux <b>acteurs de la diplomatie</b>, des relations "
                    "internationales et de la coopération entre les États ;",
                    "Aux <b>institutions culturelles</b>, patrimoniales et "
                    "éducatives ;",
                    "Aux <b>étudiants, enseignants, chercheurs et "
                    "universitaires</b> intéressés par les questions de "
                    "civilisation, d'histoire, de patrimoine et de dialogue "
                    "interculturel ;",
                    "Aux <b>diasporas</b>, attachées à leurs racines et "
                    "désireuses de faire découvrir leur pays d'origine ;",
                    "Aux <b>voyageurs</b>, passionnés de découverte, "
                    "d'histoire et de rencontres humaines ;",
                    "Ainsi qu'à <b>tous les téléspectateurs</b> convaincus "
                    "que la connaissance de l'autre constitue l'un des "
                    "fondements de la paix et de la compréhension mutuelle.",
                ]},
                {"type": "p", "text":
                    "Au-delà de sa dimension culturelle et patrimoniale, "
                    "L'Âme des Nations offre également un regard inédit sur "
                    "les chefs d'État. En partageant leurs souvenirs, leurs "
                    "anecdotes, leurs émotions et leur attachement à leur "
                    "pays, ils se révèlent sous un jour profondément humain. "
                    "Cette proximité crée une résonance universelle, "
                    "permettant à chaque téléspectateur de se reconnaître "
                    "dans des valeurs, des expériences et des récits qui "
                    "dépassent les frontières."},
                {"type": "p", "text":
                    "Le Chef de l'État n'y apparaît plus seulement comme un "
                    "dirigeant. Il devient un homme ou une femme "
                    "profondément attaché à son histoire, à sa culture et à "
                    "son peuple. En partageant des souvenirs, des anecdotes "
                    "et des émotions universelles, il rappelle qu'avant de "
                    "représenter une nation, il en est aussi l'un des "
                    "enfants."},
                {"type": "p", "text":
                    "Par son écriture intemporelle et son regard "
                    "profondément humain, L'Âme des Nations dépasse le cadre "
                    "de l'actualité. Chaque épisode est conçu pour conserver "
                    "sa pertinence au fil du temps et constituer une "
                    "ressource audiovisuelle durable, destinée à être "
                    "regardée, partagée et transmise aux générations "
                    "futures."},
                {"type": "p", "text":
                    "À travers cette collection, l'ambition est de réunir un "
                    "public sans distinction de langue, de culture ou de "
                    "continent autour d'une conviction commune : derrière "
                    "chaque nation se trouvent une histoire, une identité et "
                    "une âme qui méritent d'être découvertes, comprises et "
                    "partagées."},
            ],
        },

        # ================================================================== #
        {
            "number": "07",
            "title": "Qui est Hana Ghezzar Bouakkaz ?",
            "blocks": [
                {"type": "two_columns", "ratio": 0.36,
                 "left": [
                     {"type": "figure", "path": img("portrait-hana.jpg"),
                      "max_w": 56, "max_h": 70,
                      "caption": "Hana Ghezzar Bouakkaz, créatrice de "
                                 "l'émission."},
                 ],
                 "right": [
                     {"type": "p", "style": "lead", "text":
                         "Journaliste audiovisuelle, productrice et "
                         "conceptrice d'émissions."},
                     {"type": "p", "text":
                         "<b>Hana Ghezzar Bouakkaz</b> a fait de la "
                         "diplomatie culturelle et du dialogue entre les "
                         "peuples le fil conducteur de son parcours "
                         "professionnel."},
                     {"type": "p", "text":
                         "À travers ses réalisations, elle s'attache à "
                         "mettre en lumière les relations entre les nations, "
                         "à valoriser les patrimoines culturels et à créer "
                         "des espaces de rencontre où le dialogue, le "
                         "respect et la connaissance mutuelle prennent le "
                         "pas sur les clivages."},
                 ]},
                {"type": "p", "text":
                    "Créatrice de l'émission <b>#AlgérieAuxYeuxDuMonde</b>, "
                    "elle reçoit des ambassadeurs, des représentants "
                    "d'organisations internationales, des responsables "
                    "institutionnels ainsi que des personnalités de premier "
                    "plan, dans le cadre d'entretiens consacrés à la "
                    "découverte des cultures, au rapprochement des peuples et "
                    "au rayonnement de l'Algérie sur la scène "
                    "internationale."},
                {"type": "p", "text":
                    "Son approche éditoriale repose sur une conviction : "
                    "<i>la diplomatie ne se construit pas uniquement dans les "
                    "institutions ; elle se nourrit également des échanges "
                    "humains, de la culture, de l'histoire et de la "
                    "connaissance réciproque des peuples.</i>"},
                {"type": "p", "text":
                    "Au fil de son parcours, elle a développé une expérience "
                    "des rencontres avec des représentants diplomatiques et "
                    "institutionnels de haut niveau, en privilégiant une "
                    "approche profondément humaine, respectueuse des "
                    "cultures et des identités nationales."},
                {"type": "p", "text":
                    "À travers <b>L'Âme des Nations</b>, <b>Hana Ghezzar "
                    "Bouakkaz</b> poursuit cette même ambition en proposant "
                    "un concept inédit où les chefs d'État sont invités à "
                    "raconter leur pays autrement : non pas uniquement à "
                    "travers l'actualité politique, mais à travers leur "
                    "histoire, leur patrimoine, leurs traditions, leurs "
                    "valeurs et les femmes et les hommes qui incarnent leur "
                    "nation."},
                {"type": "p", "text":
                    "Son objectif est de contribuer, par le langage "
                    "universel de l'image, au rapprochement entre les peuples "
                    "et de promouvoir une diplomatie culturelle fondée sur le "
                    "dialogue, le respect mutuel et la célébration de la "
                    "diversité des civilisations."},
                {"type": "p", "text":
                    "Pour elle, chaque rencontre est une passerelle entre "
                    "les cultures, et chaque nation possède une histoire qui "
                    "mérite d'être racontée avec justesse, élégance et "
                    "respect."},
                {"type": "quote",
                 "text":
                     "Je crois que les plus belles relations entre les "
                     "peuples naissent d'une meilleure connaissance de leurs "
                     "histoires, de leurs cultures et de leurs valeurs. Mon "
                     "travail consiste à créer ces rencontres. Parce "
                     "qu'au-delà des frontières, des langues et des "
                     "institutions, chaque nation possède une âme. Et chaque "
                     "âme mérite d'être racontée.",
                 "author": "Hana Ghezzar Bouakkaz"},
            ],
        },

        # ================================================================== #
        {
            "number": "08",
            "title": "Photothèque",
            "intro":
                "Rencontres conduites dans le cadre des émissions de la "
                "créatrice, avec les représentations diplomatiques de "
                "nombreux pays : une illustration concrète de la diplomatie "
                "culturelle qui inspire L'Âme des Nations.",
            "blocks": [
                {"type": "photos", "cols": 2, "max_h": 72, "items": [
                    {"path": img("ph-usa.jpg"),
                     "caption": "États-Unis — rencontre à la résidence "
                                "diplomatique."},
                    {"path": img("ph-chine.jpg"),
                     "caption": "Chine — entretien officiel."},
                    {"path": img("ph-uk.jpg"),
                     "caption": "Royaume-Uni — rencontre diplomatique."},
                    {"path": img("ph-canada.jpg"),
                     "caption": "Canada — rencontre diplomatique."},
                ]},
                {"type": "photos", "cols": 3, "max_h": 52, "items": [
                    {"path": img("ph-colombie.jpg"), "caption": "Colombie."},
                    {"path": img("ph-zimbabwe.jpg"), "caption": "Zimbabwe."},
                    {"path": img("ph-bangladesh.jpg"),
                     "caption": "Bangladesh."},
                    {"path": img("ph-azerbaidjan.jpg"),
                     "caption": "Azerbaïdjan."},
                    {"path": img("ph-croatie.jpg"), "caption": "Croatie."},
                    {"path": img("ph-tunisie.jpg"), "caption": "Tunisie."},
                    {"path": img("ph-turquie.jpg"), "caption": "Turquie."},
                    {"path": img("ph-vietnam.jpg"), "caption": "Vietnam."},
                    {"path": img("ph-usa2.jpg"),
                     "caption": "États-Unis — entretien."},
                ]},
            ],
        },
    ],

    # --------------------------------------------------------------------- #
    "closing": {
        "number": "",
        "title": "Contact",
        "new_page": True,
        "blocks": [
            {"type": "quote", "text":
                "Chaque nation possède une âme.<br/>"
                "Cette émission est une invitation à la raconter."},
            {"type": "figure", "path": img("signature.jpg"),
             "max_w": 72, "max_h": 36,
             "caption": "Hana Ghezzar Bouakkaz — créatrice et productrice "
                        "de l'émission."},
            {"type": "box_grid", "cols": 1, "align": "left", "size": 10,
             "items": [
                 "hanabouakkaz@outlook.com",
                 "+213 (0) 660 769 763",
             ]},
            {"type": "callout", "style": "neutral", "title": None,
             "text":
                 "Concept, écriture et présentation : Hana Ghezzar Bouakkaz. "
                 "Document de présentation — version 1.0, septembre 2026. "
                 "Référence HGB-ADN-2026."},
        ],
    },
}
