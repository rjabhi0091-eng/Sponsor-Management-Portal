import re

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's print out the sections to see the structure
matches = re.findall(r'<section[^>]*>|<header[^>]*>', content)
print(matches)

# Let's also print the buttons in header-actions
actions = re.search(r'<div class="header-actions">(.*?)</div>', content, re.DOTALL)
if actions:
    print("Header actions:", actions.group(1))

