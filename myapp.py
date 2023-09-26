import time
from flask import Flask

app = Flask(__name__)

@app.route("/") # this route is working
def index():
    data = b"Hello, World after 10 seconds!\n"
    time.sleep(10)
    return data

@app.route("/status")
def status():
    return "Status right away!"
