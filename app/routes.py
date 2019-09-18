from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello,Juanzhi,this is a test!"