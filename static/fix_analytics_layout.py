import os
import shutil
import re

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'
brain_dir = r'C:\Users\rjabh\.gemini\antigravity-ide\brain\cbcef1a8-10fd-46d8-9abd-441c53efcdf8'

# Find the generated bg image
bg_img_path = None
for f in os.listdir(brain_dir):
    if f.startswith('dashboard_bg_') and f.endswith('.png'):
        bg_img_path = os.path.join(brain_dir, f)
        break

if bg_img_path:
    target_bg = os.path.join(base_dir, 'dashboard-bg.png')
    shutil.copy(bg_img_path, target_bg)
    print("Background image copied!")
else:
    print("Background image not found.")

# Update analytics.html layout and background
analytics_path = os.path.join(base_dir, 'analytics.html')
with open(analytics_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add background style to body of analytics page specifically
if '<body style="' not in content:
    content = content.replace('<body>', '<body style="background: url(\'dashboard-bg.png\') no-repeat center center fixed; background-size: cover;">')

# Ensure everything inside page-shell is properly centered
# Let's add a centralizing style to the injected sections
# We will wrap the sections (marketing, media, windows) in a centering div if not already there,
# or simply add centering CSS rules to the analytics.html head.

style_injection = """
  <style>
    /* Force centering on all major panels in analytics page */
    .marketing-window-analytics, 
    .insights-window-analytics,
    .social-marketing,
    .media-section,
    #registrations-tables {
        max-width: 1200px !important;
        margin: 0 auto !important;
        width: 100% !important;
    }
    .management-header, .panel-heading, .marketing-head, .media-header {
        text-align: center !important;
        margin: 0 auto !important;
        justify-content: center !important;
        align-items: center !important;
        display: flex !important;
        flex-direction: column !important;
    }
    .hero-dashboard-grid, .marketing-grid, .media-grid, .analysis-grid {
        justify-content: center !important;
        margin: 0 auto !important;
    }
  </style>
</head>
"""

if '/* Force centering on all major panels' not in content:
    content = content.replace('</head>', style_injection)

with open(analytics_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Layout fixed and background set!")
