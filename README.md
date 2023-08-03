# Numérisation des Xassidas en TXT

Ce projet vise à numériser les Xassidas en format texte (txt) et les rendre accessibles via l'application web [xassida.sn](www.xassida.sn).
<p>
Ce repository contient des xassidas en format texte (txt) organisés en fonction des confréries et leurs auteurs.
</p>

Le projet est entièrement open-source et est ouvert aux contributions.

## Comment contribuer ?

1. Avoir le texte d'un xassida (.txt) bien écrit
2. Formatter le texte (voir <a href="#format">**Format à respecter**</a> ci dessous)
3. Organiser le xassida en fonction de la confrérie et de l'auteur (voir <a href="#structure">structure</a>).
   
   **NB**: **Veillez bien vérifier la saisie des accents car la transcription en français se fait automatiquement voir [Transcription](https://github.com/Tariha/transcription)**


<h2 id="format">Format à Respecter</h2>
Un xassida et ses traductions doivent avoir exactement le même format:

1. Les **Chapitres** commencent par 3 diez **###**
2. Les **versets (beyit)** doivent être séparés par 2 diez **##**

**NB**: **Si le xassida ne comporte pas de chapitre le ficher doit aussi commencé par 3 diez ###**
(voir [un example](xassidas/tidjan/autre/yaman_azhara/yaman_azhara.txt))
![example.png](example.png)

<h2 id="structure">Structure des fichiers</h2>

```
xassidas
├── mouride
│   └── cheikh_ahmadou_bamba
        ├── midadi (xassida)
        │   ├── en
        │   │   └── midadi.txt (traduction anglais)
        │   ├── fr
        │   │   └── midadi.txt (traduction français)
        │   └── midadi.txt  (texte arabe)
└── tidjan
    └── cheikh_tidiane_sy
        ├── abuna (xassida)
        │   ├── abuna.txt (texte arabe)
        │   └── fr
        │       └── abuna.txt (traduction français)
```

## Pour les Developpeurs

### Requirements
- **Python 3.9 ou Supérieur**

### Installer les dépendances
```bash
  pip install -r requirements.txt
```
## Les scripts

1. ### parse_xassida.py :
    Ce script sera utilisé pour extraire les xassidas et leur traductions en format json.
    ```bash
    python parse_xassida.py [-t tariha] [-a auteur] [-x xassida]
    ```
    <details>
      <resume>Sortie Json</resume>

    ```json
    {
      "name": "sample",
      "chapters": [
        {
          "name": "الفاتحة",
          "number": 1,
          "verses": [
            {
              "number": 0,
              "key": "1:0",
              "text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
              "words": [
                {
                  "position": 0,
                  "text": "بِسْمِ",
                  "transcription": "bismi"
                },
                {
                  "position": 1,
                  "text": "اللَّهِ",
                  "transcription": "l-lahi"
                },
                {
                  "position": 2,
                  "text": "الرَّحْمَٰنِ",
                  "transcription": "r-raḥmāni"
                },
                {
                  "position": 3,
                  "text": "الرَّحِيمِ",
                  "transcription": "r-raḥīmi"
                }
              ],
              "translations": []
            },
            ...
          ],
        },
        ...
      ],
      "translated_names": [],
      "audios": [],
      "translated_lang": []
      }
    ```
    </details>

2. ### parse_translations.py :
    Ce script sera utilisé pour extraire et inserer dans le ficher ci-dessus les traductions s'ils existent.
    ```bash
    python parse_translations.py [-t tariha] [-a auteur] [-x xassida]
    ```
    <details>
      <resume>Sortie Json</resume>
  
    ```json
    {
      "name": "sample",
      "chapters": [
        {
          "name": "الفاتحة",
          "number": 1,
          "verses": [
            {
              "number": 0,
              "key": "1:0",
              "text": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
              "words": [
                {
                  "position": 0,
                  "text": "بِسْمِ",
                  "transcription": "bismi"
                },
                {
                  "position": 1,
                  "text": "اللَّهِ",
                  "transcription": "l-lahi"
                },
                {
                  "position": 2,
                  "text": "الرَّحْمَٰنِ",
                  "transcription": "r-raḥmāni"
                },
                {
                  "position": 3,
                  "text": "الرَّحِيمِ",
                  "transcription": "r-raḥīmi"
                }
              ],
              "translations": [
                {
                  "lang": "en",
                  "text": "In the name of Allah, the Entirely Merciful, the Especially Merciful.",
                  "author": ""
                }
              ]
            },
            ...
          ]
        },
        ...
      ],
      "translated_names": [],
      "audios": [],
      "translated_lang": []
    }
    ```
    </details>

3. ### parse_author.py:
    Ce script permet de regrouper les sorties **Json** des xassidas d'un auteur dans un même fichier json
    ```bash
    python parse_author.py [-t tariha] [-a auteur]
    ```
  
## Technologies utilisées

- [Arabic Keyboard Online LEXILOGOS](https://www.lexilogos.com/keyboard/arabic.htm): Outil permettant d'écrire en arabe
- Python3: Les différents scripts (transcription, formattage des fichiers) ont été écrits en python

## Licence
Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE  pour plus d'informations.