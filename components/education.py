import streamlit as st
from datetime import datetime


def format_date(date_str):
    """Format date string."""
    if not date_str:
        return ""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m")
        return date_obj.strftime("%b %Y")
    except:
        return date_str


def render_education(education_data):
    """Render the education section with cards."""

    st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)

    for edu in education_data:
        institution = edu.get("institution", "Institution")
        degree = edu.get("degree", "Degree")
        field = edu.get("field", "")
        location = edu.get("location", "")
        start_date = format_date(edu.get("start_date", ""))
        end_date = format_date(edu.get("end_date", ""))
        gpa = edu.get("gpa")
        honors = edu.get("honors", [])
        relevant_coursework = edu.get("relevant_coursework", [])
        achievements = edu.get("achievements", [])

        # Build education card HTML
        card_html = f"""
        <div class="education-card">
            <h3 class="education-degree">{degree} in {field}</h3>
            <div class="education-institution">{institution}</div>
            <div class="education-meta">
                📍 {location} | 📅 {start_date} - {end_date}
            </div>
        """

        # GPA
        if gpa:
            card_html += f'<div class="education-meta">🎓 GPA: {gpa}</div>'

        # Honors
        if honors:
            card_html += '<div style="margin-top: 1rem;"><strong>Honors:</strong><ul class="achievement-list">'
            for honor in honors:
                card_html += f'<li class="achievement-item">{honor}</li>'
            card_html += '</ul></div>'

        # Achievements (for certifications)
        if achievements:
            card_html += '<div style="margin-top: 1rem;"><ul class="achievement-list">'
            for achievement in achievements:
                card_html += f'<li class="achievement-item">{achievement}</li>'
            card_html += '</ul></div>'

        # Relevant Coursework
        if relevant_coursework:
            card_html += '<div style="margin-top: 1rem;"><strong>Relevant Coursework:</strong><div class="tech-tags">'
            for course in relevant_coursework:
                card_html += f'<span class="tech-tag">{course}</span>'
            card_html += '</div></div>'

        card_html += '</div>'

        st.markdown(card_html, unsafe_allow_html=True)

    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)
