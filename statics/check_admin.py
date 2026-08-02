import re
js = open('app.js', 'r', encoding='utf8').read()
admin = open('admin.html', 'r', encoding='utf8').read()
ids = re.findall(r'document\.getElementById\(([\'\"])(.*?)\1\)', js)
missing = [m[1] for m in ids if f'id="{m[1]}"' not in admin and f"id='{m[1]}'" not in admin]
print('Missing IDs in admin.html:', set(missing))
