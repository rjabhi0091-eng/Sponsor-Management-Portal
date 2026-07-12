import os
import re

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

def extract_section(filepath, section_id):
    if not os.path.exists(filepath):
        return ""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find main content (usually skipping header/nav/footer)
    # We can just extract everything between <div class="page-shell"> and <script> or <footer>
    match = re.search(r'<div class="page-shell">.*?<section class="nav-section">.*?</section>\s*(?:<div class="page-header-banner".*?</div>)?\s*(?:<div class="hero-image-banner".*?</div>)?\s*(<section.*?)<script', content, flags=re.DOTALL)
    if match:
        return f'<div id="{section_id}" class="spa-section">\n' + match.group(1) + '\n</div>'
    return ""

about_content = extract_section(os.path.join(base_dir, 'about.html'), 'about')
media_content = extract_section(os.path.join(base_dir, 'media.html'), 'media')
work_content = extract_section(os.path.join(base_dir, 'work.html'), 'work')
contact_content = extract_section(os.path.join(base_dir, 'contact.html'), 'contact')

new_index = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>R-Abhi Tech Solution</title>
  <link rel="stylesheet" href="styles.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
</head>
<body class="spa-body">

  <div class="spa-bg"></div>

  <nav class="spa-nav">
    <div class="spa-logo"><span class="logo-white">R-Abhi Tech</span> <span class="logo-orange">Solution</span></div>
    <ul class="spa-menu">
      <li><a href="#home">HOME</a></li>
      <li><a href="#about">ABOUT</a></li>
      <li><a href="#media">MEDIA</a></li>
      <li><a href="#work">WORK</a></li>
      <li><a href="#contact">CONTACT</a></li>
      <li><a href="/admin">ADMIN</a></li>
    </ul>
    <div class="spa-search">
      <input type="text" placeholder="Type to Search">
      <button>Search</button>
    </div>
  </nav>

  <div class="spa-container" id="home">
    <div class="hero-left">
      <h1>Sponsor Management &<br><span class="highlight">Marketing</span><br>Portal</h1>
      <p>Sponsor Management is a specialization of the digital stream. We use advanced tools, analytics, and software to create powerful brand identities.</p>
      <button class="btn-join">JOIN US</button>
    </div>
    
    <div class="hero-right">
      <div class="login-box">
        <h2 class="login-title">Login Here</h2>
        <form class="login-form" id="spa-login-form">
          <input type="email" placeholder="Enter Email Here" required>
          <input type="password" placeholder="Enter Password Here" required>
          <button type="submit" class="btn-login">Login</button>
        </form>
        <p class="signup-text">Don't have an account?<br><a href="#register">Sign up</a> here</p>
        <p class="social-text">Log in with</p>
        <div class="social-icons">
          <i class="fab fa-facebook-f"></i>
          <i class="fab fa-instagram"></i>
          <i class="fab fa-twitter"></i>
          <i class="fab fa-google"></i>
          <i class="fab fa-skype"></i>
        </div>
      </div>
    </div>
  </div>

  <div class="spa-content-sections">
    {about_content}
    {media_content}
    {work_content}
    {contact_content}
    
    <!-- Original Registration Forms moved to bottom so they can sign up -->
    <div id="register" class="spa-section" style="padding: 4rem 2rem; max-width: 1200px; margin: 0 auto;">
      <h2 style="text-align:center; color:white; margin-bottom:2rem; font-size:2.5rem;">Register Account</h2>
      <div class="register-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem;">
        <article class="register-card" style="background: rgba(0,0,0,0.6); padding: 2rem; border-radius: 12px; border-top: 4px solid #f97316;">
          <h3 style="color: #f97316; font-size: 1.5rem; margin-bottom: 0.5rem;">Sponsor Registration</h3>
          <form id="register-sponsor-form" class="record-form">
            <label style="color:white">Name<input type="text" id="register-sponsor-name" required /></label>
            <label style="color:white">Email<input type="email" id="register-sponsor-email" required /></label>
            <label style="color:white">Phone<input type="text" id="register-sponsor-phone" required /></label>
            <label style="color:white">Password<input type="password" id="register-sponsor-password" required autocomplete="new-password" /></label>
            <button type="submit" style="background:#f97316; border:none; padding:0.8rem; color:black; font-weight:bold; width:100%; border-radius:5px; margin-top:1rem;">Register</button>
          </form>
        </article>
        <article class="register-card" style="background: rgba(0,0,0,0.6); padding: 2rem; border-radius: 12px; border-top: 4px solid #f97316;">
          <h3 style="color: #f97316; font-size: 1.5rem; margin-bottom: 0.5rem;">Client Registration</h3>
          <form id="register-client-form" class="record-form">
            <label style="color:white">Name<input type="text" id="register-client-name" required /></label>
            <label style="color:white">Email<input type="email" id="register-client-email" required /></label>
            <label style="color:white">Company<input type="text" id="register-client-company" required /></label>
            <label style="color:white">Password<input type="password" id="register-client-password" required autocomplete="new-password" /></label>
            <button type="submit" style="background:#f97316; border:none; padding:0.8rem; color:black; font-weight:bold; width:100%; border-radius:5px; margin-top:1rem;">Register</button>
          </form>
        </article>
      </div>
    </div>
  </div>

  <script src="app.js"></script>
