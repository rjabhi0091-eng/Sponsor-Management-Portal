import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

# 1. Update index.html
html_path = os.path.join(base_dir, 'index.html')
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update Hero Text
old_hero_title = "<h1>Web Design & <br><span>Development</span> <br>Course</h1>"
new_hero_title = "<h1>Sponsor Management &<br><span>Marketing</span> <br>Portal</h1>"
html = html.replace(old_hero_title, new_hero_title)

old_hero_desc = """<p class="par">Lorem ipsum dolor sit amet consectetur adipisicing elit. <br> Suscipit fugit animi iusto, temporibus voluptatum laboriosam distinctio, <br> quasi unde alias facilis sequi. Aut debitis voluptatibus quas?</p>"""
new_hero_desc = """<p class="par">Connecting brands, startups, and influencers with top-tier sponsorship opportunities.<br> We provide powerful social media growth strategies and digital marketing solutions <br>to maximize your market presence and ROI.</p>"""
html = html.replace(old_hero_desc, new_hero_desc)

# Add Navigation Link for Services
old_nav = """<li><a href="#about">ABOUT</a></li>"""
new_nav = """<li><a href="#services">SERVICES</a></li>
                    <li><a href="#about">ABOUT</a></li>"""
html = html.replace(old_nav, new_nav)

# Add Services Section
services_html = """
        <!-- SERVICES SECTION -->
        <section id="services" class="clean-section dark-bg">
            <div class="section-container">
                <h2 class="section-title">OUR <span>SERVICES</span></h2>
                <div class="services-grid">
                    <div class="service-card">
                        <div class="service-icon"><ion-icon name="briefcase-outline"></ion-icon></div>
                        <h3>Sponsor Management</h3>
                        <p>We connect your brand with the right sponsors. From pitch decks to deal closures, we manage the entire sponsorship acquisition workflow.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon"><ion-icon name="megaphone-outline"></ion-icon></div>
                        <h3>Social Media Marketing</h3>
                        <p>Boost your online presence with targeted campaigns on Instagram, LinkedIn, Facebook, and Twitter. We turn followers into active clients.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon"><ion-icon name="people-circle-outline"></ion-icon></div>
                        <h3>Brand Partnerships</h3>
                        <p>We build strategic partnerships between influencers and brands, creating content that engages audiences and drives measurable business growth.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon"><ion-icon name="stats-chart-outline"></ion-icon></div>
                        <h3>Digital Analytics</h3>
                        <p>Track your campaign performance in real-time. We provide transparent insights into client engagement and marketing ROI.</p>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert Services Section right before About Section
html = html.replace('<!-- ABOUT SECTION -->', services_html + '\n        <!-- ABOUT SECTION -->')

# Make About Section have transparent background instead of dark-bg if it conflicts, but let's see. 
# In rebuild_site_clean.py, ABOUT was transparent, WORK was dark-bg. Now SERVICES is dark-bg, so it alternates nicely.
# HOME (image) -> SERVICES (dark-bg) -> ABOUT (transparent) -> WORK (dark-bg) -> MEDIA (transparent) -> CONTACT (dark-bg)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update styles.css
css_path = os.path.join(base_dir, 'styles.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

if '.services-grid' not in css:
    services_css = """

/* SERVICES SECTION */
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

.service-card {
    background: #222;
    padding: 40px 30px;
    border-radius: 10px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border-bottom: 4px solid transparent;
}

.service-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    border-bottom: 4px solid #ff7200;
}

.service-icon ion-icon {
    font-size: 50px;
    color: #ff7200;
    margin-bottom: 20px;
}

.service-card h3 {
    color: #fff;
    font-size: 22px;
    margin-bottom: 15px;
    letter-spacing: 1px;
}

.service-card p {
    color: #bbb;
    line-height: 1.6;
    font-size: 15px;
}
"""
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(services_css)

print("Updated index.html and styles.css with services section and new hero text.")
