import os

css_content = """
/* Global Redesign & Alignment Styles (Appended) */
body {
  background-color: #0f172a; /* Dark modern blue-gray */
  color: #cbd5e1;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.6;
}
.page-shell {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 5%;
}

/* Typography & Colors */
h1, h2, h3, h4 { color: #ffffff; }
.eyebrow { color: #3b82f6; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }

/* Buttons - Enhanced Styling */
button, .secondary, .primary {
  padding: 12px 24px;
  border-radius: 50px; /* Pill shape */
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.primary {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  border: none;
  color: #fff;
}
.primary:hover { 
  transform: translateY(-2px);
  box-shadow: 0 8px 15px rgba(59, 130, 246, 0.4);
}
.secondary {
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.5);
  color: #60a5fa;
}
.secondary:hover { 
  background: rgba(59, 130, 246, 0.2); 
  transform: translateY(-2px);
  border-color: #3b82f6;
  color: #fff;
}

/* Hero Section (Side-by-side image) */
.site-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  margin-top: 40px;
  margin-bottom: 60px;
}
.hero-copy {
  flex: 1;
  text-align: left !important;
}
.hero-business-image {
  flex: 1;
  text-align: right;
}
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 20px;
}
.hero-social {
  margin-top: 20px;
  display: flex;
  gap: 15px;
}
.social-link { color: #3b82f6; text-decoration: none; transition: 0.3s; }
.social-link:hover { color: #60a5fa; }

/* Navigation */
.nav-section { margin-top: 20px; }
.site-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  background: #1e293b;
  padding: 15px;
  border-radius: 50px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
.site-nav a { color: #cbd5e1; text-decoration: none; transition: 0.3s; padding: 5px 10px; border-radius: 20px; }
.site-nav a:hover { color: #fff; background: rgba(59,130,246,0.2); }
.bottom-nav { display: none; } /* Hide mobile nav on desktop */

/* Grids & Cards */
.hero-dashboard-grid, .feature-grid, .register-grid, .about-grid, .team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin: 30px 0;
}
.hero-dashboard-card, .feature-card, .register-card, .about-card, .team-card, .metric-card {
  background: #1e293b;
  padding: 25px;
  border-radius: 16px;
  border: 1px solid #334155;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.hero-dashboard-card:hover, .feature-card:hover, .team-card:hover { 
  transform: translateY(-8px); 
  border-color: #3b82f6; 
  box-shadow: 0 12px 20px rgba(0,0,0,0.2);
}

/* Panels (Sponsors, Clients, Marketing) */
.management-panel, .window-panel {
  display: flex;
  gap: 30px;
  margin-top: 20px;
  align-items: flex-start;
}
.management-sidebar, .window-panel-sidebar {
  flex: 0 0 260px;
  background: #1e293b;
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.management-content, .window-panel-content {
  flex: 1;
  background: #1e293b;
  padding: 20px;
  border-radius: 16px;
  overflow-x: auto;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

/* Tables */
table { width: 100%; border-collapse: separate; border-spacing: 0; margin-top: 15px; }
th, td { padding: 15px; border-bottom: 1px solid #334155; text-align: left; }
th { background: #0f172a; color: #3b82f6; font-weight: 600; text-transform: uppercase; font-size: 13px; letter-spacing: 1px; }
th:first-child { border-top-left-radius: 8px; }
th:last-child { border-top-right-radius: 8px; }
tr:hover td { background: #334155; }

/* Forms */
form label { display: block; margin-bottom: 15px; font-weight: 600; color: #cbd5e1; }
form input, form select, form textarea {
  width: 100%;
  padding: 12px;
  margin-top: 6px;
  border-radius: 8px;
  border: 1px solid #475569;
  background: #0f172a;
  color: #fff;
  transition: all 0.3s;
}
form input:focus, form select:focus, form textarea:focus { 
  border-color: #3b82f6; 
  outline: none; 
  box-shadow: 0 0 0 3px rgba(59,130,246,0.2);
}

/* Sections */
section { padding: 80px 0; border-bottom: 1px solid #1e293b; }
.section-head { text-align: center; margin-bottom: 50px; max-width: 800px; margin-left: auto; margin-right: auto; }

@media (max-width: 900px) {
  .site-header { flex-direction: column; text-align: center; }
  .hero-copy { text-align: center !important; }
  .hero-actions { justify-content: center; }
  .management-panel, .window-panel { flex-direction: column; }
  .management-sidebar, .window-panel-sidebar { flex: auto; width: 100%; }
}
"""

with open("d:/WebPortal/Sponsor-Management-Portal/static/style.css", "a", encoding="utf-8") as f:
    f.write("\\n" + css_content + "\\n")

print("CSS appended successfully!")
