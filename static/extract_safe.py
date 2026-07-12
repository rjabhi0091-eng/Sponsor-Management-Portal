import sys
import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'
with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    lines = f.readlines()

def get_section(start_idx):
    section = []
    depth = 0
    for line in lines[start_idx:]:
        section.append(line)
        if '<section' in line:
            depth += 1
        if '</section>' in line:
            depth -= 1
        if depth == 0:
            break
    return ''.join(section)

# 206 is the start index for marketing (line 207)
marketing_html = get_section(206)
# 769 is the start index for media (line 770)
media_html = get_section(769)

with open(os.path.join(base_dir, 'analytics.html'), 'r', encoding='utf-8') as f:
    analytics_content = f.read()

# Splitting cleanly
parts = analytics_content.split('<div class="page-shell">')
header = parts[0]
footer = '</div>\n<script src="app.js"></script>\n</body>\n</html>'

with open(os.path.join(base_dir, 'marketing.html'), 'w', encoding='utf-8') as f:
    f.write(header + '<div class="page-shell">\n' + marketing_html + footer)

with open(os.path.join(base_dir, 'media.html'), 'w', encoding='utf-8') as f:
    f.write(header + '<div class="page-shell">\n' + media_html + footer)

content = ''.join(lines)
content = content.replace(marketing_html, '')
content = content.replace(media_html, '')

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(content)

print("Safely extracted marketing and media!")
