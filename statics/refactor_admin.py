import re
import os

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/admin.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to redesign admin.html to have a sidebar with links to Home, Dashboard, Analytics, Registration Board.
# We will use the layout requested.

new_admin_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#3b82f6" />
    <title>Admin Dashboard - R-Abhi Tech Solution</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="admin-styles.css">
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
    <style>
        body { margin: 0; padding: 0; font-family: sans-serif; display: flex; height: 100vh; overflow: hidden; }
        
        .admin-sidebar {
            width: 250px;
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(12px);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
            display: flex;
            flex-direction: column;
            padding: 20px 0;
        }
        
        .admin-sidebar h2 { color: #3b82f6; text-align: center; margin-bottom: 30px; font-size: 22px; }
        
        .sidebar-link {
            padding: 15px 25px;
            color: #cbd5e1;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 15px;
            font-size: 16px;
            transition: 0.3s;
            border-left: 3px solid transparent;
        }
        
        .sidebar-link:hover, .sidebar-link.active {
            background: rgba(59, 130, 246, 0.15);
            color: #fff;
            border-left: 3px solid #3b82f6;
        }
        
        .admin-main {
            flex: 1;
            overflow-y: auto;
            padding: 30px 5%;
        }

        .tab-content {
            display: none;
        }
        .tab-content.active {
            display: block;
        }
        
        .action-btn { padding: 8px 12px; border-radius: 6px; border: none; font-weight: bold; cursor: pointer; color: #fff; }
        .btn-approve { background: #10b981; }
        .btn-delete { background: #ef4444; }
    </style>
</head>
<body>

    <div class="admin-sidebar">
        <h2>Admin Panel</h2>
        <a href="index.html" class="sidebar-link"><ion-icon name="home-outline"></ion-icon> Front Page (Home)</a>
        <a href="#" class="sidebar-link active" onclick="switchTab('dashboard')"><ion-icon name="grid-outline"></ion-icon> Dashboard</a>
        <a href="#" class="sidebar-link" onclick="switchTab('analytics')"><ion-icon name="stats-chart-outline"></ion-icon> Analytics Board</a>
        <a href="#" class="sidebar-link" onclick="switchTab('registration')"><ion-icon name="people-outline"></ion-icon> Registration Board</a>
    </div>

    <div class="admin-main">
        
        <!-- Dashboard Tab -->
        <div id="dashboard" class="tab-content active">
            <h1 style="color: #fff; margin-bottom: 20px;">Dashboard Overview</h1>
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
            <div>
                <img src="dashboard-bg.png" alt="Dashboard Chart" style="width: 100%; border-radius: 16px; opacity: 0.8; object-fit: cover; max-height: 400px;">
            </div>
        </div>

        <!-- Analytics Board Tab -->
        <div id="analytics" class="tab-content">
            <h1 style="color: #fff; margin-bottom: 20px;">Analytics Board</h1>
            <div class="glass-panel" style="padding: 30px; border-radius: 16px; color: #cbd5e1;">
                <h2>System Analytics</h2>
                <p>Detailed performance analytics and platform engagement metrics.</p>
                <div style="display: flex; gap: 20px; margin-top: 20px;">
                    <img src="Social_media_marketing.png" alt="Analytics" style="width: 48%; border-radius: 12px;">
                    <img src="types-of-social-media-marketing.png" alt="Types" style="width: 48%; border-radius: 12px;">
                </div>
            </div>
        </div>

        <!-- Registration Board Tab -->
        <div id="registration" class="tab-content">
            <h1 style="color: #fff; margin-bottom: 20px;">Registration Board</h1>
            
            <div class="admin-table-wrapper glass-panel" style="padding: 30px; border-radius: 16px; overflow-x: auto;">
                <h3 style="color: #fff; margin-bottom: 20px;"><ion-icon name="people-circle-outline"></ion-icon> Manage Registrations</h3>
                <table style="width: 100%; text-align: left; border-collapse: collapse;">
                    <thead>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.2); color: #3b82f6;">
                            <th style="padding: 12px;">ID</th>
                            <th style="padding: 12px;">Type</th>
                            <th style="padding: 12px;">Name</th>
                            <th style="padding: 12px;">Email</th>
                            <th style="padding: 12px;">Status</th>
                            <th style="padding: 12px;">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color: #cbd5e1;">
                            <td style="padding: 12px;">#1001</td>
                            <td style="padding: 12px;">Sponsor</td>
                            <td style="padding: 12px;">Rahul Sharma</td>
                            <td style="padding: 12px;">rahul@example.com</td>
                            <td style="padding: 12px; color: #f59e0b;">Pending</td>
                            <td style="padding: 12px;">
                                <button class="action-btn btn-approve" onclick="alert('Approved!')">Approve</button>
                                <button class="action-btn btn-delete" onclick="this.parentElement.parentElement.remove()">Delete</button>
                            </td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color: #cbd5e1;">
                            <td style="padding: 12px;">#1002</td>
                            <td style="padding: 12px;">Client</td>
                            <td style="padding: 12px;">Priya Singh</td>
                            <td style="padding: 12px;">priya@brand.com</td>
                            <td style="padding: 12px; color: #f59e0b;">Pending</td>
                            <td style="padding: 12px;">
                                <button class="action-btn btn-approve" onclick="alert('Approved!')">Approve</button>
                                <button class="action-btn btn-delete" onclick="this.parentElement.parentElement.remove()">Delete</button>
                            </td>
                        </tr>
                        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1); color: #cbd5e1;">
                            <td style="padding: 12px;">#1003</td>
                            <td style="padding: 12px;">Sponsor</td>
                            <td style="padding: 12px;">Amit Kumar</td>
                            <td style="padding: 12px;">amit@tech.in</td>
                            <td style="padding: 12px; color: #10b981;">Active</td>
                            <td style="padding: 12px;">
                                <button class="action-btn btn-delete" onclick="this.parentElement.parentElement.remove()">Delete</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

    </div>

    <script>
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.sidebar-link').forEach(link => link.classList.remove('active'));
            
            document.getElementById(tabId).classList.add('active');
            event.currentTarget.classList.add('active');
        }
    </script>
</body>
</html>"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_admin_html)

print("Redesigned admin.html successfully.")
