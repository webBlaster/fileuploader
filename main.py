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
        result = admin.auth_status()
        if result['logged'] == False:
            flash(result['message'])
            return redirect(url_for('index'))
        else:
            result = admin.logout()
            flash(result['message'])
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
            return redirect(url_for('dashboard'))
        else:
            flash(result['message'])
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

#register route
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

#dashboard route
@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    if request.method == 'POST':
        result = admin.auth_status()
        if result['logged'] == True:
            tittle = escape(request.form['tittle'])
            image = request.files['image']
            result = picture.upload_image(tittle, image)
            print(result)
            flash(result['message'])
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('index'))
    else:
        result = admin.auth_status()
        if result['logged'] == True:
            result = picture.get_all_images()
            return render_template('dashboard.html', images=result)
        else:
            return redirect(url_for('index'))

#get all images
@app.route('/images', methods=['GET'])
def all_images():
    result = picture.get_all_images()
    return jsonify(result)

#delete image
@app.route('/delete_image/<int:id>', methods=['GET','POST'])
def delete_image(id):
    status = admin.auth_status()
    if status['logged'] == True:
        if request.method == 'POST':
            result = picture.delete_image(id)
            flash(result['message'])
            return redirect(url_for('dashboard'))
        else:
            return render_template('confirm_delete.html',id=id)
    else:
        return redirect(url_for('index'))


# Default port:
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.debug = True
    app.run(host='0.0.0.0', port=port)