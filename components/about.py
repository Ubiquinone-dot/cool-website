import streamlit as st


def render_about(about_data):
    """Render the about section with summary and skills."""

    st.markdown('<h2 class="section-header">About</h2>', unsafe_allow_html=True)

    summary = about_data.get("summary", "")
    skills = about_data.get("skills", [])

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
        st.markdown('<h3 style="font-family: VT323, monospace; color: #4a7c59;">Skills</h3>', unsafe_allow_html=True)

        for skill_group in skills:
            category = skill_group.get("category", "Skills")
            items = skill_group.get("items", [])

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
