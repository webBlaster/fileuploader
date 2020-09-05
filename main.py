from flask import request, escape, render_template, url_for, redirect, jsonify, flash
from config import app
from model.objects import admin, picture
import os
@app.route('/')
def index():
    return render_template('login.html')

#sign out route
@app.route('/signout', methods=['GET'])
def signout():
        result = admin.logout()
        if result['logged'] == False:
            flash(result['message'])
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

#sign in route
@app.route('/signin', methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        email = escape(request.form['email'])
        password = escape(request.form['password'])
        result = admin.login(email, password)
        if result['logged'] == True:
            flash(result['message'])
            return render_template('dashboard.html')
        else:
            flash(result['message'])
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

# register route
@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email = escape(request.form['email'])
        password = escape(request.form['password'])
        result = admin.signup(email, password)
        if result['registered'] == True:
            flash(result['message'])
            return redirect(url_for('index'))
        else:
            flash(result['message'])
            return render_template('register.html')
    else:
        return render_template('register.html')

# dashboard route
@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    if request.method == 'POST':
        return render_template('dashboard.html')
    else:
        result = admin.auth_status()
        if result['logged'] == True:
            return render_template('dashboard.html')
        else:
            return redirect(url_for('index'))

# Default port:
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.debug = True
    app.run(host='0.0.0.0', port=port)