import re

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

actions = re.search(r'<div class="header-actions">(.*?)</div>', content, re.DOTALL)
if actions:
    with open('actions.txt', 'w', encoding='utf-8') as f2:
        f2.write(actions.group(1))
