import streamlit as st


def render_about(about_data, personal_data=None):
    """Render the about section with summary and skills."""

    st.markdown('<h2 class="section-header">About</h2>', unsafe_allow_html=True)

    summary = about_data.get("summary", "")
    skills = about_data.get("skills", [])

    # Get languages from personal data if provided
    languages = []
    if personal_data:
        languages = personal_data.get("languages", [])

    # Create two columns for summary and skills
    col1, col2 = st.columns([2, 1])

    with col1:
        # Summary in retro card
        summary_html = f"""
        <div class="retro-card">
            <p>{summary.replace(chr(10), '<br><br>')}</p>
        </div>
        """
        st.markdown(summary_html, unsafe_allow_html=True)

    with col2:
        # Skills by category
        # st.markdown('<h3 style="font-family: VT323, monospace; color: #4a7c59;">Skills</h3>', unsafe_allow_html=True)

        # Add languages at the top if provided
        if languages:
            language_html = f"""
            <div class="skill-category">
                <div class="skill-category-title">Languages</div>
                <div>
                    {''.join([f'<span class="skill-item">{lang}</span>' for lang in languages])}
                </div>
            </div>
            """
            st.markdown(language_html, unsafe_allow_html=True)

        for skill_group in skills:
            category = skill_group.get("category", "Skills")
            items = skill_group.get("items", [])

            # Skip Languages category if it exists since we're showing it separately
            if category.lower() == "languages" and languages:
                continue

            category_html = f"""
            <div class="skill-category">
                <div class="skill-category-title">{category}</div>
                <div>
                    {''.join([f'<span class="skill-item">{item}</span>' for item in items])}
                </div>
            </div>
            """
            st.markdown(category_html, unsafe_allow_html=True)

    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)
