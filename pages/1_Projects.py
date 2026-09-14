import os

import streamlit as st

from config import PROFILE, PROJECTS
from styles import inject_css

st.set_page_config(page_title=f"Projects - {PROFILE['name']}", page_icon="📁", layout="centered")
inject_css()

st.markdown("## Projects")
st.markdown("<span class='muted'>A selection of things I've built.</span>", unsafe_allow_html=True)

if not PROJECTS:
    st.info("No projects added yet - edit `PROJECTS` in config.py.")

for project in PROJECTS:
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        image = project.get("image")
        if image:
            is_url = image.startswith("http://") or image.startswith("https://")
            if is_url or os.path.exists(image):
                st.image(image, width=480)

        if project.get("date"):
            st.markdown(f"#### {project['title']} &nbsp;<span class='muted'>· {project['date']}</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"#### {project['title']}")
        st.write(project["description"])

        if project.get("tags"):
            tags_html = "".join(f"<span class='tag'>{t}</span>" for t in project["tags"])
            st.markdown(tags_html, unsafe_allow_html=True)

        link_cols = st.columns(2)
        if project.get("demo_url"):
            link_cols[0].link_button("🔗 Live Demo", project["demo_url"], use_container_width=True)
        if project.get("repo_url"):
            link_cols[1].link_button("💻 Source Code", project["repo_url"], use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)
