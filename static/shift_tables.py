import os
import re

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'
admin_path = os.path.join(base_dir, 'admin.html')
analytics_path = os.path.join(base_dir, 'analytics.html')
index_path = os.path.join(base_dir, 'index.html')

# 1. Extract tables from admin.html
with open(admin_path, 'r', encoding='utf-8') as f:
    admin_content = f.read()

# Grab all .admin-table-wrapper blocks
tables_matches = re.finditer(r'(<div class="admin-table-wrapper">.*?</div>\n        </div>)', admin_content, re.DOTALL)
# Actually, the div closes early. Let's find exactly the wrappers.
# We have two wrappers: Sponsor Registrations and Client Registrations.
tables_match = re.search(r'(<div class="admin-table-wrapper">.*</table>\n        </div>.*</table>\n        </div>)', admin_content, re.DOTALL)

tables_html = tables_match.group(1) if tables_match else ""

# Wait, the regex might be fragile. Let's just do a simpler search.
wrapper1 = re.search(r'(<div class="admin-table-wrapper">\s*<h3>.*?Sponsor Registrations.*?</div>)', admin_content, re.DOTALL)
wrapper2 = re.search(r'(<div class="admin-table-wrapper">\s*<h3>.*?Client Registrations.*?</div>)', admin_content, re.DOTALL)

table1 = wrapper1.group(1) if wrapper1 else ""
table2 = wrapper2.group(1) if wrapper2 else ""

# 2. Append tables to analytics.html
with open(analytics_path, 'r', encoding='utf-8') as f:
    analytics_content = f.read()

# Find where to inject them. Below the Live Analytics grid, before the Marketing Window.
# The marketing window divider is: <!-- ================== WINDOW PANELS ================== -->
injection_point = "<!-- ================== WINDOW PANELS ================== -->"
if injection_point in analytics_content:
    divider = "\n<!-- ================== REGISTRATION TABLES ================== -->\n<br><hr style=\"border-color: #334155; margin: 40px 0;\"><br>\n"
    tables_combined = f'<div id="registrations-tables" style="max-width: 1400px; margin: 0 auto;">\n{table1}\n{table2}\n</div>\n'
    new_analytics = analytics_content.replace(injection_point, divider + tables_combined + "\n" + injection_point)
    with open(analytics_path, 'w', encoding='utf-8') as f:
        f.write(new_analytics)
    print("Tables added to analytics.html")
else:
    print("Could not find injection point in analytics.html")

# 3. Clean up index.html
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Remove CTA Strip (Ready to move sponsors...)
cta_match = re.search(r'(<section class="cta-strip">.*?</section>)', index_content, re.DOTALL)
if cta_match:
    index_content = index_content.replace(cta_match.group(1), '')

# Remove entire Management Window
# This might span multiple sections, so let's find the start and find the matching closing tag.
def remove_section(html_content, class_name):
    # Find start
    idx = html_content.find(f'<section class="{class_name}">')
    if idx == -1:
        return html_content
    depth = 0
    end_idx = -1
    # Simple parser to find matching </section>
    # We will slice and use regex to find all <section and </section tags
    temp_content = html_content[idx:]
    tag_pattern = re.compile(r'</?section.*?>')
    for m in tag_pattern.finditer(temp_content):
        tag = m.group(0)
        if tag.startswith('</section'):
            depth -= 1
        else:
            depth += 1
        
        if depth == 0:
            end_idx = idx + m.end()
            break
    
    if end_idx != -1:
        return html_content[:idx] + html_content[end_idx:]
    return html_content

index_content = remove_section(index_content, "management-window")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("index.html cleaned up!")
