from flask import Flask, send_from_directory, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory('static', 'index.html')


@app.route('/<path:path>')
def catch_all(path):
    return redirect('https://twitter.com/' + path, code=301)
