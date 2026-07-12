import re

file_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

dashboard_html = """
    <section id="registration-stats" class="live-analytics" style="margin-top: 60px; margin-bottom: 40px;">
      <div class="hero-dashboard" style="text-align: center; max-width: 1200px; margin: 0 auto; background: rgba(15, 23, 42, 0.6); padding: 40px; border-radius: 24px; border: 1px solid rgba(56, 189, 248, 0.2); box-shadow: 0 20px 40px rgba(0,0,0,0.4);">
        <div class="hero-dashboard-head" style="margin-bottom: 30px;">
          <span class="eyebrow" style="color: #38bdf8; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;">Live Analytics</span>
          <h2 style="font-size: 2.2rem; margin: 10px 0; color: #fff;">Registration Counters</h2>
          <p style="color: #94a3b8; max-width: 600px; margin: 0 auto;">See in real-time how many sponsors and clients are registering on the portal right now.</p>
        </div>
        <div class="hero-dashboard-grid" style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
          <article class="hero-dashboard-card accent-1" style="background: rgba(255,255,255,0.05); padding: 25px; border-radius: 16px; min-width: 200px; border-top: 3px solid #38bdf8;">
            <span style="display: block; font-size: 1rem; color: #cbd5e1; margin-bottom: 10px;">Total Sponsors</span>
            <strong id="hero-dashboard-sponsors" style="font-size: 2.5rem; color: #fff;">0</strong>
          </article>
          <article class="hero-dashboard-card accent-2" style="background: rgba(255,255,255,0.05); padding: 25px; border-radius: 16px; min-width: 200px; border-top: 3px solid #10b981;">
            <span style="display: block; font-size: 1rem; color: #cbd5e1; margin-bottom: 10px;">Total Clients</span>
            <strong id="hero-dashboard-clients" style="font-size: 2.5rem; color: #fff;">0</strong>
          </article>
          <article class="hero-dashboard-card accent-3" style="background: rgba(255,255,255,0.05); padding: 25px; border-radius: 16px; min-width: 200px; border-top: 3px solid #f59e0b;">
            <span style="display: block; font-size: 1rem; color: #cbd5e1; margin-bottom: 10px;">Total Registrations</span>
            <strong id="hero-dashboard-registrations" style="font-size: 2.5rem; color: #fff;">0</strong>
          </article>
        </div>
      </div>
    </section>
"""

# Insert before <footer class="site-footer">
if '<footer class="site-footer">' in content:
    content = content.replace('<footer class="site-footer">', dashboard_html + '\n    <footer class="site-footer">')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Bottom dashboard injected successfully!")
else:
    print("Could not find footer to inject before.")
