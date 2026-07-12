import re
import os

index_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
work_path = 'd:/WebPortal/Sponsor-Management-Portal/static/work.html'

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract live-analytics section from index.html
match = re.search(r'(\s*<section id="live-analytics" class="live-analytics">.*?</section>)', index_content, flags=re.DOTALL)
if match:
    analytics_section = match.group(1)
    
    # Remove from index.html
    new_index_content = index_content.replace(analytics_section, '')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_index_content)
        
    # Add to work.html
    with open(work_path, 'r', encoding='utf-8') as f:
        work_content = f.read()
        
    # Insert before <section class="social-marketing" id="marketing">
    new_work_content = work_content.replace('<section class="social-marketing" id="marketing">', analytics_section + '\n\n    <section class="social-marketing" id="marketing">')
    
    with open(work_path, 'w', encoding='utf-8') as f:
        f.write(new_work_content)
        
    print("Successfully moved live-analytics section from index.html to work.html")
else:
    print("live-analytics section not found in index.html")
