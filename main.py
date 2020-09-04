from flask import request, escape, render_template, url_for, redirect, jsonify
from config import app
from model.objects import admin, picture

@app.route('/')
def index():
    return render_template('login.html')

#sign in route
@app.route('/signin', methods=['POST','GET'])
def signin():
    email = escape(request.form('email'))
    password = escape(request.form('password'))
    return render_template('login.html')

# register route
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email = escape(request.form('email'))
        password = escape(request.form('password'))
        return render_template('register.html')
    else:
        return render_template('register.html')



# Default port:
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)