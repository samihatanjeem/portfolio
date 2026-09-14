"""Shared CSS for a clean, minimal look across all pages."""

import streamlit as st

CUSTOM_CSS = """
<style>
    /* Tighten default top padding */
    .block-container {
        padding-top: 2.2rem;
        padding-bottom: 4rem;
        max-width: 900px;
    }

    /* Headings */
    h1, h2, h3 {
        font-weight: 700;
        letter-spacing: -0.02em;
    }

    /* Card look for containers with the "card" class via markdown wrapper */
    .card {
        border: 1px solid rgba(232, 135, 158, 0.25);
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
        background: #FFFDF9;
        transition: box-shadow 0.15s ease, transform 0.15s ease;
    }
    .card:hover {
        box-shadow: 0 4px 18px rgba(232, 135, 158, 0.18);
        transform: translateY(-2px);
    }

    /* Tag pills */
    .tag {
        display: inline-block;
        padding: 0.15rem 0.6rem;
        margin: 0.15rem 0.3rem 0.15rem 0;
        border-radius: 999px;
        background: #FBE7EC;
        color: #C2557A;
        font-size: 0.8rem;
        font-weight: 600;
    }

    /* Section spacing */
    .section-gap {
        margin-top: 2.5rem;
    }

    /* Muted text */
    .muted {
        color: #8A7A7A;
        font-size: 0.95rem;
    }

    a {
        color: #C2557A;
    }
</style>
"""


def inject_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
