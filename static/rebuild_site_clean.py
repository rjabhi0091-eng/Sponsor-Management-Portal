import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

# ----------------- HTML CONTENT -----------------

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>R-Abhi Tech Solution</title>
    <link rel="stylesheet" href="styles.css">
    <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
</head>
<body>

    <!-- HERO SECTION (User's Exact Code) -->
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
                </ul>
            </div>

            <div class="search">
                <input class="srch" type="search" name="" placeholder="Type To Search">
                <a href="#"> <button class="btn">Search</button></a>
            </div>
        </div> 

        <div class="content">
            <h1>Sponsor Management & <br><span>Marketing</span> <br>Portal</h1>
            <p class="par">A polished sponsor portal and social media marketing hub for business use.<br> Ready to launch, manage relationships, and drive campaigns.</p>

            <button class="cn"><a href="#about">JOIN US</a></button>

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

    <!-- CLEAN SECTIONS -->
    <div class="sections-wrapper">

        <!-- ABOUT SECTION -->
        <section id="about" class="clean-section">
            <div class="section-container">
                <h2 class="section-title">ABOUT <span>US</span></h2>
                <div class="about-flex">
                    <div class="about-text">
                        <h3>R-ABHI TECH SOLUTION</h3>
                        <p>We are a professional Sponsor Management and Social Media Marketing agency dedicated to helping businesses, startups, events, organizations, influencers, and brands maximize their market presence and business growth.</p>
                        <p>We specialize in sponsorship acquisition, brand partnerships, digital marketing, social media management, content creation, influencer marketing, and event promotions. Our team works strategically to connect brands with the right sponsors and target audiences, ensuring maximum visibility, engagement, and return on investment.</p>
                    </div>
                    <div class="about-cards">
                        <div class="card">
                            <h4>Mission</h4>
                            <p>To empower businesses and brands through innovative sponsorship solutions and result-oriented digital marketing strategies.</p>
                        </div>
                        <div class="card">
                            <h4>Vision</h4>
                            <p>To become one of India's most trusted Sponsor Management and Digital Marketing companies by delivering exceptional service.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- WORK / DASHBOARD SECTION -->
        <section id="work" class="clean-section dark-bg">
            <div class="section-container">
                <h2 class="section-title">PORTAL <span>DASHBOARD</span></h2>
                
                <div class="dashboard-stats">
                    <div class="stat-box">
                        <h3>Total Sponsors</h3>
                        <h2 id="total-sponsors">0</h2>
                    </div>
                    <div class="stat-box">
                        <h3>Total Clients</h3>
                        <h2 id="total-clients">0</h2>
                    </div>
                    <div class="stat-box">
                        <h3>Active Clients</h3>
                        <h2 id="active-clients">0</h2>
                    </div>
                </div>

                <div class="management-panels">
                    <div class="management-box">
                        <h3>Manage Sponsors</h3>
                        <form id="sponsor-form" class="management-form">
                            <input type="hidden" id="sponsor-id" />
                            <input type="text" id="sponsor-name" placeholder="Sponsor Name" required>
                            <input type="email" id="sponsor-email" placeholder="Sponsor Email" required>
                            <input type="text" id="sponsor-phone" placeholder="Sponsor Phone" required>
                            <select id="sponsor-status-select" required>
                                <option value="prospect">Prospect</option>
                                <option value="active">Active</option>
                                <option value="inactive">Inactive</option>
                            </select>
                            <button class="btnn" type="submit">Save Sponsor</button>
                        </form>
                    </div>

                    <div class="management-box">
                        <h3>Manage Clients</h3>
                        <form id="client-form" class="management-form">
                            <input type="hidden" id="client-id" />
                            <input type="text" id="client-name" placeholder="Client Name" required>
                            <input type="email" id="client-email" placeholder="Client Email" required>
                            <input type="text" id="client-company" placeholder="Client Company" required>
                            <select id="client-status-select" required>
                                <option value="active">Active</option>
                                <option value="inactive">Inactive</option>
                                <option value="prospect">Prospect</option>
                            </select>
                            <button class="btnn" type="submit">Save Client</button>
                        </form>
                    </div>
                </div>
            </div>
        </section>

        <!-- MEDIA SECTION -->
        <section id="media" class="clean-section">
            <div class="section-container">
                <h2 class="section-title">MEDIA <span>GALLERY</span></h2>
                <div class="media-grid">
                    <div class="media-item">
                        <img src="https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=400&q=80" alt="Gallery">
                        <h3>Photo Gallery</h3>
                    </div>
                    <div class="media-item">
                        <img src="https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=400&q=80" alt="Videos">
                        <h3>Video Library</h3>
                    </div>
                    <div class="media-item">
                        <img src="https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=400&q=80" alt="Shorts">
                        <h3>Shorts & Clips</h3>
                    </div>
                </div>
            </div>
        </section>

        <!-- CONTACT & REGISTER SECTION -->
        <section id="contact" class="clean-section dark-bg">
            <div class="section-container">
                <div class="contact-register-flex">
                    
                    <div class="contact-box" id="register">
                        <h2 class="section-title">REGISTER <span>NOW</span></h2>
                        <form id="register-sponsor-form" class="management-form">
                            <input type="text" id="register-sponsor-name" placeholder="Name" required>
                            <input type="email" id="register-sponsor-email" placeholder="Email" required>
                            <input type="text" id="register-sponsor-phone" placeholder="Phone" required>
                            <input type="password" id="register-sponsor-password" placeholder="Password" required>
                            <button class="btnn" type="submit">Register Account</button>
                        </form>
                    </div>

                    <div class="contact-box">
                        <h2 class="section-title">CONTACT <span>US</span></h2>
                        <p class="contact-info"><strong>Email:</strong> rjabhi0091@gmail.com</p>
                        <p class="contact-info"><strong>Phone:</strong> +91 93350-49370</p>
                        <p class="contact-info"><strong>Office:</strong> New Delhi, India</p>
                        
                        <form id="contact-form" class="management-form" style="margin-top: 20px;">
                            <input type="text" id="contact-name" placeholder="Your Name" required>
                            <input type="email" id="contact-email" placeholder="Your Email" required>
                            <textarea id="contact-message-input" placeholder="Your Message" rows="3" required></textarea>
                            <button class="btnn" type="submit">Send Message</button>
                        </form>
                    </div>

                </div>
            </div>
        </section>

        <footer>
            <p>Built for Sponsor Portfolio Management. Powered by R-Abhi Tech Solution.</p>
        </footer>
    </div>

    <script src="app.js"></script>
</body>
</html>
"""

# ----------------- CSS CONTENT -----------------

css_content = """/* RESET AND BASE */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: #121212;
    color: #fff;
    overflow-x: hidden;
}

