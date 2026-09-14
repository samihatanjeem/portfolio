# Portfolio Site (Streamlit)

A clean, minimal multi-page portfolio built with Streamlit.

## Pages

- **About** (`About.py`) - hero section, bio, resume download
- **Projects** - project cards with tags, links, and GitHub preview thumbnails
- **Skills** - skills grouped by category
- **Certifications** - list of certificates completed
- **Experience** - work history + education timeline
- **Contact** - social links + a form that opens a pre-filled email (no backend needed)

## Customize your content

All personal content lives in one file: **`config.py`**. Edit `PROFILE`, `SOCIAL_LINKS`,
`PROJECTS`, `SKILLS`, `EXPERIENCE`, and `EDUCATION` there - no need to touch the page files.

Add your photo, resume, and any project images to the `assets/` folder (see `assets/README.md`).

## Run locally

```bash
pip install -r requirements.txt
streamlit run About.py
```

The app opens at http://localhost:8501.

## Deploy for free

The easiest option is [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push this folder to a GitHub repo.
2. Go to share.streamlit.io, sign in, and click "New app".
3. Point it at your repo and set the main file to `About.py`.
4. Deploy - you'll get a public URL to share on your resume/LinkedIn.

## Theme

Colors and font live in `.streamlit/config.toml`. Shared CSS (cards, tag pills, spacing)
is in `styles.py`.
