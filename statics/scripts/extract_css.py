import os
import re

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

# Extract from login.html
login_html_path = os.path.join(base_dir, 'login.html')
with open(login_html_path, 'r', encoding='utf-8') as f:
    login_html = f.read()

login_style_match = re.search(r'<style>(.*?)</style>', login_html, flags=re.DOTALL)
login_css = ""
if login_style_match:
    login_css = login_style_match.group(1).strip()
    login_html = re.sub(r'<style>.*?</style>', '', login_html, flags=re.DOTALL)
    with open(login_html_path, 'w', encoding='utf-8') as f:
        f.write(login_html)


# Extract from admin.html
admin_html_path = os.path.join(base_dir, 'admin.html')
with open(admin_html_path, 'r', encoding='utf-8') as f:
    admin_html = f.read()

admin_style_match = re.search(r'<style>(.*?)</style>', admin_html, flags=re.DOTALL)
admin_css = ""
if admin_style_match:
    admin_css = admin_style_match.group(1).strip()
    admin_html = re.sub(r'<style>.*?</style>', '', admin_html, flags=re.DOTALL)
    with open(admin_html_path, 'w', encoding='utf-8') as f:
        f.write(admin_html)

# Append to style.css
style_css_path = os.path.join(base_dir, 'style.css')
with open(style_css_path, 'a', encoding='utf-8') as f:
    if login_css:
        f.write("\n\n/* LOGIN PAGE CSS */\n")
        f.write(login_css)
    if admin_css:
        f.write("\n\n/* ADMIN PAGE CSS */\n")
        f.write(admin_css)

print("Extracted inline styles from login.html and admin.html and appended them to style.css")
