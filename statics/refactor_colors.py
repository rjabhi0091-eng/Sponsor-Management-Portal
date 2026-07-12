import re

filepath_css = 'd:/WebPortal/Sponsor-Management-Portal/static/style.css'
filepath_html = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'

# 1. Update style.css
with open(filepath_css, 'r', encoding='utf-8') as f:
    css = f.read()

new_root = """:root {
  color-scheme: dark;
  --bg: #09090b;
  --page-bg: #18181b;
  --panel-bg: rgba(24, 24, 27, 0.7);
  --section-bg: rgba(24, 24, 27, 0.6);
  --card-bg: rgba(39, 39, 42, 0.6);
  --input-bg: rgba(39, 39, 42, 0.8);
  --panel-border: rgba(139, 92, 246, 0.3);
  --panel-border-soft: rgba(255, 255, 255, 0.1);
  --input-border: rgba(255, 255, 255, 0.15);
  --text: #ffffff;
  --muted: #a1a1aa;
  --muted-soft: #71717a;
  --brand: #3b82f6;
  --accent: #8b5cf6;
  --accent-2: #6366f1;
  --accent-3: #10b981;
  --accent-4: #f43f5e;
  --accent-soft: rgba(139, 92, 246, 0.15);
  --button-bg: linear-gradient(135deg, #3b82f6, #8b5cf6);
  --button-secondary: rgba(255, 255, 255, 0.05);
  --button-text: #ffffff;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  font-size: 16px;
}"""

css = re.sub(r':root\s*\{[^}]*\}', new_root, css, count=1)

# Fix background radial gradients to match new theme
css = css.replace(
    'radial-gradient(circle at top left, rgba(6, 182, 212, 0.18), transparent 28%),\n    radial-gradient(circle at bottom right, rgba(236, 72, 153, 0.14), transparent 22%),\n    linear-gradient(180deg, rgba(4, 25, 46, 0.94), rgba(9, 39, 65, 1))',
    'radial-gradient(circle at top left, rgba(59, 130, 246, 0.15), transparent 30%),\n    radial-gradient(circle at bottom right, rgba(139, 92, 246, 0.15), transparent 30%),\n    linear-gradient(180deg, #09090b, #18181b)'
)
css = css.replace('background-color: #0f172a;', 'background-color: #09090b;')
css = css.replace('background: rgba(15, 23, 42, 0.6) !important;', 'background: rgba(24, 24, 27, 0.7) !important;')

with open(filepath_css, 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Update index.html inline colors
with open(filepath_html, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace light blues and hardcoded dark blues in index.html
html = html.replace('#38bdf8', '#8b5cf6') # change old accent blue to violet
html = html.replace('#0f172a', '#18181b') # change input backgrounds
html = html.replace('#cbd5e1', '#a1a1aa') # change muted text
html = html.replace('rgba(15, 23, 42, 0.7)', 'rgba(24, 24, 27, 0.7)') # glass panels
html = html.replace('#475569', 'rgba(255,255,255,0.15)') # input borders

with open(filepath_html, 'w', encoding='utf-8') as f:
    f.write(html)

print("Colors and theme successfully updated to professional Zinc/Violet/Blue.")
