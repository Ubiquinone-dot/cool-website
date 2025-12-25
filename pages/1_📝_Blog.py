import streamlit as st
import yaml
from pathlib import Path
from datetime import datetime
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from components.header import render_header


# Page configuration
st.set_page_config(
    page_title="Blog | Celine Vural",
    page_icon="📝",
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


def format_date(date_str):
    """Format date string."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except:
        return date_str


def render_blog_post(post):
    """Render a single blog post card."""
    title = post.get("title", "Untitled")
    date = format_date(post.get("date", ""))
    content = post.get("content", "")
    tags = post.get("tags", [])

    post_html = f"""
    <div class="retro-card" style="margin-bottom: 2rem;">
        <h3 style="font-family: VT323, monospace; font-size: 2.5rem; color: #4a7c59; margin-bottom: 0.5rem;">{title}</h3>
        <p style="color: #4a5c4a; font-size: 0.9rem; margin-bottom: 1rem;">📅 {date}</p>
        <div style="line-height: 1.8; color: #2d3e2d;">
            {content.replace(chr(10), '<br><br>')}
        </div>
    """

    if tags:
        post_html += '<div class="tech-tags" style="margin-top: 1rem;">'
        for tag in tags:
            post_html += f'<span class="tech-tag">{tag}</span>'
        post_html += '</div>'

    post_html += '</div>'

    st.markdown(post_html, unsafe_allow_html=True)


def main():
    """Blog page with posts."""

    # Load custom CSS
    load_css()

    # Load configuration
    config = load_config()

    # Extract personal and blog data
    personal = config.get("personal", {})
    blog_posts = config.get("blog_posts", [])

    # Render header (minimal version)
    st.markdown(
        f'<h1 style="font-family: VT323, monospace; text-align: center; color: #4a7c59; font-size: 4rem; margin: 2rem 0;">'
        f'📝 Blog'
        f'</h1>',
        unsafe_allow_html=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    # Render blog posts
    if blog_posts:
        for post in blog_posts:
            render_blog_post(post)
    else:
        st.markdown(
            '<div class="retro-card" style="text-align: center; padding: 3rem;">'
            '<h3 style="font-family: VT323, monospace; color: #4a7c59;">Coming Soon!</h3>'
            '<p>Blog posts will appear here. Check back later!</p>'
            '</div>',
            unsafe_allow_html=True
        )

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
