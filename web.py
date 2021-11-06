from flask import Flask, render_template
from logger import Watcher

app = Flask(__name__)
mylogger = Watcher()
mylogger.run()

@app.route("/")
def render():
    return render_template('logs.html', objects=mylogger.logs())