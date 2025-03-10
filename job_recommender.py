# 📌 Bibliothèques standards
import os
import sys
import re
import csv
import time
import glob
from io import StringIO
from datetime import date

# 📌 Manipulation de données
import pandas as pd
import numpy as np

# 📌 Web Scraping & Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# 📌 Traitement du langage naturel (NLP)
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from deep_translator import GoogleTranslator  # , DeeplTranslator, PonsTranslator
from langdetect import detect  # Détection de langue

# 📌 Visualisation des données
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 📌 Gestion des fichiers (PDF, DOCX, TXT)
import PyPDF2
import pdfplumber
import docx2txt
import pickle

# 📌 Machine Learning & NLP avancé
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr

# 📌 Skill Extraction (SkillNer)
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

# 📌 Streamlit (Interface utilisateur)
import streamlit as st

# 📌 Modules personnalisés
sys.path.insert(0, 'ultility')
import language
from language import google_translate_to_en, google_translate_to_de, job_description_translation

# 📌 Gestion des fichiers PDF (alternative)
import fitz  

def make_clickable(val):
    return f'<a target="_blank" href="{val}">Link to apply</a>'

@st.cache_data
def load_file(upload_file, typ):
    if (typ != 'application/pdf') & (typ != 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'):
        st.error('File is not in correct format. Please upload again')
        return None
    
    elif (typ == 'application/pdf'):        
        document = fitz.open(stream=upload_file.read(), filetype="pdf")
        page_count = document.page_count
        CV_text = ''
        for i in range(page_count):
            CV_text += document.load_page(i).get_text()
        return CV_text
        
    elif (typ == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'):
        CV_text = docx2txt.process(upload_file)
        return CV_text

@st.cache_data   
def skill_extractor_model():
    nlp = spacy.load("en_core_web_md")
    skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)
    return skill_extractor

def cosin_similarity(df, cv_skill_text, number, tfidf_model):
    df = df.reset_index()
    tfidf_skill = tfidf_model.transform([cv_skill_text])
    lst_job_description_en = df['skill_extraction'].tolist()
    tfidf_job_description = tfidf_model.transform(lst_job_description_en)
    
    cosin_sim = cosine_similarity(tfidf_skill, tfidf_job_description)
    df['cosin_similarity'] = np.array(cosin_sim).ravel()
    return df.sort_values(by='cosin_similarity', ascending=False).head(number)

def KNN_similartity(df, cv_skill_text, number, tfidf_model):
    df = df.reset_index()
    tfidf_skill = tfidf_model.transform([cv_skill_text])
    lst_job_description_en = df['skill_extraction'].tolist()
    tfidf_job_description = tfidf_model.transform(lst_job_description_en)
    
    nearest_neighbor = NearestNeighbors(n_neighbors=number)
    nearest_neighbor.fit(tfidf_job_description)
    result_KNN = nearest_neighbor.kneighbors(tfidf_skill)
    lst_index = np.array(result_KNN[1]).ravel().tolist()

    return df.loc[lst_index, :]

def person_corr_similarity(df, cv_skill_text, number, tfidf_model):
    df = df.reset_index()
    tfidf_skill = tfidf_model.transform([cv_skill_text])
    lst_job_description_en = df['skill_extraction'].tolist()
    tfidf_job_description = tfidf_model.transform(lst_job_description_en)
    
    tfidf_skill_dense = tfidf_skill.todense().tolist()[0]
    
    lst_pearson_corr = []
    for job_description in tfidf_job_description:
        job_description_dense = job_description.todense().tolist()[0]
        lst_pearson_corr.append(pearsonr(tfidf_skill_dense, job_description_dense)[0])
    df['pearson_corr'] = lst_pearson_corr
    
    return df.sort_values(by='pearson_corr', ascending=False).head(number)

@st.cache_data
def load_dataframe():
    df_job = pd.read_csv('data/skill_extraction_Skiller_08.08_final_web.csv')
    df_job_en = df_job.loc[df_job['language'] == 'en'].copy()
    df_job_de = df_job.loc[df_job['language'] == 'de'].copy()
    df_skill_data = pd.read_csv('data/skill_name.csv')
    return df_job, df_job_en, df_job_de, df_skill_data

def job_recommender_run(df):  
    # Vérification de l'upload du fichier
    # 🎯 Catchy title with colors
    st.markdown(
        "<h2 style='color:#4CAF50;'>🚀 Find Your Dream Job in Just a Few Clicks!</h2>", 
        unsafe_allow_html=True
    )

    # 📥 CV upload section
    upload_file = st.file_uploader("📂 **Please upload your CV (.pdf or .docx)**", type=["pdf", "docx"])

    # If no file is uploaded
    if upload_file is None:
        st.markdown("""
        <div style='background-color:#f9f9f9; padding:15px; border-radius:10px;'>
            <p style='font-size:16px;'>🔎 Upload your CV in <strong>.pdf</strong> or <strong>.docx</strong> format to discover job opportunities tailored to your profile.</p>
            <ul style='font-size:15px;'>
                <li>📑 Your CV will be analyzed to extract your <strong>skills</strong>.</li>
                <li>💼 We will match your skills with available <strong>job descriptions</strong>.</li>
                <li>🌍 You will receive the <strong>top 20  most suitable job offers</strong> based on:
                    <ul>
                        <li>🗺️ The language selected in the sidebar</li>
                        <li>📍 Your preferred location</li>
                        <li>📊 The job level you choose</li>
                    </ul>
                </li>
            </ul>
            <p style='font-size:14px; color:#FF5722;'>⚠️ Make sure your CV is updated with key skills to get accurate recommendations.</p>
        </div>
        """, unsafe_allow_html=True)

    # If a file is uploaded
    else:
        st.success("✅ CV uploaded successfully! Analyzing... 🔄")
        # Chargement du CV et détection de la langue
        cv_text = load_file(upload_file, upload_file.type)
        lang_detect = detect(cv_text)

        # Si la langue n'est pas l'anglais, traduire en anglais
        if lang_detect != 'en':
            cv_text = google_translate_to_en(cv_text, lang_detect)

        # Extraction des compétences du CV
        skill_extractor = skill_extractor_model()
        cv_skill = skill_extractor.annotate(cv_text)['results']['full_matches']
        print(cv_skill)
        cv_skill_text = ', '.join([skill.get('term', '') for skill in cv_skill if 'term' in skill])

        # Charger le modèle TF-IDF
        tfidf_model = pickle.load(open('model/tfidf_model_0808.pkl', 'rb'))

        # Traitement de la similarité cosinus
        number = 20
        top_job = cosin_similarity(df, cv_skill_text, number, tfidf_model)        
        top_job = top_job.reset_index()
        top_job.rename(columns={'position': 'Position', 'company_name': 'Company', 'location': 'Location', 'skill_extraction': 'Skill', 'link': 'Link'}, inplace=True)

        # Formater le tableau pour rendre les liens cliquables
        top_job_link_format = top_job[['Position', 'Company', 'Location', 'Link']].style.format({'Link': make_clickable})
        top_job_link_format = top_job_link_format.to_html(escape=False)
        st.markdown("""
        <h2 style='color:#4CAF50; font-weight:bold;'>
            📊 Top 20 Recommended Jobs Based on Your CV Analysis
        </h2>
    """, unsafe_allow_html=True)
        # Afficher le tableau avec les liens cliquables
        st.write(top_job_link_format, unsafe_allow_html=True)

        # Charger les données
        df_job, df_job_en, df_job_de, df_skill_data = load_dataframe()

if __name__ == "__main__":
    df_job, df_job_en, df_job_de, df_skill_data = load_dataframe()
    job_recommender_run(df_job)
