import re
js = open('app.js', 'r', encoding='utf8').read()
html = open('index.html', 'r', encoding='utf8').read()
ids = re.findall(r'document\.getElementById\(([\'\"])(.*?)\1\)', js)
missing = [m[1] for m in ids if f'id="{m[1]}"' not in html and f"id='{m[1]}'" not in html]
print('Missing IDs:', set(missing))
