import base64
import os

import streamlit as st

from config import PROFILE, SOCIAL_LINKS
from styles import inject_css

st.set_page_config(
    page_title=f"{PROFILE['name']} - Portfolio",
    page_icon="👋",
    layout="centered",
)

inject_css()

# --- Hero section ---
col_img, col_text = st.columns([1, 2], gap="large")

with col_img:
    if os.path.exists(PROFILE["profile_image"]):
        with open(PROFILE["profile_image"], "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
        ext = os.path.splitext(PROFILE["profile_image"])[1].lstrip(".").lower()
        mime = "jpeg" if ext in ("jpg", "jpeg") else ext
        st.markdown(
            f"""
            <div style="width:100%; aspect-ratio:1/1; border-radius:50%; overflow:hidden;">
                <img src="data:image/{mime};base64,{img_b64}"
                     style="width:100%; height:100%; object-fit:cover; display:block;" />
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div style="
                width:100%; aspect-ratio:1/1; border-radius:50%;
                background:#FBE7EC; display:flex;
                align-items:center; justify-content:center;
                font-size:3rem; color:#C2557A; font-weight:700;">
                {initial}
            </div>
            """.format(initial=PROFILE["name"][:1].upper()),
            unsafe_allow_html=True,
        )

with col_text:
    st.markdown(f"## {PROFILE['name']}")
    st.markdown(f"**{PROFILE['title']}**")
    st.markdown(f"<span class='muted'>{PROFILE['tagline']}</span>", unsafe_allow_html=True)

    link_cols = st.columns(len(SOCIAL_LINKS))
    for c, (label, url) in zip(link_cols, SOCIAL_LINKS.items()):
        c.link_button(label, url, use_container_width=True)

st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
st.markdown("### About")
st.write(PROFILE["bio"])

if PROFILE.get("location"):
    st.markdown(f"📍 {PROFILE['location']}")

# --- Resume download ---
if os.path.exists(PROFILE["resume_path"]):
    with open(PROFILE["resume_path"], "rb") as f:
        st.download_button(
            "📄 Download Resume",
            data=f,
            file_name=os.path.basename(PROFILE["resume_path"]),
            mime="application/pdf",
        )
else:
    st.caption(
        f"ℹ️ Add your resume PDF at `{PROFILE['resume_path']}` to enable the download button."
    )

st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
st.info("Use the sidebar to explore my **Projects**, **Skills**, **Experience**, and **Contact** info.")
