import os
import re

files_to_clean = ['about.html', 'contact.html', 'media.html', 'registration.html', 'work.html']

nav_regex = re.compile(r'\s*<section class="nav-section">.*?</section>', re.DOTALL)

for file in files_to_clean:
    path = os.path.join(os.getcwd(), file)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove nav-section
        new_content = nav_regex.sub('', content)
        
        # Change header actions to just a Back button if not already changed
        header_actions_regex = re.compile(r'<div class="header-actions">.*?</div>', re.DOTALL)
        standard_header = '''<div class="header-actions">
      <a href="/" class="secondary" style="text-decoration:none;display:inline-flex;align-items:center;justify-content:center;" data-icon="⬅️">Back to Home</a>
    </div>'''
        new_content = header_actions_regex.sub(standard_header, new_content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Processed {file}')
