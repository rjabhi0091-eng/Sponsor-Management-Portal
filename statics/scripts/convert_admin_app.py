import re

index_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
admin_path = 'd:/WebPortal/Sponsor-Management-Portal/static/admin.html'

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Find the hero-cards section
match = re.search(r'(<section class="hero-cards">.*?</section>)', index_content, re.DOTALL)
hero_cards_html = match.group(1) if match else ""

if hero_cards_html:
    # Remove from index.html
    index_content = index_content.replace(hero_cards_html, '')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Metrics removed from index.html.")

with open(admin_path, 'r', encoding='utf-8') as f:
    admin_content = f.read()

# 1. Add manifest and change title
admin_content = admin_content.replace('<title>Admin Dashboard</title>', '<title>Admin Editing App</title>\n  <link rel="manifest" href="manifest.json">')

# 2. Add an App Header (mobile friendly)
app_header = """
  <header class="app-bar" style="background: #1e293b; padding: 15px 20px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #334155; position: sticky; top: 0; z-index: 1000;">
    <div style="display: flex; align-items: center; gap: 10px;">
        <img src="logo.png" alt="Logo" style="height: 32px; width: 32px; border-radius: 8px;">
        <h1 style="margin: 0; font-size: 1.2rem; color: #fff;">Admin Editing App</h1>
    </div>
    <a href="analytics.html" style="color: #38bdf8; text-decoration: none; font-weight: bold; font-size: 0.9rem;">View Dashboard</a>
  </header>
"""

# The admin.html currently has:
# <body>
#   <div class="admin-container">
if '<div class="admin-container">' in admin_content:
    admin_content = admin_content.replace('<div class="admin-container">', app_header + '\n  <div class="admin-container">')

# 3. Inject the hero cards (portfolio metrics) at the top of admin-content
if hero_cards_html:
    # Change class a bit for admin app integration
    admin_metrics = hero_cards_html.replace('class="hero-cards"', 'class="hero-cards" style="margin-top: 20px; margin-bottom: 20px;"')
    
    inject_point = '<main class="admin-content">'
    if inject_point in admin_content:
        admin_content = admin_content.replace(inject_point, inject_point + '\n' + admin_metrics)
    else:
        # fallback
        admin_content = admin_content.replace('<h1>Admin Dashboard</h1>', '<h1>Admin Dashboard</h1>\n' + admin_metrics)

# 4. Hide original H1 since we have an App Bar now
admin_content = admin_content.replace('<h1>Admin Dashboard</h1>', '<h1 style="display:none;">Admin Dashboard</h1>')

with open(admin_path, 'w', encoding='utf-8') as f:
    f.write(admin_content)

print("Admin converted to Editing App and metrics moved!")
