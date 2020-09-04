from flask import request, escape, render_template, url_for, redirect, jsonify
from config import app
from model.objects import admin, picture

@app.route('/')
def index():
    return render_template('dashboard.html')

#sign in route
@app.route('/signin', methods=['POST','GET'])
def login():
    email = escape(request.json.get('email'))
    password = escape(request.json.get('password'))
    return "signin"

# register route
@app.route('/register', methods=['POST','GET'])
def register():
    email = escape(request.json.get('email'))
    password = escape(request.json.get('password'))

    return "register"



# Default port:
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)