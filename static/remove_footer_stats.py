import re

file_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the footer-status block
match = re.search(r'(<div class="footer-status">.*?</div>\n      <p>Built for Sponsor Portfolio)', content, re.DOTALL)
if match:
    content = re.sub(r'<div class="footer-status">.*?</div>\n      <p>Built for Sponsor Portfolio', '<p>Built for Sponsor Portfolio', content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("footer-status removed!")
else:
    print("footer-status not found. Trying simpler regex.")
    content = re.sub(r'<div class="footer-status">.*?</div>', '', content, flags=re.DOTALL)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("footer-status removed (simple regex)!")
