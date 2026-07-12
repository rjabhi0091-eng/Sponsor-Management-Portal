import re

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/admin.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Sidebar Updates
# Find the end of the sidebar links (</div> of admin-sidebar)
sidebar_replacement = """        <a href="#" class="sidebar-link" onclick="switchTab('registration')"><ion-icon name="people-outline"></ion-icon>
            Registration Board</a>
        <a href="#" class="sidebar-link" onclick="switchTab('feedback')"><ion-icon name="chatbubbles-outline"></ion-icon>
            Feedback Review</a>

        <div style="margin-top: auto; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
            <a href="#" class="sidebar-link"><ion-icon name="settings-outline"></ion-icon> Settings</a>
            <a href="#" class="sidebar-link"><ion-icon name="person-circle-outline"></ion-icon> Profile Login</a>
        </div>
    </div>"""
content = content.replace("""        <a href="#" class="sidebar-link" onclick="switchTab('registration')"><ion-icon name="people-outline"></ion-icon>
            Registration Board</a>
    </div>""", sidebar_replacement)

# 2. Dashboard Updates (Export to Excel, Graph Analytics, Number Analytics)
dashboard_replacement = """        <!-- Dashboard Tab -->
        <div id="dashboard" class="tab-content active">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <h1 style="color: #fff; margin: 0;">Dashboard Overview</h1>
                <button class="action-btn" style="background: #10b981; display: flex; align-items: center; gap: 8px;"><ion-icon name="document-text-outline"></ion-icon> Export to Excel</button>
            </div>
            
            <h3 style="color: #cbd5e1; margin-bottom: 10px;">Number Analytic Board</h3>
            <div class="hero-dashboard-grid glass-panel" style="margin-bottom: 40px; padding: 20px;">
                <article class="hero-dashboard-card">
                    <span>Total Sponsors</span>
                    <strong>42</strong>
                </article>
                <article class="hero-dashboard-card">
                    <span>Total Clients</span>
                    <strong>156</strong>
                </article>
                <article class="hero-dashboard-card">
                    <span>Pending Approvals</span>
                    <strong style="color: #ef4444;">12</strong>
                </article>
            </div>

            <h3 style="color: #cbd5e1; margin-bottom: 10px;">Graph Analytics Board</h3>
            <div class="glass-panel" style="padding: 20px; border-radius: 16px;">
                <img src="dashboard-bg.png" alt="Dashboard Chart"
                    style="width: 100%; border-radius: 12px; opacity: 0.9; object-fit: cover; max-height: 400px;">
            </div>
        </div>"""
content = re.sub(r'<!-- Dashboard Tab -->.*?</div>\s*</div>', dashboard_replacement, content, flags=re.DOTALL)

# 3. Feedback Review Tab (Insert before <script>)
feedback_tab = """        <!-- Feedback Review Tab -->
        <div id="feedback" class="tab-content">
            <h1 style="color: #fff; margin-bottom: 20px;">Feedback Review</h1>
            <div class="glass-panel" style="padding: 30px; border-radius: 16px; color: #cbd5e1;">
                <h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="star-outline"></ion-icon> User Feedback & Reviews</h3>
                <div style="display: flex; flex-direction: column; gap: 15px;">
                    <div style="background: rgba(255,255,255,0.05); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                        <strong style="color: #38bdf8;">Rajesh Kumar</strong> - <span style="font-size: 14px; color: #94a3b8;">Sponsor</span>
                        <p style="margin-top: 10px; font-size: 15px;">"The new dashboard is fantastic. It's very easy to track campaign ROI."</p>
                    </div>
                    <div style="background: rgba(255,255,255,0.05); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);">
                        <strong style="color: #10b981;">Sneha Patil</strong> - <span style="font-size: 14px; color: #94a3b8;">Client</span>
                        <p style="margin-top: 10px; font-size: 15px;">"Adding my portfolio was super seamless. Thanks!"</p>
                    </div>
                </div>
            </div>
        </div>

    </div>"""
content = content.replace('    </div>\n\n    <script>', feedback_tab + '\n\n    <script>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Admin panel updated successfully.")
