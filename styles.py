"""Shared CSS for the single-page portfolio: typography, nav, cards, motion."""

import streamlit as st

CUSTOM_CSS = f"""
<style>
    /* Streamlit scrolls an inner container, not the document - so smooth
       scrolling has to be set there or anchor jumps teleport instantly. */
    html, body {{ scroll-behavior: smooth; }}
    [data-testid="stMain"],
    [data-testid="stAppViewContainer"] {{ scroll-behavior: smooth !important; }}

    /* Hide default Streamlit chrome entirely so the page reads as a site, not an app.
       Our own nav no longer lives in the top strip (it's a right-side rail now),
       so there's no more reason to keep any part of this toolbar interactive. */
    #MainMenu {{ display: none !important; }}
    footer {{ display: none !important; }}
    header[data-testid="stHeader"] {{ display: none !important; }}

    .stApp {{ background: #FFFDF9; }}

    /* Streamlit adds a default gap between every element block, even
       invisible/zero-height ones (our injected <style> tag, the brand
       div, the nav rail) - that stacks up as dead space before any real
       content. Our own CSS (.divider, .section-inner, etc.) already
       controls spacing explicitly, so this is safe to zero out globally. */
    [data-testid="stVerticalBlock"] {{ gap: 0 !important; }}

    .block-container {{
        padding-top: 0.6rem;
        padding-bottom: 5rem;
        padding-right: 9.5rem;
        max-width: 980px;
    }}

    h1, h2, h3, h4 {{
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #33262A;
    }}

    p, li, span {{ color: #4A3B3B; }}

    a {{ color: #C2557A; text-decoration: none; }}

    /* ---------- Brand mark (top-left) ---------- */
    .site-brand {{
        position: fixed;
        top: 1.3rem; left: 1.5rem;
        font-weight: 700;
        font-size: 1rem;
        color: #33262A;
        letter-spacing: -0.01em;
        z-index: 9999;
    }}

    /* ---------- Thin vertical nav rail (right side) ---------- */
    .site-nav {{
        position: fixed;
        top: 0; right: 0; bottom: 0;
        width: 132px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255, 253, 249, 0.85);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-left: 1px solid rgba(232, 135, 158, 0.2);
        z-index: 9999;
    }}
    .site-nav-links {{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.9rem;
    }}
    .site-nav-links a {{
        display: block;
        color: #4A3B3B;
        font-size: 0.8rem;
        font-weight: 600;
        position: relative;
        text-align: center;
        padding-top: 1.5rem;
        transition: color 0.2s ease, transform 0.2s ease;
    }}
    .site-nav-links a:hover {{
        color: #C2557A;
        transform: scale(1.08);
    }}
    .site-nav-cat {{
        position: absolute;
        top: 0.1rem;
        left: 50%;
        transform: translate(-50%, 0) scale(0.3) rotate(-8deg);
        font-size: 1.5rem;
        opacity: 0;
        pointer-events: none;
        transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.2s ease;
        filter: drop-shadow(0 4px 6px rgba(51, 38, 42, 0.25));
    }}
    .site-nav-links a:hover .site-nav-cat {{
        transform: translate(-50%, -0.3rem) scale(1) rotate(0deg);
        opacity: 1;
    }}

    @media (max-width: 720px) {{
        .site-nav {{ width: 92px; }}
        .site-nav-links {{ gap: 1.3rem; }}
        .site-nav-links a {{ font-size: 0.7rem; padding-top: 1.3rem; }}
        .site-nav-cat {{ font-size: 1.2rem; }}
        .block-container {{ padding-right: 6rem; }}
        .site-brand {{ font-size: 0.85rem; left: 1rem; }}
    }}

    /* ---------- Sections ---------- */
    .section {{
        padding-top: 1.5rem;
        margin-top: -1.5rem;
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

    /* ---------- Hero flank (photo centered, greeting split left/right) ---------- */
    .hero-flank {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0;
        margin-bottom: 1.5rem;
    }}
    .hero-flank-col {{
        display: flex;
        flex-direction: column;
        justify-content: center;
        gap: 0;
        flex: 0 1 auto;
        min-width: 0;
        padding: 1rem 0;
    }}
    .hero-flank-col-left {{ align-items: flex-end; text-align: right; }}
    .hero-flank-col-right {{ align-items: flex-start; text-align: left; }}
    .hero-flank-word {{
        font-size: clamp(2.4rem, 8vw, 6rem);
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.05;
        color: #33262A;
        white-space: nowrap;
    }}
    .hero-flank-word.accent {{ color: #C2557A; font-weight: 600; font-size: clamp(1.5rem, 4.5vw, 2.8rem); }}
    .type-left {{ animation: typeInLeft 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; will-change: transform, opacity; }}
    .type-right {{ animation: typeInRight 0.8s cubic-bezier(0.16, 1, 0.3, 1) both; will-change: transform, opacity; }}
    @keyframes typeInLeft {{
        from {{ opacity: 0; transform: translateX(-36px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    @keyframes typeInRight {{
        from {{ opacity: 0; transform: translateX(36px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}
    .hero-cutout-photo {{
        flex-shrink: 0;
        max-height: 480px;
        width: auto;
        max-width: 100%;
        display: block;
        filter: drop-shadow(0 24px 28px rgba(51, 38, 42, 0.18));
    }}
    .hero-below {{
        text-align: center;
        margin-bottom: 3rem;
    }}
    .hero-below .hero-title {{ margin-bottom: 0.3rem; }}
    .hero-below .hero-tagline {{ max-width: 36rem; margin: 0 auto 1.5rem; }}
    .hero-below .icon-row {{ justify-content: center; }}

    @media (max-width: 820px) {{
        .hero-flank {{ flex-direction: column; gap: 0.5rem; }}
        .hero-flank-col {{
            flex-direction: row; height: auto; width: 100%;
            justify-content: center; gap: 0.6rem; padding: 0;
        }}
        .hero-flank-col-left, .hero-flank-col-right {{ text-align: center; align-items: center; }}
        .hero-flank-word {{ font-size: clamp(1.6rem, 8vw, 2.4rem); white-space: normal; }}
        .hero-flank-word.accent {{ font-size: clamp(1.1rem, 5vw, 1.4rem); }}
        .hero-cutout-photo {{ max-height: 320px; order: -1; margin-bottom: 0.5rem; }}
    }}

    /* ---------- Org logos (education / experience) ---------- */
    .org-meta-row {{
        display: flex;
        align-items: center;
        gap: 0.65rem;
        margin-bottom: 0.6rem;
        flex-wrap: wrap;
    }}
    .org-logo-wrap {{
        width: 56px;
        height: 34px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }}
    .edu-indent {{
        margin-left: calc(56px + 0.65rem);
    }}
    .org-logo {{
        height: 34px !important;
        width: auto !important;
        max-width: 56px !important;
        object-fit: contain !important;
        border-radius: 6px;
        flex-shrink: 0;
    }}
    .org-meta {{
        font-size: 1rem;
        font-weight: 600;
        color: #4A3B3B;
    }}

    /* ---------- Scroll-triggered reveal (JS toggles .pre-hide/.in-view) ---------- */
    /* Section-level: the heading block glides up as the section arrives. */
    .reveal {{
        transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1),
                    transform 0.85s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .reveal.pre-hide {{ opacity: 0; transform: translateY(34px); }}
    .reveal.in-view {{ opacity: 1; transform: translateY(0); }}

    /* Item-level: individual cards / timeline entries rise in as they each
       reach the viewport, so long sections stay alive the whole way down
       instead of everything appearing at once at the section boundary. */
    .reveal-item {{
        transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1),
                    transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
        will-change: transform, opacity;
    }}
    .reveal-item.pre-hide {{ opacity: 0; transform: translateY(26px) scale(0.985); }}
    .reveal-item.in-view {{ opacity: 1; transform: translateY(0) scale(1); }}

    /* ---------- Cat runner (click-to-navigate animation) ---------- */
    .cat-runner {{
        position: fixed;
        right: 28px;
        font-size: 1.9rem;
        z-index: 10000;
        pointer-events: none;
        filter: drop-shadow(0 6px 8px rgba(51, 38, 42, 0.3));
        animation-name: catRunDown;
        animation-duration: 1s;
        animation-timing-function: cubic-bezier(0.45, 0, 0.55, 1);
        animation-fill-mode: forwards;
    }}
    .cat-runner.run-up {{ animation-name: catRunUp; }}
    @keyframes catRunDown {{
        0%   {{ transform: translateY(0) scale(1) rotate(0deg); opacity: 1; }}
        10%  {{ transform: translateY(-16px) scale(1.15, 0.9) rotate(-10deg); }}
        22%  {{ transform: translateY(60px) scale(0.9, 1.1) rotate(6deg); }}
        34%  {{ transform: translateY(46px) scale(1.1, 0.9) rotate(-8deg); }}
        46%  {{ transform: translateY(150px) scale(0.9, 1.1) rotate(6deg); }}
        58%  {{ transform: translateY(136px) scale(1.1, 0.9) rotate(-8deg); }}
        70%  {{ transform: translateY(230px) scale(0.9, 1.1) rotate(6deg); }}
        85%  {{ transform: translateY(280px) scale(1, 1) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(320px) scale(0.6) rotate(0deg); opacity: 0; }}
    }}
    @keyframes catRunUp {{
        0%   {{ transform: translateY(0) scale(1) rotate(0deg); opacity: 1; }}
        10%  {{ transform: translateY(16px) scale(1.15, 0.9) rotate(10deg); }}
        22%  {{ transform: translateY(-60px) scale(0.9, 1.1) rotate(-6deg); }}
        34%  {{ transform: translateY(-46px) scale(1.1, 0.9) rotate(8deg); }}
        46%  {{ transform: translateY(-150px) scale(0.9, 1.1) rotate(-6deg); }}
        58%  {{ transform: translateY(-136px) scale(1.1, 0.9) rotate(8deg); }}
        70%  {{ transform: translateY(-230px) scale(0.9, 1.1) rotate(-6deg); }}
        85%  {{ transform: translateY(-280px) scale(1, 1) rotate(0deg); opacity: 1; }}
        100% {{ transform: translateY(-320px) scale(0.6) rotate(0deg); opacity: 0; }}
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
        max-width: 440px;
        border-radius: 10px;
        overflow: hidden;
        margin: 0 auto 1.1rem;
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
