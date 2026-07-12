import re

# 1. Update style.css to reduce search-panel space
css_path = 'd:/WebPortal/Sponsor-Management-Portal/static/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Let's find anything related to .search-panel
if '.search-panel' in css:
    css = re.sub(r'(\.search-panel\s*\{[^}]*padding:\s*)([^;]+)', r'\1 10px 20px', css)
    css = re.sub(r'(\.search-section\s*\{[^}]*margin:\s*)([^;]+)', r'\1 10px 0', css)
    css = re.sub(r'(\.search-panel\s*\{[^}]*margin:\s*)([^;]+)', r'\1 10px auto', css)
    
# Let's also enforce it at the end just in case
css += """
.search-section { margin-bottom: 15px !important; margin-top: 15px !important; }
.search-panel { padding: 15px 25px !important; margin-bottom: 10px !important; }
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update colors in admin.html and analytics.html
def update_colors(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('#38bdf8', '#8b5cf6') # accent blue to violet
    html = html.replace('#3b82f6', '#8b5cf6') # accent blue to violet
    html = html.replace('#0f172a', '#18181b') # input/backgrounds
    html = html.replace('#cbd5e1', '#a1a1aa') # muted text
    html = html.replace('rgba(15, 23, 42, 0.9)', 'rgba(24, 24, 27, 0.9)') # sidebar
    html = html.replace('rgba(15, 23, 42, 0.7)', 'rgba(24, 24, 27, 0.7)') # glass panels
    html = html.replace('rgba(15, 23, 42, 0.6)', 'rgba(24, 24, 27, 0.6)') # tabs
    html = html.replace('#475569', 'rgba(255,255,255,0.15)') # input borders
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_colors('d:/WebPortal/Sponsor-Management-Portal/static/admin.html')
update_colors('d:/WebPortal/Sponsor-Management-Portal/static/analytics.html')

print("Search bar space reduced and global portal colors updated successfully.")
