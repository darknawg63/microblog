from app import app

@app.route('/')
@app.route('/index/')
def index():
	greeting = {"greet" :"Hello, World!"}
    return greeting['greet']