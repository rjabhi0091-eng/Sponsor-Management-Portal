import os
import re

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

marketing_path = os.path.join(base_dir, 'marketing.html')
media_path = os.path.join(base_dir, 'media.html')
analytics_path = os.path.join(base_dir, 'analytics.html')

def get_sections_from_file(filepath):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = []
    # Find all <section>...</section>
    matches = re.finditer(r'(<section.*?</section>)', content, re.DOTALL)
    for m in matches:
        sections.append(m.group(1))
    return '\n\n'.join(sections)

marketing_sections = get_sections_from_file(marketing_path)
media_sections = get_sections_from_file(media_path)

with open(analytics_path, 'r', encoding='utf-8') as f:
    analytics_content = f.read()

# Insert the sections before the closing </div> of page-shell in analytics.html
# Find the footer start
footer_marker = "  </div> <!-- end page-shell -->"
if footer_marker not in analytics_content:
    footer_marker = "  <script src=\"app.js\">"

divider = """
<!-- ================== MERGED SECTIONS ================== -->
<br><br><hr style="border-color: #334155; margin: 40px 0;"><br>
"""

new_analytics_content = analytics_content.replace(footer_marker, divider + marketing_sections + "\n\n" + media_sections + "\n" + footer_marker)

# Update the header navigation links inside analytics.html to point to `#marketing` and `#media`
new_analytics_content = new_analytics_content.replace('href="marketing.html"', 'href="#marketing"')
new_analytics_content = new_analytics_content.replace('href="media.html"', 'href="#media"')

with open(analytics_path, 'w', encoding='utf-8') as f:
    f.write(new_analytics_content)

print("Merged successfully!")
