#!/usr/bin/env python3
"""Builds the CNP website pages into ../public_html.

Edit the content below (projects, team, text), then run:
    python3 tools/build.py
The generated HTML in public_html/ is what goes live on cnpesl.com.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public_html"

SITE = "https://cnpesl.com"
PHONE = "+234 806 909 4133"
PHONE_LINK = "+2348069094133"
WHATSAPP = "https://wa.me/2348069094133"
EMAIL = "office@cnpesl.com"
ADDRESS = "13 Tangayika Crescent, Crown Estate, Lekki, Lagos, Nigeria"
MAP_EMBED = "https://www.google.com/maps?q=13+Tangayika+Crescent,+Crown+Estate,+Lekki,+Lagos,+Nigeria&output=embed"

NAV = [("index.html", "Home"), ("services.html", "Services"), ("projects.html", "Projects"), ("about.html", "About")]

# ---------------------------------------------------------------- projects
# kind "model" = 3D structural model on white (shown whole, not cropped)
DESIGN_PROJECTS = [
    dict(name="Enyimba Hotel (Radisson), Aba", place="Aba, Abia State", scope="Structural assessment, design and construction supervision", sector="Hospitality",
         img="enyimba-radisson-render.jpg", alt="Render of the Radisson hotel, Aba"),
    dict(name="Piers Place, Yaba", place="Yaba, Lagos", scope="Structural design and supervision", sector="Commercial",
         img="piers-place-completed.jpg", alt="Completed Piers Place office building in Yaba"),
    dict(name="Royal Centre, Oniru", place="Victoria Island, Lagos", scope="Structural design and construction supervision", sector="Commercial",
         img="oniru-royal-centre.jpg", alt="Structural model of the Royal Centre at Oniru", kind="model"),
    dict(name="Commercial development, Norman Street", place="South-West Ikoyi, Lagos", scope="Structural design of a 4-storey development", sector="Commercial",
         img="norman-street-ikoyi.jpg", alt="Structural model of the Norman Street development", kind="model"),
    dict(name="The Mall, Karu", place="International Market, Mararaba, Nasarawa State", scope="Structural design of a shopping mall", sector="Retail",
         img="mall-karu.jpg", alt="Render of The Mall, Karu", kind="model"),
    dict(name="LEAP Africa Leadership Centre", place="Abijo Town, Lekki-Epe Expressway", scope="Structural design of a 6-storey building", sector="Institutional",
         img="leap-africa.jpg", alt="Structural frame model of the LEAP Africa Leadership Centre", kind="model"),
    dict(name="K'Maroun Complex, Ijora", place="Ijora, Lagos", scope="Structural engineering design", sector="Commercial",
         img="kmaroun-ijora.jpg", alt="3D structural view of the K'Maroun Complex", kind="model"),
    dict(name="Lekki Hub / GTBank branch, Jabi", place="Jabi, Abuja", scope="Structural design for building remodelling", sector="Corporate",
         img="gtbank-jabi.jpg", alt="Render of the remodelled GTBank branch at Jabi"),
]

SURVEYS = [
    dict(name="Bookshop House, Broad Street", place="Lagos Island", img="bookshop-house.jpg", alt="Bookshop House on Broad Street, Lagos",
         text="Structural assessment using NDT methods to appraise severe fire damage to the existing structural frame."),
    dict(name="Enyimba Hotel, Aba", place="Aba, Abia State", img="enyimba-hotel-existing.jpg", alt="Existing Enyimba Hotel structure in Aba",
         text="Comprehensive structural integrity assessment and extensive NDT mapping of a long-standing hotel structure."),
    dict(name="Total E&P Cooperative Logistics Base, Oniru", place="Victoria Island, Lagos", img="total-ep-oniru.jpg", alt="Total E&P logistics warehouse at Oniru",
         text="High-precision structural integrity assessment and comprehensive NDT evaluation of a critical logistics facility."),
    dict(name="Purple Mall, Lekki", place="Lekki, Lagos", img="purple-mall-lekki.jpg", alt="Purple Mall, Lekki",
         text="Structural engineering review and complete structural integrity assessment to verify material capacity."),
]

HOME_PICKS = [0, 1, 2, 5, 7, 4]  # indices into DESIGN_PROJECTS shown on the home page

# -------------------------------------------------------------------- team
LEADERS = [
    dict(name="Engr. Chukwuma Mbachu", role="Principal Partner", quals="B.Sc., MNSE, MNICE, COREN, MASCE",
         text="Leads structural engineering, NDT interpretation and business development."),
    dict(name="Engr. Moses Ebrugba", role="Associate Partner", quals="M.Sc. (Civil Eng.), C.Eng., MNSE, COREN",
         text="Oversees civil infrastructure and quality assurance and control."),
    dict(name="Engr. Nnamdi Udeh", role="Associate Partner", quals="B.Sc., MNSE, MNIStructE",
         text="Links the NDT laboratory with field operations and keeps equipment calibrated."),
    dict(name="Engr. Emmanuel Okoye", role="Project Manager", quals="B.Sc., C.Eng.",
         text="Manages project execution and the deployment of structural engineering work."),
]
CORE = [
    dict(name="Jennifer Peters", role="Senior Structural Engineer", text="Advanced structural analysis, data interpretation and detailed assessment reports."),
    dict(name="Taiwo Sowunmi", role="Field Inspection Engineer", text="On-site structural inspections and material sampling."),
    dict(name="Ruth Okeniyi", role="HSE and Site Safety Officer", text="Compliance with safety and environmental standards. B.Sc. Civil Engineering, First Class Honours (University of Lagos)."),
    dict(name="Daniel Olamide", role="Engineering Technician", text="Support for engineering operations and equipment handling."),
]

# --------------------------------------------------------------- templates
FONTS = '<link rel="preload" href="assets/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>'


def head(title, desc, path):
    url = SITE + "/" + ("" if path == "index.html" else path)
    return f"""<!doctype html>
