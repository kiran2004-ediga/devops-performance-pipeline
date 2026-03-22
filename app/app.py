from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps Pipeline!"

@app.route("/load")
def load():
    time.sleep(2)
    return "This endpoint simulates load"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)