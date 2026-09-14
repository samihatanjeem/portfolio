"""Shared CSS for the single-page portfolio: typography, nav, cards, motion."""

import streamlit as st

NAV_HEIGHT = 64

CUSTOM_CSS = f"""
<style>
    html {{ scroll-behavior: smooth; }}

    /* Hide default Streamlit chrome so the page reads as a site, not an app */
    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}
    header[data-testid="stHeader"] {{ background: transparent; }}

    .stApp {{ background: #FFFDF9; }}

    .block-container {{
        padding-top: {NAV_HEIGHT + 24}px;
        padding-bottom: 5rem;
        max-width: 980px;
    }}

    h1, h2, h3, h4 {{
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #33262A;
    }}

    p, li, span {{ color: #4A3B3B; }}

    a {{ color: #C2557A; text-decoration: none; }}

    /* ---------- Sticky top nav ---------- */
    .site-nav {{
        position: fixed;
        top: 0; left: 0; right: 0;
        height: {NAV_HEIGHT}px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255, 253, 249, 0.85);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(232, 135, 158, 0.18);
        z-index: 9999;
    }}
    .site-nav-inner {{
        width: 100%;
        max-width: 980px;
        padding: 0 1.5rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    .site-nav-brand {{
        font-weight: 700;
        font-size: 1rem;
        color: #33262A;
        letter-spacing: -0.01em;
    }}
    .site-nav-links {{
        display: flex;
        gap: 1.75rem;
        flex-wrap: wrap;
    }}
    .site-nav-links a {{
        color: #4A3B3B;
        font-size: 0.9rem;
        font-weight: 500;
        position: relative;
        padding-bottom: 4px;
    }}
    .site-nav-links a::after {{
        content: "";
        position: absolute;
        left: 0; bottom: 0;
        width: 0%;
        height: 2px;
        background: #C2557A;
        transition: width 0.25s ease;
    }}
    .site-nav-links a:hover::after {{ width: 100%; }}
    .site-nav-links a:hover {{ color: #C2557A; }}

    @media (max-width: 640px) {{
        .site-nav-links {{ gap: 1rem; }}
        .site-nav-links a {{ font-size: 0.8rem; }}
    }}

    /* ---------- Sections ---------- */
    .section {{
        padding-top: 5rem;
        margin-top: -5rem;
    }}
    .section-inner {{ padding: 2.5rem 0; }}
    .section-label {{
        text-transform: uppercase;
        letter-spacing: 0.12em;
        font-size: 0.75rem;
        font-weight: 700;
        color: #C2557A;
        margin-bottom: 0.5rem;
    }}
    .section-title {{
        font-size: clamp(1.6rem, 3.2vw, 2.2rem);
        margin-bottom: 2rem;
    }}

    /* ---------- Hero ---------- */
    .hero-name {{
        font-size: clamp(2.4rem, 6vw, 4rem);
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.05;
        margin-bottom: 0.4rem;
        color: #33262A;
    }}
    .hero-title {{
        font-size: clamp(1.1rem, 2vw, 1.35rem);
        font-weight: 600;
        color: #C2557A;
        margin-bottom: 0.6rem;
    }}
    .hero-tagline {{
        font-size: 1.05rem;
        color: #7A6A6A;
        max-width: 32rem;
        margin-bottom: 1.5rem;
    }}

    /* ---------- Fade/slide-in on load ---------- */
    @keyframes fadeSlideUp {{
        from {{ opacity: 0; transform: translateY(16px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    .reveal {{
        animation: fadeSlideUp 0.7s ease both;
    }}

    /* ---------- Icon buttons (hero social links) ---------- */
    .icon-row {{ display: flex; gap: 0.75rem; flex-wrap: wrap; }}
    .icon-btn {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.55rem 1rem;
        border-radius: 999px;
        border: 1px solid rgba(232, 135, 158, 0.35);
        background: #FFFFFF;
        color: #33262A;
        font-size: 0.88rem;
        font-weight: 600;
        transition: background 0.2s ease, border-color 0.2s ease, transform 0.15s ease;
    }}
    .icon-btn:hover {{
        background: #FBE7EC;
        border-color: #C2557A;
        transform: translateY(-2px);
        color: #33262A;
    }}
    .icon-btn-glyph {{ width: 18px; height: 18px; display: inline-flex; color: #C2557A; }}
    .icon-btn-glyph svg {{ width: 100%; height: 100%; }}

    /* ---------- Cards ---------- */
    .card {{
        border: 1px solid rgba(232, 135, 158, 0.22);
        border-radius: 16px;
        padding: 1.5rem 1.75rem;
        margin-bottom: 1.25rem;
        background: #FFFFFF;
        transition: box-shadow 0.2s ease, transform 0.2s ease, border-color 0.2s ease;
    }}
    .card:hover {{
        box-shadow: 0 10px 30px rgba(232, 135, 158, 0.16);
        transform: translateY(-3px);
        border-color: rgba(232, 135, 158, 0.4);
    }}
    .card-image {{
        width: 100%;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 1rem;
        aspect-ratio: 1200 / 630;
        background: #FBE7EC;
    }}
    .card-image img {{
        width: 100%; height: 100%; object-fit: cover; display: block;
    }}
    .card-title {{
        font-size: 1.15rem;
        font-weight: 700;
        color: #33262A;
        margin-bottom: 0.15rem;
    }}
    .card-meta {{
        font-size: 0.85rem;
        color: #9A8A8A;
        margin-bottom: 0.75rem;
    }}
    .card-body {{
        font-size: 0.95rem;
        color: #4A3B3B;
        line-height: 1.55;
        margin-bottom: 0.75rem;
    }}
    .card-impact {{
        font-size: 0.9rem;
        color: #33262A;
        background: #FBE7EC;
        border-left: 3px solid #C2557A;
        border-radius: 6px;
        padding: 0.6rem 0.85rem;
        margin-bottom: 0.9rem;
        line-height: 1.5;
    }}
    .card-impact b {{ color: #C2557A; }}

    /* ---------- Tag pills ---------- */
    .tag-row {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 0.75rem; }}
    .tag {{
        display: inline-block;
        padding: 0.2rem 0.65rem;
        border-radius: 999px;
        background: #FBE7EC;
        color: #C2557A;
        font-size: 0.78rem;
        font-weight: 600;
    }}

    /* ---------- Icon pill links (repo/demo) ---------- */
    .pill-row {{ display: flex; gap: 0.6rem; flex-wrap: wrap; margin-top: 0.25rem; }}
    .icon-pill {{
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.4rem 0.85rem;
        border-radius: 999px;
        border: 1px solid rgba(232, 135, 158, 0.3);
        font-size: 0.82rem;
        font-weight: 600;
        color: #33262A;
        transition: background 0.2s ease, transform 0.15s ease;
    }}
    .icon-pill:hover {{ background: #FBE7EC; transform: translateY(-1px); color: #33262A; }}
    .icon-pill-glyph {{ width: 14px; height: 14px; display: inline-flex; color: #C2557A; }}
    .icon-pill-glyph svg {{ width: 100%; height: 100%; }}

    /* ---------- Skill groups ---------- */
    .skill-group-title {{
        font-size: 0.95rem;
        font-weight: 700;
        color: #33262A;
        margin: 1.25rem 0 0.5rem;
    }}

    /* ---------- Experience timeline ---------- */
    .timeline-item {{
        position: relative;
        padding-left: 1.5rem;
        border-left: 2px solid rgba(232, 135, 158, 0.3);
        padding-bottom: 2rem;
    }}
    .timeline-item::before {{
        content: "";
        position: absolute;
        left: -6px; top: 4px;
        width: 10px; height: 10px;
        border-radius: 50%;
        background: #C2557A;
    }}
    .timeline-item:last-child {{ border-left-color: transparent; }}

    /* ---------- Muted text / divider ---------- */
    .muted {{ color: #8A7A7A; font-size: 0.95rem; }}
    .divider {{ height: 1px; background: rgba(232, 135, 158, 0.2); margin: 3.5rem 0; }}

    /* ---------- Footer ---------- */
    .site-footer {{
        text-align: center;
        color: #9A8A8A;
        font-size: 0.85rem;
        padding-top: 3rem;
    }}
</style>
"""


def inject_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
