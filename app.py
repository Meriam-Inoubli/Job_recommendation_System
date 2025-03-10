import streamlit as st
from page_statistics import statistics_page
from about import about_page
from cover_letter import cover_letter_page
from job_recommender import job_recommender_run, load_dataframe
from home import home_page
import re

# Configuration de la page
st.set_page_config(
    page_title="AI-Powered Job Matching",
    page_icon="💼",
    layout="wide"
)

# Inject custom CSS to left-align all text and content
st.markdown("""
    <style>
    /* Force text and block elements to align left */
    .main, .block-container {
        text-align: left !important;
        align-items: flex-start !important;
    }
   
    /* Override Streamlit's default centering for markdown and widgets */
    .stMarkdown, .stTextInput, .stButton, .stFileUploader, .stSuccess {
        text-align: left !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# Fonction principale pour gérer la navigation
def main():
    # Ajouter une barre latérale pour la navigation
    with st.sidebar:
        st.title("Navigation")
        page = st.radio(
            "Choose a page",
            ["Home", "Job Recommendation", "Cover Letter", "Statistics", "About"],
            index=0  # Par défaut, sélectionnez la première option
        )

    # Afficher la page correspondante
    if page == "Home":
        home_page()
    elif page == "Job Recommendation":
        # Choisir la langue
        language = st.sidebar.selectbox("Language", ["English", "German", "Both"])
        df_job, df_job_en, df_job_de, df_skill_data = load_dataframe()
        if language == 'English':
            df = df_job_en.copy()
        elif language == 'German':
            df = df_job_de.copy()
        else:
            df = df_job.copy()

        # Choisir la ville
        lst_city = list(df['location'].unique())
        lst_city.insert(0, 'All cities')
        city = st.sidebar.selectbox("City", lst_city)
           
        if city != 'All cities':
            df = df[df['location'].str.contains(city, na=False, case=False)]  
           
        # Filtrer par niveau d'expérience
        level = st.sidebar.selectbox('Type of level', ['Junior', 'Senior', 'Both'])
        senior_pattern = r'(Senior|Lead|Experienced|Principal|Head|Director)'
           
        if level == 'Senior':
            df = df[df['position'].str.contains(senior_pattern, flags=re.IGNORECASE, regex=True, na=False)]
        elif level == 'Junior':
            df = df[~df['position'].str.contains(senior_pattern, flags=re.IGNORECASE, regex=True, na=False)]
        job_recommender_run(df)
    elif page == "Statistics":
        statistics_page()
    elif page == "Cover Letter":
        cover_letter_page()
    elif page == "About":
        about_page()

if __name__ == "__main__":
    main()