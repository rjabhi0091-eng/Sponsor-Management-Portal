import re
import os

login_html_path = 'd:/WebPortal/Sponsor-Management-Portal/static/login.html'
index_html_path = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'

# 1. Completely rewrite login.html
login_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#8b5cf6" />
    <title>Login - R-Abhi Tech Solution</title>
    <link rel="stylesheet" href="style.css">
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
    <style>
        .login-wrapper {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #09090b;
            position: relative;
            padding: 40px 20px;
        }
        .back-home {
            position: absolute;
            top: 30px;
            left: 5%;
            color: #a1a1aa;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 16px;
            transition: 0.3s;
        }
        .back-home:hover {
            color: #8b5cf6;
        }
        .login-container {
            width: 100%;
            max-width: 900px;
            text-align: center;
        }
        .login-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }
        .login-card {
            background: rgba(24, 24, 27, 0.7);
            backdrop-filter: blur(12px);
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.1);
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .login-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(139, 92, 246, 0.2);
            border-color: rgba(139, 92, 246, 0.4);
        }
        .login-card h2 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        .form-group {
            text-align: left;
            margin-bottom: 15px;
        }
        .form-group label {
            color: #a1a1aa;
            display: block;
            margin-bottom: 5px;
            font-size: 14px;
        }
        .form-group input {
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.15);
            background: #18181b;
            color: #fff;
            box-sizing: border-box;
        }
        .login-btn {
            width: 100%;
            background: linear-gradient(135deg, #3b82f6, #8b5cf6);
            color: #fff;
            padding: 12px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
            font-size: 16px;
            transition: opacity 0.3s;
        }
        .login-btn:hover {
            opacity: 0.9;
        }
    </style>
</head>
<body>

    <div class="login-wrapper">
        <a href="index.html" class="back-home"><ion-icon name="arrow-back-outline"></ion-icon> Back to Home</a>
        
        <div class="login-container">
            <h1 style="color: #fff; font-size: 32px; margin-bottom: 10px;">Portal Access</h1>
            <p style="color: #a1a1aa;">Please select your account type to login.</p>

            <div class="login-grid">
                <!-- Sponsor Login -->
                <div class="login-card">
                    <h2><ion-icon name="business-outline"></ion-icon> Sponsor Login</h2>
                    <form onsubmit="event.preventDefault(); window.location.href='analytics.html';">
                        <div class="form-group">
                            <label>Email Address</label>
                            <input type="email" required placeholder="sponsor@company.com" />
                        </div>
                        <div class="form-group">
                            <label>Password</label>
                            <input type="password" required placeholder="********" />
                        </div>
                        <button type="submit" class="login-btn">Login as Sponsor</button>
                    </form>
                </div>

                <!-- Client Login -->
                <div class="login-card">
                    <h2><ion-icon name="person-outline"></ion-icon> Client Login</h2>
                    <form onsubmit="event.preventDefault(); window.location.href='analytics.html';">
                        <div class="form-group">
                            <label>Email Address</label>
                            <input type="email" required placeholder="client@brand.com" />
                        </div>
                        <div class="form-group">
                            <label>Password</label>
                            <input type="password" required placeholder="********" />
                        </div>
                        <button type="submit" class="login-btn">Login as Client</button>
                    </form>
                </div>

                <!-- Admin Login -->
                <div class="login-card">
                    <h2><ion-icon name="shield-checkmark-outline"></ion-icon> Admin Login</h2>
                    <form onsubmit="event.preventDefault(); window.location.href='admin.html';">
                        <div class="form-group">
                            <label>Email Address</label>
                            <input type="email" required placeholder="admin@portal.com" />
                        </div>
                        <div class="form-group">
                            <label>Password</label>
                            <input type="password" required placeholder="********" />
                        </div>
                        <button type="submit" class="login-btn">Login as Admin</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

</body>
</html>"""

with open(login_html_path, 'w', encoding='utf-8') as f:
    f.write(login_content)

# 2. Update index.html
with open(index_html_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Change the Login button link in the header from #login-portals to login.html
index_content = index_content.replace('href="#login-portals" class="primary" data-icon="🔐"', 'href="login.html" class="primary" data-icon="🔐"')

# Remove the #login-portals section from index.html completely
login_section_regex = re.compile(r'<section id="login-portals".*?</section>', re.DOTALL)
index_content = re.sub(login_section_regex, '', index_content)

# Also update the nav link from #login-portals to login.html if it exists
index_content = index_content.replace('<a href="#login-portals">Login Portals</a>', '<a href="login.html">Login Portals</a>')

with open(index_html_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("login.html updated and linked successfully.")
