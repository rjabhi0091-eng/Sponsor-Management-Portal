import re

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reduce paddings
content = content.replace('padding: 80px 20px;', 'padding: 40px 20px;')
content = content.replace('margin: 60px 0;', 'margin: 30px 0;')

# 2. Inject Login Portals right after the hero cards
login_section_html = """
    <section id="login-portals" style="padding: 40px 20px; text-align: center; max-width: 1200px; margin: 0 auto;">
      <div class="section-head" style="margin-bottom: 40px;">
        <span class="eyebrow" style="color: #38bdf8; font-weight: bold; text-transform: uppercase;">Access</span>
        <h2 style="color: #fff; font-size: 2.5rem; margin: 10px 0;">Login Portals</h2>
        <p style="color: #cbd5e1;">Access your dashboard as a Sponsor, Client, or Admin.</p>
      </div>
      <div class="hero-dashboard-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
        
        <!-- Sponsor Login -->
        <article class="glass-panel" style="background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 16px; text-align: center;">
          <h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="business-outline"></ion-icon> Sponsor Login</h3>
          <form class="record-form" style="text-align: left;" onsubmit="event.preventDefault(); window.location.href='analytics.html';">
            <label style="color: #cbd5e1; display: block; margin-bottom: 5px;">Email Address</label>
            <input type="email" required placeholder="sponsor@company.com" style="width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box;" />
            <label style="color: #cbd5e1; display: block; margin-bottom: 5px;">Password</label>
            <input type="password" required placeholder="********" style="width: 100%; padding: 12px; margin-bottom: 20px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box;" />
            <button type="submit" class="primary" style="width: 100%; justify-content: center; background: #3b82f6; color: #fff; padding: 12px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;">Login as Sponsor</button>
          </form>
        </article>

        <!-- Client Login -->
        <article class="glass-panel" style="background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 16px; text-align: center;">
          <h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="person-outline"></ion-icon> Client Login</h3>
          <form class="record-form" style="text-align: left;" onsubmit="event.preventDefault(); window.location.href='analytics.html';">
            <label style="color: #cbd5e1; display: block; margin-bottom: 5px;">Email Address</label>
            <input type="email" required placeholder="client@brand.com" style="width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box;" />
            <label style="color: #cbd5e1; display: block; margin-bottom: 5px;">Password</label>
            <input type="password" required placeholder="********" style="width: 100%; padding: 12px; margin-bottom: 20px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box;" />
            <button type="submit" class="primary" style="width: 100%; justify-content: center; background: #3b82f6; color: #fff; padding: 12px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;">Login as Client</button>
          </form>
        </article>

        <!-- Admin Login -->
        <article class="glass-panel" style="background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.1); padding: 30px; border-radius: 16px; text-align: center;">
          <h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="shield-checkmark-outline"></ion-icon> Admin Login</h3>
          <form class="record-form" style="text-align: left;" onsubmit="event.preventDefault(); window.location.href='admin.html';">
            <label style="color: #cbd5e1; display: block; margin-bottom: 5px;">Email Address</label>
            <input type="email" required placeholder="admin@portal.com" style="width: 100%; padding: 12px; margin-bottom: 15px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box;" />
            <label style="color: #cbd5e1; display: block; margin-bottom: 5px;">Password</label>
            <input type="password" required placeholder="********" style="width: 100%; padding: 12px; margin-bottom: 20px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: #fff; box-sizing: border-box;" />
            <button type="submit" class="primary" style="width: 100%; justify-content: center; background: #3b82f6; color: #fff; padding: 12px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;">Login as Admin</button>
          </form>
        </article>
      </div>
    </section>
"""

# Insert login section after the hero-cards section
if "login-portals" not in content:
    content = content.replace('</section>\n\n    <section class="landing-features">', '</section>\n' + login_section_html + '\n    <section class="landing-features">')

# 3. Add images to make it attractive
# In the about section, inject an image if it doesn't have one.
about_img = """<img src="dashboard-bg.png" alt="About Us" style="width: 100%; border-radius: 16px; margin-bottom: 30px; opacity: 0.9; max-height: 350px; object-fit: cover; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">"""
about_section_idx = content.find('<section id="about"')
if about_section_idx != -1 and 'dashboard-bg.png' not in content[about_section_idx:]:
    content = content.replace('<div class="about-copy">', '<div class="about-copy">\n        ' + about_img)

# Remove extra `<br>` tags that create blank space
content = content.replace('<br>\n<br>', '')
content = content.replace('<br><br>', '')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("index.html polished successfully")
