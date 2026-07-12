import os

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/login.html'

html_content = """<!DOCTYPE html>
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
        body {
            margin: 0;
            padding: 0;
            background-color: #09090b;
            color: #fff;
            font-family: 'Inter', system-ui, sans-serif;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
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
            z-index: 100;
            transition: 0.3s;
        }
        .back-home:hover {
            color: #8b5cf6;
        }

        .login-card {
            background: rgba(24, 24, 27, 0.7);
            backdrop-filter: blur(12px);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.1);
            width: 100%;
            max-width: 420px;
            text-align: center;
            transition: 0.3s;
        }

        /* Selection Section */
        .selection-section {
            display: flex;
            background: rgba(0,0,0,0.3);
            border-radius: 12px;
            padding: 5px;
            margin-bottom: 30px;
            border: 1px solid rgba(255,255,255,0.05);
        }

        .select-btn {
            flex: 1;
            background: transparent;
            border: none;
            color: #a1a1aa;
            padding: 10px 0;
            font-size: 14px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }

        .select-btn.active {
            background: rgba(139, 92, 246, 0.2);
            color: #fff;
            border: 1px solid rgba(139, 92, 246, 0.4);
            box-shadow: 0 0 10px rgba(139, 92, 246, 0.1);
        }

        .login-card h2 {
            margin-top: 0;
            font-size: 26px;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 25px;
            transition: 0.3s;
        }

        .form-group {
            text-align: left;
            margin-bottom: 20px;
        }

        .form-group label {
            color: #a1a1aa;
            display: block;
            margin-bottom: 8px;
            font-size: 14px;
        }

        .form-group input {
            width: 100%;
            padding: 14px;
            border-radius: 8px;
            border: 1px solid rgba(255,255,255,0.15);
            background: #18181b;
            color: #fff;
            box-sizing: border-box;
            transition: 0.3s;
        }

        .form-group input:focus {
            outline: none;
            border-color: #8b5cf6;
            box-shadow: 0 0 10px rgba(139, 92, 246, 0.2);
        }

        .login-btn {
            width: 100%;
            background: linear-gradient(135deg, #3b82f6, #8b5cf6);
            color: #fff;
            padding: 14px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
            font-size: 16px;
            transition: opacity 0.3s, transform 0.3s;
        }

        .login-btn:hover {
            opacity: 0.9;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>

    <a href="index.html" class="back-home"><ion-icon name="arrow-back-outline"></ion-icon> Back to Home</a>

    <div class="login-card">
        
        <!-- Selection Section -->
        <div class="selection-section">
            <button class="select-btn active" onclick="setLoginType('sponsor', this)">Sponsor</button>
            <button class="select-btn" onclick="setLoginType('client', this)">Client</button>
            <button class="select-btn" onclick="setLoginType('admin', this)">Admin</button>
        </div>

        <h2 id="login-title"><ion-icon name="business-outline" id="login-icon"></ion-icon> <span id="login-text">Sponsor Login</span></h2>
        
        <form id="login-form" onsubmit="handleLogin(event)">
            <div class="form-group">
                <label>Email Address</label>
                <input type="email" id="email-input" required placeholder="sponsor@company.com" />
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" required placeholder="********" />
            </div>
            <button type="submit" class="login-btn" id="submit-btn">Login as Sponsor</button>
        </form>

    </div>

    <script>
        let currentType = 'sponsor';

        function setLoginType(type, btnElement) {
            currentType = type;
            
            // Update active button
            document.querySelectorAll('.select-btn').forEach(btn => btn.classList.remove('active'));
            btnElement.classList.add('active');

            // Update UI elements based on selection
            const icon = document.getElementById('login-icon');
            const text = document.getElementById('login-text');
            const emailInput = document.getElementById('email-input');
            const submitBtn = document.getElementById('submit-btn');

            if (type === 'sponsor') {
                icon.name = 'business-outline';
                text.innerText = 'Sponsor Login';
                emailInput.placeholder = 'sponsor@company.com';
                submitBtn.innerText = 'Login as Sponsor';
            } else if (type === 'client') {
                icon.name = 'person-outline';
                text.innerText = 'Client Login';
                emailInput.placeholder = 'client@brand.com';
                submitBtn.innerText = 'Login as Client';
            } else if (type === 'admin') {
                icon.name = 'shield-checkmark-outline';
                text.innerText = 'Admin Login';
                emailInput.placeholder = 'admin@portal.com';
                submitBtn.innerText = 'Login as Admin';
            }
        }

        function handleLogin(event) {
            event.preventDefault();
            if (currentType === 'admin') {
                window.location.href = 'admin.html';
            } else {
                window.location.href = 'analytics.html';
            }
        }
    </script>
</body>
</html>
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("login.html updated with selection section successfully.")
