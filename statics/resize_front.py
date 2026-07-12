import os
import re

index_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert About Company section
about_html = """
    <section class="section-block about-company" style="margin-top: 1rem; margin-bottom: 2rem; padding: 2rem; background: var(--panel-bg); border-radius: 16px; border: 1px solid var(--panel-border);">
      <div class="section-head" style="margin-bottom: 1rem;">
        <span class="eyebrow" style="color: #38bdf8;">About Company</span>
        <h2 style="font-size: 1.8rem;">R-ABHI TECH SOLUTION</h2>
      </div>
      <p style="color: var(--muted); line-height: 1.6; font-size: 1rem;">
        We are a professional Sponsor Management and Social Media Marketing agency dedicated to helping businesses, startups, influencers, and brands maximize their market presence. We specialize in digital marketing, social media management, and creating powerful brand identities.
      </p>
    </section>
"""

if 'About Company' not in content:
    content = content.replace('</header>\n\n    <section class="hero-cards">', '</header>\n' + about_html + '\n    <section class="hero-cards">')

# 2. Resize inline background heights
# hero-cards from 100px to 70px
content = content.replace('height: 100px;', 'height: 70px;')
# quick-links from 80px to 60px
content = content.replace('height: 80px;', 'height: 60px;')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html to include About Company and smaller inline images")
