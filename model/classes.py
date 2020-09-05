  
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
            check = db.session.query(admin).first()
            if check == None:
                new_user = admin(
                        email = email,
                        password = password,
                   )

                #Store user details
                db.session.add(new_user)
                db.session.commit()
                return {
                        "message":"new user registered",
                        "registered": False
                        }
            else:
                return {
                        "message":"Admin already exists",
                        "registered": False
                        }          
        else:
            return {
                    "message":"make sure to fill in all fields",
                    "registered": False 
                    }

    def login(self, email, password):
        #make sure data is not empty
        if email and password is not None:
            if 'email' in session:
                return {
                        "message": "user already signed in",
                        "email": session['email'],
                        "id": session['id'],
                        "logged": True
                        }
        #check if details are in the database
            check = db.session.query(admin).filter_by(email = email).first()
            if check == None:
                return {
                        "message": "the email provided is not registered",
                        "logged": False 
                    }
        #check if password matches        
            else:
                result = check_password_hash(check.password, password)
                if result == True:
                    #start user session
                    session['id'] = check.id
                    session['email'] = check.email
                    return {
                        "message": "login successful",
                        "logged": True
                        }
                else:
                    return {
                        "message": "password incorrect",
                        "logged": False 
                    }
        else:
            return {
                    "message": "really!! post man?",
                    "logged": False 
                    }
    
    def logout(self):
        #unset session variables
        del session['id']
        del session['email']
        
        return {
                "message": "user logged out",
                "logged": False 
                }
    def auth_status(self):
        if 'email' in session:
            return {
                "logged":True
                }
        else:
            return {
                    "logged": False 
                    }



class Picture():
    def upload_image(self, tittle):
        pass
    def delete_image(self, id):
        pass
    def get_all_images(self):
        pass