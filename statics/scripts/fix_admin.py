import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

admin_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - R-Abhi Tech Solution</title>
    <link rel="stylesheet" href="styles.css">
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
</head>
<body class="admin-body">

    <!-- ADMIN HEADER -->
    <div class="admin-header-bg">
        <div class="navbar">
            <div class="icon">
                <h2 class="logo">R-ABHI<br><span class="logo-sub">TECH SOLUTION</span></h2>
            </div>
            <div class="menu">
                <ul>
                    <li><a href="/">HOME</a></li>
                    <li><a href="/#services">SERVICES</a></li>
                    <li><a href="/#about">ABOUT</a></li>
                    <li><a href="/#work">WORK</a></li>
                    <li><a href="/#media">MEDIA</a></li>
                    <li><a href="/#contact">CONTACT</a></li>
                </ul>
            </div>
        </div> 
    </div>

    <!-- ADMIN DASHBOARD CONTENT -->
    <div class="sections-wrapper">
        <section class="clean-section">
            <div class="section-container">
                <h2 class="section-title">ADMIN <span>DASHBOARD</span></h2>
                
                <div class="admin-tables-container">
                    <!-- SPONSORS TABLE -->
                    <div class="admin-table-wrapper">
                        <div class="table-header">
                            <h3><ion-icon name="briefcase"></ion-icon> Registered Sponsors</h3>
                        </div>
                        <table class="admin-table">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Phone</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody id="sponsor-list">
                                <!-- Populated by app.js -->
                            </tbody>
                        </table>
                    </div>

                    <!-- CLIENTS TABLE -->
                    <div class="admin-table-wrapper" style="margin-top: 50px;">
                        <div class="table-header">
                            <h3><ion-icon name="people"></ion-icon> Registered Clients</h3>
                        </div>
                        <table class="admin-table">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Company</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody id="client-list">
                                <!-- Populated by app.js -->
                            </tbody>
                        </table>
                    </div>

                </div>
            </div>
        </section>
        
        <footer>
            <p>Admin Dashboard - R-Abhi Tech Solution.</p>
        </footer>
    </div>

    <script src="app.js"></script>
</body>
</html>
"""

# Append CSS for Admin page
admin_css = """

/* ADMIN DASHBOARD SPECIFIC CSS */
.admin-body {
    background-color: #121212;
}

.admin-header-bg {
    background: #000;
    border-bottom: 2px solid #ff7200;
    padding-top: 10px;
    padding-bottom: 10px;
}

.admin-tables-container {
    background: #1a1a1a;
    padding: 40px;
    border-radius: 10px;
}

.admin-table-wrapper {
    overflow-x: auto;
}

.table-header {
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.table-header h3 {
    color: #ff7200;
    font-size: 24px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.admin-table {
    width: 100%;
    border-collapse: collapse;
    color: #fff;
    text-align: left;
}

.admin-table th, .admin-table td {
    padding: 15px;
    border-bottom: 1px solid #333;
}

.admin-table th {
    background: #ff7200;
    color: #000;
    font-weight: bold;
    text-transform: uppercase;
    font-size: 14px;
}

.admin-table tbody tr:hover {
    background: #222;
}

/* Action Buttons inside Admin Table */
.admin-table .action-btn {
    padding: 8px 12px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    margin-right: 5px;
    transition: 0.3s;
}

.admin-table .edit-btn,
.admin-table .edit-sponsor-btn,
.admin-table .edit-client-btn {
    background-color: #4CAF50;
    color: white;
}

.admin-table .delete-btn,
.admin-table .delete-sponsor-btn,
.admin-table .delete-client-btn {
    background-color: #f44336;
    color: white;
}

.admin-table .action-btn:hover {
    opacity: 0.8;
}
"""

with open(os.path.join(base_dir, 'admin.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)

with open(os.path.join(base_dir, 'styles.css'), 'a', encoding='utf-8') as f:
    f.write(admin_css)

print("Fixed admin.html and appended CSS to styles.css.")