<html lang="en-NG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/alpha01-helipad-pour.jpg">
<meta name="theme-color" content="#1e4f50">
<link rel="icon" type="image/png" sizes="32x32" href="assets/img/icon-32.png">
<link rel="apple-touch-icon" href="assets/img/icon-180.png">
{FONTS}
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(path):
    cur = ' aria-current="page"'
    links = "".join(
        f'<a href="{href}"{cur if href == path else ""}>{label}</a>' for href, label in NAV)
    return f"""<header class="site-head">
  <div class="wrap">
    <a class="brand" href="index.html"><img src="assets/img/cnp-logo.png" width="760" height="268" alt="CNP Engineering Services"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn" href="contact.html"{' aria-current="page"' if path == "contact.html" else ""}>Contact us</a></nav>
  </div>
</header>
<main id="main">
"""


def footer():
    return f"""</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="foot-logo" href="index.html"><img src="assets/img/cnp-logo.png" width="760" height="268" alt="CNP Engineering Services"></a>
        <p style="margin-top:16px">Integrated structural design, construction supervision and advanced diagnostics.</p>
      </div>
      <div>
        <h4>Office</h4>
        <p>13 Tangayika Crescent,<br>Crown Estate, Lekki,<br>Lagos, Nigeria</p>
      </div>
      <div>
        <h4>Talk to us</h4>
        <ul>
          <li><a href="tel:{PHONE_LINK}">{PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{WHATSAPP}">WhatsApp</a></li>
        </ul>
      </div>
      <div>
        <h4>Follow</h4>
        <ul>
          <li><a href="https://www.linkedin.com/company/cnp-engineering-services/">LinkedIn</a></li>
          <li><a href="https://www.instagram.com/cnp_engineering_services/">Instagram</a></li>
          <li><a href="https://www.youtube.com/@cnpmedia9969">YouTube</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-base">
      <span>&copy; <span data-year>2026</span> CNP Engineering Services Ltd. RC 1424081.</span>
      <span>COREN-registered practice. Lagos State licensed NDT laboratory.</span>
    </div>
  </div>
</footer>
<a class="wa" href="{WHATSAPP}" aria-label="Chat with CNP on WhatsApp">WhatsApp us</a>
<script src="assets/js/site.js" defer></script>
</body>
</html>
"""


def page(path, title, desc, body):
    (OUT / path).write_text(head(title, desc, path) + header(path) + body + footer(), encoding="utf-8")


def tb(cells, wide=None, cols=None):
    style = f' style="--cols:{cols}"' if cols else ""
    w = f'<div class="wide"><span class="k">Project</span><span class="v">{escape(wide)}</span></div>' if wide else ""
    inner = "".join(f'<div><span class="k">{escape(k)}</span><span class="v">{escape(v)}</span></div>' for k, v in cells)
    return f'<div class="tb"{style}>{w}{inner}</div>'


def project_card(p):
    cls = "img model" if p.get("kind") == "model" else "img"
    return f"""<figure class="project">
  <div class="{cls}"><img src="assets/img/{p['img']}" alt="{escape(p['alt'])}" loading="lazy"></div>
  <figcaption>{tb([("Location", p['place']), ("Sector", p['sector']), ("Scope", p['scope'])], wide=p['name'])}</figcaption>
</figure>"""


