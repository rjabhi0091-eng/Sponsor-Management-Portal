import os
import re
import shutil

index_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
reg_path = 'd:/WebPortal/Sponsor-Management-Portal/static/registration.html'

# 1. Read registration forms
with open(reg_path, 'r', encoding='utf-8') as f:
    reg_content = f.read()

match = re.search(r'(\s*<section class="registration-section" id="register">.*?</section>)', reg_content, flags=re.DOTALL)
if match:
    registration_forms = match.group(1)
else:
    registration_forms = ""

# 2. Modify index.html
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Insert the registration forms after the hero visual in index.html, creating a split layout
# Let's actually put it below the quick-links, or maybe right below the hero-cards.
# The user said: "front page per ek side me small kar ke argest karo" (adjust it small on one side).
# Currently, header#overview has grid-template-columns: 1.3fr 1fr.
# We can replace the hero-visual image with the registration forms, or add a third column, or put it below in a new compact section.
# Let's create a new section right below hero-cards:
compact_registration = registration_forms.replace('class="registration-section"', 'class="registration-section compact-reg" style="margin-top:2rem;"')
# Make inputs smaller by using inline styles or relying on existing CSS. The grid already makes them side-by-side.

index_content = index_content.replace('</section>\n\n    <section class="section-block quick-links-section">', '</section>\n' + compact_registration + '\n    <section class="section-block quick-links-section">')

# Remove registration from quick links
index_content = re.sub(r'<a href="/registration".*?</a>', '', index_content, flags=re.DOTALL)
# Remove registration from nav
index_content = re.sub(r'<a href="/registration".*?>Registration</a>', '', index_content)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

# 3. Remove registration from all other HTML files' nav
for file in ['about.html', 'contact.html', 'media.html', 'work.html', 'admin.html', 'login.html']:
    path = os.path.join('d:/WebPortal/Sponsor-Management-Portal/static', file)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = re.sub(r'<a href="/registration".*?>Registration</a>', '', content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

# 4. Delete registration.html
if os.path.exists(reg_path):
    os.remove(reg_path)

print("Registration forms moved to index, nav updated, and registration.html deleted.")
