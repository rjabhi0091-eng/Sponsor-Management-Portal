import os
import re

files_to_restore = ['about.html', 'contact.html', 'media.html', 'registration.html', 'work.html']

header_actions_new = '''<div class="header-actions">
      <a href="/login?role=sponsor" class="secondary" data-icon="🔐" style="text-decoration:none;display:inline-flex;align-items:center;justify-content:center;">Sponsor Login</a>
      <a href="/login?role=client" class="secondary" data-icon="👥" style="text-decoration:none;display:inline-flex;align-items:center;justify-content:center;">Client Login</a>
      <a href="/login?role=admin" class="secondary" data-icon="🛠️" style="text-decoration:none;display:inline-flex;align-items:center;justify-content:center;">Admin Login</a>
      <a id="open-admin-btn" href="/admin" class="primary" data-icon="🛠️" style="text-decoration:none;display:inline-flex;align-items:center;justify-content:center;">Admin Dashboard</a>
    </div>'''

nav_template = '''
    <section class="nav-section">
      <nav class="site-nav">
        <a href="/">Home</a>
        <a href="/about"{about_active}>About</a>
        <a href="/media"{media_active}>Media</a>
        <a href="/registration"{registration_active}>Registration</a>
        <a href="/work"{work_active}>Work</a>
        <a href="/contact"{contact_active}>Contact</a>
        <a href="/admin">Admin</a>
      </nav>
    </section>'''

for file in files_to_restore:
    path = os.path.join(os.getcwd(), file)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Replace header actions
        content = re.sub(r'<div class="header-actions">.*?</div>', header_actions_new, content, flags=re.DOTALL)
        
        # 2. Insert nav-section if not exists
        if '<section class="nav-section">' not in content:
            # Determine active class
            about_a = ' class="active"' if file == 'about.html' else ''
            media_a = ' class="active"' if file == 'media.html' else ''
            reg_a = ' class="active"' if file == 'registration.html' else ''
            work_a = ' class="active"' if file == 'work.html' else ''
            contact_a = ' class="active"' if file == 'contact.html' else ''
            
            nav_html = nav_template.format(
                about_active=about_a,
                media_active=media_a,
                registration_active=reg_a,
                work_active=work_a,
                contact_active=contact_a
            )
            
            # Insert after <div class="page-shell">
            content = content.replace('<div class="page-shell">', '<div class="page-shell">' + nav_html)
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Restored {file}')
