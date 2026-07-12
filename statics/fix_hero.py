import re

file_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I will replace the entire <header class="site-header" id="overview"> ... </header> block
new_hero = """    <header class="site-header" id="overview" style="display: flex; flex-direction: row; align-items: center; justify-content: space-between; gap: 40px; padding: 40px 20px; flex-wrap: wrap;">
      <div class="hero-copy" style="flex: 1; min-width: 300px; text-align: left;">
        <span class="eyebrow" style="font-size: 14px; font-weight: 600; color: #38bdf8; display: block; margin-bottom: 12px; letter-spacing: 1px; text-transform: uppercase;">Sponsor & Client Portal</span>
        <h1 style="font-size: 3rem; line-height: 1.15; margin: 0 0 20px 0; font-weight: 800; color: #ffffff;">Sponsor Management and Social Media Marketing</h1>
        <p style="font-size: 1.1rem; line-height: 1.6; margin: 0 0 15px 0; color: #94a3b8; max-width: 90%;">Reimagine how brands and sponsors collaborate with transparent workflows and powerful campaign tools. Built for trust, growth, and business-ready deployment across teams and client networks.</p>
        <p style="font-size: 1rem; margin: 0 0 25px 0; color: #64748b; border-left: 3px solid #38bdf8; padding-left: 15px;">A polished sponsor portal and social media marketing hub for business use — ready to launch, manage relationships, and drive campaigns.</p>
        
        <div class="hero-social" style="margin-top: 30px; display: flex; gap: 15px; justify-content: flex-start;">
          <a href="#contact" class="social-link" style="color: #cbd5e1; text-decoration: none; font-size: 0.95rem;">Instagram</a>
          <a href="#about" class="social-link" style="color: #cbd5e1; text-decoration: none; font-size: 0.95rem;">LinkedIn</a>
          <a href="analytics.html#media" class="social-link" style="color: #cbd5e1; text-decoration: none; font-size: 0.95rem;">Twitter</a>
        </div>
      </div>
      
      <div class="hero-business-image" style="flex: 1; min-width: 300px; display: flex; justify-content: center; position: relative;">
        <!-- Glowing background effect behind the image -->
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 80%; height: 80%; background: radial-gradient(circle, rgba(56,189,248,0.2) 0%, rgba(15,23,42,0) 70%); filter: blur(40px); z-index: 0;"></div>
        
        <img src="https://images.unsplash.com/photo-1542744173-8e7e53415bb0?auto=format&fit=crop&w=600&q=80" 
             alt="Social Media Marketing & Sponsor Management Team" 
             style="position: relative; z-index: 1; width: 100%; max-width: 500px; border-radius: 20px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5); object-fit: cover; border: 1px solid rgba(255, 255, 255, 0.1); transform: perspective(1000px) rotateY(-5deg);" />
      </div>
    </header>"""

# Use regex to find and replace the current hero section
# The current hero starts with <header class="site-header" id="overview"> and ends with </header>
# But there might be other </header> inside. Actually it's the first </header> after <header class="site-header" id="overview">
import re
content = re.sub(r'<header class="site-header" id="overview">.*?</header>', new_hero, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero section redesigned successfully!")
