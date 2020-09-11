from app import app

@app.route("/")
def index():
    return "Hello World"

@app.route("/aisa")
def hello():
    return "Hello, Aisa"
