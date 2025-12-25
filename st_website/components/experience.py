import streamlit as st
from datetime import datetime


def format_date(date_str):
    """Format date string or return 'Present'."""
    if not date_str or date_str.lower() == "present":
        return "Present"
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m")
        return date_obj.strftime("%b %Y")
    except:
        return date_str


def render_experience(experience_data):
    """Render the work experience section with timeline cards."""

    st.markdown('<h2 class="section-header">Work Experience</h2>', unsafe_allow_html=True)

    for exp in experience_data:
        company = exp.get("company", "Company Name")
        position = exp.get("position", "Position")
        location = exp.get("location", "")
        start_date = format_date(exp.get("start_date", ""))
        end_date = format_date(exp.get("end_date", ""))
        description = exp.get("description", "")
        achievements = exp.get("achievements", [])
        technologies = exp.get("technologies", [])

        # Build experience card HTML
        card_html = f"""
        <div class="experience-card">
            <div class="experience-header">
                <h3 class="experience-position">{position}</h3>
                <div class="experience-company">{company}</div>
                <div class="experience-meta">
                    📍 {location} | 📅 {start_date} - {end_date}
                </div>
            </div>
        """

        # Description
        if description:
            card_html += f'<div class="experience-description">{description}</div>'

        # Achievements
        if achievements:
            card_html += '<ul class="achievement-list">'
            for achievement in achievements:
                card_html += f'<li class="achievement-item">{achievement}</li>'
            card_html += '</ul>'

        # Technologies
        if technologies:
            card_html += '<div class="tech-tags">'
            for tech in technologies:
                card_html += f'<span class="tech-tag">{tech}</span>'
            card_html += '</div>'

        card_html += '</div>'

        st.markdown(card_html, unsafe_allow_html=True)

    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)
