import streamlit as st

from config import PROFILE, SKILLS
from styles import inject_css

st.set_page_config(page_title=f"Skills - {PROFILE['name']}", page_icon="🛠️", layout="centered")
inject_css()

st.markdown("## Skills")
st.markdown("<span class='muted'>Tools and areas I work with.</span>", unsafe_allow_html=True)

if not SKILLS:
    st.info("No skills added yet - edit `SKILLS` in config.py.")

for category, items in SKILLS.items():
    st.markdown(f"#### {category}")
    tags_html = "".join(f"<span class='tag'>{item}</span>" for item in items)
    st.markdown(f"<div class='card'>{tags_html}</div>", unsafe_allow_html=True)