def survey_row(s):
    return f"""<article class="survey">
  <img src="assets/img/{s['img']}" alt="{escape(s['alt'])}" loading="lazy">
  <div><h3>{escape(s['name'])}</h3><div class="where">{escape(s['place'])}</div><p>{escape(s['text'])}</p></div>
</article>"""


NDT_BAND = """<section class="band on-dark grid-bg" id="ndt">
  <div class="wrap ndt">
    <div>
      <h2>Our NDT laboratory</h2>
      <p class="intro">CNP runs a fully equipped non-destructive testing laboratory, licensed by the Lagos State Government. Quality assurance managers and facility owners get clear, data-driven evidence of how their structures and materials are performing.</p>
      <ul class="checks">
        <li>Structural investigation</li>
        <li>Material appraisal</li>
        <li>Accurate data gathering</li>
      </ul>
    </div>
    <div class="equip">
      <div>
        <h3>Strength and integrity</h3>
        <h4>Equipment</h4><p>Original Schmidt hammers, MATEST ultrasonic pulse velocity tester</p>
        <h4>Purpose</h4><p>Compressive strength measurement and internal uniformity assessment, detecting voids and deep-seated anomalies</p>
      </div>
      <div>
        <h3>Sub-surface and rebar</h3>
        <h4>Equipment</h4><p>Profoscope, LG-G100 rebar detector</p>
        <h4>Purpose</h4><p>Locating embedded reinforcement, measuring concrete cover and mapping rebar grids</p>
      </div>
      <div>
        <h3>Dimensional and flaw</h3>
        <h4>Equipment</h4><p>HC-F600 crack tester, ultrasonic thickness gauge, 100 m laser tape, precision calipers</p>
        <h4>Purpose</h4><p>Micro-flaw detection, thickness measurement where only one face is accessible, and exact dimensional records</p>
      </div>
    </div>
  </div>
</section>
"""

CTA = f"""<section class="band on-dark cta">
  <div class="wrap">
    <h2>Planning a build, or worried about one?</h2>
    <p>Talk to us about structural design, a site assessment or laboratory testing.</p>
    <div class="actions">
      <a class="btn" href="tel:{PHONE_LINK}">Call {PHONE}</a>
      <a class="btn ghost" href="{WHATSAPP}">Message us on WhatsApp</a>
      <a class="btn ghost" href="mailto:{EMAIL}">Email {EMAIL}</a>
    </div>
  </div>
</section>
"""

CREDS = """<div class="creds">
  <div><h3>COREN registered</h3><p>Our engineers are registered with the Council for the Regulation of Engineering in Nigeria and hold individual certifications for the services they perform.</p></div>
  <div><h3>Licensed NDT laboratory</h3><p>Licensed by the Lagos State Government to operate as a private non-destructive testing laboratory.</p></div>
  <div><h3>Safety and standards</h3><p>Design, supervision and laboratory work follow strict safety, operational and environmental standards, with a dedicated HSE officer on our team.</p></div>
</div>"""


