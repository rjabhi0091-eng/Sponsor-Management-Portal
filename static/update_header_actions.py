import re

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_actions = """
      <a href="analytics.html" class="secondary" data-icon="🛠️"
        style="text-decoration:none;display:inline-flex;align-items:center;justify-content:center;padding:8px 16px;border-radius:8px;">Dashboard</a>
      <a href="#login-portals" class="primary" data-icon="🔐"
        style="text-decoration:none;display:inline-flex;align-items:center;justify-content:center;padding:8px 16px;border-radius:8px;background:var(--button-bg);color:#fff;">Login</a>
"""

content = re.sub(r'<div class="header-actions">.*?</div>', f'<div class="header-actions">{new_actions}    </div>', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated header actions order and simplified buttons.")
