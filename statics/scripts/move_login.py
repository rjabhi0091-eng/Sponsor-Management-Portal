import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

# 1. Read index.html
with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    index_html = f.read()

# 2. Extract the login form HTML from index.html
# We'll use string manipulation to remove the form div.
start_form = '<div class="form">'
end_form = '</div>\n        </div>\n    </div>'

# Find the start index of the form
form_start_idx = index_html.find(start_form)
form_end_idx = index_html.find('</div>\n        </div>\n    </div>', form_start_idx)

if form_start_idx != -1 and form_end_idx != -1:
    # The actual form ends right before the closing divs of the content block.
    # Let's do a more precise extraction or just regex.
    pass

import re
# Regex to match the <div class="form">...</div> correctly.
# The form contains nested divs (<div class="icons">...</div>)
# It's better to just copy the block we know is there.
form_block = """<div class="form">
                <h2>Login Here</h2>
                <form id="spa-login-form">
                    <input type="email" name="email" placeholder="Enter Email Here" required>
                    <input type="password" name="" placeholder="Enter Password Here" required>
                    <button class="btnn" type="submit">Login</button>
                </form>

                <p class="link">Don't have an account?<br>
                <a href="#register">Sign up </a> here</p>
                <p class="liw">Log in with</p>

                <div class="icons">
                    <a href="#"><ion-icon name="logo-facebook"></ion-icon></a>
                    <a href="#"><ion-icon name="logo-instagram"></ion-icon></a>
                    <a href="#"><ion-icon name="logo-twitter"></ion-icon></a>
                    <a href="#"><ion-icon name="logo-google"></ion-icon></a>
                    <a href="#"><ion-icon name="logo-skype"></ion-icon></a>
                </div>
            </div>"""

# Remove form_block from index.html
if form_block in index_html:
    index_html = index_html.replace(form_block, '')
else:
    # Try finding it with spaces collapsed
    print("Could not find exact form_block. Trying regex.")
    index_html = re.sub(r'<div class="form">.*?<div class="icons">.*?</div>\s*</div>', '', index_html, flags=re.DOTALL)

# Add LOGIN link to the navbar in index.html
nav_list_old = """<li><a href="#contact">CONTACT</a></li>
                </ul>"""
nav_list_new = """<li><a href="#contact">CONTACT</a></li>
                    <li><a href="login.html">LOGIN</a></li>
                </ul>"""
index_html = index_html.replace(nav_list_old, nav_list_new)

# Save index.html
with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

# 3. Create login.html
login_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - R-Abhi Tech Solution</title>
    <link rel="stylesheet" href="styles.css">
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
    <style>
        .login-main {
            width: 100%;
            background: linear-gradient(to top, rgba(0,0,0,0.5) 50%, rgba(0,0,0,0.5) 50%), url('https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=1920&q=80');
            background-position: center;
            background-size: cover;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .login-form-container {
            width: 320px;
            background: linear-gradient(to top, rgba(0,0,0,0.8) 50%, rgba(0,0,0,0.8) 50%);
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .login-form-container h2 {
            font-family: sans-serif;
            text-align: center;
            color: #ff7200;
            font-size: 24px;
            background-color: #fff;
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 25px;
        }
        .login-form-container input {
            width: 100%;
            height: 40px;
            background: transparent;
            border: none;
            border-bottom: 1px solid #ff7200;
            color: #fff;
            font-size: 16px;
            margin-bottom: 25px;
        }
        .login-form-container input:focus {
            outline: none;
        }
        .login-form-container .btnn {
            width: 100%;
            height: 45px;
            background: #ff7200;
            border: none;
            font-size: 18px;
            border-radius: 10px;
            cursor: pointer;
            color: #fff;
            font-weight: bold;
            transition: 0.4s ease;
        }
        .login-form-container .btnn:hover {
            background: #fff;
            color: #ff7200;
        }
        .login-form-container .link {
            font-size: 16px;
            padding-top: 20px;
            text-align: center;
            color: #fff;
        }
        .login-form-container .link a {
            text-decoration: none;
            color: #ff7200;
        }
        .login-form-container .liw {
            padding-top: 15px;
            padding-bottom: 10px;
            text-align: center;
            color: #fff;
        }
        .icons {
            display: flex;
            justify-content: center;
            gap: 15px;
        }
        .icons ion-icon {
            color: #fff;
            font-size: 25px;
            transition: 0.3s ease;
        }
        .icons ion-icon:hover {
            color: #ff7200;
        }
        .back-home {
            margin-top: 30px;
            text-decoration: none;
            color: #fff;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .back-home:hover {
            color: #ff7200;
        }
    </style>
</head>
<body>

    <div class="login-main">
        <a href="index.html" class="back-home"><ion-icon name="arrow-back-outline"></ion-icon> Back to Home</a>
        <br>
        <div class="login-form-container">
            <h2>Login Here</h2>
            <form id="spa-login-form">
                <input type="email" name="email" placeholder="Enter Email Here" required>
                <input type="password" name="" placeholder="Enter Password Here" required>
                <button class="btnn" type="submit">Login</button>
            </form>

            <p class="link">Don't have an account?<br>
            <a href="index.html#register">Sign up </a> here</p>
            <p class="liw">Log in with</p>

            <div class="icons">
                <a href="#"><ion-icon name="logo-facebook"></ion-icon></a>
                <a href="#"><ion-icon name="logo-instagram"></ion-icon></a>
                <a href="#"><ion-icon name="logo-twitter"></ion-icon></a>
                <a href="#"><ion-icon name="logo-google"></ion-icon></a>
                <a href="#"><ion-icon name="logo-skype"></ion-icon></a>
            </div>
        </div>
    </div>

    <script src="app.js"></script>
</body>
</html>
"""

with open(os.path.join(base_dir, 'login.html'), 'w', encoding='utf-8') as f:
    f.write(login_html)

print("Moved login form to login.html")
