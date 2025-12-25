import streamlit as st
import yaml
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

# Import components
from components.header import render_header
from components.about import render_about
from components.experience import render_experience
from components.education import render_education


# Page configuration
st.set_page_config(
    page_title="CV | Celine Vural",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)


@st.cache_data
def load_config():
    """Load configuration from YAML file."""
    config_path = Path(__file__).parent.parent / "config.yaml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def load_css():
    """Load and inject custom CSS."""
    css_path = Path(__file__).parent.parent / "assets" / "styles.css"
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def main():
    """CV page with full details."""

    # Load custom CSS
    load_css()

    # Load configuration
    config = load_config()

    # Extract sections from config
    personal = config.get("personal", {})
    about = config.get("about", {})
    experience = config.get("experience", [])
    education = config.get("education", [])

    # Render sections
    render_header(personal)

    # Horizontal divider
    st.markdown("<hr>", unsafe_allow_html=True)

    render_about(about, personal)

    # Horizontal divider
    st.markdown("<hr>", unsafe_allow_html=True)

    render_experience(experience)

    # Horizontal divider
    st.markdown("<hr>", unsafe_allow_html=True)

    render_education(education)

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align: center; color: #4a5c4a; font-family: Space Mono, monospace; font-size: 0.85rem; padding: 2rem 0;">'
        'Made with Streamlit 🌿'
        '</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
