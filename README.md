# Job Recommendation System 💼🔍

Ce projet est un système de recommandation d'emplois basé sur le traitement du langage naturel (NLP). Il analyse le CV de l'utilisateur et recommande les 20 meilleurs emplois alignés avec son profil. Les offres d'emploi sont extraites de LinkedIn et Indeed. De plus, l'utilisateur peut générer une lettre de motivation pour une offre spécifique et obtenir des statistiques détaillées sur les compétences techniques et les langages les plus demandés.
![image](https://github.com/user-attachments/assets/e9689be7-eabf-42a6-b4c7-0a20ed36c8fd)

---

## Fonctionnalités ✨

1. **Recommandation d'emplois** 📝:
   - L'utilisateur télécharge son CV (format PDF ou DOCX).
   - Le système analyse le CV et recommande les 20 meilleurs emplois alignés avec son profil.

2. **Génération de lettre de motivation** 💌:
   - L'utilisateur peut fournir l'URL d'une offre d'emploi.
   - Le système génère une lettre de motivation personnalisée pour cette offre.

3. **Statistiques et insights** 📊:
   - Analyse des compétences techniques et des langages les plus demandés dans les offres d'emploi.
   - Statistiques sur les localisations et les titres de poste les plus populaires.
   - Visualisation des compétences techniques et des soft skills les plus recherchés.

## 📂 Structure du Projet

```plaintext
Job_recommendation_System/
├── Webscrapping/                                                           # Scripts de web scraping pour LinkedIn, Indeed et Glassdoor
│ ├── chromedriver.exe                                                      # Pilote Chrome pour Selenium
│ ├── glassdoor_refactor.ipynb                                              # Notebook pour le scraping de Glassdoor
│ ├── indeed_refactor.ipynb                                                 # Notebook pour le scraping de Indeed
│ ├── linkedin_refactor.ipynb                                               # Notebook pour le scraping de LinkedIn
│ └── pass_linkedin.txt                                                     # Fichier contenant les identifiants LinkedIn
├── data/                                                                   # Dossier contenant les données brutes et traitées
│ ├── data_full_translate_to_en_de_23_2907_drop_duplicates.csv              # Données traduites et nettoyées
│ ├── skill_extraction_Skiller_03.08_final.csv                              # Extraction des compétences
│ ├── skill_extraction_Skiller_03.08_final_web.csv                          # Extraction des compétences (web)
│ ├── skill_extraction_Skiller_03.08_final_web_v1.csv                       # Extraction des compétences (web v1)
│ ├── skill_extraction_Skiller_08.08_final_web.csv                          # Extraction des compétences (web finale)
│ └── skill_name.csv                                                        # Liste des compétences
├── data_exploratory/                                                       # Notebooks pour l'exploration et le nettoyage des données
│ ├── data_cleaning.ipynb                                                   # Nettoyage des données
│ └── data_exploratory.ipynb                                                # Exploration des données
├── model/                                                                  # Modèles de machine learning et NLP
│ ├── als_model.pkl                                                         # Modèle ALS pour la recommandation
│ ├── skill_extractor.pkl                                                   # Modèle d'extraction des compétences
│ ├── skill_extractor_sm.pkl                                                # Modèle d'extraction des compétences (version light)
│ ├── tfidf_model.pkl                                                       # Modèle TF-IDF
│ └── tfidf_model_0808.pkl                                                  # Modèle TF-IDF mis à jour
├── picture/                                                                # Dossier contenant les images utilisées dans l'application
├── ultility/                                                               # Scripts utilitaires
│ ├── cleaning.py                                                           # Fonctions de nettoyage des données
│ └── language.py                                                           # Fonctions de traitement du langage
├── README.md                                                               # Fichier README
├── about.py                                                                # Page "À propos" de l'application
├── app.py                                                                  # Point d'entrée de l'application
├── cover_letter.py                                                         # Génération de lettres de motivation
├── home.py                                                                 # Page d'accueil de l'application
├── job_recommender.py                                                      # Système de recommandation d'emplois
├── page_statistics.py                                                      # Page des statistiques et insights
└── requirements.txt                                                        # Dépendances du projet
```

---

## Technologies utilisées 💻

- **Langages** : Python
- **Frameworks** : Streamlit (interface utilisateur)
- **Traitement de texte** : spaCy, NLTK, PyPDF2 (pour l'analyse de CV)
- **Web scraping** : BeautifulSoup, Selenium (pour extraire les offres d'emploi)
- **Machine Learning** : Scikit-learn, TensorFlow (pour la recommandation)
- **Visualisation** : Matplotlib, Seaborn, Plotly (pour les statistiques)
- **Génération de texte** : OpenAI GPT (pour les lettres de motivation)

---

## Étapes détaillées du projet 🔍

### 1. **Web Scraping**
   - **Objectif** : Extraire les offres d'emploi de LinkedIn, Indeed et Glassdoor.
   - **Outils** : Selenium, BeautifulSoup.
   - **Processus** :
     1. **Configuration de Selenium** : Utilisation de `chromedriver.exe` pour automatiser la navigation sur les sites web.
     2. **Connexion aux sites** : Les identifiants LinkedIn sont stockés dans `pass_linkedin.txt` pour une connexion automatisée.
     3. **Extraction des données** : Les offres d'emploi sont extraites en parcourant les pages web et en récupérant les informations clés (titre, description, localisation, etc.).
     4. **Sauvegarde des données** : Les données extraites sont sauvegardées dans des fichiers CSV pour un traitement ultérieur.

### 2. **Data Cleaning**
   - **Objectif** : Nettoyer les données brutes pour les rendre utilisables.
   - **Outils** : Pandas, NumPy.
   - **Processus** :
     1. **Suppression des doublons** : Les offres d'emploi en double sont supprimées.
     2. **Traitement des valeurs manquantes** : Les champs vides sont remplis ou supprimés.
     3. **Normalisation des données** : Les textes sont convertis en minuscules, les caractères spéciaux sont supprimés, et les formats de date sont standardisés.
     4. **Traduction des données** : Les offres d'emploi sont traduites en anglais pour une analyse cohérente.

### 3. **Data Exploration**
   - **Objectif** : Explorer les données pour identifier des tendances et des insights.
   - **Outils** : Pandas, Matplotlib, Seaborn.
   - **Processus** :
     1. **Analyse des compétences** : Les compétences techniques les plus demandées sont identifiées.
     2. **Visualisation des données** : Des graphiques sont générés pour montrer les tendances des offres d'emploi par localisation, titre de poste et compétences.
     3. **Extraction des insights** : Les insights sont utilisés pour améliorer le système de recommandation.

### 4. **Traitement du Langage Naturel (NLP)**
   - **Objectif** : Analyser les textes des offres d'emploi et des CV pour extraire des informations clés.
   - **Outils** : spaCy, NLTK, PyPDF2.
   - **Processus** :
     1. **Tokenisation** : Les textes sont divisés en mots ou phrases.
     2. **Lemmatisation** : Les mots sont réduits à leur forme de base (par exemple, "running" devient "run").
     3. **Suppression des stop words** : Les mots courants (comme "le", "de", "et") sont supprimés.
     4. **Extraction des entités nommées** : Les noms, lieux, dates et autres entités sont extraits.

### 5. **Extraction des Compétences**
   - **Objectif** : Identifier les compétences techniques et les soft skills dans les offres d'emploi et les CV.
   - **Outils** : spaCy, Scikit-learn.
   - **Processus** :
     1. **Création d'un corpus de compétences** : Une liste de compétences techniques et de soft skills est créée à partir des données disponibles.
     2. **Matching des compétences** : Les compétences sont identifiées dans les textes en utilisant des techniques de matching de mots-clés.
     3. **Modélisation** : Un modèle TF-IDF est utilisé pour pondérer l'importance des compétences dans les offres d'emploi.

### 6. **Création du Corpus**
   - **Objectif** : Construire un corpus de textes pour entraîner les modèles NLP.
   - **Outils** : spaCy, NLTK.
   - **Processus** :
     1. **Collecte des textes** : Les descriptions d'offres d'emploi et les CV sont collectés.
     2. **Prétraitement des textes** : Les textes sont nettoyés et normalisés.
     3. **Création du corpus** : Les textes sont organisés en un corpus structuré pour l'analyse et la modélisation.

---

## Installation 🛠️

### 1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/Meriam-Inoubli/Job_recommendation_System.git
   ```
### 2. **Accéder au dossier du projet**
   ```bash
   cd Job_recommendation_System
   ```
### 3. **Créer un environnement virtuel (optionnel mais recommandé)**
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```
### 4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
## Utilisation 🚀
### 1. **Lancer l'application Streamlit**
   ```bash
   streamlit run app.py
   ```
### 2. **Ouvrir l'application dans le navigateur**
L'application sera accessible à l'adresse suivante : http://localhost:8501.

### 3. **Télécharger votre CV**
Sur la page d'accueil, téléchargez votre CV au format PDF ou DOCX.

### 4. **Obtenir les recommandations d'emplois**
Le système analysera votre CV et affichera les 20 meilleurs emplois alignés avec votre profil.

### 5. **Générer une lettre de motivation**
Entrez l'URL d'une offre d'emploi.
Le système générera une lettre de motivation personnalisée basée sur votre CV et les détails de l'offre.

### 6. **Explorer les statistiques**
Consultez les statistiques sur les compétences techniques, les langages de programmation, les localisations et les titres de poste les plus demandés.

## Auteur 👩‍💻
Meriam Inoubli : meriam.inoubli@dauphine.tn
Ferdaws Ziadia : ferdaws.ziadia@dauphine.tn

## Licence 📜
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

