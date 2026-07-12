import re

file_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove hero-actions block
match = re.search(r'(<div class="hero-actions">.*?</div>\n        <div class="hero-social">)', content, re.DOTALL)
if match:
    # We want to remove the hero-actions but keep hero-social
    # Actually, we can just remove hero-actions block
    content = re.sub(r'<div class="hero-actions">.*?</div>', '', content, flags=re.DOTALL)
    print("hero-actions removed.")

# Make sure the image looks great. It has a style tag inline, we can leave it or enhance it.
# Current image:
# <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1200&q=80" alt="Social Media Marketing & Sponsor Management Team" style="width: 100%; max-width: 900px; border-radius: 16px; box-shadow: 0 15px 40px rgba(0,0,0,0.4); object-fit: cover; border: 4px solid rgba(255, 255, 255, 0.1);" />

# Let's add a bit more padding or margin to make it a "beautiful portal"
content = content.replace('style="margin-top: 40px; text-align: center;"', 'style="margin-top: 60px; text-align: center; padding-bottom: 20px;"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Portal beautified!")
