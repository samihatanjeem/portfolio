import os

import streamlit as st

from config import CERTIFICATIONS, PROFILE
from styles import inject_css

st.set_page_config(page_title=f"Certifications - {PROFILE['name']}", page_icon="🎓", layout="centered")
inject_css()

st.markdown("## Certifications")
st.markdown("<span class='muted'>Courses and certificates I've completed.</span>", unsafe_allow_html=True)

if not CERTIFICATIONS:
    st.info("No certifications added yet - edit `CERTIFICATIONS` in config.py.")

for cert in CERTIFICATIONS:
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        image = cert.get("image")
        if image:
            is_url = image.startswith("http://") or image.startswith("https://")
            if is_url or os.path.exists(image):
                st.image(image, width=480)

        st.markdown(f"#### {cert['title']}")
        st.markdown("</div>", unsafe_allow_html=True)
