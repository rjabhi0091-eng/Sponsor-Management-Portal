import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

# Update index.html
with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<h2 class="logo">PraRoz</h2>', '<h2 class="logo">R-ABHI<br><span class="logo-sub">TECH SOLUTION</span></h2>')

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html)


# Update styles.css
with open(os.path.join(base_dir, 'styles.css'), 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the background image
old_bg = "https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1920&q=80"
new_bg = "https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=1920&q=80"
css = css.replace(old_bg, new_bg)

# Update logo CSS to accommodate longer text
if '.logo-sub' not in css:
    logo_sub_css = """
.logo {
    color: #ff7200;
    font-size: 28px;
    font-family: Arial;
    line-height: 1.2;
}

.logo-sub {
    font-size: 14px;
    color: #fff;
    letter-spacing: 2px;
}
"""
    # Replace the old logo block
    css = css.replace('.logo {\n    color: #ff7200;\n    font-size: 35px;\n    font-family: Arial;\n}', logo_sub_css.strip())

with open(os.path.join(base_dir, 'styles.css'), 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated logo to R-ABHI TECH SOLUTION and changed background image to social media.")
