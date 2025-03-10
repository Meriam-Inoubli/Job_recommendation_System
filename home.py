import streamlit as st

# Streamlit page configuration
def home_page():
    # Title and description
    st.title("🌟 AI-Powered Job Matching")
    st.markdown(
        """
        **Welcome to your future career success!**  
        Our AI-powered tool helps you find the best job opportunities, craft personalized motivation letters, and analyze your CV for better results.  
        Say goodbye to generic applications and hello to standing out effortlessly.
        """
    )

    # Add a visual separator
    st.markdown("---")

    # Features Section
    st.header("🚀 Key Features")
    st.markdown(
        """
        Discover how our platform can help you land your dream job:
        """
    )

    # Use columns for a clean layout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            **📄 Upload Your CV**  
            Upload your CV to get personalized job recommendations tailored to your skills and experience.
            """
        )
    with col2:
        st.markdown(
            """
            **🔍 Top 20 Job Matches**  
            Receive a curated list of the top 20 job opportunities in the Data field based on your CV.
            """
        )
    with col3:
        st.markdown(
            """
            **📝 Generate Cover Letters**  
            Provide a job offer link, and our AI will craft a personalized motivation letter for you.
            """
        )

    # Add a visual separator
    st.markdown("---")

    # How It Works Section
    st.header("📌 How It Works")
    st.markdown(
        """
        Follow these simple steps to maximize your job search:
        """
    )

    # Use a numbered list for clarity
    st.markdown(
        """
        1. **Upload Your CV**: Start by uploading your CV in the **CV Analysis** section.  
        2. **Get Job Recommendations**: Receive a list of the top 20 jobs matching your profile.  
        3. **Generate Cover Letters**: Pick a job offer you like and generate a tailored motivation letter in the **Cover Letter** section.  
        4. **Analyze Your CV**: Use the **Statistics** section to gain insights into your CV and improve it.
        """
    )

    

if __name__ == "__main__":
    home_page()