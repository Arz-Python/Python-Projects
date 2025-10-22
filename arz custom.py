<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arz - Python Developer</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            width: 90%;
            padding: 40px;
        }

        .hero {
            text-align: center;
            margin-bottom: 60px;
            animation: fadeInDown 1s ease-out;
        }

        .logo {
            font-size: 80px;
            font-weight: bold;
            color: #fff;
            text-shadow: 0 0 20px rgba(255, 255, 255, 0.5),
                         0 0 40px rgba(255, 255, 255, 0.3);
            margin-bottom: 20px;
            animation: glow 2s ease-in-out infinite alternate;
            letter-spacing: 15px;
        }

        .tagline {
            font-size: 24px;
            color: #fff;
            margin-bottom: 10px;
            animation: fadeIn 1.5s ease-out;
        }

        .subtitle {
            font-size: 18px;
            color: rgba(255, 255, 255, 0.8);
            animation: fadeIn 2s ease-out;
        }

        .python-badge {
            display: inline-block;
            background: linear-gradient(135deg, #3776ab 0%, #ffd343 100%);
            color: white;
            padding: 15px 30px;
            border-radius: 50px;
            font-weight: bold;
            font-size: 20px;
            margin: 30px 0;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            animation: bounce 2s infinite;
        }

        .skills {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }

        .skill-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: fadeInUp 1s ease-out;
            border: 2px solid rgba(255, 255, 255, 0.2);
        }

        .skill-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
            background: rgba(255, 255, 255, 0.2);
        }

        .skill-icon {
            font-size: 50px;
            margin-bottom: 15px;
        }

        .skill-title {
            color: #fff;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .skill-desc {
            color: rgba(255, 255, 255, 0.8);
            font-size: 14px;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 50px;
            animation: fadeInUp 1.5s ease-out;
        }

        .social-btn {
            display: flex;
            align-items: center;
            gap: 15px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            color: white;
            text-decoration: none;
            padding: 20px 40px;
            border-radius: 50px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s ease;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .social-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.1);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .social-icon {
            font-size: 30px;
        }

        .youtube {
            background: linear-gradient(135deg, #FF0000 0%, #CC0000 100%);
        }

        .discord {
            background: linear-gradient(135deg, #7289DA 0%, #5B6EAE 100%);
        }

        .floating-shapes {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .shape {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: float 20s infinite ease-in-out;
        }

        .shape1 {
            width: 100px;
            height: 100px;
            top: 10%;
            left: 10%;
            animation-delay: 0s;
        }

        .shape2 {
            width: 150px;
            height: 150px;
            top: 60%;
            right: 10%;
            animation-delay: 2s;
        }

        .shape3 {
            width: 80px;
            height: 80px;
            bottom: 20%;
            left: 20%;
            animation-delay: 4s;
        }

        .code-snippet {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px;
            padding: 20px;
            margin: 30px auto;
            max-width: 600px;
            text-align: left;
            font-family: 'Courier New', monospace;
            color: #00ff00;
            font-size: 14px;
            animation: typing 3s steps(40) infinite;
            overflow: hidden;
            white-space: nowrap;
            border-left: 4px solid #00ff00;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes glow {
            from {
                text-shadow: 0 0 20px rgba(255, 255, 255, 0.5),
                            0 0 40px rgba(255, 255, 255, 0.3);
            }
            to {
                text-shadow: 0 0 30px rgba(255, 255, 255, 0.8),
                            0 0 60px rgba(255, 255, 255, 0.5),
                            0 0 80px rgba(255, 255, 255, 0.3);
            }
        }

        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            50% {
                transform: translateY(-30px) rotate(180deg);
            }
        }

        @keyframes typing {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }

        @media (max-width: 768px) {
            .logo {
                font-size: 50px;
                letter-spacing: 8px;
            }

            .tagline {
                font-size: 20px;
            }

            .social-links {
                flex-direction: column;
                align-items: center;
            }

            .skill-card {
                margin-bottom: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="floating-shapes">
        <div class="shape shape1"></div>
        <div class="shape shape2"></div>
        <div class="shape shape3"></div>
    </div>

    <div class="container">
        <div class="hero">
            <div class="logo">ARZ</div>
            <div class="tagline">Professional Python Developer</div>
            <div class="subtitle">Building powerful solutions with clean code</div>
            <div class="python-badge">🐍 Python Expert</div>
        </div>

        <div class="code-snippet">
            >> print("Hello, I'm Arz - Your Python Specialist!")
        </div>

        <div class="skills">
            <div class="skill-card" style="animation-delay: 0.2s">
                <div class="skill-icon">🐍</div>
                <div class="skill-title">Python Mastery</div>
                <div class="skill-desc">Expert in Python programming with advanced knowledge in automation, data structures, and algorithm optimization</div>
            </div>

            <div class="skill-card" style="animation-delay: 0.4s">
                <div class="skill-icon">🤖</div>
                <div class="skill-title">Automation</div>
                <div class="skill-desc">Creating efficient automated solutions and scripts to streamline workflows and boost productivity</div>
            </div>

            <div class="skill-card" style="animation-delay: 0.6s">
                <div class="skill-icon">💻</div>
                <div class="skill-title">GUI Development</div>
                <div class="skill-desc">Building intuitive desktop applications with Tkinter and modern user interfaces</div>
            </div>

            <div class="skill-card" style="animation-delay: 0.8s">
                <div class="skill-icon">📊</div>
                <div class="skill-title">Data Processing</div>
                <div class="skill-desc">Analyzing and processing data with Python libraries for meaningful insights</div>
            </div>

            <div class="skill-card" style="animation-delay: 1s">
                <div class="skill-icon">🔧</div>
                <div class="skill-title">Problem Solving</div>
                <div class="skill-desc">Tackling complex challenges with elegant and efficient Python solutions</div>
            </div>

            <div class="skill-card" style="animation-delay: 1.2s">
                <div class="skill-icon">🚀</div>
                <div class="skill-title">Innovation</div>
                <div class="skill-desc">Constantly learning and implementing cutting-edge Python technologies</div>
            </div>
        </div>

        <div class="social-links">
            <a href="YOUR_YOUTUBE_LINK_HERE" target="_blank" class="social-btn youtube">
                <span class="social-icon">▶️</span>
                <span>YouTube Channel</span>
            </a>
            <a href="YOUR_DISCORD_LINK_HERE" target="_blank" class="social-btn discord">
                <span class="social-icon">💬</span>
                <span>Discord Server</span>
            </a>
        </div>
    </div>

    <script>
        // Add smooth scroll effect
        document.querySelectorAll('.social-btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                this.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    this.style.transform = 'scale(1.1)';
                }, 100);
            });
        });

        // Random shape animation
        const shapes = document.querySelectorAll('.shape');
        shapes.forEach(shape => {
            setInterval(() => {
                const randomX = Math.random() * 100;
                const randomY = Math.random() * 100;
                shape.style.left = randomX + '%';
                shape.style.top = randomY + '%';
            }, 8000);
        });
    </script>
</body>
</html>
