# -*- coding: utf-8 -*-
"""Generate the Johnson's Fence Company static site."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://johnsoncityfence.net"
NAME = "Johnson's Fence Company"
SOURCE = "Johnson City Fence"
PHONE = "(423) 468-2697"
TEL = "+14234682697"
LAT = 36.3134397
LNG = -82.3534727
TALLY = (
    "https://tally.so/embed/xX6B0y?alignLeft=1&hideTitle=1"
    "&transparentBackground=1&dynamicHeight=1&source=Johnson+City+Fence"
)

SERVICES = [
    ("services.html", "All services"),
    ("wood-fence.html", "Wood fencing"),
    ("vinyl-fence.html", "Vinyl fencing"),
    ("aluminum-fence.html", "Aluminum fencing"),
    ("chain-link-fence.html", "Chain-link fencing"),
    ("metal-fence.html", "Metal fencing"),
    ("picket-fence.html", "Picket fencing"),
    ("privacy-fence.html", "Privacy fencing"),
    ("farm-fence.html", "Farm fencing"),
    ("commercial-fencing.html", "Commercial fencing"),
    ("gate-installation.html", "Gate installation"),
    ("fence-repair.html", "Fence repair"),
]
FOOTER_SERVICES = [s for s in SERVICES if s[0] != "services.html"]

LOCATIONS = [
    ("fence-company-jonesborough-tn.html", "Jonesborough"),
    ("fence-company-elizabethton-tn.html", "Elizabethton"),
    ("fence-company-gray-tn.html", "Gray"),
    ("fence-company-boones-creek-tn.html", "Boones Creek"),
    ("fence-company-piney-flats-tn.html", "Piney Flats"),
    ("fence-company-telford-tn.html", "Telford"),
    ("fence-company-limestone-tn.html", "Limestone"),
    ("fence-company-unicoi-tn.html", "Unicoi"),
    ("fence-company-washington-county-tn.html", "Washington County"),
]

PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
MENU_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>'


OFFICE_HOURS = "Monday–Sunday: 7 am – 7 pm"
PHONE_ICON = (
    '<svg class="phone-icon" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1.1-.3 1.2.4 2.5.6 3.8.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.6.6 3.8.1.4 0 .8-.3 1.1L6.6 10.8z"/>'
    "</svg>"
)


def phone_link(extra_class=""):
    cls = "phone-link" + (f" {extra_class}" if extra_class else "")
    return f'<a class="{cls}" href="tel:{TEL}">{PHONE_ICON}<strong>{PHONE}</strong></a>'


def canonical(path):
    if path in ("", "index.html"):
        return SITE + "/index.html"
    return SITE + "/" + path


def call_btn(cls="btn btn-ghost"):
    return f'<a class="{cls}" href="tel:{TEL}">{PHONE_SVG}{PHONE}</a>'


def tally_block():
    return f'''<div class="quote-card" id="quote">
      <h2>Get a free quote</h2>
      <p class="quote-note">Tell us the town, the fence type, and roughly how much line you need.</p>
      <iframe data-tally-src="{TALLY}" loading="lazy" width="100%" height="552" frameborder="0" marginheight="0" marginwidth="0" title="Get a free quote"></iframe>
    </div>'''


def crumbs(items):
    parts = ['<a href="index.html">Home</a>']
    for href, label in items[:-1]:
        parts.append(f'<a href="{href}">{label}</a>')
    parts.append(items[-1][1])
    return f'<p class="crumbs">{" / ".join(parts)}</p>'


def faq_cards(items):
    blocks = []
    for q, a in items:
        blocks.append(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>')
    return '<div class="faq-grid">' + "".join(blocks) + "</div>"


def header(current):
    def link(href, label):
        cur = ' aria-current="page"' if href == current else ""
        return f'<a href="{href}"{cur}>{label}</a>'

    svc_links = "".join(link(h, l) for h, l in SERVICES)
    loc_links = link("service-areas.html", "All service areas") + "".join(
        link(h, l) for h, l in LOCATIONS
    )
    quote_href = "#quote" if current == "index.html" else "contact.html#quote"
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="topbar">
    <div class="container topbar-inner">
      <span>Free estimates in Johnson City and Washington County</span>
      <a href="tel:{TEL}">{PHONE}</a>
    </div>
  </div>
  <div class="container header-inner">
    <a class="logo-link" href="index.html" aria-label="{NAME} home"><img src="logo.svg" alt="{NAME}" width="280" height="56"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{MENU_SVG}</button>
    <nav class="nav" id="site-nav" aria-label="Primary">
      {link("index.html", "Home")}
      <details>
        <summary>Services</summary>
        <div class="nav-panel">{svc_links}</div>
      </details>
      <details>
        <summary>Service area</summary>
        <div class="nav-panel">{loc_links}</div>
      </details>
      {link("faq.html", "FAQ")}
      {link("about.html", "About")}
      {link("contact.html", "Contact")}
    </nav>
    <div class="header-actions">
      {call_btn()}
      <a class="btn btn-primary" href="{quote_href}">Get a free quote</a>
    </div>
  </div>
</header>'''


OFFICE_HOURS_DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
OFFICE_HOURS_TIME = "7 am – 7 pm"


def office_hours_block():
    rows = "".join(f"<div><span>{day}</span><span>{OFFICE_HOURS_TIME}</span></div>" for day in OFFICE_HOURS_DAYS)
    return f'<div class="hours-list">{rows}</div>'


def footer():
    services = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in FOOTER_SERVICES)
    return f'''<footer class="site-footer">
  <div class="footer-accent"></div>
  <div class="container footer-grid">
    <div>
      <h2>Company</h2>
      <img src="logo.svg" alt="" width="280" height="56">
      <p style="margin-top:0.9rem">Fence installation and repair for homes, farms, and commercial lots in Johnson City, Tennessee and nearby towns.</p>
      <a class="footer-phone" href="tel:{TEL}">{PHONE}</a>
      <ul style="margin-top:0.8rem">
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h2>Services</h2>
      <ul>{services}</ul>
    </div>
    <div>
      <h2>Quick links</h2>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="services.html">Services</a></li>
        <li><a href="faq.html">FAQ</a></li>
        <li><a href="service-areas.html">Service areas</a></li>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
    <div>
      <h2>Office Hours</h2>
      {office_hours_block()}
    </div>
  </div>
  <div class="container footer-base">
    <p>© 2026 {NAME}.</p>
    <p><a href="sitemap.xml">XML sitemap</a> · <a href="robots.txt">robots.txt</a></p>
  </div>
</footer>
<nav class="callbar" aria-label="Call or request a quote">
  <a class="btn btn-ink" href="tel:{TEL}">{PHONE_SVG}Call</a>
  <a class="btn btn-primary" href="contact.html#quote">Free quote</a>
</nav>'''


TALLY_SCRIPT = '''<script>var d=document,w="https://tally.so/widgets/embed.js",v=function(){"undefined"!=typeof Tally?Tally.loadEmbeds():d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach((function(e){e.src=e.dataset.tallySrc}))};if("undefined"!=typeof Tally)v();else if(d.querySelector('script[src="'+w+'"]')==null){var s=d.createElement("script");s.src=w,s.onload=v,s.onerror=v,d.body.appendChild(s);}</script>'''


def layout(filename, title, description, body, graph, og_image="/images/hero.jpg"):
    url = canonical(filename)
    schema = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="{NAME}">
  <meta property="og:image" content="{SITE}{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <script type="application/ld+json">{schema}</script>
</head>
<body>
{header(filename)}
<main id="main">
{body}
</main>
{footer()}
<script src="main.js"></script>
{TALLY_SCRIPT}
</body>
</html>
'''
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)


def business_node():
    areas = [
        {"@type": "City", "name": "Johnson City, TN"},
        {"@type": "AdministrativeArea", "name": "Washington County, TN"},
    ]
    for _, name in LOCATIONS:
        if name == "Washington County":
            continue
        kind = "AdministrativeArea" if name.endswith("County") else "City"
        areas.append({"@type": kind, "name": f"{name}, TN"})
    catalog = []
    for href, label in FOOTER_SERVICES:
        catalog.append({
            "@type": "Offer",
            "itemOffered": {
                "@type": "Service",
                "@id": canonical(href) + "#service",
                "name": label + " in Johnson City, TN",
                "url": canonical(href),
                "provider": {"@id": SITE + "/#business"},
            },
        })
    return {
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": SITE + "/#business",
        "name": NAME,
        "url": SITE + "/index.html",
        "telephone": "+1-423-468-2697",
        "image": SITE + "/images/hero.jpg",
        "logo": SITE + "/logo.svg",
        "description": "Fence installation and repair for homes, farms, and commercial lots in Johnson City, Tennessee and nearby Washington County. Service-area business with no public storefront listed.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Johnson City",
            "addressRegion": "TN",
            "addressCountry": "US",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
        "areaServed": [
            {
                "@type": "GeoCircle",
                "name": "About 25 miles around Johnson City, Tennessee",
                "geoMidpoint": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG},
                "geoRadius": 40234,
            },
            *areas,
        ],
        "knowsAbout": [
            "Wood fence installation",
            "Vinyl fence installation",
            "Aluminum fence installation",
            "Chain-link fence installation",
            "Ornamental metal fencing",
            "Picket fencing",
            "Privacy fencing",
            "Farm fencing",
            "Commercial fencing",
            "Fence gate installation",
            "Fence repair",
            "Clay soil fence posts in East Tennessee",
            "Johnson City fence height and sight-triangle rules",
            "Tennessee 811 utility locate before digging",
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Fence installation and repair",
            "itemListElement": catalog,
        },
        "potentialAction": {
            "@type": "CommunicateAction",
            "name": "Request a fence estimate",
            "target": SITE + "/contact.html",
        },
    }


def webpage(filename, name, description, main_id):
    return {
        "@type": "WebPage",
        "@id": canonical(filename) + "#webpage",
        "url": canonical(filename),
        "name": name,
        "description": description,
        "isPartOf": {"@id": SITE + "/#website"},
        "about": {"@id": main_id},
        "publisher": {"@id": SITE + "/#business"},
        "inLanguage": "en-US",
    }


def website_node():
    return {
        "@type": "WebSite",
        "@id": SITE + "/#website",
        "url": SITE + "/index.html",
        "name": NAME,
        "publisher": {"@id": SITE + "/#business"},
        "inLanguage": "en-US",
    }


def crumbs_schema(filename, trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/index.html"}]
    for i, (href, label) in enumerate(trail, start=2):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": label,
            "item": canonical(href) if href else canonical(filename),
        })
    return {"@type": "BreadcrumbList", "@id": canonical(filename) + "#breadcrumb", "itemListElement": items}


def faq_schema(filename, items):
    return {
        "@type": "FAQPage",
        "@id": canonical(filename) + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }


def steps(items):
    lis = []
    for i, (title, text) in enumerate(items, start=1):
        lis.append(f'<li><span class="num">{i}</span><span><strong>{title}</strong> {text}</span></li>')
    return '<ol class="steps">' + "".join(lis) + "</ol>"


def factors(items):
    blocks = []
    for title, text in items:
        blocks.append(f'<article class="factor"><h3>{title}</h3><p>{text}</p></article>')
    return '<div class="factor-grid">' + "".join(blocks) + "</div>"


def related(links):
    bits = " · ".join(f'<a href="{h}">{l}</a>' for h, l in links)
    return f'<p style="margin-top:1rem">Related: {bits}</p>'


HOME_FAQS = [
    (
        "How much does a fence cost in Johnson City, TN?",
        "The price follows the line we measure: length, height, material, gates, and whether an old fence has to come out. Clay that holds water, a slope, tree roots, and rock on a ridge lot all change the labor. We do not publish a per-foot menu. The estimate comes from the property.",
    ),
    (
        "Can you set fence posts in the clay and rock around Johnson City?",
        "Yes. Valley lots in Washington County are often clay that stays wet after rain, and ridge lots toward Unicoi and Buffalo Mountain can hit rock. Posts go in concrete, with the mix crowned so water does not pool at the post. If a hole hits solid rock or a stretch stays saturated, we say so before we set it.",
    ),
    (
        "Do you offer wood, vinyl, aluminum, chain link, and farm fencing?",
        "Yes. Wood and vinyl cover privacy and picket work. Aluminum and ornamental metal cover open lines and gates. Chain link covers yards, dogs, and work lots. Farm fencing covers rail and wire for animals on longer runs in places like Telford and Limestone. Repair is part of the same call.",
    ),
    (
        "Do I need a permit to put up a fence in Johnson City?",
        "Inside the city, published standards allow a standard residential fence up to 7 feet without a structural permit. Taller than that needs a building permit. On a corner lot, the 25-foot sight triangle stays at 3 feet so drivers can see. A historic overlay can also require design review. Outside the city, confirm the parcel with Washington County or the town that actually governs it. An HOA can be stricter than any of them.",
    ),
    (
        "Can you repair a leaning fence, or does the whole line have to come out?",
        "If the posts are still sound, we replace the boards, rails, mesh, or gate that failed and leave the rest. If the posts have rotted at the ground line or heaved out of the clay, new boards on those posts will lean again, and that stretch should be rebuilt. We will tell you which it is after we see the line.",
    ),
]


def home():
    cards = [
        ("wood-fence.html", "images/wood.jpg", "Stained wood privacy fence with vertical boards along a lawn", "Wood fencing", "Privacy and shadowbox wood for a backyard screen you can stain to the house. Posts are set in concrete for clay soil around Johnson City."),
        ("vinyl-fence.html", "images/vinyl-green.jpg", "Gray vinyl privacy fence along a row of houses", "Vinyl fencing", "Privacy and rail vinyl that stays straight through humid summers and cold winters. A fit when you do not want to stain the fence each year."),
        ("aluminum-fence.html", "images/aluminum.jpg", "Black aluminum fence with vertical pickets along a lawn", "Aluminum fencing", "Open aluminum picket for front yards, pools, and lines on a slope. It does not rust in East Tennessee humidity and does not need paint."),
        ("chain-link-fence.html", "images/chain-link.jpg", "Green vinyl-coated chain-link fence across a grassy field", "Chain-link fencing", "Galvanized and vinyl-coated chain link for yards, dogs, and work lots. A screen can be added where you need a visual break."),
        ("metal-fence.html", "images/metal.png", "Black metal fence with rounded vertical pickets", "Metal fencing", "Ornamental steel for heavier decorative lines and wide drive gates. Stronger than aluminum, and the finish has to be maintained."),
        ("picket-fence.html", "images/picket.jpg", "White picket fence in front of a house and garden", "Picket fencing", "Open picket for front yards and gardens where you want a boundary, not a wall. Heights stay lower so the street view stays clear."),
        ("privacy-fence.html", "images/vinyl-privacy.jpg", "White vinyl fence with a solid privacy panel and a semi-private section", "Privacy fencing", "Solid wood or vinyl panels that close a backyard off from the next house. Built for side and rear yards, not a corner sight line."),
        ("farm-fence.html", "images/farm.jpg", "White rail fence running through a green pasture", "Farm fencing", "Rail and woven wire for horses and cattle on longer pasture runs. Built for Washington County acreage, not a backyard panel."),
        ("commercial-fencing.html", "images/commercial.jpg", "Black metal rail fence along a maintained lawn", "Commercial fencing", "Heavier chain link, rail, and vehicle gates for yards and job sites. Specified for a work lot, not a house privacy panel."),
        ("gate-installation.html", "images/gate.jpg", "Double driveway gate between masonry posts", "Gate installation", "Walk gates and drive gates hung on posts sized for the opening. New installs, plus repairs when a gate sags or will not latch."),
        ("fence-repair.html", "images/repair.jpg", "A carpenter resetting boards on a wood fence gate", "Fence repair", "Boards, posts, and gates replaced where the rest of the line is still sound. If the posts have failed, we say that before we patch them."),
    ]
    card_html = []
    for href, img, alt, title, text in cards:
        card_html.append(f'''<a class="service-card" href="{href}">
        <span class="media"><img src="{img}" alt="{alt}" width="925" height="615" loading="lazy"></span>
        <span class="body"><h3>{title}</h3><p>{text}</p><span class="more">View service</span></span>
      </a>''')
    gallery = [
        ("images/wood.jpg", "Stained wood privacy fence along a lawn"),
        ("images/vinyl-green.jpg", "Gray vinyl privacy fence beside houses"),
        ("images/picket.jpg", "White picket fence in a front yard"),
        ("images/chain-link.jpg", "Green chain-link fence in a field"),
        ("images/aluminum.jpg", "Black aluminum picket fence"),
        ("images/farm.jpg", "White rail fence in a pasture"),
    ]
    ghtml = "".join(f'<figure><img src="{src}" alt="{alt}" loading="lazy"></figure>' for src, alt in gallery)
    chips = "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in LOCATIONS)
    desc = "Johnson's Fence Company installs and repairs wood, vinyl, aluminum, chain-link, and farm fencing in Johnson City, TN. Call (423) 468-2697."
    body = f'''<section class="hero">
  <div class="hero-media"><img src="images/hero.jpg" alt="Wood privacy fence along a backyard lawn beside a house" width="1200" height="800" fetchpriority="high"></div>
  <div class="hero-shade"></div>
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Johnson City, Tennessee</p>
      <h1>Fence company in Johnson City, TN</h1>
      <p class="lede">Wood, vinyl, aluminum, chain link, and farm fencing for houses, pastures, and commercial lots. New lines, replacements, repairs, and gates are quoted from the property.</p>
      <div class="hero-actions">
        {call_btn("btn btn-primary btn-lg")}
        <a class="btn btn-ghost btn-lg" href="#quote">Request an estimate</a>
      </div>
      <ul class="hero-points">
        <li>Homes, farms, and work lots</li>
        <li>Posts set for valley clay and ridge rock</li>
        <li>Free on-site estimates</li>
      </ul>
    </div>
    {tally_block()}
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="kicker">Materials and work</p>
      <h2>Fence services in Johnson City</h2>
      <p>Start with the job. A backyard screen, a front-yard picket, a dog run, and a pasture line are not the same fence.</p>
    </div>
    <div class="card-grid services">{"".join(card_html)}</div>
  </div>
</section>
<section class="band">
  <div class="container section">
    <div class="section-head">
      <p class="kicker">Styles</p>
      <h2>Fences we install</h2>
      <p>Privacy, picket, chain link, aluminum, and rail from the crew that walks the line in Johnson City and nearby towns.</p>
    </div>
    <div class="gallery">{ghtml}</div>
  </div>
</section>
<section class="section soft">
  <div class="container split-2">
    <div>
      <h2>Houses</h2>
      <p>Backyard privacy, pet runs, pool barriers, and property-line replacements. Most in-town jobs are a wood or vinyl screen on the side and rear, with a gate that fits the mower. Corner lots keep the sight triangle low so drivers can see past the fence.</p>
      <a class="more" href="privacy-fence.html">Privacy fencing</a>
    </div>
    <div>
      <h2>Lots and acreage</h2>
      <p>A storage yard in Piney Flats needs heavier chain link and a vehicle gate. A pasture in Telford or Limestone needs rail or wire sized for the animals, not a backyard panel. Tell us how the ground is used and we will spec the line for that use.</p>
      <a class="more" href="farm-fence.html">Farm fencing</a>
    </div>
  </div>
</section>
<section class="section">
  <div class="container split-2">
    <div>
      <h2>How a fence job is quoted</h2>
      <ol class="steps">
        <li><span class="num">1</span><span><strong>Name the job.</strong> Screen, contain animals, mark a line, or secure a lot. That choice picks the material faster than a photo.</span></li>
        <li><span class="num">2</span><span><strong>Walk the ground.</strong> Clay, rock, slope, trees, and the distance from the driveway all change the posts and the labor.</span></li>
        <li><span class="num">3</span><span><strong>Count the openings.</strong> A fence with the wrong gate is a daily problem. Walk gates and drive gates are priced as their own pieces.</span></li>
        <li><span class="num">4</span><span><strong>Repair or replace.</strong> Sound posts can take new boards. Posts that have rotted at the ground line cannot. We say which one you have.</span></li>
      </ol>
    </div>
    <div class="panel">
      <h2>Repairs and gates</h2>
      <p>Leaning posts, missing boards, and sagging gates show up after a wet winter or a wind event. If the rest of the line is sound, we repair the failed section. If the posts have let go in the clay, we will tell you to rebuild that run.</p>
      <p>Gates are hung on posts sized for the opening, with hardware that can carry the weight. A walk gate and a drive gate are different builds.</p>
      <a class="more" href="fence-repair.html">Fence repair</a>
    </div>
  </div>
</section>
<section class="band">
  <div class="container section">
    <h2>Service area</h2>
    <p>We work in Johnson City and nearby communities, roughly a 25-mile drive. Each place puts a different demand on the fence: tight in-town lots, HOA subdivisions, wet river bottoms, and longer farm lines.</p>
    <ul class="chips">{chips}</ul>
    <p style="margin-top:1rem"><a href="service-areas.html" style="color:white">All service areas</a></p>
  </div>
</section>
<section class="section">
  <div class="container">
    <h2>Questions before you call</h2>
    <div style="margin-top:1.2rem">{faq_cards(HOME_FAQS)}</div>
    <p style="margin-top:1rem"><a href="faq.html">More fence questions</a></p>
  </div>
</section>
<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>Ready to walk the line?</h2>
      <p>Call {PHONE} or send the lot details. Estimates are free.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary btn-lg" href="#quote">Get a free quote</a>
      {call_btn("btn btn-ink btn-lg")}
    </div>
  </div>
</section>'''
    graph = [
        business_node(),
        website_node(),
        webpage("index.html", "Fence company in Johnson City, TN", desc, SITE + "/#business"),
        faq_schema("index.html", HOME_FAQS),
    ]
    layout(
        "index.html",
        "Fence Company in Johnson City, TN | Johnson's Fence Company",
        desc,
        body,
        graph,
    )


def service_gallery(s):
    """Primary service image plus one other service image."""
    order = [h for h, _ in s["related"]] + [o["file"] for o in SERVICES_DATA]
    by_file = {o["file"]: o for o in SERVICES_DATA}
    shots = [s]
    for f in order:
        o = by_file.get(f)
        if o and o["file"] != s["file"] and o["image"] != s["image"]:
            shots.append(o)
            break
    figs = "".join(
        f'<figure class="service-shot"><img src="{o["image"]}" alt="{o["alt"]}" width="925" height="615" loading="lazy" decoding="async"></figure>'
        for o in shots
    )
    return f'<div class="service-gallery">{figs}</div>'


def service_related(s):
    links = list(s["related"])
    seen = {h for h, _ in links} | {s["file"]}
    for h, l in FOOTER_SERVICES:
        if len(links) >= 4:
            break
        if h not in seen:
            links.append((h, l))
            seen.add(h)
    return "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in links[:4])


def service_layout(s):
    filename = s["file"]
    desc = s["description"]
    faqs = s["faqs"]
    towns = "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in LOCATIONS)
    body = f'''<div class="crumb-bar"><div class="container">{crumbs([("services.html", "Services"), (filename, s["crumb"])])}</div></div>
<section class="page-hero service-hero">
  <div class="container">
    <div class="service-hero-inner">
      <p class="eyebrow">{s["crumb"]}</p>
      <h1>{s["h1"]}</h1>
      <p class="lede">{s["intro"]}</p>
      <div class="hero-actions">
        {call_btn("btn btn-primary btn-lg")}
        <a class="btn btn-ghost btn-lg" href="contact.html#quote">Get a free quote</a>
      </div>
    </div>
  </div>
</section>
<section class="section service-body">
  <div class="container service-layout">
    <div class="service-main">
      {service_gallery(s)}
      <div class="prose service-copy">
        <h2>When this fence is the right job</h2>
        <p>{s["when"]}</p>
        <h2>How the work goes</h2>
        {steps(s["process"])}
        {s["after"]}
        <h2>What changes the estimate</h2>
        <p>We price the line on your lot. These are the pieces that move the number.</p>
        {factors(s["factors"])}
        <h2>Questions about {s["faq_label"]}</h2>
        {faq_cards(faqs)}
      </div>
    </div>
    <aside class="service-aside" aria-label="Estimate and related services">
      <div class="side-card">
        <p class="side-kicker">Talk through the line</p>
        <p>Call or send the town, the approximate length, and the gate count. We will tell you if the job is a repair, a replacement, or a different material than you started with.</p>
        <p class="side-phone">{phone_link("phone-link-lg")}</p>
        <p class="side-hours">{OFFICE_HOURS}</p>
        <p><a class="btn btn-primary" href="contact.html#quote">Get a free quote</a></p>
      </div>
      <div class="side-card side-card-muted">
        <p class="side-kicker">Related</p>
        <ul class="side-links">{service_related(s)}</ul>
      </div>
    </aside>
  </div>
</section>
<section class="section section-towns">
  <div class="container">
    <h2>Towns we serve</h2>
    <ul class="chips light-chips">{towns}</ul>
    <p class="towns-links"><a href="service-areas.html">Service areas</a> · <a href="contact.html#quote">Request an estimate</a> · <a href="services.html">All services</a></p>
  </div>
</section>'''
    graph = [
        business_node(),
        webpage(filename, s["h1"], desc, canonical(filename) + "#service"),
        {
            "@type": "Service",
            "@id": canonical(filename) + "#service",
            "name": s["h1"],
            "description": desc,
            "url": canonical(filename),
            "provider": {"@id": SITE + "/#business"},
            "areaServed": {"@type": "City", "name": "Johnson City, TN"},
            "serviceType": s["crumb"],
        },
        crumbs_schema(filename, [("services.html", "Services"), (filename, s["crumb"])]),
        faq_schema(filename, faqs),
    ]
    layout(filename, s["title"], desc, body, graph, og_image="/" + s["image"])
SERVICES_DATA = [
    {
        "file": "wood-fence.html",
        "title": "Wood Fence Installation in Johnson City, TN",
        "description": "Wood privacy and shadowbox fences in Johnson City, TN. Posts set in concrete for clay soil. Call (423) 468-2697 for a free estimate.",
        "h1": "Wood fence installation in Johnson City, TN",
        "crumb": "Wood fencing",
        "faq_label": "wood fencing",
        "image": "images/wood.jpg",
        "alt": "Stained wood privacy fence with vertical boards along a lawn",
        "intro": "Privacy, shadowbox, and board-on-board wood for yards that want a solid screen and a stain that matches the house. We measure the line, set posts for clay, and price each gate on its own.",
        "when": "Choose wood when the job is a backyard screen, a stained match to the siding, or a repair on a wood line whose posts are still solid. A tall privacy run belongs on the side and rear. On a corner lot in the city, the 25-foot sight triangle stays at 3 feet, so a 6-foot wood wall does not belong across that view. Shaded older yards stay damp at the ground line, which is where untreated boards fail first.",
        "process": [
            ("Walk the line.", "We note the slope, trees, gates, and who owns the property pins."),
            ("Check the rule.", "City height, a historic overlay, and any HOA color sheet come before the lumber order."),
            ("Set the posts.", "Posts go in concrete in the clay, crowned at the top so water does not sit against the wood."),
            ("Hang the fence and the gate.", "Rails, boards, and a gate that latches without dragging on the ground."),
        ],
        "after": "<p>Call Tennessee 811 before anyone digs. In a mature Johnson City yard the roots and the irrigation line are as likely to change the layout as the slope is. If an old fence is coming out, that labor is its own line on the estimate.</p>",
        "factors": [
            ("Length and height", "A 4-foot side return and a 6-foot rear screen are different amounts of lumber, even on the same lot."),
            ("Grade and trees", "Stepping a panel down a slope, or working around a trunk, takes more posts than a flat run."),
            ("Gates", "A 4-foot walk gate and a 10-foot drive opening are priced separately. The posts have to carry the swing."),
            ("Removal and finish", "Pulling an old line, hauling it, and staining the new wood all move the number."),
        ],
        "related": [("privacy-fence.html", "Privacy fencing"), ("picket-fence.html", "Picket fencing"), ("fence-repair.html", "Fence repair")],
        "faqs": [
            ("How much does a wood fence cost in Johnson City?", "It depends on the footage, the height, the number of gates, and whether the old fence comes out. Clay, a slope, and a long carry from the driveway add labor. We measure the line and give you a number for that property. We do not quote a citywide price per foot."),
            ("Can you match the stain on a wood fence that is already there?", "We can come close on a new section if you tell us the color, or we can stain the new run and leave the old boards as they are. An exact match on weathered wood is unlikely. If the posts under the old section have rotted, matching the color will not keep that part standing."),
            ("Do I need a permit for a 6-foot wood privacy fence in the city?", "Published city standards allow a standard residential fence up to 7 feet without a structural permit. Over 7 feet needs a building permit. Corner sight triangles stay at 3 feet. A historic overlay or an HOA can add its own review. Confirm the parcel before the posts go in."),
            ("Will a wood fence rot in a shaded Johnson City yard?", "Shade and summer humidity keep the ground line damp, and that is where rot starts. Concrete crowned away from the post, and a finish you actually maintain, slow that down. If you do not want that upkeep, a vinyl privacy fence is the closer fit."),
            ("Can you repair a few wood sections instead of replacing the line?", "Yes, when the posts are still solid. We replace the failed boards or the gate and leave the sound run. If the posts have rotted or heaved, new boards on those posts will lean again, and that stretch should be rebuilt."),
        ],
    },
    {
        "file": "vinyl-fence.html",
        "title": "Vinyl Fence Installation in Johnson City, TN",
        "description": "Vinyl privacy and rail fences in Johnson City, TN for yards that do not want a yearly stain. Call (423) 468-2697 for a free estimate.",
        "h1": "Vinyl fence installation in Johnson City, TN",
        "crumb": "Vinyl fencing",
        "faq_label": "vinyl fencing",
        "image": "images/vinyl-green.jpg",
        "alt": "Gray vinyl privacy fence running along a row of houses",
        "intro": "Privacy, picket, and ranch-rail vinyl for a straight line that does not need a yearly stain. A practical fit for humid summers and freeze-thaw winters around Johnson City.",
        "when": "Choose vinyl when the HOA names a color, when you do not want to stain, or when a wood line in a damp yard has already rotted at the ground. Vinyl is a poor choice for a horse that leans on a fence, and it is not the heavy spec for a commercial vehicle gate. On a slope, panels are racked or stepped. We say which one the grade actually needs.",
        "process": [
            ("Confirm the style.", "Privacy, picket, or rail, plus the color the HOA or the house actually calls for."),
            ("Lay out the grade.", "A Johnson City side yard often drops toward the rear. We decide racked or stepped before the panels are ordered."),
            ("Set the posts.", "Vinyl posts still go in concrete. Clay that holds water will move a shallow post the same way it moves a wood one."),
            ("Assemble and gate.", "Panels, caps, and a gate leaf that clears the high spot in the yard."),
        ],
        "after": "<p>Vinyl does not rot, and it also does not hide a bad layout. A panel forced onto a steep grade looks wavy. We would rather step that section than stretch it. Rails for a pasture are on the <a href=\"farm-fence.html\">farm fencing</a> page, because a house-yard vinyl panel is the wrong product for livestock.</p>",
        "factors": [
            ("Style and height", "A 6-foot privacy panel costs more material than a 4-foot picket on the same footage."),
            ("Color", "White, tan, and gray are common. A special color can change the lead time and the price."),
            ("Slope", "Stepping a grade uses more posts and more cuts than a level run along a flat rear line."),
            ("Gates and removal", "Each opening is its own leaf and hardware. Hauling an old wood fence is extra labor."),
        ],
        "related": [("privacy-fence.html", "Privacy fencing"), ("picket-fence.html", "Picket fencing"), ("aluminum-fence.html", "Aluminum fencing")],
        "faqs": [
            ("How much does a vinyl fence cost in Johnson City?", "Privacy vinyl usually costs more per foot than a basic wood line and less upkeep after that. Height, color, slope, and gates move the quote. We price the measured line, not a catalog rate."),
            ("Can vinyl handle a freeze and a hot summer here?", "Yes. The panels are made for outdoor temperature swings. The part that fails in this climate is usually a post set too shallow in wet clay, not the vinyl itself. Posts go in concrete, crowned at the top."),
            ("Do you offer vinyl if the HOA only allows a certain color?", "Yes, when that color is a real product we can order. Send the HOA sheet with the request so the quote uses the right panel. We will not guess from the fence next door."),
            ("Is vinyl a good farm fence?", "Ranch-rail vinyl can mark a line or a light paddock. It is not what we use for cattle pressure or a horse that cribs and leans. Those jobs are rail or wire built for the animal."),
            ("Can you put vinyl on a sloped Johnson City lot?", "Yes. Mild slopes can be racked so the bottom follows the grade. Steeper drops are stepped. Forcing a panel to do both is how you get a gap a dog walks under."),
        ],
    },
    {
        "file": "aluminum-fence.html",
        "title": "Aluminum Fence Installation in Johnson City, TN",
        "description": "Aluminum picket fences in Johnson City, TN for front yards, pools, and slopes. No paint cycle. Call (423) 468-2697.",
        "h1": "Aluminum fence installation in Johnson City, TN",
        "crumb": "Aluminum fencing",
        "faq_label": "aluminum fencing",
        "image": "images/aluminum.jpg",
        "alt": "Black aluminum fence with vertical pickets along a lawn",
        "intro": "Open aluminum picket for front yards, pool barriers, and lines that have to follow a slope. It stays straight in humidity and does not ask for a paint cycle the way steel does.",
        "when": "Choose aluminum when you want a boundary people can see through: a front yard, a pool enclosure, or a side line that should not feel like a wall. It is the wrong product for a privacy screen and the wrong product for a heavy drive gate that needs a steel frame. Ornamental steel is on the <a href=\"metal-fence.html\">metal fencing</a> page. Aluminum racks well on the grade changes common on Johnson City side yards.",
        "process": [
            ("Pick the height and the picket spacing.", "Front yards and corner sight triangles stay lower. Pool barriers follow the adopted pool code, not a decorative height."),
            ("Check the grade.", "Aluminum sections can rack. We still mark where a step is cleaner than a rack."),
            ("Set posts in concrete.", "Even a light fence moves if the clay lets the post go. Concrete and a crowned top are standard."),
            ("Hang sections and gates.", "A pool gate needs self-closing hardware. A yard gate needs a latch you can use with one hand."),
        ],
        "after": "<p>Black is the finish we install most. It reads as a line, not a wall, which is why it shows up on frontages where a privacy panel would block the house. If the job is a solid screen, look at <a href=\"privacy-fence.html\">privacy fencing</a> instead.</p>",
        "factors": [
            ("Height and style", "A 4-foot open picket and a 5-foot pool barrier are different sections and different hardware."),
            ("Grade", "Racking is included in a normal slope. A steep drop that has to be stepped takes more posts."),
            ("Gates", "A self-closing pool gate is a different piece of hardware than a simple walk gate."),
            ("Footage", "Open aluminum is priced on the measured run, including corners and the posts at each end."),
        ],
        "related": [("metal-fence.html", "Metal fencing"), ("picket-fence.html", "Picket fencing"), ("gate-installation.html", "Gate installation")],
        "faqs": [
            ("How much does an aluminum fence cost in Johnson City?", "It is usually more per foot than chain link and less maintenance than painted steel. Height, gates, and slope decide the number. Pool hardware adds cost because the gate has to close itself."),
            ("Can aluminum be used as a pool fence?", "Yes, when the height, the picket spacing, and the self-closing gate meet the pool barrier code the city has adopted. A decorative 3-foot picket is not automatically a legal pool barrier. We spec the barrier to the rule, then build that."),
            ("Will aluminum rust in East Tennessee humidity?", "Aluminum does not rust the way bare steel does. It can stain if a sprinkler throws minerals on it, and a scratched finish should be touched up. It does not need the repaint cycle of ornamental steel."),
            ("Do I need a permit for an aluminum front-yard fence?", "A standard residential fence up to 7 feet does not need a structural permit inside the city. A corner sight triangle still cannot exceed 3 feet. Front-yard height can also be limited by an HOA even when the city allows more. Confirm both."),
            ("Can you install aluminum on a hill?", "Yes. That is one of the reasons people pick it here. Sections rack to follow a mild grade. Very steep ground is stepped so the bottom does not open a gap."),
        ],
    },
    {
        "file": "chain-link-fence.html",
        "title": "Chain-Link Fence Installation in Johnson City, TN",
        "description": "Chain-link fence installation in Johnson City, TN for yards, dogs, and work lots. Galvanized or vinyl-coated. Call (423) 468-2697.",
        "h1": "Chain-link fence installation in Johnson City, TN",
        "crumb": "Chain-link fencing",
        "faq_label": "chain-link fencing",
        "image": "images/chain-link.jpg",
        "alt": "Green vinyl-coated chain-link fence running across a grassy field",
        "intro": "Galvanized and vinyl-coated chain link for yards, dogs, and light commercial lots. A practical fence when you need containment more than a solid screen.",
        "when": "Choose chain link for a dog run, a side yard, a playground edge, or a lot where you still want to see through the fence. Add slats or a screen only where a visual break matters. It is not a horse fence, and a residential fabric gauge is not the spec for a storage yard that takes vehicle traffic. That heavier build is on the <a href=\"commercial-fencing.html\">commercial fencing</a> page.",
        "process": [
            ("Set the use.", "Dog, yard line, or work lot. The use picks the height, the gauge, and whether the fabric is coated."),
            ("Mark utilities.", "Tennessee 811 before the terminal posts go in. Corner posts and gate posts carry the tension."),
            ("Set posts and pour.", "Terminal posts in concrete, line posts on spacing that holds the fabric tight in clay soil."),
            ("Stretch, tie, and hang the gate.", "Fabric pulled tight, ties on the mesh, and a gate that does not drag."),
        ],
        "after": "<p>Green and black vinyl-coated fabric is what we use when the fence sits in view of the house. Bare galvanized is fine on a back run or a work lot where appearance is not the point. A privacy slat changes the wind load, so we do not add a full screen without checking the post spacing.</p>",
        "factors": [
            ("Height and gauge", "A 4-foot yard fence and a 6-foot dog fence use different fabric and often different posts."),
            ("Coating", "Vinyl-coated fabric costs more than galvanized and holds up better where you look at it every day."),
            ("Gates", "A walk gate is simple. A double drive gate needs heavier posts and a drop rod or a cane bolt."),
            ("Screen or slats", "Adding a visual screen is material and labor, and it changes how the fence takes wind."),
        ],
        "related": [("commercial-fencing.html", "Commercial fencing"), ("gate-installation.html", "Gate installation"), ("fence-repair.html", "Fence repair")],
        "faqs": [
            ("How much does a chain-link fence cost in Johnson City?", "Footage, height, coating, and gates set the price. A coated residential run costs more than bare galvanized. A commercial gauge with a vehicle gate is a different quote entirely. We measure before we number it."),
            ("Can you install chain link for a dog in a Johnson City yard?", "Yes. Height and a latch the dog cannot open matter more than the color. Tell us the breed and whether the dog climbs or digs. A digger may need the fabric extended or buried at the bottom, which is part of the layout."),
            ("Do you offer vinyl-coated chain link?", "Yes. Green and black are the coatings we install most on house lots. Galvanized is available when the fence is out of sight or the budget is the constraint."),
            ("Is chain link allowed in Johnson City?", "The city does not publish a banned-materials list for ordinary residential fences. An HOA often does. If your subdivision restricts chain link, the covenants control. Send that sheet with the request."),
            ("Can you add privacy to an existing chain-link fence?", "Often, if the posts and the top rail are still sound. Slats or a screen add wind load. If the line posts are already loose in the clay, we fix the posts before we add anything that catches air."),
        ],
    },
    {
        "file": "metal-fence.html",
        "title": "Metal Fence Installation in Johnson City, TN",
        "description": "Ornamental steel fencing and metal gates in Johnson City, TN. Heavier than aluminum, with a finish to maintain. Call (423) 468-2697.",
        "h1": "Metal fence installation in Johnson City, TN",
        "crumb": "Metal fencing",
        "faq_label": "metal fencing",
        "image": "images/metal.png",
        "alt": "Black metal fence with rounded vertical pickets",
        "intro": "Ornamental steel for lines and gates that need more strength than aluminum. A finish you can maintain, not a rust-proof promise.",
        "when": "Choose steel when the gate is wide, the look is ornamental iron, or the line has to take more abuse than a light aluminum picket. Choose aluminum instead when you want an open fence with almost no finish work. Steel in this climate needs a coating that stays intact. A scratch left bare will rust. We talk about that before the order, because a steel fence is a different upkeep job than the aluminum one next to it.",
        "process": [
            ("Decide steel or aluminum.", "If the answer is a light open line, we send you to aluminum. Steel is for weight and for certain gate spans."),
            ("Spec the finish.", "Powder coat or paint, and a plan for touch-up. Humidity finds every bare spot."),
            ("Set structural posts.", "Gate posts are sized for the leaf, not borrowed from the line posts. Concrete in clay, crowned at the top."),
            ("Hang and adjust.", "Leaves, hinges, and latches set so the gate closes without a lift."),
        ],
        "after": "<p>Metal fencing on this page means ornamental steel and iron-style work. Chain link is its own system. If the photo you have in mind is a black picket that never needs paint, that is usually <a href=\"aluminum-fence.html\">aluminum</a>.</p>",
        "factors": [
            ("Steel versus aluminum", "Steel costs more to build and more to keep finished. The quote names which metal you are buying."),
            ("Gate width", "A double drive gate is the expensive piece. The line on either side is the smaller share."),
            ("Finish", "A coated system costs more up front than bare primed steel and fails slower if the coat stays whole."),
            ("Grade and corners", "Ornamental panels do not rack like aluminum. Steep ground means more posts and custom cuts."),
        ],
        "related": [("aluminum-fence.html", "Aluminum fencing"), ("gate-installation.html", "Gate installation"), ("commercial-fencing.html", "Commercial fencing")],
        "faqs": [
            ("How much does a metal fence cost in Johnson City?", "Ornamental steel is priced on the style, the gate span, and the finish. It is not the same number as aluminum or chain link. A wide drive gate can cost more than the rest of a short frontage. We measure the opening before we quote it."),
            ("Can you install wrought-iron style fencing?", "Yes, in steel sections that look like traditional iron. True antique iron repair is a different job. Tell us if you are matching an old section or starting a new line, because the hardware and the finish are not the same."),
            ("Will a steel fence rust here?", "It will, wherever the coating is broken and water sits. East Tennessee humidity and freeze-thaw make that faster than a dry climate. We spec a finish and we tell you it has to be touched up. If you do not want that job, use aluminum."),
            ("Do you build metal drive gates?", "Yes. The posts, the hinges, and the latch are sized for the leaf. A gate that is too heavy for its posts sags within a season. That is a layout decision, not something we fix with a bigger hinge later."),
            ("Is metal fencing the same as aluminum fencing?", "No. Aluminum is lighter and does not rust. Steel is stronger and needs a maintained finish. We will tell you which one the opening actually requires instead of using one word for both."),
        ],
    },
    {
        "file": "picket-fence.html",
        "title": "Picket Fence Installation in Johnson City, TN",
        "description": "Wood and vinyl picket fences for front yards in Johnson City, TN. Open lines that keep sight distance. Call (423) 468-2697.",
        "h1": "Picket fence installation in Johnson City, TN",
        "crumb": "Picket fencing",
        "faq_label": "picket fencing",
        "image": "images/picket.jpg",
        "alt": "White picket fence in front of a house and garden",
        "intro": "Open picket, in wood or vinyl, for front yards and gardens that need a boundary without a wall. Heights stay low enough to keep the street view clear.",
        "when": "Choose picket when the fence is in front of the house, along a walk, or around a garden. It marks the yard and still lets the house show. It is a weak privacy fence and a weak dog fence for an animal that can jump a 3-foot line. On a Johnson City corner lot, the sight triangle cannot exceed 3 feet, which is why a short picket is often the fence that actually fits the frontage.",
        "process": [
            ("Place it.", "Front yard, side return, or garden. The place decides the height before the style does."),
            ("Pick wood or vinyl.", "Wood can be painted to the trim. Vinyl holds a color without that repaint. Both can be a picket."),
            ("Mind the triangle.", "On a corner, we keep the fence at or under 3 feet inside the 25-foot sight triangle."),
            ("Set a gate on the walk.", "The opening should match the path you already use, not a spot that is merely convenient to build."),
        ],
        "after": "<p>A picket fence and a <a href=\"privacy-fence.html\">privacy fence</a> solve different problems. If the goal is to block the neighbor’s view of the patio, picket will disappoint you. If the goal is a front boundary that still looks open, privacy board is the wrong product.</p>",
        "factors": [
            ("Height", "A 3-foot front picket and a 4-foot side picket are different amounts of material and different rule checks."),
            ("Material", "Painted wood and vinyl picket are both available. Paint is upkeep. Vinyl is a higher material cost."),
            ("Spacing", "Wider gaps cost less lumber and contain less. Closer pickets read more like a short screen."),
            ("Gates and corners", "Every walk opening and every corner post is its own piece of the quote."),
        ],
        "related": [("wood-fence.html", "Wood fencing"), ("vinyl-fence.html", "Vinyl fencing"), ("aluminum-fence.html", "Aluminum fencing")],
        "faqs": [
            ("How much does a picket fence cost in Johnson City?", "Short frontages cost less than a full backyard privacy line because the height and the footage are smaller. Wood versus vinyl, the number of gates, and a corner layout still move the price. We measure the frontage."),
            ("Can you put a picket fence in a front yard?", "Yes, when the height fits the city rule and any HOA sheet. Corner lots are the constraint: inside the 25-foot sight triangle the fence stays at 3 feet. A tall privacy fence does not belong there."),
            ("Do you build wood picket and vinyl picket?", "Both. Wood is the one you paint to match shutters or trim. Vinyl is the one you are not repainting. The layout is the same. The upkeep is not."),
            ("Will a picket fence hold a dog?", "Only a dog that cannot jump or squeeze the gaps. A 3-foot picket is a boundary, not a kennel. If containment is the job, look at chain link or a taller privacy line on the side and rear."),
            ("Can picket match an older Johnson City house?", "Wood picket, painted, is the usual match for an older front yard. We set the height to the street and the corner rule, not to a photo of a cottage. Spacing and post caps are chosen on site."),
        ],
    },
    {
        "file": "privacy-fence.html",
        "title": "Privacy Fence Installation in Johnson City, TN",
        "description": "Wood and vinyl privacy fences in Johnson City, TN for side and rear yards. Call (423) 468-2697 for a free on-site estimate.",
        "h1": "Privacy fence installation in Johnson City, TN",
        "crumb": "Privacy fencing",
        "faq_label": "privacy fencing",
        "image": "images/vinyl-privacy.jpg",
        "alt": "White vinyl fence with a solid privacy panel meeting a semi-private section",
        "intro": "Solid wood or vinyl panels that close a backyard off from the next house. A screen for the side and rear, not a front-yard wall and not a security system.",
        "when": "Choose a privacy fence when the goal is to block the view into a patio, a pool deck, or a rear yard. Wood gives you a stainable screen. Vinyl gives you the same screen without a stain cycle. Neither one is a burglar alarm. On a corner, the tall solid section stops before the sight triangle. Exposed lots on a ridge catch more wind, so post spacing has to match a solid wall, not an open picket.",
        "process": [
            ("Pick the material.", "Wood or vinyl, based on upkeep and whatever the HOA already wrote down."),
            ("Keep it off the front triangle.", "Tall privacy stays on the side and rear. The corner view for drivers stays open."),
            ("Set posts for a solid wall.", "A privacy panel catches wind. Posts are in concrete, spaced for that load, crowned in the clay."),
            ("Hang panels and a useful gate.", "The gate is wide enough for the mower. The latch works from the side you use."),
        ],
        "after": "<p>Semi-privacy, with gaps between pickets, is a middle option when you want light and air and only a partial screen. The photo on this page shows both a gapped section and a solid panel. We can mix them on one line if the rear needs the screen and the side does not.</p>",
        "factors": [
            ("Wood or vinyl", "The two materials price differently and age differently. The quote names which one."),
            ("Height", "Inside the city, over 7 feet needs a building permit. Most house screens are at or under that."),
            ("Wind and grade", "A solid fence on an exposed or sloping lot needs a layout a flat catalog photo does not show."),
            ("Gates", "One mower gate is normal. A second opening for a side yard changes the price."),
        ],
        "related": [("wood-fence.html", "Wood fencing"), ("vinyl-fence.html", "Vinyl fencing"), ("picket-fence.html", "Picket fencing")],
        "faqs": [
            ("How much does a privacy fence cost in Johnson City?", "Material, height, footage, gates, and removal of the old fence decide it. Vinyl privacy and wood privacy are different prices on the same line. Slope and trees add labor. We do not publish a flat rate."),
            ("Can you install a privacy fence on the property line?", "Often, if it stays on your side of the pins, out of easements, and out of the right-of-way. The city does not survey the line for you. Know where the pins are, and tell the neighbor before the posts go in."),
            ("Do I need a privacy fence or a picket fence?", "Privacy, if you want the view blocked. Picket, if you want a low open edge in front of the house. Using a 6-foot solid panel as a front fence on a corner lot conflicts with the sight-triangle rule."),
            ("Will a solid fence blow over on a windy lot?", "It can, if the posts are shallow. Exposed yards toward the ridges need post depth and spacing that account for a solid surface. We will not use open-picket spacing on a privacy wall and hope."),
            ("Can you mix solid panels and spaced pickets?", "Yes. A solid rear line and a more open side return is a common layout. Both sections are on one estimate so the posts and the gate still line up."),
        ],
    },
    {
        "file": "farm-fence.html",
        "title": "Farm Fence Installation in Johnson City, TN",
        "description": "Rail and woven-wire farm fencing near Johnson City for horses and cattle. Longer runs in Washington County. Call (423) 468-2697.",
        "h1": "Farm fence installation near Johnson City, TN",
        "crumb": "Farm fencing",
        "faq_label": "farm fencing",
        "image": "images/farm.jpg",
        "alt": "White rail fence dividing a green pasture",
        "intro": "Rail and woven wire for horses, cattle, and property lines on acreage. Built for a pasture, not copied from a backyard panel.",
        "when": "Choose farm fence when the line is long and the point is animals or a field boundary. Horses need a fence they can see, such as rail. Cattle can be held with woven wire, sometimes with a strand of electric. We do not put horses on barbed wire. A house-yard vinyl privacy panel is the wrong product once the run leaves the yard and enters the field. Those longer lines are common toward Telford and Limestone, where the parcels are agricultural rather than subdivision lots.",
        "process": [
            ("Name the animals.", "Horses, cattle, goats, or a boundary with no stock. The animal picks the fence."),
            ("Walk the braces and gates.", "Corners, ends, and the truck gate carry the load. A straight run is the cheap part."),
            ("Set posts for the ground.", "Creek bottoms stay soft. Ridge edges hit rock. Post depth follows the hole we actually dig."),
            ("Stretch wire or hang rail.", "Wire is pulled and stapled. Rail is set so a horse can see it. Gates latch for the opening you drive."),
        ],
        "after": "<p>A farm job is quoted on corners, braces, gates, and brush, not on a neighborhood per-foot habit. If you also want a privacy screen around the house, that is a second fence and a second number. See <a href=\"wood-fence.html\">wood fencing</a> for the yard line.</p>",
        "factors": [
            ("Animal", "A horse rail fence and a cattle wire fence are different materials, even on the same farm."),
            ("Length and terrain", "A flat pasture and a line that crosses a wet draw do not take the same posts."),
            ("Gates", "A 12-foot farm gate for a truck or a trailer is its own piece of the quote."),
            ("Clearing", "Brush, an old wire fence, and grown-in posts add time before the new line starts."),
        ],
        "related": [("wood-fence.html", "Wood fencing"), ("chain-link-fence.html", "Chain-link fencing"), ("fence-company-telford-tn.html", "Telford")],
        "faqs": [
            ("How much does farm fencing cost near Johnson City?", "Long runs are priced on posts, braces, wire or rail, and gates, plus clearing. A short paddock by the barn is a different job from a property-line wire across a field. We walk it before we number it."),
            ("Can you fence horses without barbed wire?", "Yes. Horses get a visible fence: rail, or a rail-and-wire mix they can see. Barbed wire is a poor horse fence and we do not spec it for them. Cattle are a different conversation and can use woven wire."),
            ("Do you build fence in Telford and Limestone?", "Yes. Those are agricultural parts of Washington County, and the jobs there are usually longer than a Johnson City backyard. Say which community you are in so we plan the drive and the materials."),
            ("Can the house yard and the pasture be different fences?", "Yes. Wood or vinyl around the house, and rail or wire on the field, is a normal layout. They are quoted separately so you can build one now."),
            ("What if the ground along the creek stays wet?", "We do not set a brace post in standing water and hope. Soft bottomland along a creek may need a moved line or a different post plan. We will say so on the walk-through."),
        ],
    },
    {
        "file": "commercial-fencing.html",
        "title": "Commercial Fence Installation in Johnson City, TN",
        "description": "Commercial chain link, rail, and vehicle gates for lots in Johnson City and Piney Flats, TN. Call (423) 468-2697.",
        "h1": "Commercial fence installation in Johnson City, TN",
        "crumb": "Commercial fencing",
        "faq_label": "commercial fencing",
        "image": "images/commercial.jpg",
        "alt": "Black metal rail fence along a maintained lawn",
        "intro": "Heavier chain link, ornamental rail, and vehicle gates for yards, shops, and job sites. Specified for the use of the lot, not borrowed from a residential panel.",
        "when": "Choose a commercial spec when trucks, equipment, or the public meet the fence. A storage yard along the Piney Flats and 11E corridor is a different fence from a backyard in Gray. Fabric gauge, post size, and the vehicle gate are the parts that change. A house-grade chain-link panel will not stand in for that. Ornamental rail is an option when the lot also has to look finished from the road.",
        "process": [
            ("Define the use.", "Storage, equipment, a customer edge, or a temporary job site. The use sets the spec."),
            ("Place the openings.", "Where trucks enter decides the gate before the long runs do."),
            ("Set a commercial post layout.", "Heavier posts, concrete, and bracing at the corners and at the gate."),
            ("Hang the gate and finish the line.", "Drop rods, cane bolts, or rollers, depending on the leaf. Then the fabric or rail."),
        ],
        "after": "<p>We do not invent access-control systems or claim a fence is a security program. We build the barrier and the gate you can actually operate. If the site is in another town’s jurisdiction, the height rule may not be the Johnson City residential 7-foot note. We confirm the parcel.</p>",
        "factors": [
            ("Spec", "Commercial gauge and post size cost more than a residential chain-link run. That difference is the point."),
            ("Vehicle gates", "A sliding or double-swing drive gate is often the largest line on the quote."),
            ("Length and paving", "Coring pavement or working around a curb adds labor a grass yard does not have."),
            ("Screen", "Privacy slats or a windscreen are optional and change the wind load on the posts."),
        ],
        "related": [("chain-link-fence.html", "Chain-link fencing"), ("metal-fence.html", "Metal fencing"), ("gate-installation.html", "Gate installation")],
        "faqs": [
            ("How much does a commercial fence cost in Johnson City?", "Gate size and spec move it more than the long run does. A vehicle opening, heavier posts, and any coring through pavement are the usual cost drivers. We look at the lot before we price it."),
            ("Can you fence a lot in Piney Flats?", "Yes. That corridor is commercial and industrial ground in Sullivan County, close enough to be in this service area. The fence is specified for trucks and yard use, not for a subdivision rear line."),
            ("Do you install barbed wire on commercial fences?", "When the site and the rule allow it, a top strand can be part of a commercial chain-link spec. It is not something we add to a residential yard. We confirm the parcel before we include it."),
            ("Is a commercial fence just a taller version of a house fence?", "No. Post size, fabric gauge, bracing, and the gate hardware are different. Using residential materials on a work yard is how a gate fails."),
            ("Can you match a black rail fence along a street frontage?", "Yes. Ornamental rail is an option where the edge of the property faces customers. The secure yard behind it can still be chain link. They are two specs on one property."),
        ],
    },
    {
        "file": "gate-installation.html",
        "title": "Fence Gate Installation in Johnson City, TN",
        "description": "Walk gates and drive gates in Johnson City, TN, including repairs for sagging or stuck gates. Call (423) 468-2697.",
        "h1": "Fence gate installation in Johnson City, TN",
        "crumb": "Gate installation",
        "faq_label": "gate installation",
        "image": "images/gate.jpg",
        "alt": "Double driveway gate set between masonry posts",
        "intro": "Walk gates and drive gates hung on posts that can carry the leaf. New openings, and repairs when a gate drags, sags, or will not latch.",
        "when": "A gate is not a leftover panel. A 3-foot walk gate, a 4-foot mower gate, and a double drive gate put different loads on the posts. Most callbacks we see are a leaf hung on posts that were never sized for it, or hinges that have pulled out of rotten wood. If the posts are sound, we can rehang hardware. If they are not, the repair is new posts, not a bigger hinge.",
        "process": [
            ("Measure the opening.", "The machine or the vehicle that has to pass, plus clearance for the swing or the slide."),
            ("Check the posts.", "Sound posts can take new hardware. Rotted or loose posts get replaced before the leaf goes on."),
            ("Choose the leaf.", "Wood, vinyl, aluminum, or steel to match the fence, in a width the opening can actually take."),
            ("Hang and latch.", "Hinges, a latch you can use, and a ground clearance that survives the high spot."),
        ],
        "after": "<p>Masonry posts, like the driveway in the photo, need hinges rated for that mount. We do not bolt a heavy steel leaf to a post that was built for a light aluminum section. If the whole fence is failing, start with <a href=\"fence-repair.html\">fence repair</a> so the gate is not the only part left standing.</p>",
        "factors": [
            ("Opening width", "A wider leaf needs heavier posts and hardware. Width is the first number we need."),
            ("Swing or slide", "A swing gate needs room to open. A slide is for a driveway that cannot give up that arc."),
            ("Material", "The leaf should match the fence. Mixing a steel gate onto a light vinyl line without the right posts fails."),
            ("Existing posts", "Reusing posts saves money only when they are still solid. We will not pretend they are."),
        ],
        "related": [("fence-repair.html", "Fence repair"), ("metal-fence.html", "Metal fencing"), ("aluminum-fence.html", "Aluminum fencing")],
        "faqs": [
            ("How much does a fence gate cost in Johnson City?", "Width, material, and whether the posts have to be replaced decide it. A walk gate on sound posts is a small job. A double drive gate with new posts is not. Tell us the opening and send a photo if you have one."),
            ("Can you fix a gate that drags on the ground?", "Often. Sometimes the hinges can be reset. Sometimes the post has leaned in the clay and has to be reset or replaced. We look at the post before we sell you a new leaf you do not need."),
            ("Can you add a gate to a fence that does not have one?", "Yes, if we can cut an opening and set posts that carry the new leaf. On a tensioned chain-link line, that also means rebuilding the terminal posts so the fabric stays tight."),
            ("Do you install double driveway gates?", "Yes. They need posts sized for both leaves and hardware that holds them, such as drop rods. A single wide leaf is sometimes the better swing. We say which one fits the driveway."),
            ("Can a pool gate be added later?", "A pool gate has to self-close and self-latch at the height the barrier code requires. We can add one when the fence itself meets the barrier rule. A short decorative gate on a 4-foot picket is not a pool gate."),
        ],
    },
    {
        "file": "fence-repair.html",
        "title": "Fence Repair in Johnson City, TN",
        "description": "Fence repair in Johnson City, TN for rotten posts, broken boards, and sagging gates. Call (423) 468-2697 to have the line looked at.",
        "h1": "Fence repair in Johnson City, TN",
        "crumb": "Fence repair",
        "faq_label": "fence repair",
        "image": "images/repair.jpg",
        "alt": "A carpenter resetting boards on a wood fence gate",
        "intro": "Boards, mesh, rails, and gates replaced where the rest of the line is still sound. If the posts have failed, we say so instead of covering them up.",
        "when": "Call for a repair when a section leans, a gate drags, boards are missing, or a chain-link run has come loose. The usual cause in this area is rot at the ground line, a post that heaved in wet clay, or wind on a solid panel. A repair is the right spend when the posts still hold. It is the wrong spend when you would be nailing new boards to posts that will fall next winter.",
        "process": [
            ("Look at the posts first.", "Sound, soft, or loose. That single check decides repair versus rebuild."),
            ("Name the failed piece.", "Boards, a rail, mesh, a cap, or the gate hardware."),
            ("Match what can be matched.", "Same board width or same fabric when the product still exists. We tell you when it does not."),
            ("Fix only the failed run.", "We do not replace a straight section to make the quote larger."),
        ],
        "after": "<p>After a wet winter, several posts in a clay yard can heave together. That is a rebuild of those holes, not a new board. If you want a full new line instead, the material pages cover <a href=\"wood-fence.html\">wood</a>, <a href=\"vinyl-fence.html\">vinyl</a>, and <a href=\"chain-link-fence.html\">chain link</a>.</p>",
        "factors": [
            ("Posts", "New posts mean digging in clay or rock. That is the expensive part of a repair."),
            ("Access", "A backyard with no gate wide enough for materials takes more time than a line off the driveway."),
            ("Matching", "Odd board widths and discontinued vinyl colors can force a close match instead of an exact one."),
            ("How much failed", "One gate is a small visit. A whole side that leans is closer to a new fence."),
        ],
        "related": [("gate-installation.html", "Gate installation"), ("wood-fence.html", "Wood fencing"), ("chain-link-fence.html", "Chain-link fencing")],
        "faqs": [
            ("How much does fence repair cost in Johnson City?", "A single gate or a few boards is a small job. Replacing several posts in clay is closer to a partial rebuild. We need to see how many posts have actually failed before we give a number."),
            ("Can you repair a fence after wind or a heavy rain?", "Yes. We separate what the weather broke from what was already rotten. Broken boards on solid posts get replaced. Posts that pulled out of wet clay get reset or replaced. We will not nail a new panel to a loose post."),
            ("Do you repair chain link as well as wood?", "Yes. Loose fabric, a bent top rail, a failed gate, and a terminal post that has leaned are all repair work. If the whole run is rusted through, replacement is the honest recommendation."),
            ("Can you just replace the boards and leave the old posts?", "Only when the posts are solid. If a screwdriver sinks into the post at the ground line, that post is done. New lumber on it will look fine until the next wet season, then it will lean again."),
            ("Is it worth repairing a fence that is mostly still standing?", "Often, yes. Replacing one bad corner and a gate costs less than a new line around the yard. We will tell you if the remaining posts are too far gone for that to make sense."),
        ],
    },
]


def services_page():
    desc = "Wood, vinyl, aluminum, chain-link, metal, picket, privacy, farm, and commercial fencing in Johnson City, TN, plus gates and repair."
    blurbs = {s["file"]: s["intro"] for s in SERVICES_DATA}
    cards = []
    for href, label in FOOTER_SERVICES:
        cards.append(f'''<a class="service-card" href="{href}">
        <span class="body"><h3>{label}</h3><p>{blurbs[href]}</p><span class="more">View service</span></span>
      </a>''')
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("services.html", "Services")])}
    <h1>Fence services in Johnson City, TN</h1>
    <p class="lede">Each fence below is a different job. Pick the one that matches the yard, the animals, or the lot, then call {PHONE} or send the details.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")} <a class="btn btn-ghost btn-lg" href="contact.html#quote">Get a free quote</a></div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="card-grid services">{"".join(cards)}</div>
  </div>
</section>'''
    graph = [
        business_node(),
        webpage("services.html", "Fence services in Johnson City, TN", desc, SITE + "/#business"),
        crumbs_schema("services.html", [("services.html", "Services")]),
    ]
    layout("services.html", "Fence Services in Johnson City, TN | Johnson's Fence Company", desc, body, graph)


FAQ_ITEMS = [
    (
        "How much does a fence cost in Johnson City, TN?",
        "The price follows the line we measure: length, height, material, gates, and whether an old fence has to come out. Clay that holds water, a slope, tree roots, and rock on a ridge lot all change the labor. We do not publish a per-foot menu. The estimate comes from the property.",
    ),
    (
        "Can you set fence posts in the clay and rock around Johnson City?",
        "Yes. Valley lots in Washington County are often clay that stays wet after rain, and ridge lots toward Unicoi and Buffalo Mountain can hit rock. Posts go in concrete, with the mix crowned so water does not pool at the post. If a hole hits solid rock or a stretch stays saturated, we say so before we set it.",
    ),
    (
        "Do you offer wood, vinyl, aluminum, chain link, and farm fencing?",
        "Yes. Wood and vinyl cover privacy and picket work. Aluminum and ornamental steel cover open lines and gates. Chain link covers yards, dogs, and work lots. Farm fencing covers rail and wire for animals on longer runs. Gates and repairs are scheduled with the same crew.",
    ),
    (
        "Do I need a permit to put up a fence in Johnson City?",
        "Inside the city, published standards allow a standard residential fence up to 7 feet without a structural permit. Taller than that needs a building permit. On a corner lot, the 25-foot sight triangle stays at 3 feet. A historic overlay can require design review before the fence changes. Outside the city limits, the parcel may fall under Washington County, another town, or the Johnson City planning region. Confirm which one applies. An HOA can be stricter than all of them.",
    ),
    (
        "Can you repair a leaning fence, or does the whole line have to come out?",
        "If the posts are still sound, we replace the boards, rails, mesh, or gate that failed and leave the rest. If the posts have rotted at the ground line or heaved out of the clay, new boards on those posts will lean again, and that stretch should be rebuilt. We will tell you which it is after we see the line.",
    ),
    (
        "Do you offer gates as their own job?",
        "Yes. A walk gate, a mower gate, and a double drive gate are different builds. We can add an opening to an existing fence when the posts can carry the leaf, or replace hardware when the posts are still solid. If the posts have failed, the gate repair includes new posts.",
    ),
    (
        "Do I need to call 811 before you dig?",
        "Someone has to. Tennessee 811 needs at least three working days of notice before excavation so utilities can be marked. We do not set posts on unmarked ground. If you have already called, tell us the ticket number when you book the visit.",
    ),
    (
        "Can you build a pool barrier that meets the code?",
        "A pool that needs a permit also needs a barrier that meets the safety code the city has adopted. Height, openings, and a self-closing, self-latching gate are part of that. We spec the barrier to the rule. A short decorative picket is not assumed to qualify.",
    ),
]


def faq_page():
    desc = "Fence cost, clay and rock, materials, Johnson City permit rules, and repairs. Answers from Johnson's Fence Company. Call (423) 468-2697."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("faq.html", "FAQ")])}
    <h1>Fence questions in Johnson City</h1>
    <p class="lede">Straight answers about price, ground, materials, city rules, and repairs. If your lot is outside the city, say so. The rule may not be the city’s.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    {faq_cards(FAQ_ITEMS)}
    <p style="margin-top:1.2rem"><a href="contact.html#quote">Request an estimate</a> or see <a href="services.html">all services</a>.</p>
  </div>
</section>'''
    graph = [
        business_node(),
        webpage("faq.html", "Fence questions in Johnson City", desc, SITE + "/#business"),
        faq_schema("faq.html", FAQ_ITEMS),
        crumbs_schema("faq.html", [("faq.html", "FAQ")]),
    ]
    layout("faq.html", "Fence FAQ for Johnson City, TN | Johnson's Fence Company", desc, body, graph)


def about_page():
    desc = "Johnson's Fence Company installs and repairs fences for homes, farms, and commercial lots in Johnson City, TN. Call (423) 468-2697."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("about.html", "About")])}
    <h1>About Johnson's Fence Company</h1>
    <p class="lede">We install and repair fences in Johnson City and nearby towns. You call, we come to the property, and you get a number for that line.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")}</div>
  </div>
</section>
<section class="section">
  <div class="container split">
    <div class="split-media"><img src="images/hero.jpg" alt="Wood privacy fence along a backyard beside a house" width="1200" height="800"></div>
    <div class="prose">
      <h2>What we take on</h2>
      <p>Wood, vinyl, aluminum, chain link, ornamental metal, picket, privacy, farm, and commercial fence, plus gates and repairs. A backyard screen, a front-yard picket, a dog run, a shop yard, and a pasture line are all work we price. They are not the same product.</p>
      <p>There is no public storefront listed. Estimates are done on the lot. The phone number is {PHONE}.</p>
    </div>
  </div>
</section>
<section class="section soft">
  <div class="container prose">
    <h2>How we work a Johnson City lot</h2>
    <p>The valley ground is often clay that holds water. Ridges toward Unicoi and Buffalo Mountain can turn up rock. Summers are humid, and winters freeze and thaw, which is hard on a post set too shallow and on wood left bare at the ground line. Inside the city, a standard residential fence can go to 7 feet without a structural permit, and a corner sight triangle stays at 3 feet. A parcel outside the city is not automatically under that rule.</p>
    <p>If the posts on an old line are sound, we repair. If they have failed, we say so. The materials we install are the ones on the <a href="services.html">services</a> pages, matched to the job.</p>
    <p><a href="service-areas.html">See the towns we serve</a> or <a href="contact.html">request an estimate</a>.</p>
  </div>
</section>'''
    graph = [
        business_node(),
        webpage("about.html", "About Johnson's Fence Company", desc, SITE + "/#business"),
        crumbs_schema("about.html", [("about.html", "About")]),
    ]
    layout("about.html", "About Johnson's Fence Company in Johnson City, TN", desc, body, graph)


def contact_page():
    desc = "Request a free fence estimate in Johnson City, TN. Call (423) 468-2697 or send the town, fence type, and approximate length."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("contact.html", "Contact")])}
    <h1>Request a fence estimate</h1>
    <p class="lede">Call {PHONE} or use the form. Estimates are free. We are a service-area company in Johnson City, with no public storefront listed.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")}</div>
  </div>
</section>
<section class="section">
  <div class="container contact-layout">
    <div class="prose">
      <h2>What to include</h2>
      <p>The town, the fence type if you know it, about how much line you need, and whether an old fence has to come out. A gate for a mower and a gate for a truck are different. Photos help.</p>
      <p>If an HOA has a written fence rule, mention that in the form so we do not order the wrong height or color.</p>
      <div class="map-frame">
        <iframe title="Map of Johnson City, Tennessee" src="https://maps.google.com/maps?q={LAT},{LNG}&amp;z=11&amp;output=embed" loading="lazy"></iframe>
        <p class="map-caption">Service area centered on Johnson City. This map marks the city, not a storefront.</p>
      </div>
    </div>
    {tally_block()}
  </div>
</section>'''
    graph = [
        business_node(),
        webpage("contact.html", "Request a fence estimate", desc, SITE + "/#business"),
        crumbs_schema("contact.html", [("contact.html", "Contact")]),
    ]
    layout("contact.html", "Contact Johnson's Fence Company in Johnson City, TN", desc, body, graph)


LOC_DATA = [
    {
        "file": "fence-company-jonesborough-tn.html",
        "name": "Jonesborough",
        "title": "Fence Company in Jonesborough, TN",
        "description": "Fence installation in Jonesborough, TN for narrow in-town lots and longer county lines outside town. Call (423) 468-2697.",
        "intro": "Jonesborough lots in town are often narrower than a new subdivision in Gray, with short side yards and older trees on the line. Outside town, the same drive reaches agricultural ground that wants a different fence.",
        "detail": "We do not treat a Jonesborough street as if it were under the Johnson City zoning ordinance. The town has its own review, and some in-town properties sit in a local historic district where a fence on the frontage can need design approval before it goes up. Ask the town if your parcel is in that district. A 6-foot privacy fence that fits a rear yard in Johnson City may be the wrong height and the wrong material on a Jonesborough frontage. Farther out, toward Washington County acreage, the job turns into rail or wire. Those are quoted as a separate line from the house yard.",
        "points": [
            ("Narrow side yards", "The gate width has to be exact. There is not much room to adjust after the concrete is in."),
            ("Town versus county", "In-town historic frontages and outlying pasture are different rules and different fences."),
            ("Older trees", "Roots along an established lot change post spacing. We lay the line around them instead of cutting through."),
        ],
        "services": [("wood-fence.html", "Wood fencing"), ("picket-fence.html", "Picket fencing"), ("farm-fence.html", "Farm fencing")],
        "faqs": [
            ("Do Johnson City’s fence heights apply in Jonesborough?", "No. Jonesborough is its own town. Bring the local rule, or we will confirm it before we order a height. A city of Johnson City number copied onto a Jonesborough frontage is how a fence gets rejected."),
            ("Can you fence a small side yard in town?", "Yes. Short runs are normal here. We measure the opening for the gate first, because a mower gate that is an inch too wide does not fit."),
            ("Do you also fence acreage outside Jonesborough?", "Yes. House-yard wood or vinyl and a field fence on the rest of the parcel are two quotes. Tell us which one you want built first."),
        ],
    },
    {
        "file": "fence-company-elizabethton-tn.html",
        "name": "Elizabethton",
        "title": "Fence Company in Elizabethton, TN",
        "description": "Fence installation in Elizabethton, TN for wet river-bottom yards and rocky hillside lots in Carter County. Call (423) 468-2697.",
        "intro": "Elizabethton sits in Carter County, with river-bottom ground that stays wet and hillside lots that climb toward rock. The post plan follows whichever of those the yard actually is.",
        "detail": "Low yards near the Watauga and Doe rivers can hold water after a hard rain. We do not set posts in a saturated hole. If a corner of the lot stays soft, the line moves onto firmer ground or we wait. Hillside streets are the opposite problem: shallow soil over rock, and a grade that has to be stepped. A privacy fence racked like a flat Johnson City backyard will gap at the bottom. Carter County and the city of Elizabethton are not Washington County, so we do not copy a Johnson City permit note onto these parcels. Confirm the rule with the office that governs the lot.",
        "points": [
            ("Wet bottoms", "River-bottom clay stays soft. Posts go in only where the hole will hold concrete."),
            ("Rocky slopes", "Hill lots need a stepped layout and a plan for holes that hit rock."),
            ("Different county", "Elizabethton rules are not the Johnson City 7-foot note. We check the parcel."),
        ],
        "services": [("privacy-fence.html", "Privacy fencing"), ("wood-fence.html", "Wood fencing"), ("aluminum-fence.html", "Aluminum fencing")],
        "faqs": [
            ("Can you install a fence in a yard that floods near the river?", "Not in standing water. We look at the low spots first. The line can often move a few feet onto higher ground. If it cannot, we wait or we change the plan."),
            ("What fence works on a steep Elizabethton lot?", "Panels are stepped so the bottom stays near the grade. Aluminum can rack on a milder slope. A single straight privacy panel pulled downhill opens a gap."),
            ("Are Elizabethton fences under Johnson City rules?", "No. Elizabethton is in Carter County and has its own city government. We confirm height and permit questions there instead of reusing the Johnson City standard."),
        ],
    },
    {
        "file": "fence-company-gray-tn.html",
        "name": "Gray",
        "title": "Fence Company in Gray, TN",
        "description": "Vinyl, wood, and aluminum fences for Gray, TN subdivisions along US-11E. HOA colors included. Call (423) 468-2697.",
        "intro": "Gray is subdivision ground along US-11E in Washington County. The fence question is usually an HOA color, a rear privacy line, and posts that will hold in valley clay.",
        "detail": "Newer neighborhoods here often write down height, color, and which side of the fence faces the neighbor. We want that sheet before we order white vinyl, stained wood, or a black aluminum front fence. Guessing from the house next door is how the material comes back. Lots are house-sized, not pastures, so the work is wood, vinyl, and aluminum, with chain link only where the covenants allow a dog run or a rear line. Irrigation on a new yard is flagged before we dig. Gray is not inside the City of Johnson City municipal limits by default, so a city permit answer does not automatically transfer.",
        "points": [
            ("HOA sheets", "Height, color, and the finished side should be in writing before the material is ordered."),
            ("House lots, not acreage", "Privacy on the rear line and a lower fence in front is the usual layout."),
            ("Valley clay", "Posts still go in concrete. New-lot irrigation lines get marked first."),
        ],
        "services": [("vinyl-fence.html", "Vinyl fencing"), ("wood-fence.html", "Wood fencing"), ("aluminum-fence.html", "Aluminum fencing")],
        "faqs": [
            ("Can you match an HOA fence color in Gray?", "If the HOA names a color or a material, we order that. Send the sheet with the estimate so the quote uses the right product."),
            ("Is chain link allowed in Gray subdivisions?", "Some allow it on the rear line and some do not. The covenants decide. We will not guess from the fence next door."),
            ("Does the Johnson City 7-foot rule apply in Gray?", "Gray is in Washington County, and many lots are outside the city limits. Do not assume the city standard. We confirm the parcel, and the HOA can be stricter than either one."),
        ],
    },
    {
        "file": "fence-company-boones-creek-tn.html",
        "name": "Boones Creek",
        "title": "Fence Company in Boones Creek, TN",
        "description": "Fencing in Boones Creek, TN for sloped lots near Boone Lake and established yards northwest of Johnson City. Call (423) 468-2697.",
        "intro": "Boones Creek mixes established yards northwest of Johnson City with lots that drop toward Boone Lake. Slope and the shoreline setback matter more here than they do on a flat street in town.",
        "detail": "A lake lot is not a place to run a privacy fence to the water because the drawing looked square. Shoreline setbacks, a shared access, and the grade down to the lake all change where posts can go. We stop the fence where the rule and the slope say to stop it. Neighborhoods away from the water are closer to a normal Johnson City house lot: side and rear privacy, a gate for the mower, and clay posts. Some of this area falls in the city’s planning region even when the mailing address says Boones Creek. We check the parcel instead of assuming.",
        "points": [
            ("Lake grade", "Lines that drop toward Boone Lake are stepped, and they stop short of a shoreline setback."),
            ("Established yards", "Older lots have trees and fences that may only need a repair, not a full replacement."),
            ("Which office governs", "City planning region and county parcels both show up in Boones Creek. We confirm which."),
        ],
        "services": [("privacy-fence.html", "Privacy fencing"), ("aluminum-fence.html", "Aluminum fencing"), ("fence-repair.html", "Fence repair")],
        "faqs": [
            ("Can you run a fence down to Boone Lake?", "Only up to the setback that applies to that lot. We do not set posts in the shoreline zone to gain a few feet of yard. The line stops where it is allowed to stop."),
            ("What about a yard in Boones Creek that is not on the water?", "Those are usually side-and-rear privacy or a repair of an older wood line. Tell us if the lot slopes. A flat-panel layout on a drop opens a gap at the bottom."),
            ("Is Boones Creek inside Johnson City?", "Some of it is in the city’s planning region and some of it is Washington County. The mailing address does not settle the permit question. We look at the parcel."),
        ],
    },
    {
        "file": "fence-company-piney-flats-tn.html",
        "name": "Piney Flats",
        "title": "Fence Company in Piney Flats, TN",
        "description": "Commercial chain link and vehicle gates in Piney Flats, TN, along the I-26 and US-11E corridor. Call (423) 468-2697.",
        "intro": "Piney Flats is commercial and industrial ground in Sullivan County, where I-26 meets US-11E. The fences here are yard perimeters and vehicle gates, not backyard privacy panels.",
        "detail": "A shop lot or a small warehouse yard needs a heavier chain-link spec, posts sized for a drive gate, and a layout that matches where trucks turn. Residential fabric and a light walk gate will not do that job. There are houses in the area too, and those are quoted as house fences, separate from the commercial line. Sullivan County is not Washington County, and Piney Flats is not under a Johnson City residential height note just because we drive there from Johnson City. We confirm the site before we order a height or a top strand.",
        "points": [
            ("Work yards", "Gauge, post size, and the truck gate are the spec. A house panel is the wrong product."),
            ("Sullivan County", "The rules here are not the City of Johnson City residential rules."),
            ("Houses still exist", "A home on the edge of the corridor is priced as a residential fence, not as a commercial yard."),
        ],
        "services": [("commercial-fencing.html", "Commercial fencing"), ("chain-link-fence.html", "Chain-link fencing"), ("gate-installation.html", "Gate installation")],
        "faqs": [
            ("Can you fence a commercial lot in Piney Flats?", "Yes. That is the main reason this page exists. Tell us the gate width the trucks need and whether the fence is on grass or through pavement."),
            ("Do you use residential chain link on these yards?", "No. A storage yard gets a commercial post and fabric spec. Residential chain link is for house lots, including houses that happen to be near the corridor."),
            ("Is Piney Flats in the Johnson City city limits?", "No. It is in Sullivan County. We do not apply the Johnson City residential fence standard to a commercial site there."),
        ],
    },
    {
        "file": "fence-company-telford-tn.html",
        "name": "Telford",
        "title": "Fence Company in Telford, TN",
        "description": "Farm and house-yard fencing in Telford, TN. Rail, woven wire, and repairs on Washington County acreage. Call (423) 468-2697.",
        "intro": "Telford is rural Washington County. Fence work here is usually a long pasture line, a farm gate, and sometimes a shorter screen around the house.",
        "detail": "We spec rail for horses and woven wire for cattle, with braces at the corners and a gate a truck can use. A backyard privacy price per foot does not describe this work. Ground along low draws stays soft after rain, so brace posts are placed where the hole will hold. The house yard, if you want one, is wood, vinyl, or chain link and is quoted on its own. Telford is not a subdivision vinyl market, and it is not inside Johnson City. County questions go to Washington County, not to the city building desk.",
        "points": [
            ("Pasture first", "Corners, braces, and farm gates matter more than picket style."),
            ("House yard second", "A short privacy or dog run by the house is a separate, smaller fence."),
            ("Soft ground", "Low draws stay wet. We do not set a corner brace in mud."),
        ],
        "services": [("farm-fence.html", "Farm fencing"), ("wood-fence.html", "Wood fencing"), ("chain-link-fence.html", "Chain-link fencing")],
        "faqs": [
            ("Do you build horse and cattle fence in Telford?", "Yes. Horses get a fence they can see, such as rail. Cattle can use woven wire. We do not put horses on barbed wire."),
            ("Can you fence just the yard and leave the field for later?", "Yes. We can look at both on one visit and build the yard first. The field stays its own number."),
            ("Does a Telford farm need a Johnson City fence permit?", "No. Telford is Washington County, not the city. Confirm any county question with Washington County zoning. The city’s 7-foot residential note is not the default here."),
        ],
    },
    {
        "file": "fence-company-limestone-tn.html",
        "name": "Limestone",
        "title": "Fence Company in Limestone, TN",
        "description": "Pasture fencing in Limestone, TN, including creek-bottom ground along the Nolichucky. Call (423) 468-2697.",
        "intro": "Limestone is agricultural Washington County. The fence jobs are property-line wire, paddocks, and lines that have to deal with bottomland that floods.",
        "detail": "Bottom ground near the Nolichucky is not the same digging as a Johnson City side yard. After high water, posts in the floodplain can loosen even when they were set in concrete. We look at whether the line should sit off the lowest ground. Cattle wire and horse rail are the products. A vinyl privacy fence around a house in Limestone is available, and it is a small share of the work compared with the field. We do not describe the community’s history on a fence estimate. The useful facts are the animals, the flood line, and the gate.",
        "points": [
            ("Bottomland", "Lines near the river are placed with flood and soft soil in mind, not on the lowest mud."),
            ("Livestock", "Wire or rail is chosen for the animals, with braces and a farm gate."),
            ("Not a subdivision", "HOA color sheets are rare here. Footage and terrain are the quote."),
        ],
        "services": [("farm-fence.html", "Farm fencing"), ("wood-fence.html", "Wood fencing"), ("gate-installation.html", "Gate installation")],
        "faqs": [
            ("Can you fence pasture in Limestone?", "Yes. That is the typical call. Tell us what the field holds and where the trucks need to pass."),
            ("What if the fence line floods?", "We will not set the main run in ground that stays under water. The line can move upslope. Posts that have already been loosened by high water are replaced, not tightened and left."),
            ("Is Limestone fencing the same quote as a Johnson City backyard?", "No. A long wire line with braces and a farm gate is a different estimate from a 6-foot privacy fence on a house lot. Say which one you need."),
        ],
    },
    {
        "file": "fence-company-unicoi-tn.html",
        "name": "Unicoi",
        "title": "Fence Company in Unicoi, TN",
        "description": "Fence installation in Unicoi, TN for rocky, sloped lots in the foothills south of Johnson City. Call (423) 468-2697.",
        "intro": "Unicoi lots sit in the foothills, south of Johnson City. Digging hits rock, yards slope, and a fence has to be stepped instead of pulled flat down the hill.",
        "detail": "Valley clay is the Johnson City problem. Rock and grade are the Unicoi problem. A post hole that stops on stone changes the layout and the labor, and we price that after we see it rather than promising a backyard production rate. Solid privacy panels on an exposed ridge also take wind, so the posts are spaced for a wall, not for an open picket. Runs are often shorter than a Washington County pasture because the usable yard itself is shorter. Unicoi is its own county and town. Johnson City fence heights do not travel with us down the highway.",
        "points": [
            ("Rock", "Holes that hit stone are called out on the estimate. We do not hide that labor in a flat rate."),
            ("Stepped panels", "Steep grade is stepped so animals and people cannot walk under the fence."),
            ("Wind on a ridge", "A solid screen on an exposed lot gets post spacing that matches the wind, not a catalog diagram."),
        ],
        "services": [("wood-fence.html", "Wood fencing"), ("privacy-fence.html", "Privacy fencing"), ("aluminum-fence.html", "Aluminum fencing")],
        "faqs": [
            ("Can you set posts when the ground is rocky?", "Yes, up to the point where the hole cannot be dug by ordinary means. If we hit solid rock, we stop and tell you what that section will take. We do not chip a shallow hole and call it a post."),
            ("Should a fence in Unicoi be racked or stepped?", "Mild slopes can be racked, especially in aluminum. Steep yard drops are stepped. A racked privacy panel on a steep grade opens a triangle at the bottom."),
            ("Do Johnson City permit rules apply in Unicoi?", "No. Unicoi is in Unicoi County. Confirm the local rule there. We will not order a height based on the Johnson City 7-foot standard."),
        ],
    },
    {
        "file": "fence-company-washington-county-tn.html",
        "name": "Washington County",
        "title": "Fence Company in Washington County, TN",
        "description": "Fence installation in Washington County, TN for city lots, county parcels, and farms. Rules differ by parcel. Call (423) 468-2697.",
        "intro": "Washington County is the service area around Johnson City, and the fence rule changes when you leave the city limits. The ground is the part that stays familiar: valley clay, and rock as you climb.",
        "detail": "Inside Johnson City, published standards let a standard residential fence go to 7 feet without a structural permit, and a corner sight triangle stays at 3 feet. A historic overlay can require a certificate of appropriateness. Outside the city, the county’s public materials point fence questions to zoning staff rather than publishing a simple city-style height table, and some nearby parcels are still inside the Johnson City planning region even with a county address. Gray, Boones Creek, Telford, and Limestone are all in this county and they are not the same job. We build to the parcel in front of us. Call Tennessee 811 before the holes are dug.",
        "points": [
            ("City versus county", "The Johnson City 7-foot note is not the default on an unincorporated parcel."),
            ("Planning region", "Johnson City’s planning area reaches into the county. A mailing address does not settle it."),
            ("Match the use", "A Gray privacy fence, a Telford pasture, and a Johnson City gate repair are three different specs."),
        ],
        "services": [("services.html", "All services"), ("farm-fence.html", "Farm fencing"), ("privacy-fence.html", "Privacy fencing")],
        "faqs": [
            ("Do I need a fence permit in unincorporated Washington County?", "The county does not publish a one-line answer the way the city does. Its zoning staff is the office that can say whether your parcel needs anything. Keep the fence off easements and the right-of-way either way. An HOA can add rules the county will not enforce for you."),
            ("What are the City of Johnson City fence limits?", "Published city standards allow a standard residential fence up to 7 feet without a structural permit. Over 7 feet needs a building permit. Inside a 25-foot corner sight triangle, the fence stays at 3 feet. Nothing should sit in the public right-of-way or block an easement."),
            ("Which fence belongs on county acreage?", "Farm fence on the long lines, and wood, vinyl, or chain link around the house if you want a screen or a dog run. See the farm page for horses versus cattle."),
        ],
    },
]


def location_pages():
    for loc in LOC_DATA:
        filename = loc["file"]
        desc = loc["description"]
        svc = "".join(f'<li><a href="{h}">{label}</a></li>' for h, label in loc["services"])
        others = "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in LOCATIONS if h != filename)
        body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("service-areas.html", "Service areas"), (filename, loc["name"])])}
    <h1>Fence company in {loc["name"]}, TN</h1>
    <p class="lede">{loc["intro"]}</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")} <a class="btn btn-ghost btn-lg" href="contact.html#quote">Get a free quote</a></div>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <h2>What fence work looks like here</h2>
    <p>{loc["detail"]}</p>
    <div style="margin-top:1.2rem">{factors(loc["points"])}</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    <h2>Services that fit {loc["name"]}</h2>
    <ul class="chips light-chips" style="margin-top:1rem">{svc}</ul>
    <div style="margin-top:1.6rem">{faq_cards(loc["faqs"])}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <h2>Nearby areas</h2>
    <ul class="chips light-chips">{others}</ul>
    <p style="margin-top:1rem"><a href="service-areas.html">Full service area</a></p>
  </div>
</section>
<section class="cta-band">
  <div class="container cta-inner">
    <div>
      <h2>Estimate for a {loc["name"]} fence</h2>
      <p>Call {PHONE} or send the lot details. Say you are in {loc["name"]} so we plan the drive.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary btn-lg" href="contact.html#quote">Get a free quote</a>
      {call_btn("btn btn-ink btn-lg")}
    </div>
  </div>
</section>'''
        place_type = "AdministrativeArea" if loc["name"] == "Washington County" else "City"
        graph = [
            business_node(),
            webpage(filename, f"Fence company in {loc['name']}, TN", desc, canonical(filename) + "#place"),
            {
                "@type": place_type,
                "@id": canonical(filename) + "#place",
                "name": loc["name"] + ", TN",
                "containedInPlace": {"@type": "State", "name": "Tennessee"},
            },
            faq_schema(filename, loc["faqs"]),
            crumbs_schema(filename, [("service-areas.html", "Service areas"), (filename, loc["name"])]),
        ]
        layout(filename, loc["title"] + " | Johnson's Fence Company", desc, body, graph)


def service_areas_page():
    desc = "Johnson's Fence Company serves Johnson City, Jonesborough, Elizabethton, Gray, Boones Creek, Piney Flats, Telford, Limestone, Unicoi, and Washington County."
    cards = []
    for loc in LOC_DATA:
        cards.append(f'''<a class="service-card" href="{loc["file"]}">
        <span class="body"><h3>{loc["name"]}</h3><p>{loc["intro"]}</p><span class="more">Fence notes for {loc["name"]}</span></span>
      </a>''')
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("service-areas.html", "Service areas")])}
    <h1>Fence service area around Johnson City</h1>
    <p class="lede">We install and repair fences within about 25 miles of Johnson City. The places below are not copies of each other. Lot size, slope, farm lines, and which office governs the parcel all change the fence.</p>
    <div class="hero-actions">{call_btn("btn btn-primary btn-lg")}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="card-grid services">{"".join(cards)}</div>
    <div class="map-frame">
      <iframe title="Map of the Johnson City, Tennessee service area" src="https://maps.google.com/maps?q={LAT},{LNG}&amp;z=10&amp;output=embed" loading="lazy"></iframe>
      <p class="map-caption">Service-area map centered on Johnson City. We do not list a public storefront.</p>
    </div>
  </div>
</section>'''
    graph = [
        business_node(),
        webpage("service-areas.html", "Fence service area around Johnson City", desc, SITE + "/#business"),
        crumbs_schema("service-areas.html", [("service-areas.html", "Service areas")]),
    ]
    layout("service-areas.html", "Fence Service Areas near Johnson City, TN", desc, body, graph)


def privacy_page():
    desc = "How Johnson's Fence Company uses the information you send with a fence estimate request."
    body = f'''<section class="page-hero">
  <div class="container">
    {crumbs([("privacy.html", "Privacy")])}
    <h1>Privacy</h1>
    <p class="lede">What we do with the details you send when you ask for a fence estimate.</p>
  </div>
</section>
<section class="section">
  <div class="container prose">
    <p>The quote form on this site is provided by Tally. When you submit it, we receive your name, phone number, email, and whatever you wrote about the job, along with a source field that tells us the lead came from {SOURCE}.</p>
    <p>We use that information to reply about a fence estimate and to schedule a look at the property. We do not sell the form contents. Calls to {PHONE} are for the same purpose.</p>
    <p>If you want a request deleted, call and say so. Do not send payment card numbers through the form.</p>
  </div>
</section>'''
    graph = [
        business_node(),
        webpage("privacy.html", "Privacy", desc, SITE + "/#business"),
        crumbs_schema("privacy.html", [("privacy.html", "Privacy")]),
    ]
    layout("privacy.html", "Privacy | Johnson's Fence Company", desc, body, graph)


def sitemap():
    paths = [
        "index.html",
        "services.html",
        "about.html",
        "contact.html",
        "faq.html",
        "service-areas.html",
        "privacy.html",
    ]
    paths += [s["file"] for s in SERVICES_DATA]
    paths += [loc["file"] for loc in LOC_DATA]
    urls = [f"  <url><loc>{canonical(p)}</loc></url>" for p in paths]
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: https://johnsoncityfence.net/sitemap.xml\n",
        encoding="utf-8",
    )
    print("wrote sitemap", len(paths))


def main():
    home()
    services_page()
    for s in SERVICES_DATA:
        service_layout(s)
    faq_page()
    about_page()
    contact_page()
    service_areas_page()
    location_pages()
    privacy_page()
    sitemap()


if __name__ == "__main__":
    main()
