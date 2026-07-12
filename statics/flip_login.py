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

        /* Flip Container */
        .scene {
            width: 380px;
            height: 520px;
            perspective: 1000px;
        }

        .card {
            width: 100%;
            height: 100%;
            position: relative;
            transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            transform-style: preserve-3d;
        }

        .card.is-flipped {
            transform: rotateY(180deg);
        }

        .card-face {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            background: rgba(24, 24, 27, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.5);
            padding: 40px 30px;
            display: flex;
            flex-direction: column;
            box-sizing: border-box;
        }

        .card-face-back {
            transform: rotateY(180deg);
        }

        .card-face h2 {
            margin-top: 0;
            font-size: 24px;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-bottom: 30px;
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

        .switch-btn {
            margin-top: auto;
            background: none;
            border: none;
            color: #a1a1aa;
            cursor: pointer;
            font-size: 14px;
            transition: 0.3s;
        }

        .switch-btn:hover {
            color: #8b5cf6;
            text-decoration: underline;
        }

        .admin-link {
            position: absolute;
            bottom: 30px;
            color: #71717a;
            text-decoration: none;
            font-size: 14px;
            transition: 0.3s;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .admin-link:hover {
            color: #f43f5e;
        }
    </style>
</head>
<body>

    <a href="index.html" class="back-home"><ion-icon name="arrow-back-outline"></ion-icon> Back to Home</a>

    <div class="scene">
        <div class="card" id="flip-card">
            
            <!-- Front Face: Sponsor Login -->
            <div class="card-face card-face-front">
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
                    <button type="submit" class="login-btn">Login</button>
                </form>
                <button class="switch-btn" onclick="flipCard()">Not a sponsor? Login as Client</button>
            </div>

            <!-- Back Face: Client Login -->
            <div class="card-face card-face-back">
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
                    <button type="submit" class="login-btn">Login</button>
                </form>
                <button class="switch-btn" onclick="flipCard()">Not a client? Login as Sponsor</button>
            </div>

        </div>
    </div>

    <!-- Admin Link at bottom -->
    <a href="admin.html" class="admin-link"><ion-icon name="shield-checkmark-outline"></ion-icon> Admin Access (Secret)</a>

    <script>
        function flipCard() {
            var card = document.getElementById('flip-card');
            card.classList.toggle('is-flipped');
        }
    </script>
</body>
</html>
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("login.html updated with 3D Flip effect successfully.")
