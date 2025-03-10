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

## Structure du projet 🏗️
Job_recommendation_System/
├── Webscrapping/ # Scripts de web scraping pour LinkedIn, Indeed et Glassdoor
│ ├── chromedriver.exe # Pilote Chrome pour Selenium
│ ├── glassdoor_refactor.ipynb # Notebook pour le scraping de Glassdoor
│ ├── indeed_refactor.ipynb # Notebook pour le scraping de Indeed
│ ├── linkedin_refactor.ipynb # Notebook pour le scraping de LinkedIn
│ └── pass_linkedin.txt # Fichier contenant les identifiants LinkedIn
├── data/ # Dossier contenant les données brutes et traitées
│ ├── data_full_translate_to_en_de_23_2907_drop_duplicates.csv # Données traduites et nettoyées
│ ├── skill_extraction_Skiller_03.08_final.csv # Extraction des compétences
│ ├── skill_extraction_Skiller_03.08_final_web.csv # Extraction des compétences (web)
│ ├── skill_extraction_Skiller_03.08_final_web_v1.csv # Extraction des compétences (web v1)
│ ├── skill_extraction_Skiller_08.08_final_web.csv # Extraction des compétences (web finale)
│ └── skill_name.csv # Liste des compétences
├── data_exploratory/ # Notebooks pour l'exploration et le nettoyage des données
│ ├── data_cleaning.ipynb # Nettoyage des données
│ └── data_exploratory.ipynb # Exploration des données
├── model/ # Modèles de machine learning et NLP
│ ├── als_model.pkl # Modèle ALS pour la recommandation
│ ├── skill_extractor.pkl # Modèle d'extraction des compétences
│ ├── skill_extractor_sm.pkl # Modèle d'extraction des compétences (version light)
│ ├── tfidf_model.pkl # Modèle TF-IDF
│ └── tfidf_model_0808.pkl # Modèle TF-IDF mis à jour
├── picture/ # Dossier contenant les images utilisées dans l'application
├── ultility/ # Scripts utilitaires
│ ├── cleaning.py # Fonctions de nettoyage des données
│ └── language.py # Fonctions de traitement du langage
├── README.md # Fichier README
├── about.py # Page "À propos" de l'application
├── app.py Point d'entrée de l'application
├── cover_letter.py # Génération de lettres de motivation
├── home.py # Page d'accueil de l'application
├── job_recommender.py # Système de recommandation d'emplois
├── page_statistics.py # Page des statistiques et insights
└── requirements.txt # Dépendances du projet
