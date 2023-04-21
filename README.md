## Numérisation des Xassidas en TXT (format txt)

Ce projet vise à numériser les Xassidas en format txt(texte) et les rendre plus accessibles aux utilisateurs avec l'application web **Tariha.sn**(en developpement).

Le projet est entièrement open-source et est ouvert aux contributions.

### Technologies utilisées

- [Arabic Keyboard Online LEXILOGOS](https://www.lexilogos.com/keyboard/arabic.htm)[Arabic Keyboard Online LEXILOGOS](https://www.lexilogos.com/keyboard/arabic.htm): Outil permettant d'écrire en arabe
- Python3: Les différents scripts (transcription, formattage des fichiers) ont été écrits en python

### Étapes du processus de numérisation

1. La saisie de texte d'un xassida (voir <a href="#format">**Format à respecter**</a> ci dessous)
2. Vérifier et corriger les erreurs
3. Organiser les Xassidas en fonction des tariha et auteurs (voir <a href="#structure">structure</a>).
   
   **NB**: **Veillez bien vérifier la saisie des accents car la transcription en français se fait automatiquement voir [Transcription](https://github.com/Tariha/transcription)**



### <h3 id="format">Format à Respecter</h3>

La saisie des xassidas et leur traductions(si disponible) doit respecter ce format

- **Les Chapitres**(s'ils exitent) $commencent$ par trois(3) **Diez(#)** suivit du titre du chapitre

- Si le xassida ne comporte pas de chapitre le ficher doit commence par trois(3) **Diez(#)**

- **Les versets** doivent être séparés par deux(2) **Diez(#)**
  
  **Ex**: (voir aussi les xassidas déjà existant)

![example.png](example.png)

### Pour les Developpeurs

**Requirements**

- **Python 3.9 ou Supérieur**

#### <h3 id="structure">Structure des fichiers</h3>

```bash
└── xassidas
    ├── mouride
    └── tidjian
        ├── maodo
        │   ├── abada
        │   │   └── abada.txt
        │   ├── allahou_hasbi
        │   │   └── allahou_hasbi.txt
        │   ├── bourdou
        │   │   └── bourdou.txt
        │   └── xassidas.json
        ├── serigne-babacar
        └── serigne-cheikh
            └── abouna
                ├── abouna.json
```

#### Les scripts

+ **parse_xassida.py**:
  
    Ce script sera utilisé pour extraire les xassidas et leur traductions en
    format json.
  
  ```bash
  python parse_xassida.py [-t tariha] [-a auteur] [-x xassida]
  ```
  
    json output
  
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

+ **parse_translation.py**:
  
  Ce script sera utilisé pour extraire et inserer dans le ficher ci-dessus les traductions s'ils existent .
  
  ```bash
  python parse_translations.py [-t tariha] [-a auteur] [-x xassida]
  ```
  
  **json output**
  
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
                "lang": "fr",
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
  
  - **parse_author.py**
    
    Ce script permet de regrouper les xassidas(**json**) d'un auteur dans un même fichier json
    
    ```shell
    python parse_author.py [-t tariha] [-a auteur]
    ```
  
  ## Licence

        Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus         d'informations.