def build():
    OUT.mkdir(exist_ok=True)

    # ------------------------------------------------------------- home
    picks = "\n".join(project_card(DESIGN_PROJECTS[i]) for i in HOME_PICKS)
    page("index.html",
         "CNP Engineering Services | Structural Engineering and NDT, Lagos",
         "Structural design, construction supervision, structural assessment and NDT testing across Nigeria. Lagos State licensed NDT laboratory.",
         f"""<section class="hero">
  <div class="wrap">
    <div>
      <h1>Building better standards.</h1>
      <p class="lede">Integrated structural design, construction supervision and advanced diagnostics, from a Lagos practice with its own licensed NDT laboratory.</p>
      <div class="actions">
        <a class="btn" href="contact.html">Discuss a project</a>
        <a class="btn ghost" href="projects.html">See our work</a>
      </div>
    </div>
    <figure>
      <img src="assets/img/alpha01-helipad-pour.jpg" width="883" height="709" alt="Concrete pour on the Alpha01 helipad deck over the Lagos lagoon">
      <figcaption>{tb([("Location", "Victoria Island, Lagos"), ("Scope", "Structural modelling to on-water casting")], wide="Alpha01 helipad and jetty", cols=2)}</figcaption>
    </figure>
  </div>
</section>

<section class="band mist">
  <div class="wrap">
    <div class="section-head"><h2>How we work</h2></div>
    <div class="pillars">
      <div class="pillar"><h3>Multi-disciplinary design</h3><p>Design, planning and front-end project services across civil, structural, water resources and transportation engineering.</p></div>
      <div class="pillar"><h3>Project management</h3><p>A fully computerised practice using modern computer-aided design, so work is delivered promptly, accurately and in step with the wider project team.</p></div>
      <div class="pillar"><h3>NDT diagnostics</h3><p>Formal quality assurance through routine audits, backed by our in-house testing laboratory, to confirm structural integrity.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><div><h2>Selected projects</h2><p>Commercial, hospitality, retail and institutional work across Nigeria.</p></div><a class="btn ghost" href="projects.html">All projects</a></div>
    <div class="projects">
{picks}
    </div>
  </div>
</section>

{NDT_BAND}
<section class="band">
  <div class="wrap">
    <div class="section-head"><h2>Certified and regulated</h2></div>
    {CREDS}
  </div>
</section>

{CTA}""")

    # --------------------------------------------------------- services
    page("services.html",
         "Services | CNP Engineering Services",
         "Structural design, civil infrastructure, structural investigation and appraisal, project supervision and NDT laboratory testing in Lagos and across Nigeria.",
         f"""<section class="page-head">
  <div class="wrap">
    <h1>Services</h1>
    <p>Full-spectrum engineering, from the first structural scheme to testing the concrete of a building that has stood for decades.</p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="caps">
      <div class="cap-group"><h3>Buildings</h3><ul><li>Residential buildings</li><li>Multi-storey commercial and public buildings</li><li>Industrial buildings</li></ul></div>
      <div class="cap-group"><h3>Infrastructure</h3><ul><li>Highway roads and drainage</li><li>Bridges, culverts and intersections</li><li>Towers and telecommunication masts</li></ul></div>
      <div class="cap-group"><h3>Assessment and delivery</h3><ul><li>Structural investigation and appraisal</li><li>Project design and supervision</li><li>Marine structures: helipads and jetties</li></ul></div>
    </div>
  </div>
</section>

<section class="band tight">
  <div class="wrap">
    <article class="service">
      <h3>Structural design</h3>
      <div><p>Analysis and design of reinforced concrete and steel structures, from homes to multi-storey commercial, hospitality and institutional buildings. We work to BS 8110, Eurocode and BS 5950, and deliver calculations and construction drawings that contractors can build from.</p></div>
    </article>
    <article class="service">
      <h3>Civil infrastructure</h3>
      <div><p>Design, planning and front-end services for roads, drainage, bridges, culverts and intersections, and for water resources and transportation works.</p></div>
    </article>
    <article class="service">
      <h3>Structural investigation and appraisal</h3>
      <div><p>Condition surveys and integrity assessments of existing buildings, including fire-damaged structures, ageing frames and buildings planned for extension or change of use. We combine site inspection, NDT and structural analysis, and give clear recommendations for repair or strengthening.</p></div>
    </article>
    <article class="service">
      <h3>Construction supervision and project management</h3>
      <div><p>Supervision of structural works on site so that what is built matches the design, with a project team that keeps clear lines of responsibility with the client and other consultants.</p></div>
    </article>
  </div>
</section>

{NDT_BAND}
{CTA}""")

    # --------------------------------------------------------- projects
    cards = "\n".join(project_card(p) for p in DESIGN_PROJECTS)
    rows = "\n".join(survey_row(s) for s in SURVEYS)
    page("projects.html",
         "Projects | CNP Engineering Services",
         "Selected structural design, supervision, condition survey and marine projects by CNP Engineering Services across Nigeria.",
         f"""<section class="page-head">
  <div class="wrap">
    <h1>Projects</h1>
    <p>Selected work in structural design and supervision, condition surveys and marine infrastructure.</p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><h2>Design and construction supervision</h2></div>
    <div class="projects">
{cards}
    </div>
  </div>
</section>

<section class="band mist">
  <div class="wrap">
    <div class="section-head"><div><h2>Condition surveys and integrity appraisals</h2><p>Assessments backed by our NDT laboratory.</p></div></div>
    <div class="surveys">
{rows}
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><h2>Marine infrastructure</h2></div>
    <div class="feature">
      <div class="main">
        <img src="assets/img/alpha01-helipad-pour.jpg" width="883" height="709" alt="Concrete pour on the Alpha01 helipad deck" loading="lazy">
        {tb([("Location", "Victoria Island, Lagos"), ("Scope", "Structural design and construction")], wide="Alpha01 helipad and jetty", cols=2)}
      </div>
      <div class="side">
        <img class="model" src="assets/img/alpha01-helipad-model.jpg" alt="Structural model of the Alpha01 helipad and access jetty" loading="lazy">
        <img src="assets/img/alpha01-helipad-aerial.jpg" alt="Aerial view of the finished Alpha01 helipad" loading="lazy">
      </div>
    </div>
    <div class="feature-copy">
      <p>End-to-end delivery of a helipad and jetty on the Lagos lagoon, from structural modelling to on-water concrete casting and final finishing.</p>
      <p>We also designed and built a residential development beside the water at Waterfront Estate, Magodo-Isheri, Lagos.</p>
    </div>
  </div>
</section>

{CTA}""")

    # ------------------------------------------------------------ about
    leaders = "\n".join(
        f'<div class="person"><h3>{escape(p["name"])}</h3><div class="role">{escape(p["role"])}</div><div class="quals">{escape(p["quals"])}</div><p>{escape(p["text"])}</p></div>'
        for p in LEADERS)
    core = "\n".join(
        f'<div class="person"><h3>{escape(p["name"])}</h3><div class="role">{escape(p["role"])}</div><p>{escape(p["text"])}</p></div>'
        for p in CORE)
    page("about.html",
         "About | CNP Engineering Services",
         "CNP Engineering Services is a Lagos engineering practice offering structural design, construction supervision and NDT diagnostics, led by COREN-registered engineers.",
         f"""<section class="page-head">
  <div class="wrap">
    <h1>About CNP</h1>
    <p>A 21st-century engineering practice: structural design, construction and advanced diagnostics under one roof.</p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="intro">CNP Engineering Services Ltd is a Nigerian engineering firm based in Lagos. We design new structures, supervise their construction, and investigate existing ones with our own Lagos State licensed NDT laboratory.</p>
    <p>Our practice is fully computerised, so we respond to clients quickly and accurately. Every project sits with an accountable engineer who can draw on specialist skills across the firm. Design, supervision and laboratory work all follow strict safety, operational and environmental standards.</p>
  </div>
</section>

<section class="band mist">
  <div class="wrap">
    <div class="section-head"><h2>Leadership</h2></div>
    <div class="team">
{leaders}
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><h2>Engineering and HSE team</h2></div>
    <div class="team core">
{core}
    </div>
  </div>
</section>

<section class="band tight">
  <div class="wrap">
    <div class="section-head"><h2>Certified and regulated</h2></div>
    {CREDS}
  </div>
</section>

{CTA}""")

    # ---------------------------------------------------------- contact
    page("contact.html",
         "Contact | CNP Engineering Services",
         "Contact CNP Engineering Services in Lekki, Lagos for structural design, site assessment and NDT laboratory services.",
         f"""<section class="page-head">
  <div class="wrap">
    <h1>Contact us</h1>
    <p>To arrange a consultation for structural design, a site assessment or laboratory testing, call, message or email our team.</p>
  </div>
</section>

<section class="band">
  <div class="wrap contact">
    <div>
      <div class="tb">
        <div><span class="k">Phone</span><span class="v"><a href="tel:{PHONE_LINK}">{PHONE}</a></span></div>
        <div><span class="k">WhatsApp</span><span class="v"><a href="{WHATSAPP}">Chat with us on WhatsApp</a></span></div>
        <div><span class="k">Email</span><span class="v"><a href="mailto:{EMAIL}">{EMAIL}</a></span></div>
        <div><span class="k">Office</span><span class="v">{ADDRESS}</span></div>
      </div>
      <div class="actions">
        <a class="btn" href="tel:{PHONE_LINK}">Call us</a>
        <a class="btn ghost" href="mailto:{EMAIL}">Send an email</a>
      </div>
    </div>
    <iframe class="map" title="Map showing the CNP office at Crown Estate, Lekki" src="{MAP_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>""")

    # -------------------------------------------------------------- 404
    page("404.html", "Page not found | CNP Engineering Services", "The page you asked for is not on this site.",
         """<section class="page-head">
  <div class="wrap">
    <h1>Page not found</h1>
    <p>That page isn't on our site. It may have moved when we updated the website.</p>
    <div class="actions"><a class="btn" href="index.html">Go to the home page</a><a class="btn ghost" href="projects.html">See our projects</a></div>
  </div>
</section>""")

    # ----------------------------------------------------- sitemap/robots
    urls = "".join(f"<url><loc>{SITE}/{'' if p == 'index.html' else p}</loc></url>" for p in ["index.html", "services.html", "projects.html", "about.html", "contact.html"])
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print("Built", sorted(p.name for p in OUT.glob("*.*")))


if __name__ == "__main__":
    build()
