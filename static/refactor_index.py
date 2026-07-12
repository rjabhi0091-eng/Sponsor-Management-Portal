import re
import os

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to embed the login boards onto the front page.
# We will create a new section called "Login Portals"

login_section_html = """
    <section id="login-portals" style="padding: 60px 20px;">
      <div class="section-head">
        <span class="eyebrow">Access</span>
        <h2>Login Portals</h2>
        <p>Access your dashboard as a Sponsor, Client, or Admin.</p>
      </div>
      <div class="hero-dashboard-grid" style="max-width: 1200px; margin: 0 auto;">
        
        <!-- Sponsor Login -->
        <article class="glass-panel" style="padding: 30px; border-radius: 16px; text-align: center;">
          <h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="business-outline"></ion-icon> Sponsor Login</h3>
          <form class="record-form" style="text-align: left;" onsubmit="event.preventDefault(); window.location.href='analytics.html';">
            <label>Email Address<input type="email" required placeholder="sponsor@company.com" /></label>
            <label>Password<input type="password" required placeholder="********" /></label>
            <button type="submit" class="primary" style="width: 100%; margin-top: 15px; justify-content: center;">Login</button>
          </form>
        </article>

        <!-- Client Login -->
        <article class="glass-panel" style="padding: 30px; border-radius: 16px; text-align: center;">
          <h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="person-outline"></ion-icon> Client Login</h3>
          <form class="record-form" style="text-align: left;" onsubmit="event.preventDefault(); window.location.href='analytics.html';">
            <label>Email Address<input type="email" required placeholder="client@brand.com" /></label>
            <label>Password<input type="password" required placeholder="********" /></label>
            <button type="submit" class="primary" style="width: 100%; margin-top: 15px; justify-content: center;">Login</button>
          </form>
        </article>

        <!-- Admin Login -->
        <article class="glass-panel" style="padding: 30px; border-radius: 16px; text-align: center;">
          <h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="shield-checkmark-outline"></ion-icon> Admin Login</h3>
          <form class="record-form" style="text-align: left;" onsubmit="event.preventDefault(); window.location.href='admin.html';">
            <label>Email Address<input type="email" required placeholder="admin@portal.com" /></label>
            <label>Password<input type="password" required placeholder="********" /></label>
            <button type="submit" class="primary" style="width: 100%; margin-top: 15px; justify-content: center;">Login</button>
          </form>
        </article>
      </div>
    </section>
"""

# Inject after hero cards
content = content.replace('</section>\n\n    <section class="section-block quick-links-section">', '</section>\n' + login_section_html + '\n    <section class="section-block quick-links-section">')

# Also, update navigation to include login links
nav_updates = content.replace('<a href="#sponsor-registration">Sponsors</a>', '<a href="#login-portals">Login Portals</a>\n        <a href="#sponsor-registration">Sponsors</a>')
content = nav_updates

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html with login portals.")
