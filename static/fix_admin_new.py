import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

admin_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - R-Abhi Tech Solution</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
        .sub-header {
            min-height: 40vh;
            width: 100%;
            background-image: linear-gradient(rgba(4,9,30,0.7),rgba(4,9,30,0.7)),url(https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1920&q=80);
            background-position: center;
            background-size: cover;
            position: relative;
            text-align: center;
            color: #fff;
        }
        .sub-header h1 {
            margin-top: 100px;
        }
        
        .admin-content {
            width: 80%;
            margin: auto;
            padding: 60px 0;
        }
        
        .admin-table-wrapper {
            margin-bottom: 50px;
            background: #fff;
            padding: 30px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            border-radius: 10px;
            overflow-x: auto;
        }
        
        .admin-table-wrapper h3 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #333;
        }
        
        .admin-table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .admin-table th, .admin-table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        .admin-table th {
            background-color: #fff3f3;
            color: #333;
            font-weight: 600;
        }
        
        .admin-table tr:hover {
            background-color: #f9f9f9;
        }
        
        .action-btn {
            padding: 8px 12px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-family: 'Poppins', sans-serif;
            font-size: 13px;
            color: #fff;
            margin-right: 5px;
            transition: 0.3s;
        }
        
        .edit-btn, .edit-sponsor-btn, .edit-client-btn {
            background-color: #4CAF50;
        }
        
        .delete-btn, .delete-sponsor-btn, .delete-client-btn {
            background-color: #f44336;
        }
        
        .action-btn:hover {
            opacity: 0.8;
        }
    </style>
</head>
<body>

    <section class="sub-header">
        <nav>
            <a href="index.html" style="color:#fff; text-decoration:none; font-size:24px; font-weight:bold; letter-spacing:2px;">R-ABHI <span style="color:#f44336;">TECH</span></a>
            <div class="nav-links" id="navLinks">
                <i class="fa fa-times" onclick="hideMenu()"></i>
                <ul>
                    <li><a href="index.html">HOME</a></li>
                    <li><a href="index.html#services">SERVICES</a></li>
                    <li><a href="index.html#dashboard">DASHBOARD</a></li>
                    <li><a href="login.html">LOGIN</a></li>
                    <li><a href="admin.html">ADMIN</a></li>
                </ul>
            </div>
            <i class="fa fa-bars" onclick="showMenu()"></i>
        </nav>
        <h1>Admin Control Panel</h1>
    </section>

    <!-- ADMIN DASHBOARD CONTENT -->
    <section class="admin-content">
        <!-- SPONSORS TABLE -->
        <div class="admin-table-wrapper">
            <h3>Registered Sponsors</h3>
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
        <div class="admin-table-wrapper">
            <h3>Registered Clients</h3>
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
    </section>

    <section class="footer">
        <h4>About R-ABHI TECH SOLUTION</h4>
        <p>We are a leading Sponsor Management and Social Media Marketing agency dedicated to helping businesses,<br> startups, and organizations maximize their market presence and business growth.</p>
        <p>Powered by <i class="fa fa-heart-o"></i> R-Abhi Tech Solution</p>
    </section>

    <script>
        var navLinks = document.getElementById("navLinks");
        function showMenu(){
            navLinks.style.right = "0";
        }
        function hideMenu(){
            navLinks.style.right = "-200px";
        }
    </script>
    <script src="app.js"></script>
</body>
</html>
"""

with open(os.path.join(base_dir, 'admin.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)

print("Fixed admin.html according to new template.")
