import re
import os

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/login.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS for new features
css_injection = """
        .password-container {
            position: relative;
            display: flex;
            align-items: center;
        }
        .password-container input {
            padding-right: 40px;
        }
        .toggle-password {
            position: absolute;
            right: 10px;
            color: #a1a1aa;
            cursor: pointer;
            font-size: 20px;
            transition: 0.3s;
        }
        .toggle-password:hover {
            color: #8b5cf6;
        }
        .login-options {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            margin-bottom: 20px;
        }
        .login-options label {
            display: flex;
            align-items: center;
            gap: 5px;
            color: #a1a1aa;
            cursor: pointer;
        }
        .login-options a {
            color: #8b5cf6;
            text-decoration: none;
            transition: 0.3s;
        }
        .login-options a:hover {
            text-decoration: underline;
        }
"""
content = content.replace("</style>", css_injection + "\n    </style>")

# 2. Modify the HTML form
form_html = """
        <form id="login-form" onsubmit="handleLogin(event)">
            <div class="form-group">
                <label>Email Address</label>
                <input type="email" id="email-input" required placeholder="sponsor@company.com" />
            </div>
            <div class="form-group">
                <label>Password</label>
                <div class="password-container">
                    <input type="password" id="password-input" required placeholder="********" />
                    <ion-icon name="eye-outline" class="toggle-password" onclick="togglePasswordVisibility()"></ion-icon>
                </div>
            </div>
            <div class="login-options">
                <label><input type="checkbox" id="remember-me"> Remember me</label>
                <a href="#" onclick="alert('Password reset link sent to your email.')">Forgot Password?</a>
            </div>
            <button type="submit" class="login-btn" id="submit-btn">Login as Sponsor</button>
        </form>
"""
content = re.sub(r'<form id="login-form".*?</form>', form_html, content, flags=re.DOTALL)

# 3. Add JS function for password toggle
js_injection = """
        function togglePasswordVisibility() {
            const passwordInput = document.getElementById('password-input');
            const icon = document.querySelector('.toggle-password');
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                icon.name = 'eye-off-outline';
            } else {
                passwordInput.type = 'password';
                icon.name = 'eye-outline';
            }
        }
"""
content = content.replace("function handleLogin(event)", js_injection + "\n        function handleLogin(event)")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("login.html updated with latest features successfully.")
