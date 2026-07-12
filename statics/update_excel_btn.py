import re

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Export to Excel with Export to Google Sheets
content = content.replace(
    '<button class="action-btn" style="background: #10b981; display: flex; align-items: center; gap: 8px;"><ion-icon name="document-text-outline"></ion-icon> Export to Excel</button>',
    '<button class="action-btn" style="background: #10b981; display: flex; align-items: center; gap: 8px;" onclick="alert(\'Connecting to Google Sheets...\')"><ion-icon name="logo-google"></ion-icon> Connect Google Sheets</button>'
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Excel to Google Sheets in admin.html")
