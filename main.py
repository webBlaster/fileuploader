from flask import request, escape
from config import app

@app.route('/')
def index():
    return "Welcome"

#login route
@app.route('/login', methods=['POST'])
def login():
    email = escape(request.json.get('email'))
    password = escape(request.json.get('password'))
    return "login"

# register route
@app.route('/register', methods=['POST'])
def register():
    username = escape(request.json.get('name'))
    email = escape(request.json.get('email'))
    password = escape(request.json.get('password'))

    return "register"



# Default port:
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)