  
#security imports
from werkzeug.security import generate_password_hash, check_password_hash
#imports for json
from flask import jsonify
#database imports
from .database_setup import db, Admin as admin, Picture as picture
#imports for session
from flask import session
class Admin():
    def signup(self, email, password):
        #make sure data is not empty
        if  email and password != None:
            #encrypt password
            password = generate_password_hash(password)
            #check if user already exist
            check = db.session.query(admin).one()
            if check == None:
                new_user = admin(
                        email = email,
                        password = password,
                   )

                #Store user details
                db.session.add(new_user)
                db.session.commit()
                return jsonify(
                    message = "new user registered successfully"
                        )
            else:
                return jsonify(
                    message = "Admin already exists",
                        )                       
        else:
            return jsonify(
                    message = "make sure to fill in all fields"
                        )

    def login(self, email, password):
        #make sure data is not empty
        if email and password is not None:
            if 'email' in session:
                return jsonify(
                        message = "user already signed in",
                        email = session['email'],
                        id = session['id'],
                        logged = True
                        )
        #check if details are in the database
            check = session.query(admin).filter_by(email = email).first()
            if check == None:
                return jsonify(
                        message = "the email provided is not registered",
                        logged = False
                        )
        #check if password matches        
            else:
                result = check_password_hash(check.password, password)
                if result == True:
                    #start user session
                    session['id'] = check.id
                    session['email'] = check.email
                    return jsonify(
                        message = "login successful welcome",
                        logged = True
                        )

                else:
                    return jsonify(
                        message = "password incorrect",
                        logged = False
                        )
        else:
            return jsonify(
                message = "really!! jerk post man?",
                logged = False
                )    
    
    def logout(self):
        #unset session variables
        del session['id']
        del session['email']
            
        return jsonify(
                message = "user has been successfully logged out",
                logged = False
                    )



class Picture():
    def upload_image(self, tittle):
        pass
    def delete_image(self, id):
        pass
    def get_all_images(self):
        pass