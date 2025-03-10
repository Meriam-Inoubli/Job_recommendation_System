import streamlit as st
import time

def statistics_page():
    st.markdown(
        """
        <div style='background-color:#f0f2f6; padding:20px; border-radius:10px;'>
            <h2 style='color:#2e86c1;'>📊 Personalized CV Analysis</h2>
            <p style='font-size:16px;'>
                Upload your CV to unlock powerful insights into the job market trends and optimize your profile for success!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    upload_file = st.file_uploader("📂 **Upload your CV (.pdf or .docx)**", type=["pdf", "docx"])
   
    # Si aucun fichier n'est téléchargé
    if upload_file is None:        
        st.markdown(
            """
            <div style='background-color:#f9f9f9; padding:20px; border-radius:10px; margin-top:20px;'>
                <h3 style='color:#2e86c1;'>💡 Unlock Powerful Insights from Your CV! 🚀</h3>
                <p style='font-size:16px;'>
                    By analyzing key trends in <strong>languages</strong>, <strong>locations</strong>, <strong>job titles</strong>, and <strong>skills</strong>,
                    we provide you with a detailed breakdown of market demands and industry expectations. 📊📈
                </p>
                <p style='font-size:16px;'>
                    ✨ Get a clear vision of where you stand and how to optimize your profile for success.
                </p>
                <p style='font-size:16px; color:#e74c3c;'>
                    📎 <strong>Upload your CV now to access personalized statistics tailored just for you!</strong> 🔍
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # Affichage des statistiques après téléchargement du CV
        st.success("✅ CV uploaded successfully! Generating insights... 🔄")

        # Section 1 : Langues dans les descriptions de poste
        st.markdown(
            """
            <div style='background-color:#f0f2f6; padding:20px; border-radius:10px; margin-top:20px;'>
                <h2 style='color:#2e86c1;'>📌 1. Languages in Job Descriptions</h2>
                <p style='font-size:16px;'>
                    Discover the most in-demand languages for <strong>Data Science</strong> and <strong>Data Analytics</strong> roles.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        with st.spinner("⏳ Generating statistics..."):
            time.sleep(4)  # Simulation d'un chargement
        col1, col2 = st.columns(2)
        with col1:
            st.image("picture/language_ds.png", caption="Data Science Languages 🖥️", use_container_width=True)
        with col2:
            st.image("picture/language_da.png", caption="Data Analytics Languages 📊", use_container_width=True)

        # Section 2 : Localisation et titres de poste
        st.markdown(
            """
            <div style='background-color:#f0f2f6; padding:20px; border-radius:10px; margin-top:20px;'>
                <h2 style='color:#2e86c1;'>📌 2. Location and Job Titles</h2>
                <p style='font-size:16px;'>
                    Explore the top locations and most common job titles in the industry.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        col3, col4 = st.columns(2)
        with col3:
            st.image("picture/location.png", caption="Top Locations 📍", use_container_width=True)
        with col4:
            st.image("picture/job_title.png", caption="Most Common Job Titles 🎯", use_container_width=True)

        # Section 3 : Compétences techniques
        st.markdown(
            """
            <div style='background-color:#f0f2f6; padding:20px; border-radius:10px; margin-top:20px;'>
                <h2 style='color:#2e86c1;'>📌 3. Technical Skills</h2>
                <p style='font-size:16px;'>
                    See the most sought-after technical skills for <strong>Data Science</strong> and <strong>Data Analytics</strong> roles.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        col5, col6 = st.columns(2)
        with col5:
            st.image("picture/ds_tech_skill.png", caption="Technical Skills for Data Science 🛠️", use_container_width=True)
        with col6:
            st.image("picture/da_tech_skill.png", caption="Technical Skills for Data Analytics 🏗️", use_container_width=True)

        # Section 4 : Compétences générales (soft skills)
        st.markdown(
            """
            <div style='background-color:#f0f2f6; padding:20px; border-radius:10px; margin-top:20px;'>
                <h2 style='color:#2e86c1;'>📌 4. Soft Skills</h2>
                <p style='font-size:16px;'>
                    Discover the essential soft skills for <strong>Data Science</strong> and <strong>Data Analytics</strong> roles.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        col7, col8 = st.columns(2)
        with col7:
            st.image("picture/ds_soft_skill.png", caption="Soft Skills for Data Science 🤝", use_container_width=True)
        with col8:
            st.image("picture/da_soft_skill.png", caption="Soft Skills for Data Analytics 🎭", use_container_width=True)

if __name__ == "__main__":
    statistics_page()