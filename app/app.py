from flask import Flask, render_template_string
import time

app = Flask(__name__)

# Simple styled HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Performance Pipeline</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #1f4037, #99f2c8);
            color: white;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: rgba(0,0,0,0.3);
            padding: 30px;
            border-radius: 12px;
            display: inline-block;
        }
        h1 {
            margin-bottom: 10px;
        }
        p {
            font-size: 18px;
        }
        .btn {
            margin-top: 20px;
            padding: 10px 20px;
            background: #00c6ff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover {
            background: #0072ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 DevOps Performance Pipeline</h1>
        <p>This app is used for performance testing using JMeter, Prometheus, and Grafana.</p>
        <button class="btn" onclick="window.location.href='/load'">
            Test Load Endpoint
        </button>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/load")
def load():
    time.sleep(2)
    return "<h2 style='text-align:center;'>⏳ Load endpoint executed successfully!</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)