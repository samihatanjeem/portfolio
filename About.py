import base64
import os

import streamlit as st

from config import CERTIFICATIONS, EDUCATION, EXPERIENCE, PROFILE, PROJECTS, SKILLS, SOCIAL_LINKS
from icons import EXTERNAL_LINK, GITHUB, LINKEDIN, MAIL, RESUME, icon_button, icon_pill
from styles import inject_css

st.set_page_config(
    page_title=f"{PROFILE['name']} - Portfolio",
    page_icon="👋",
    layout="centered",
)

inject_css()


def render_html(html: str) -> None:
    """Render an HTML fragment as a single line.

    Streamlit's markdown renderer treats a blank line inside a raw-HTML block
    as the end of that block, so any multi-line f-string built by
    concatenating smaller pieces (e.g. several icon buttons joined together)
    can silently fall back to showing literal HTML text. Collapsing all
    whitespace to single spaces makes that class of bug impossible.
    """
    st.markdown(" ".join(html.split()), unsafe_allow_html=True)


def file_to_data_uri(path: str) -> str:
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    ext = os.path.splitext(path)[1].lstrip(".").lower()
    mime = "jpeg" if ext in ("jpg", "jpeg") else ext
    return f"data:image/{mime};base64,{b64}"


def reveal(delay: float = 0.0) -> str:
    return f'style="animation-delay:{delay}s"'


# ---------- Sticky nav ----------
nav_links = ["About", "Education", "Experience", "Projects", "Certifications", "Contact"]
nav_html = "".join(f'<a href="#{n.lower()}">{n}</a>' for n in nav_links)
render_html(
    f"""
    <div class="site-nav">
        <div class="site-nav-inner">
            <div class="site-nav-brand">{PROFILE['name']}</div>
            <div class="site-nav-links">{nav_html}</div>
        </div>
    </div>
    """
)

# ---------- Hero / About (cutout photo over big text, Skills panel on the right) ----------
first_name = PROFILE["name"].split()[0]
cutout_path = PROFILE.get("profile_cutout_image", "")
has_cutout = bool(cutout_path) and os.path.exists(cutout_path)

if has_cutout:
    hero_visual_html = f"""
        <div class="hero-cutout-wrap">
            <div class="hero-cutout-text">
                <div class="hero-greeting">Hey there!</div>
                <div class="hero-name-big">I'm {first_name}</div>
            </div>
            <img class="hero-cutout-photo" src="{file_to_data_uri(cutout_path)}" />
        </div>
    """
elif os.path.exists(PROFILE["profile_image"]):
    hero_visual_html = f"""
        <div style="width:220px; height:220px; border-radius:50%; overflow:hidden; margin:0 auto 1.5rem; background:#FBE7EC;">
            <img src="{file_to_data_uri(PROFILE["profile_image"])}" style="width:100%;height:100%;object-fit:cover;display:block;" />
        </div>
    """
else:
    hero_visual_html = f"""
        <div style="width:220px; height:220px; border-radius:50%; margin:0 auto 1.5rem; background:#FBE7EC;
             display:flex;align-items:center;justify-content:center;
             font-size:4rem;color:#C2557A;font-weight:700;">{PROFILE['name'][:1].upper()}</div>
    """

social_icons = {"GitHub": GITHUB, "LinkedIn": LINKEDIN, "Email": MAIL}
social_html = "".join(
    icon_button(social_icons.get(label, MAIL), url, label) for label, url in SOCIAL_LINKS.items()
)
if os.path.exists(PROFILE["resume_path"]):
    resume_data_uri = file_to_data_uri(PROFILE["resume_path"])
    social_html += icon_button(RESUME, resume_data_uri, "Resume")

skill_groups_html = ""
for category, items in SKILLS.items():
    tags_html = "".join(f'<span class="tag">{item}</span>' for item in items)
    skill_groups_html += f'<div class="skill-group-title">{category}</div><div class="tag-row">{tags_html}</div>'

render_html(
    f"""
    <section id="about" class="section">
        <div class="section-inner reveal" {reveal(0.0)}>
            {hero_visual_html}
            <div class="hero-below">
                <div class="hero-title">{PROFILE['title']}</div>
                <div class="hero-tagline">{PROFILE['tagline']}</div>
                <div class="icon-row">{social_html}</div>
            </div>
            <div class="about-grid">
                <div class="about-left">
                    <p style="font-size:1.05rem; line-height:1.7;">{PROFILE['bio']}</p>
                    <p class="muted">📍 {PROFILE.get('location', '')}</p>
                </div>
                <div class="about-right">
                    <div class="skills-panel">
                        <div class="section-label">Tools &amp; areas</div>
                        <div class="skills-panel-title">Skills</div>
                        {skill_groups_html if SKILLS else '<p class="muted">No skills added yet.</p>'}
                    </div>
                </div>
            </div>
        </div>
    </section>
    """
)

render_html('<div class="divider"></div>')

