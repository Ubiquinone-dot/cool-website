import streamlit as st


def render_header(personal_data):
    """Render the header section with name, title, and social links."""

    name = personal_data.get("name", "Your Name")
    title = personal_data.get("title", "Your Title")
    tagline = personal_data.get("tagline", "")
    links = personal_data.get("links", [])

    # Header HTML with retro styling
    header_html = f"""
    <div class="header-container">
        <h1 class="header-title">{name}</h1>
        <p class="header-subtitle">{title}</p>
        {f'<p class="header-tagline">{tagline}</p>' if tagline else ''}
    </div>
    """

    st.markdown(header_html, unsafe_allow_html=True)

    # Social links
    if links:
        links_html = '<div class="social-links">'
        for link in links:
            icon = link.get("icon", "🔗")
            name = link.get("name", "Link")
            url = link.get("url", "#")
            links_html += f'<a href="{url}" target="_blank" rel="noopener noreferrer" class="social-link">{icon} {name}</a>'
        links_html += '</div>'
        st.markdown(links_html, unsafe_allow_html=True)
