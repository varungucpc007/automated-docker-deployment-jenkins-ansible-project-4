from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Pipeline | Automated Deployment</title>
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
            padding: 20px;
            position: relative;
            overflow-x: hidden;
        }

        /* Animated background effect */
        body::before {
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: moveBackground 20s linear infinite;
            pointer-events: none;
        }

        @keyframes moveBackground {
            0% {
                transform: translate(0, 0);
            }
            100% {
                transform: translate(50px, 50px);
            }
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
            max-width: 1200px;
            width: 100%;
            transform: translateY(0);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: slideIn 0.6s ease-out;
            position: relative;
            z-index: 1;
        }

        .container:hover {
            transform: translateY(-5px);
            box-shadow: 0 25px 70px rgba(0, 0, 0, 0.4);
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
        }

        .header h1 {
            color: white;
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            position: relative;
            z-index: 1;
        }

        .tech-stack {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
            flex-wrap: wrap;
            position: relative;
            z-index: 1;
        }

        .tech-badge {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            padding: 8px 20px;
            border-radius: 20px;
            color: white;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            cursor: default;
        }

        .tech-badge:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.05);
        }

        .content {
            padding: 50px;
            text-align: center;
        }

        .main-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 30px;
            animation: fadeInUp 0.8s ease-out 0.2s both;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .description {
            color: #555;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 40px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            animation: fadeInUp 0.8s ease-out 0.4s both;
        }

        .pipeline-steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 40px;
            animation: fadeInUp 0.8s ease-out 0.6s both;
        }

        .step {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 25px;
            border-radius: 15px;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .step::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            transition: left 0.5s ease;
        }

        .step:hover::before {
            left: 100%;
        }

        .step:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        .step-icon {
            font-size: 3rem;
            margin-bottom: 15px;
        }

        .step h3 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1.3rem;
        }

        .step p {
            color: #666;
            font-size: 0.9rem;
            line-height: 1.4;
        }

        .status-badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px 25px;
            border-radius: 25px;
            font-weight: 600;
            margin-top: 20px;
            animation: pulse 2s infinite;
            cursor: default;
        }

        @keyframes pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.8;
            }
        }

        .footer {
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
            border-top: 1px solid #e0e0e0;
        }

        @media (max-width: 768px) {
            .main-message {
                font-size: 1.5rem;
            }
            
            .content {
                padding: 30px 20px;
            }
            
            .pipeline-steps {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 1.8rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 CI/CD Pipeline Automation</h1>
            <div class="tech-stack">
                <span class="tech-badge">🐳 Docker</span>
                <span class="tech-badge">🔧 Jenkins</span>
                <span class="tech-badge">📦 Ansible</span>
                <span class="tech-badge">🐙 GitHub</span>
                <span class="tech-badge">☁️ Docker Hub</span>
                <span class="tech-badge">🐍 Flask</span>
            </div>
        </div>
        
        <div class="content">
            <div class="main-message">
                Automated Docker Deployment
            </div>
            
            <div class="description">
                Experience fully automated CI/CD pipeline with seamless integration of 
                Jenkins, Ansible, GitHub, and Docker Hub for efficient application deployment.
            </div>
            
            <div class="pipeline-steps">
                <div class="step">
                    <div class="step-icon">📝</div>
                    <h3>GitHub Push</h3>
                    <p>Developer pushes code to GitHub repository triggering the pipeline</p>
                </div>
                
                <div class="step">
                    <div class="step-icon">⚙️</div>
                    <h3>Jenkins Build</h3>
                    <p>Jenkins automatically detects changes and initiates build process</p>
                </div>
                
                <div class="step">
                    <div class="step-icon">🐳</div>
                    <h3>Docker Build</h3>
                    <p>Creates optimized Docker image with all dependencies</p>
                </div>
                
                <div class="step">
                    <div class="step-icon">📤</div>
                    <h3>Docker Hub Push</h3>
                    <p>Pushes the built image to Docker Hub registry</p>
                </div>
                
                <div class="step">
                    <div class="step-icon">🔄</div>
                    <h3>Ansible Deploy</h3>
                    <p>Ansible automates deployment across target servers</p>
                </div>
                
                <div class="step">
                    <div class="step-icon">✅</div>
                    <h3>Live Application</h3>
                    <p>Application successfully deployed and accessible</p>
                </div>
            </div>
            
            <div class="status-badge">
                🟢 Pipeline Active | Version 1.0.0
            </div>
        </div>
        
        <div class="footer">
            <p>⚡ Fully Automated CI/CD Pipeline | Jenkins + Ansible + GitHub + Docker Hub | Continuous Deployment Ready</p>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 30px 30px;
            transform: rotate(45deg);
            pointer-events: none;
            to {
                opacity: 1;

        .header::before {
            content: '';
            padding: 30px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
                transform: translateY(0);
            }
        }

        .header {

