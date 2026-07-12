import re
import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'
index_path = os.path.join(base_dir, 'index.html')
marketing_path = os.path.join(base_dir, 'marketing.html')
media_path = os.path.join(base_dir, 'media.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Grab everything before the first section
header_match = re.search(r'(.*?)(<section id="live-analytics")', content, re.DOTALL)
if header_match:
    header_content = header_match.group(1)
else:
    print("Could not find header")
    exit(1)

# Modify navigation links in the header content
header_content = header_content.replace('href="#marketing"', 'href="marketing.html"')
header_content = header_content.replace('href="#media"', 'href="media.html"')
header_content = header_content.replace('href="#management"', 'href="index.html#management"')
header_content = header_content.replace('href="#clients"', 'href="index.html#clients"')
header_content = header_content.replace('href="#overview"', 'href="index.html#overview"')
header_content = header_content.replace('href="#contact"', 'href="index.html#contact"')

# Ensure the site-nav links are also updated
header_content = header_content.replace('href="index.html#marketing">Marketing</a>', 'href="marketing.html">Marketing</a>')
header_content = header_content.replace('href="index.html#media">Media</a>', 'href="media.html">Media</a>')


footer_content = """
  </div> <!-- end page-shell -->
  <script src="app.js"></script>
</body>
</html>
"""

# Extract marketing section
marketing_match = re.search(r'(<section id="marketing".*?</section>)', content, re.DOTALL)
if marketing_match:
    marketing_section = marketing_match.group(1)
    with open(marketing_path, 'w', encoding='utf-8') as f:
        # Wrap the section in page-shell if it's not already
        f.write(header_content + '\\n<div class="page-shell">\\n' + marketing_section + footer_content)
    # remove from index.html
    content = content.replace(marketing_section, '')
    print("Marketing extracted")

# Extract media section
media_match = re.search(r'(<section id="media".*?</section>)', content, re.DOTALL)
if media_match:
    media_section = media_match.group(1)
    with open(media_path, 'w', encoding='utf-8') as f:
        f.write(header_content + '\\n<div class="page-shell">\\n' + media_section + footer_content)
    # remove from index.html
    content = content.replace(media_section, '')
    print("Media extracted")

# Update index.html navigation links
content = content.replace('href="#marketing"', 'href="marketing.html"')
content = content.replace('href="#media"', 'href="media.html"')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Extraction completed!")
