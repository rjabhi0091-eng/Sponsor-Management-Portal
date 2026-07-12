import re

path = 'd:/WebPortal/Sponsor-Management-Portal/static/styles.css'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reduce h1 and h2 sizes
content = re.sub(r'h1 \{.*?font-size: clamp\(.*?\).*?\}', 'h1 {\n  margin-bottom: 1rem;\n  font-size: clamp(2rem, 3vw, 2.5rem);\n  letter-spacing: -0.02em;\n  color: #f8fafc;\n}', content, flags=re.DOTALL)
content = re.sub(r'h2 \{.*?font-size: clamp\(.*?\).*?\}', 'h2 {\n  margin-bottom: 1rem;\n  font-size: clamp(1.5rem, 2vw, 2rem);\n  letter-spacing: -0.01em;\n  color: #f1f5f9;\n}', content, flags=re.DOTALL)

# 2. Reduce hero illustration size
content = content.replace('header#overview .hero-visual img.hero-illustration {\n  width: 100%;\n  max-width: 500px;\n  height: auto;\n}', 'header#overview .hero-visual img.hero-illustration {\n  width: 100%;\n  max-width: 350px;\n  height: auto;\n}')

# 3. Reduce padding for sections
content = content.replace('padding: 3rem 0;', 'padding: 1.5rem 0;')
content = content.replace('margin-bottom: 2.5rem;', 'margin-bottom: 1.5rem;')

# 4. Make hero card grid smaller
# If it has grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
content = content.replace('minmax(280px, 1fr)', 'minmax(220px, 1fr)')

# 5. Make register card grid smaller
# If it has grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
content = content.replace('minmax(320px, 1fr)', 'minmax(250px, 1fr)')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("CSS adjustments complete")
