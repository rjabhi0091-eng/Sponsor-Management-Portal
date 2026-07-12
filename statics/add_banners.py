import os
import re

files_and_images = {
    'about.html': 'https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1920&q=80',
    'contact.html': 'https://images.unsplash.com/photo-1423666639041-f56000c27a9a?auto=format&fit=crop&w=1920&q=80',
    'media.html': 'https://images.unsplash.com/photo-1616469829581-73993eb86b02?auto=format&fit=crop&w=1920&q=80',
    'registration.html': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1920&q=80',
    'work.html': 'https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=1920&q=80'
}

titles = {
    'about.html': 'About Us',
    'contact.html': 'Contact Us',
    'media.html': 'Media Hub',
    'registration.html': 'Registration',
    'work.html': 'Marketing Workflow'
}

subtitles = {
    'about.html': 'Our story, mission, and team.',
    'contact.html': 'Get in touch and chat with AI.',
    'media.html': 'Social media content, influencers, and videos.',
    'registration.html': 'Join the ultimate sponsor portal.',
    'work.html': 'Track campaigns and social media marketing.'
}

banner_template = """  <div class="page-header-banner" style="height: 250px; background: linear-gradient(180deg, rgba(6, 182, 212, 0.6), rgba(4, 25, 46, 0.9)), url('{image_url}') center/cover; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; color: white;">
    <h1 style="font-size: 3rem; margin-bottom: 0.5rem; text-shadow: 0 4px 6px rgba(0,0,0,0.5);">{title}</h1>
    <p style="font-size: 1.2rem; color: rgba(255,255,255,0.85); text-shadow: 0 2px 4px rgba(0,0,0,0.5);">{subtitle}</p>
  </div>
"""

for file, img_url in files_and_images.items():
    path = os.path.join(os.getcwd(), file)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'page-header-banner' not in content:
            banner = banner_template.format(image_url=img_url, title=titles[file], subtitle=subtitles[file])
            new_content = content.replace('<div class="page-shell">', '<div class="page-shell">\n' + banner)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Added banner to {file}')
