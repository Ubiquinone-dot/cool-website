# Personal CV Website

A minimalist personal CV website with a green lofi, retro aesthetic built using Streamlit.

## Features

- Clean, minimalist design with retro styling
- Easy content management via YAML configuration
- Responsive layout for mobile and desktop
- Sections: About, Work Experience, Education
- Green lofi color palette with vintage typography

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Ubiquinone-dot/cool-website.git
cd cool-website
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

Or using the old requirements.txt (if preferred):
```bash
pip install -r requirements.txt
```

### Configuration

Edit `config.yaml` to customize your CV content:
- Personal information (name, title, contact)
- About section (summary, skills)
- Work experience
- Education

### Running Locally

```bash
streamlit run app.py
```

The website will open in your browser at `http://localhost:8501`

## Customization

### Styling
Edit `assets/styles.css` to customize colors, fonts, and visual elements.

### Content
All CV content is managed in `config.yaml` for easy updates without touching code.

## Deployment

### Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click

### Other Options
- Docker deployment
- Cloud platforms (AWS, GCP, Azure)

## Tech Stack

- **Framework**: Streamlit
- **Language**: Python
- **Config**: YAML
- **Styling**: Custom CSS

## License

MIT License - feel free to use this for your own CV website!
