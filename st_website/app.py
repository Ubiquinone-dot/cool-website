import streamlit as st
import yaml
from pathlib import Path

# Import components
from components.header import render_header


# Page configuration
st.set_page_config(
    page_title="Celine Vural",
    page_icon="🌿",
    layout="wide",
    # initial_sidebar_state="collapsed"
)


@st.cache_data
def load_config():
    """Load configuration from YAML file."""
    config_path = Path(__file__).parent / "config.yaml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def load_css():
    """Load and inject custom CSS."""
    css_path = Path(__file__).parent / "assets" / "styles.css"
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def main():
    """Main landing page."""

    # Load custom CSS
    load_css()

    # Load configuration
    config = load_config()

    # Extract personal info
    personal = config.get("personal", {})
    about = config.get("about", {})

    # Render header
    render_header(personal)

    # Horizontal divider
    st.markdown("<hr>", unsafe_allow_html=True)

    # Welcome section
    st.markdown('<h2 class="section-header">Welcome!</h2>', unsafe_allow_html=True)

    summary = about.get("summary", "")

    welcome_html = f"""
    <div class="retro-card" style="font-size: 1.1rem; line-height: 1.8;">
        <p>{summary.replace(chr(10), '<br><br>')}</p>
    </div>
    """
    st.markdown(welcome_html, unsafe_allow_html=True)

    # Quick navigation cards
    st.markdown('<h2 class="section-header">Explore</h2>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        nav_card_html = """
        <div class="retro-card" style="text-align: center; min-height: 150px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">📝</div>
            <h3 style="margin: 0; font-family: VT323, monospace; color: #4a7c59;">Blog</h3>
            <p style="margin-top: 0.5rem; font-size: 0.9rem;">Read my thoughts and stories</p>
        </div>
        """
        st.markdown(nav_card_html, unsafe_allow_html=True)
        st.page_link("pages/1_📝_Blog.py", label="Go to Blog →", icon="📝")

    with col2:
        nav_card_html = """
        <div class="retro-card" style="text-align: center; min-height: 150px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">📄</div>
            <h3 style="margin: 0; font-family: VT323, monospace; color: #4a7c59;">CV</h3>
            <p style="margin-top: 0.5rem; font-size: 0.9rem;">View my experience and education</p>
        </div>
        """
        st.markdown(nav_card_html, unsafe_allow_html=True)
        st.page_link("pages/2_📄_CV.py", label="Go to CV →", icon="📄")

    with col3:
        # Get social links
        links = personal.get("links", [])
        nav_card_html = """
        <div class="retro-card" style="text-align: center; min-height: 150px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">🌍</div>
            <h3 style="margin: 0; font-family: VT323, monospace; color: #4a7c59;">Connect</h3>
            <p style="margin-top: 0.5rem; font-size: 0.9rem;">Find me on social media</p>
        </div>
        """
        st.markdown(nav_card_html, unsafe_allow_html=True)
        # Show social links
        if links and len(links) > 0:
            first_link = links[0]
            st.link_button(f"{first_link['icon']} {first_link['name']}", first_link['url'])

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: center; color: #4a5c4a; font-family: Space Mono, monospace; font-size: 0.85rem; padding: 2rem 0;">'
        'Made with Streamlit 🌿 | Use the sidebar to navigate →'
        '</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