# ---------- Education ----------
edu_html = ""
for edu in EDUCATION:
    courses_html = ""
    if edu.get("courses"):
        tags = "".join(f'<span class="tag">{c}</span>' for c in edu["courses"])
        courses_html = f'<div class="muted" style="margin-top:0.5rem;">Relevant courses</div><div class="tag-row">{tags}</div>'
    edu_html += f"""
        <div class="timeline-item">
            <div class="card-title">{edu['degree']}</div>
            <div class="card-meta">{edu['institution']} &nbsp;·&nbsp; {edu['period']}</div>
            <div class="card-body">{edu.get('description', '')}</div>
            {courses_html}
        </div>
    """

render_html(
    f"""
    <section id="education" class="section">
        <div class="section-inner reveal" {reveal(0.05)}>
            <div class="section-label">Where I've studied</div>
            <div class="section-title">Education</div>
            {edu_html}
        </div>
    </section>
    """
)

render_html('<div class="divider"></div>')

# ---------- Experience ----------
exp_html = ""
for job in EXPERIENCE:
    bullets = job.get("bullets") or [job.get("description", "")]
    bullets_html = "".join(f"<li>{b}</li>" for b in bullets if b)
    impact_html = f'<div class="card-impact"><b>Impact —</b> {job["impact"]}</div>' if job.get("impact") else ""
    exp_html += f"""
        <div class="timeline-item">
            <div class="card-title">{job['role']}</div>
            <div class="card-meta">{job['organization']} &nbsp;·&nbsp; {job['period']}</div>
            {impact_html}
            <ul style="margin:0; padding-left:1.1rem; font-size:0.92rem; line-height:1.6;">{bullets_html}</ul>
        </div>
    """

render_html(
    f"""
    <section id="experience" class="section">
        <div class="section-inner reveal" {reveal(0.05)}>
            <div class="section-label">Where I've worked</div>
            <div class="section-title">Experience</div>
            {exp_html}
        </div>
    </section>
    """
)

render_html('<div class="divider"></div>')

# ---------- Projects ----------
project_cards = ""
for p in PROJECTS:
    tags_html = "".join(f'<span class="tag">{t}</span>' for t in p.get("tags", []))
    links_html = ""
    if p.get("demo_url"):
        links_html += icon_pill(EXTERNAL_LINK, p["demo_url"], "Live Demo")
    if p.get("repo_url"):
        links_html += icon_pill(GITHUB, p["repo_url"], "Source Code")
    image_html = f'<div class="card-image"><img src="{p["image"]}" /></div>' if p.get("image") else ""
    impact_html = f'<div class="card-impact"><b>Impact —</b> {p["impact"]}</div>' if p.get("impact") else ""
    project_cards += f"""
        <div class="card">
            {image_html}
            <div class="card-title">{p['title']}</div>
            <div class="card-meta">{p.get('date', '')}</div>
            <div class="card-body">{p['description']}</div>
            {impact_html}
            <div class="tag-row">{tags_html}</div>
            <div class="pill-row">{links_html}</div>
        </div>
    """

render_html(
    f"""
    <section id="projects" class="section">
        <div class="section-inner reveal" {reveal(0.05)}>
            <div class="section-label">What I've built</div>
            <div class="section-title">Projects</div>
            {project_cards if PROJECTS else '<p class="muted">No projects added yet.</p>'}
        </div>
    </section>
    """
)

render_html('<div class="divider"></div>')

# ---------- Certifications ----------
cert_cards = ""
for c in CERTIFICATIONS:
    image = c.get("image")
    img_html = ""
    if image:
        if image.startswith("http://") or image.startswith("https://"):
            img_html = f'<div class="card-image"><img src="{image}" /></div>'
        elif os.path.exists(image):
            img_html = f'<div class="card-image"><img src="{file_to_data_uri(image)}" /></div>'
    cert_cards += f"""
        <div class="card">
            {img_html}
            <div class="card-title">{c['title']}</div>
        </div>
    """

render_html(
    f"""
    <section id="certifications" class="section">
        <div class="section-inner reveal" {reveal(0.05)}>
            <div class="section-label">Always learning</div>
            <div class="section-title">Certifications</div>
            {cert_cards if CERTIFICATIONS else '<p class="muted">No certifications added yet.</p>'}
        </div>
    </section>
    """
)

render_html('<div class="divider"></div>')

# ---------- Contact ----------
contact_icons = {"GitHub": GITHUB, "LinkedIn": LINKEDIN, "Email": MAIL}
contact_html = "".join(
    icon_button(contact_icons.get(label, MAIL), url, label) for label, url in SOCIAL_LINKS.items()
)

render_html(
    f"""
    <section id="contact" class="section">
        <div class="section-inner reveal" {reveal(0.05)}>
            <div class="section-label">Let's talk</div>
            <div class="section-title">Contact</div>
            <p style="max-width:32rem;">Have a project in mind or just want to say hi? Reach out any of these ways.</p>
            <div class="icon-row">{contact_html}</div>
            <p class="muted" style="margin-top:1.5rem;">
                📞 {PROFILE.get('phone', '')} &nbsp;&nbsp; 📍 {PROFILE.get('location', '')}
            </p>
        </div>
    </section>
    <div class="site-footer">© {PROFILE['name']}</div>
    """
)
