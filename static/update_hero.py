import re
import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'
index_path = os.path.join(base_dir, 'index.html')

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The user's requested HTML for the hero section
user_html = """
    <div class="main" id="home">
        <div class="navbar">
            <div class="icon">
                <h2 class="logo">PraRoz</h2>
            </div>

            <div class="menu">
                <ul>
                    <li><a href="#home">HOME</a></li>
                    <li><a href="#about">ABOUT</a></li>
                    <li><a href="#work">WORK</a></li>
                    <li><a href="#media">MEDIA</a></li>
                    <li><a href="#contact">CONTACT</a></li>
                    <li><a href="/admin">ADMIN</a></li>
                </ul>
            </div>

            <div class="search">
                <input class="srch" type="search" name="" placeholder="Type To text">
                <a href="#"> <button class="btn">Search</button></a>
            </div>
        </div> 

        <div class="content">
            <h1>Web Design & <br><span>Development</span> <br>Course</h1>
            <p class="par">Lorem ipsum dolor sit amet consectetur adipisicing elit. <br> Suscipit fugit animi iusto, temporibus voluptatum laboriosam distinctio, <br> quasi unde alias facilis sequi. Aut debitis voluptatibus quas?</p>

            <button class="cn"><a href="#">JOIN US</a></button>

            <div class="form">
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
            </div>
        </div>
    </div>
"""

# Replace everything from <div class="spa-bg"> to </div> </div> before <div class="spa-content-sections">
pattern = r'<div class="spa-bg"></div>.*?</div>\s*</div>\s*</div>'
new_content = re.sub(pattern, user_html, content, flags=re.DOTALL)

# Add ionicons script to head if not present
if "ionicons.js" not in new_content:
    new_content = new_content.replace('</head>', '  <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>\n  <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>\n</head>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html with user's HTML code")
