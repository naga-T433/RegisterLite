from register_lite import app

@app.route('/')
def index():
    return 'Hellow World!'
