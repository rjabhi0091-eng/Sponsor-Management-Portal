import re

files_to_check = [
    'd:/WebPortal/Sponsor-Management-Portal/static/index.html',
    'd:/WebPortal/Sponsor-Management-Portal/static/analytics.html',
    'd:/WebPortal/Sponsor-Management-Portal/static/login.html'
]

for file_path in files_to_check:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Replace "Admin Dashboard" button text with "Dashboard"
    content = content.replace('>Admin Dashboard</a>', '>Dashboard</a>')
    content = content.replace('Admin Dashboard</button>', 'Dashboard</button>')
    
    # Ensure href="/admin" or href="admin.html" becomes href="analytics.html" for Dashboard link
    # Specifically for the Dashboard button:
    # <a href="/admin" class="secondary" ...>Dashboard</a>
    content = re.sub(r'<a\s+href=["\'](?:/admin|admin\.html)["\']([^>]*)>Dashboard</a>', r'<a href="analytics.html"\1>Dashboard</a>', content)
    
    # Also fix the site-nav link
    content = re.sub(r'<a href=["\'](?:/admin|admin\.html)["\']>Admin</a>', r'<a href="analytics.html">Dashboard</a>', content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {file_path}")

print("Dashboard links updated.")
