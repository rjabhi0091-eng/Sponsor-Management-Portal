import re
import os

filepath = 'd:/WebPortal/Sponsor-Management-Portal/static/login.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add CSS for social login
css_injection = """
        .login-btn:hover {
            opacity: 0.9;
            transform: translateY(-2px);
        }

        /* Social Login Styles */
        .divider {
            display: flex;
            align-items: center;
            text-align: center;
            color: #71717a;
            margin: 20px 0;
            font-size: 14px;
        }
        .divider::before, .divider::after {
            content: '';
            flex: 1;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        .divider::before { margin-right: 10px; }
        .divider::after { margin-left: 10px; }

        .social-login {
            display: flex;
            gap: 15px;
            justify-content: center;
        }
        .social-btn {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: #fff;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            transition: 0.3s;
        }
        .social-btn:hover {
            background: rgba(139, 92, 246, 0.2);
            border-color: rgba(139, 92, 246, 0.4);
            transform: translateY(-2px);
        }
"""
content = content.replace("""        .login-btn:hover {
            opacity: 0.9;
            transform: translateY(-2px);
        }""", css_injection)


# Add HTML for social login
html_injection = """
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

        <div class="divider">Or continue with</div>
        <div class="social-login">
            <button class="social-btn" title="Login with Google" onclick="alert('Google Login feature coming soon!')"><ion-icon name="logo-google"></ion-icon></button>
            <button class="social-btn" title="Login with Facebook" onclick="alert('Facebook Login feature coming soon!')"><ion-icon name="logo-facebook"></ion-icon></button>
            <button class="social-btn" title="Login with Twitter/X" onclick="alert('Twitter/X Login feature coming soon!')"><ion-icon name="logo-twitter"></ion-icon></button>
            <button class="social-btn" title="Login with Apple" onclick="alert('Apple Login feature coming soon!')"><ion-icon name="logo-apple"></ion-icon></button>
        </div>
"""
content = re.sub(r'<form id="login-form".*?</form>', html_injection, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Social login buttons added successfully.")
