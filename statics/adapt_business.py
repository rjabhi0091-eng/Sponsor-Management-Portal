import os

base_dir = 'd:/WebPortal/Sponsor-Management-Portal/static'

index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>R-Abhi Tech Solution - Sponsor Management</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>

    <section class="header" id="home">
        <nav>
            <a href="index.html" style="color:#fff; text-decoration:none; font-size:24px; font-weight:bold; letter-spacing:2px;">R-ABHI <span style="color:#f44336;">TECH</span></a>
            <div class="nav-links" id="navLinks">
                <i class="fa fa-times" onclick="hideMenu()"></i>
                <ul>
                    <li><a href="#home">HOME</a></li>
                    <li><a href="#services">SERVICES</a></li>
                    <li><a href="#dashboard">DASHBOARD</a></li>
                    <li><a href="#testimonials">CLIENTS</a></li>
                    <li><a href="login.html">LOGIN</a></li>
                    <li><a href="admin.html">ADMIN</a></li>
                </ul>
            </div>
            <i class="fa fa-bars" onclick="showMenu()"></i>
        </nav>

        <div class="text-box">
            <h1>Premier Sponsor & Client Management Portal</h1>
            <p>Empowering businesses, startups, and influencers with top-tier sponsorship opportunities and <br>powerful digital marketing strategies for explosive growth.</p>
            <a href="#dashboard" class="hero-btn">Go To Dashboard</a>
        </div>
    </section>

    <!-- Services Section -->
    <section class="course" id="services">
        <h1>Our Core Services</h1>
        <p>Comprehensive solutions designed to elevate your brand and connect you with the right partners.</p>

        <div class="row">
            <div class="course-col">
                <h3>Sponsor Management</h3>
                <p>We handle everything from pitching to closing deals. Secure the best sponsorships for your events, campaigns, and organizational goals.</p>
            </div>
            <div class="course-col">
                <h3>Client Acquisition</h3>
                <p>Build and maintain a robust client portfolio. We help you attract, manage, and retain high-value clients through targeted strategies.</p>
            </div>
            <div class="course-col">
                <h3>Social Media Marketing</h3>
                <p>Boost your digital footprint with data-driven social media campaigns. Turn followers into active clients and maximize engagement.</p>
            </div>
        </div>
    </section>

    <!-- Dashboard Section -->
    <section class="campus" id="dashboard">
        <h1>Management Dashboard</h1>
        <p>Add and manage your Sponsors and Clients seamlessly from this interface.</p>

        <!-- Stats Overview -->
        <div class="stats-row">
            <div class="stat-box">
                <h3>Total Sponsors</h3>
                <h1 id="total-sponsors">0</h1>
            </div>
            <div class="stat-box">
                <h3>Total Clients</h3>
                <h1 id="total-clients">0</h1>
            </div>
            <div class="stat-box">
                <h3>Active Clients</h3>
                <h1 id="active-clients">0</h1>
            </div>
        </div>

        <div class="row" style="align-items: stretch;">
            <!-- Sponsor Form -->
            <div class="management-col">
                <h3>Manage Sponsors</h3>
                <form id="sponsor-form" class="mgmt-form">
                    <input type="hidden" id="sponsor-id" />
                    <input type="text" id="sponsor-name" placeholder="Sponsor Name" required>
                    <input type="email" id="sponsor-email" placeholder="Email Address" required>
                    <input type="text" id="sponsor-phone" placeholder="Phone Number" required>
                    <select id="sponsor-status-select" required>
                        <option value="prospect">Prospect</option>
                        <option value="active">Active</option>
                        <option value="inactive">Inactive</option>
                    </select>
                    <button type="submit" class="hero-btn red-btn">Save Sponsor</button>
                </form>
            </div>

            <!-- Client Form -->
            <div class="management-col">
                <h3>Manage Clients</h3>
                <form id="client-form" class="mgmt-form">
                    <input type="hidden" id="client-id" />
                    <input type="text" id="client-name" placeholder="Client Name" required>
                    <input type="email" id="client-email" placeholder="Email Address" required>
                    <input type="text" id="client-company" placeholder="Company/Brand" required>
                    <select id="client-status-select" required>
                        <option value="active">Active</option>
                        <option value="inactive">Inactive</option>
                        <option value="prospect">Prospect</option>
                    </select>
                    <button type="submit" class="hero-btn red-btn">Save Client</button>
                </form>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="testimonials" id="testimonials">
        <h1>What Our Clients Say</h1>
        <p>Real feedback from businesses and influencers who trust us.</p>

        <div class="row">
            <div class="testimonial-col">
                <img src="images/user1.jpg" alt="User" onerror="this.src='https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=150&q=80'">
                <div>
                    <p>"R-ABHI TECH SOLUTION completely transformed our sponsorship acquisition strategy. We secured three major brand deals in our first quarter."</p>
                    <h3>Christine Berkley</h3>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star-o"></i>
                </div>
            </div>
            <div class="testimonial-col">
                <img src="images/user2.jpg" alt="User" onerror="this.src='https://images.unsplash.com/photo-1599566150163-29194dcaad36?auto=format&fit=crop&w=150&q=80'">
                <div>
                    <p>"The client management portal is a game changer. It is so easy to track prospects and manage active client relationships."</p>
                    <h3>David Wood</h3>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star"></i>
                    <i class="fa fa-star-half-o"></i>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="cta">
        <h1>Ready to elevate your brand presence <br>and secure premium sponsors?</h1>
        <a href="login.html#register" class="hero-btn">REGISTER NOW</a>
    </section>

    <!-- Footer -->
    <section class="footer">
        <h4>About R-ABHI TECH SOLUTION</h4>
        <p>We are a leading Sponsor Management and Social Media Marketing agency dedicated to helping businesses,<br> startups, and organizations maximize their market presence and business growth.</p>
        <div class="icons">
            <i class="fa fa-facebook"></i>
            <i class="fa fa-twitter"></i>
            <i class="fa fa-instagram"></i>
            <i class="fa fa-linkedin"></i>
        </div>
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

css_additions = """

/* --- Management Dashboard Extensions --- */
.stats-row {
    display: flex;
    justify-content: space-between;
    width: 80%;
    margin: 40px auto;
    gap: 20px;
}
.stat-box {
    flex-basis: 31%;
    background: #fff3f3;
    padding: 30px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
.stat-box h1 {
    font-size: 48px;
    color: #f44336;
    margin-top: 10px;
}
.management-col {
    flex-basis: 48%;
    background: #fff;
    border-radius: 10px;
    padding: 40px;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
    text-align: left;
}
.management-col h3 {
    margin-bottom: 20px;
    color: #333;
    font-size: 24px;
}
.mgmt-form input,
.mgmt-form select {
    width: 100%;
    padding: 12px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-family: 'Poppins', sans-serif;
    font-size: 14px;
}
.red-btn {
    border: 1px solid #f44336;
    background: #f44336;
    color: #fff;
    width: 100%;
    text-align: center;
}
.red-btn:hover {
    background: #fff;
    color: #f44336;
}

@media(max-width: 700px){
    .stats-row {
        flex-direction: column;
    }
}
"""

with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

with open(os.path.join(base_dir, 'style.css'), 'a', encoding='utf-8') as f:
    f.write(css_additions)

print("Re-adapted the University Template into the Business Website.")