</body>
</html>
"""

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(new_index)

# Create CSS adjustments
css_additions = """
/* SPA Styles matching screenshot */
.spa-body {
  margin: 0;
  padding: 0;
  font-family: 'Arial', sans-serif;
  color: white;
  background: #000;
  min-height: 100vh;
}

.spa-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat;
  z-index: -1;
}

.spa-bg::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.4);
}

.spa-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 5%;
  background: transparent;
}

.spa-logo {
  font-size: 2rem;
  font-weight: bold;
}
.logo-orange {
  color: #f97316;
}

.spa-menu {
  list-style: none;
  display: flex;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.spa-menu a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  font-size: 0.9rem;
  letter-spacing: 1px;
}

.spa-menu a:hover {
  color: #f97316;
}

.spa-search {
  display: flex;
  background: #000;
  border-radius: 4px;
  overflow: hidden;
  border: 1px solid #333;
}

.spa-search input {
  background: transparent;
  border: none;
  color: white;
  padding: 0.6rem 1rem;
  outline: none;
  width: 150px;
}

.spa-search button {
  background: #f97316;
  border: none;
  color: white;
  padding: 0.6rem 1.2rem;
  cursor: pointer;
  font-weight: bold;
}

.spa-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 4rem 8%;
  min-height: 80vh;
}

.hero-left {
  flex: 1;
  max-width: 600px;
}

.hero-left h1 {
  font-size: 3.5rem;
  line-height: 1.2;
  margin-bottom: 1rem;
}

.hero-left .highlight {
  color: #f97316;
}

.hero-left p {
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
  color: #e2e8f0;
}

.btn-join {
  background: #f97316;
  color: black;
  border: none;
  padding: 1rem 2.5rem;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 4px;
  cursor: pointer;
}

.hero-right {
  flex: 0 0 350px;
}

.login-box {
  background: rgba(0, 0, 0, 0.7);
  padding: 2.5rem 2rem;
  border-radius: 12px;
  text-align: center;
}

.login-title {
  background: white;
  color: #f97316;
  padding: 0.5rem;
  border-radius: 4px;
  margin-bottom: 2rem;
  font-size: 1.2rem;
}

.login-form input {
  width: 100%;
  background: transparent;
  border: none;
  border-bottom: 1px solid #f97316;
  color: white;
  padding: 0.8rem 0;
  margin-bottom: 1.5rem;
  outline: none;
}

.login-form input::placeholder {
  color: #94a3b8;
}

.btn-login {
  width: 100%;
  background: #f97316;
  color: black;
  border: none;
  padding: 0.8rem;
  font-weight: bold;
  border-radius: 4px;
  margin-bottom: 1.5rem;
  cursor: pointer;
}

.signup-text {
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.signup-text a {
  color: #f97316;
  text-decoration: none;
}

.social-text {
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.social-icons {
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.social-icons i {
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
}

.spa-content-sections {
  background: rgba(15, 23, 42, 0.95);
  padding-bottom: 4rem;
}

.spa-section {
  padding: 4rem 5%;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}
"""

with open(os.path.join(base_dir, 'styles.css'), 'a', encoding='utf-8') as f:
    f.write(css_additions)

# Delete old html files to complete the SPA transformation
for old_file in ['about.html', 'media.html', 'work.html', 'contact.html', 'login.html']:
    p = os.path.join(base_dir, old_file)
    if os.path.exists(p):
        os.remove(p)

print("SPA built successfully")
