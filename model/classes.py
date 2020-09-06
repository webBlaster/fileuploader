  
#security imports
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
#imports for json
from flask import jsonify
#database imports
from .database_setup import db, Admin as admin, Picture as picture
#imports for session
from flask import session
#cloudinary
import cloudinary as cloud
from cloudinary import api, uploader
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
                "message":"user is logged in",
                "logged":True
                }
        else:
            return {
                    "message": "user logged out",
                    "logged": False 
                    }



class Picture():
    def upload_image(self, tittle, image):
        image_name = secure_filename(image.filename)
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            #upload on cloudinary
            result = uploader.upload(image)
            if result['created_at']:
                public_id = result['public_id']
                url = result['secure_url']
                new_picture = picture(
                        tittle = tittle,
                        public_id = public_id,
                        url = url
                        )

                #Store picture details in database
                db.session.add(new_picture)
                db.session.commit()
                return {
                "message":"upload successful"
                }
            else:
                return result
        else:
            return {
                "message":"only image files can be uploaded"
                }
    def delete_image(self, id):
        #get dictionary from db with id
        image = db.session.query(picture).filter_by(id = id).first()
        public_id = image.public_id

        #delete picture on cloudinary with the public_id
        result = uploader.destroy(public_id)

        #based on the respose delete from db or return error message
        if result['result'] == 'ok':
            return {
                "message":"image deleted",
                "deleted":True
                }
        else:
            return {
                "message":"image failed to delete try again later",
                "deleted":False
                }

    def get_all_images(self):
        images = db.session.query(picture).all()
        image_list = []
        for image in images:
            image_list.append({
                'id':image.id,
                'tittle':image.tittle,
                'url':image.url
            })
        return image_list