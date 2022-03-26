from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_view():
		return "<h1>This app is useless. You can press the button.</h1><button>Press it!</button>"
