import streamlit as st

from config import EDUCATION, EXPERIENCE, PROFILE
from styles import inject_css

st.set_page_config(page_title=f"Experience - {PROFILE['name']}", page_icon="💼", layout="centered")
inject_css()

st.markdown("## Experience")

if not EXPERIENCE:
    st.info("No experience added yet - edit `EXPERIENCE` in config.py.")

for job in EXPERIENCE:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"#### {job['role']}")
    st.markdown(f"**{job['organization']}** &nbsp;·&nbsp; <span class='muted'>{job['period']}</span>", unsafe_allow_html=True)
    bullets = job.get("bullets") or [job.get("description", "")]
    for bullet in bullets:
        if bullet:
            st.markdown(f"- {bullet}")
    st.markdown("</div>", unsafe_allow_html=True)

if EDUCATION:
    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
    st.markdown("## Education")

    for edu in EDUCATION:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"#### {edu['degree']}")
        st.markdown(f"**{edu['institution']}** &nbsp;·&nbsp; <span class='muted'>{edu['period']}</span>", unsafe_allow_html=True)
        st.write(edu["description"])
        if edu.get("courses"):
            st.markdown("<span class='muted'>Relevant courses:</span>", unsafe_allow_html=True)
            tags_html = "".join(f"<span class='tag'>{c}</span>" for c in edu["courses"])
            st.markdown(tags_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
