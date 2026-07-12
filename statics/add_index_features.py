import re

filepath_html = 'd:/WebPortal/Sponsor-Management-Portal/static/index.html'
filepath_css = 'd:/WebPortal/Sponsor-Management-Portal/static/style.css'

# 1. Update style.css
with open(filepath_css, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Floating Actions (Back to Top & Chat) */
.floating-actions {
    position: fixed;
    bottom: 30px;
    right: 30px;
    display: flex;
    flex-direction: column;
    gap: 15px;
    z-index: 1000;
}
.float-btn {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    color: #fff;
    border: none;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    transition: 0.3s;
    opacity: 0;
    visibility: hidden;
    transform: translateY(20px);
}
.float-btn.show {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}
.float-btn:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(139, 92, 246, 0.4);
}
.chat-btn {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}
"""
css += new_css

with open(filepath_css, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html
with open(filepath_html, 'r', encoding='utf-8') as f:
    html = f.read()

html_injection = """
    <!-- Floating Actions -->
    <div class="floating-actions">
        <button class="float-btn" id="backToTop" onclick="window.scrollTo({top: 0, behavior: 'smooth'})" title="Back to Top">
            <ion-icon name="arrow-up-outline"></ion-icon>
        </button>
        <button class="float-btn chat-btn" onclick="alert('Live chat support connecting...')" title="Live Chat Support">
            <ion-icon name="chatbubbles-outline"></ion-icon>
        </button>
    </div>

    <script>
        // Back to Top Logic
        window.addEventListener('scroll', () => {
            const btn = document.getElementById('backToTop');
            if (window.scrollY > 300) {
                btn.classList.add('show');
            } else {
                btn.classList.remove('show');
            }
        });
    </script>
</body>
"""

html = html.replace("</body>", html_injection)

with open(filepath_html, 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated with latest features successfully.")
