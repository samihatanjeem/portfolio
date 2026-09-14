import urllib.parse

import streamlit as st

from config import PROFILE, SOCIAL_LINKS
from styles import inject_css

st.set_page_config(page_title=f"Contact - {PROFILE['name']}", page_icon="✉️", layout="centered")
inject_css()

st.markdown("## Contact")
st.markdown(
    "<span class='muted'>Have a project in mind or just want to say hi? Reach out.</span>",
    unsafe_allow_html=True,
)
st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

link_cols = st.columns(len(SOCIAL_LINKS))
for c, (label, url) in zip(link_cols, SOCIAL_LINKS.items()):
    c.link_button(label, url, use_container_width=True)

if PROFILE.get("phone") or PROFILE.get("location"):
    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
    if PROFILE.get("phone"):
        st.markdown(f"📞 {PROFILE['phone']}")
    if PROFILE.get("location"):
        st.markdown(f"📍 {PROFILE['location']}")

st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)
st.markdown("#### Send a message")
st.caption(
    "This opens your visitor's email app with the message pre-filled - "
    "no backend or API key required."
)

with st.form("contact_form"):
    name = st.text_input("Your name")
    sender_email = st.text_input("Your email")
    message = st.text_area("Message", height=150)
    submitted = st.form_submit_button("Prepare Email", use_container_width=True)

if submitted:
    if not name or not sender_email or not message:
        st.warning("Please fill in all fields.")
    else:
        subject = f"Portfolio contact from {name}"
        body = f"{message}\n\n- {name} ({sender_email})"
        mailto_url = (
            f"mailto:{PROFILE['email']}"
            f"?subject={urllib.parse.quote(subject)}"
            f"&body={urllib.parse.quote(body)}"
        )
        st.success("Click below to send your message:")
        st.link_button("📤 Open Email to Send", mailto_url, use_container_width=True)
