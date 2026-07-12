import re
import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'
index_path = os.path.join(base_dir, 'index.html')
marketing_path = os.path.join(base_dir, 'marketing.html')
media_path = os.path.join(base_dir, 'media.html')
analytics_path = os.path.join(base_dir, 'analytics.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Grab header up to the first section (live-analytics)
header_match = re.search(r'(.*?)(<section)', content, re.DOTALL)
if not header_match:
    print("Could not find header")
    exit(1)
header_content = header_match.group(1)

# Update links in header
header_content = header_content.replace('href="#marketing"', 'href="marketing.html"')
header_content = header_content.replace('href="#media"', 'href="media.html"')
header_content = header_content.replace('href="#management"', 'href="index.html#management"')
header_content = header_content.replace('href="#clients"', 'href="index.html#clients"')
header_content = header_content.replace('href="#overview"', 'href="index.html#overview"')
header_content = header_content.replace('href="#contact"', 'href="index.html#contact"')
# Also for the view insights button
header_content = header_content.replace('id="view-insights-btn"', 'onclick="window.location.href=\\\'analytics.html\\\'"')

footer_content = """
  </div> <!-- end page-shell -->
  <script src="app.js"></script>
</body>
</html>
"""

# 1. Extract Analytics
analytics_match = re.search(r'(<section id="live-analytics".*?</section>)', content, re.DOTALL)
if analytics_match:
    analytics_section = analytics_match.group(1)
    with open(analytics_path, 'w', encoding='utf-8') as f:
        f.write(header_content + '\\n<div class="page-shell">\\n' + analytics_section + footer_content)
    content = content.replace(analytics_section, '')
    print("Analytics extracted")

# 2. Extract Marketing
marketing_match = re.search(r'(<section id="marketing".*?</section>)', content, re.DOTALL)
if marketing_match:
    marketing_section = marketing_match.group(1)
    with open(marketing_path, 'w', encoding='utf-8') as f:
        f.write(header_content + '\\n<div class="page-shell">\\n' + marketing_section + footer_content)
    content = content.replace(marketing_section, '')
    print("Marketing extracted")

# 3. Extract Media
media_match = re.search(r'(<section id="media".*?</section>)', content, re.DOTALL)
if media_match:
    media_section = media_match.group(1)
    with open(media_path, 'w', encoding='utf-8') as f:
        f.write(header_content + '\\n<div class="page-shell">\\n' + media_section + footer_content)
    content = content.replace(media_section, '')
    print("Media extracted")

# Update any remaining links in index.html
content = content.replace('href="#marketing"', 'href="marketing.html"')
content = content.replace('href="#media"', 'href="media.html"')
content = content.replace('id="view-insights-btn"', 'onclick="window.location.href=\\\'analytics.html\\\'"')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Extraction completed!")
