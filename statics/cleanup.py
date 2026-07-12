import os
base = 'd:/WebPortal/Sponsor-Management-Portal/static/'

if os.path.exists(base + 'marketing.html'):
    os.remove(base + 'marketing.html')
if os.path.exists(base + 'media.html'):
    os.remove(base + 'media.html')

with open(base + 'index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('href="marketing.html"', 'href="analytics.html#marketing"')
content = content.replace('href="media.html"', 'href="analytics.html#media"')

with open(base + 'index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Cleanup and links updated safely!')
