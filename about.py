import streamlit as st

def about_page():
    # Title and description
    st.title("💡 About the Application")

    st.markdown(
        """
        ### 🌟 Welcome to the Future of Job Applications!
        Our revolutionary application uses artificial intelligence to help you find jobs that match your profile
        and craft personalized cover letters for every opportunity. Say goodbye to generic applications—
        stand out effortlessly and increase your chances of success!
        """
    )

    # Add a visual separator
    st.markdown("---")

    # Main Features
    st.subheader("📌 Main Features")
    st.markdown(
        """
        Discover the key features of our application:
        """
    )

    # Use columns for better layout
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            """
            **🔍 Job Recommendations**  
            Find job offers tailored to your profile using natural language processing (NLP).
            """
        )
    with col2:
        st.markdown(
            """
            **📝 Cover Letter Generation**  
            Create personalized cover letters based on the job offer and your resume.
            """
        )
    with col3:
        st.markdown(
            """
            **📊 Market Statistics**  
            Visualize job market trends, such as the most in-demand technical skills and languages.
            """
        )
    with col4:
        st.markdown(
            """
            **📑 Resume Analysis**  
            Upload your resume to gain insights into the skills and keywords to highlight.
            """
        )


    # Add a visual separator
    st.markdown("---")

    # Technologies Used Section
    st.subheader("🛠️ Technologies and Tools")
    st.markdown(
        """
        Our application is powered by a wide range of cutting-edge technologies and libraries to deliver a seamless and intelligent experience. Here's a glimpse of what's under the hood:
        """
    )

    # Use columns for better layout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            **📌 Data Manipulation**  
            - `pandas`  
            - `numpy`  
            - `csv`  
            """
        )
    with col2:
        st.markdown(
            """
            **📌 Web Scraping**  
            - `Selenium`  
            - `BeautifulSoup`  
            - `requests`  
            """
        )
    with col3:
        st.markdown(
            """
            **📌 Natural Language Processing (NLP)**  
            - `spaCy`  
            - `nltk`  
            - `deep_translator`  
            """
        )

    # Second row of columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            **📌 Machine Learning**  
            - `scikit-learn`  
            - `cosine_similarity`  
            - `NearestNeighbors`  
            """
        )
    with col2:
        st.markdown(
            """
            **📌 File Handling**  
            - `PyPDF2`  
            - `pdfplumber`  
            - `docx2txt`  
            """
        )
    with col3:
        st.markdown(
            """
            **📌 Visualization**  
            - `matplotlib`  
            - `WordCloud`  
            """
        )

    st.markdown("---")
    st.subheader("📧 Cover Letter Generation Technologies")
    st.markdown(
        """
        Our **Cover Letter Generation** feature leverages advanced AI models and frameworks to create personalized and compelling cover letters. Here are the key technologies behind it:
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            **📌 AI Models**  
            - `Groq API`  
            - `llama-3.3-70b-versatile`  
            """
        )
    with col2:
        st.markdown(
            """
            **📌 Frameworks**  
            - `LangChain`  
            - `PromptTemplate`  
            """
        )
    with col3:
        st.markdown(
            """
            **📌 Utilities**  
            - `WebBaseLoader`  
            - `Pydantic`  
            """
        )

    # Add a visual separator
    st.markdown("---")

    # How It Works Section
    st.subheader("🔧 How It Works")
    st.markdown(
        """
        Our application uses advanced algorithms and techniques to analyze job offers, resumes, and generate personalized recommendations. Here's a breakdown of the process:
        - **Job Offer Analysis**: We extract keywords and key requirements to compare them with your profile.
        - **Resume Analysis**: Your resume is processed to identify skills and experiences.
        - **Matching Algorithm**: We use **cosine similarity** and **nearest neighbors** to match your profile with the most relevant job offers.
        - **Cover Letter Generation**: Based on the job description and your resume, our AI crafts a personalized cover letter using state-of-the-art language models.
        """
    )

    # Add a visual separator
    st.markdown("---")

    # About the Team Section
    st.subheader("👥 About the Team")
    st.markdown(
        """
        This application was developed by **Meriam Innoubli** and **Ferdaws Ziadia**, two enthusiasts of artificial intelligence and innovation.
        Together, we combined our expertise in AI, natural language processing, and software development to create a powerful
        and intuitive tool that simplifies job searching and cover letter writing.

        Our goal? To help you shine in your job search through innovative technological solutions.
        """
    )

    # Add a footer
    st.markdown("---")
    st.markdown(
        """
        **💡 Pro Tip:** Customize your cover letter further by adding specific achievements or skills relevant to the job!
        """
    )