html {
    scroll-behavior: smooth;
}

/* ---------------- HERO SECTION (User's Exact Code CSS) ---------------- */
.main {
    width: 100%;
    background: linear-gradient(to top, rgba(0,0,0,0.5) 50%, rgba(0,0,0,0.5) 50%), url('https://images.unsplash.com/photo-1519681393784-d120267933ba?auto=format&fit=crop&w=1920&q=80');
    background-position: center;
    background-size: cover;
    min-height: 100vh;
    position: relative;
}

.navbar {
    width: 1200px;
    max-width: 90%;
    height: 75px;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.icon {
    width: 200px;
}

.logo {
    color: #ff7200;
    font-size: 35px;
    font-family: Arial;
}

.menu ul {
    display: flex;
}

.menu ul li {
    list-style: none;
    margin-left: 40px;
    font-size: 14px;
}

.menu ul li a {
    text-decoration: none;
    color: #fff;
    font-weight: bold;
    transition: 0.4s ease-in-out;
}

.menu ul li a:hover {
    color: #ff7200;
}

.search {
    display: flex;
    align-items: center;
}

.srch {
    font-family: 'Times New Roman';
    width: 200px;
    height: 40px;
    background: transparent;
    border: 1px solid #ff7200;
    color: #fff;
    border-right: none;
    font-size: 16px;
    padding: 10px;
    border-bottom-left-radius: 5px;
    border-top-left-radius: 5px;
}

.btn {
    width: 100px;
    height: 40px;
    background: #ff7200;
    border: 2px solid #ff7200;
    color: #fff;
    font-size: 15px;
    border-bottom-right-radius: 5px;
    border-top-right-radius: 5px;
    transition: 0.2s ease;
    cursor: pointer;
}

.btn:hover {
    color: #000;
}

.btn:focus, .srch:focus {
    outline: none;
}

.content {
    width: 1200px;
    max-width: 90%;
    margin: auto;
    color: #fff;
    position: relative;
    padding-top: 50px;
}

.content h1 {
    font-family: 'Times New Roman';
    font-size: 50px;
    letter-spacing: 2px;
}

.content span {
    color: #ff7200;
    font-size: 65px;
}

.content .par {
    padding-bottom: 25px;
    font-family: Arial;
    letter-spacing: 1.2px;
    line-height: 30px;
    margin-top: 10px;
}

.content .cn {
    width: 160px;
    height: 40px;
    background: #ff7200;
    border: none;
    font-size: 18px;
    border-radius: 10px;
    cursor: pointer;
    transition: .4s ease;
}

.content .cn a {
    text-decoration: none;
    color: #000;
    transition: .3s ease;
    font-weight: bold;
}

.cn:hover {
    background-color: #fff;
}

.form {
    width: 280px;
    height: 420px;
    background: linear-gradient(to top, rgba(0,0,0,0.8) 50%, rgba(0,0,0,0.8) 50%);
    position: absolute;
    top: 50px;
    right: 0;
    border-radius: 10px;
    padding: 25px;
}

.form h2 {
    font-family: sans-serif;
    text-align: center;
    color: #ff7200;
    font-size: 22px;
    background-color: #fff;
    border-radius: 10px;
    padding: 8px;
    margin-bottom: 20px;
}

.form input {
    width: 100%;
    height: 35px;
    background: transparent;
    border: none;
    border-bottom: 1px solid #ff7200;
    color: #fff;
    font-size: 15px;
    letter-spacing: 1px;
    margin-bottom: 20px;
    font-family: sans-serif;
}

.form input:focus {
    outline: none;
}

::placeholder {
    color: #fff;
}

.btnn {
    width: 100%;
    height: 40px;
    background: #ff7200;
    border: none;
    font-size: 18px;
    border-radius: 10px;
    cursor: pointer;
    color: #fff;
    transition: 0.4s ease;
    font-weight: bold;
}

.btnn:hover {
    background: #fff;
    color: #ff7200;
}

.form .link {
    font-size: 16px;
    padding-top: 15px;
    text-align: center;
}

.form .link a {
    text-decoration: none;
    color: #ff7200;
}

.liw {
    padding-top: 15px;
    padding-bottom: 10px;
    text-align: center;
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


/* ---------------- NEW CLEAN SECTIONS ---------------- */

.sections-wrapper {
    background-color: #121212;
}

.clean-section {
    padding: 80px 5%;
}

.dark-bg {
    background-color: #1a1a1a;
}

.section-container {
    max-width: 1200px;
    margin: 0 auto;
}

.section-title {
    font-size: 36px;
    text-align: center;
    margin-bottom: 50px;
    letter-spacing: 2px;
}

.section-title span {
    color: #ff7200;
}

/* ABOUT SECTION */
.about-flex {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
}

.about-text {
    flex: 1;
    min-width: 300px;
}

.about-text h3 {
    font-size: 24px;
    color: #ff7200;
    margin-bottom: 20px;
}

.about-text p {
    line-height: 1.8;
    color: #ccc;
    margin-bottom: 15px;
}

.about-cards {
    flex: 1;
    min-width: 300px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.card {
    background: #222;
    padding: 30px;
    border-left: 4px solid #ff7200;
    border-radius: 5px;
}

.card h4 {
    font-size: 20px;
    margin-bottom: 10px;
    color: #ff7200;
}

.card p {
    color: #ccc;
    line-height: 1.6;
}

/* WORK / DASHBOARD SECTION */
.dashboard-stats {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 50px;
    flex-wrap: wrap;
}

.stat-box {
    flex: 1;
    background: #222;
    padding: 30px;
    text-align: center;
    border-radius: 10px;
    border-bottom: 4px solid #ff7200;
}

.stat-box h3 {
    font-size: 18px;
    color: #ccc;
    margin-bottom: 10px;
}

.stat-box h2 {
    font-size: 40px;
    color: #ff7200;
}

.management-panels {
    display: flex;
    gap: 30px;
    flex-wrap: wrap;
}

.management-box {
    flex: 1;
    background: #222;
    padding: 30px;
    border-radius: 10px;
    min-width: 300px;
}

.management-box h3 {
    color: #ff7200;
    margin-bottom: 20px;
    font-size: 22px;
}

.management-form input,
.management-form select,
.management-form textarea {
    width: 100%;
    padding: 12px;
    background: #121212;
    border: 1px solid #333;
    color: #fff;
    margin-bottom: 15px;
    border-radius: 5px;
}

.management-form input:focus,
.management-form select:focus,
.management-form textarea:focus {
    outline: none;
    border-color: #ff7200;
}

/* MEDIA SECTION */
.media-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.media-item {
    background: #222;
    border-radius: 10px;
    overflow: hidden;
}

.media-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-bottom: 3px solid #ff7200;
}

.media-item h3 {
    padding: 20px;
    text-align: center;
}

/* CONTACT & REGISTER SECTION */
.contact-register-flex {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
}

.contact-box {
    flex: 1;
    min-width: 300px;
    background: #222;
    padding: 40px;
    border-radius: 10px;
}

.contact-info {
    font-size: 16px;
    color: #ccc;
    margin-bottom: 10px;
}

footer {
    text-align: center;
    padding: 30px;
    background: #111;
    color: #666;
    border-top: 1px solid #222;
}
"""

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(os.path.join(base_dir, 'styles.css'), 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Rebuilt index.html and styles.css cleanly from scratch")
