# PDF to Markdown

Convertit automatiquement des fichiers PDF en Markdown via GitHub Actions.

## Fonctionnement

1. Dépose un fichier `.pdf` dans le dossier `pdfs/`
2. Fais un commit et un push
3. GitHub Actions détecte le nouveau PDF, lance `convert.py` et commit le fichier `.md` correspondant dans `markdown/`

## Structure du projet

```
pdf-to-markdown/
├── pdfs/               # Dépose tes PDFs ici
├── markdown/           # Les fichiers Markdown générés apparaissent ici
├── convert.py          # Script de conversion
├── requirements.txt    # Dépendances Python
└── .github/
    └── workflows/
        └── pdf-to-md.yml  # Pipeline GitHub Actions
```

## Utilisation locale

```bash
pip install -r requirements.txt
python convert.py
```

## Dépendances

- [pdfplumber](https://github.com/jsvine/pdfplumber) — extraction du texte depuis les PDFs
- [pypdf](https://github.com/py-pdf/pypdf) — manipulation de fichiers PDF
