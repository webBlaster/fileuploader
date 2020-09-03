  
#security imports
from werkzeug.security import generate_password_hash, check_password_hash
#imports for json
from flask import jsonify
#database imports
from database_setup import db, Admin as admin, Picture as picture
class Admin():
    def signup(self):
        pass
    def login(self):
        pass
    def logout(self):
        pass


class Picture():
    def upload_image(self):
        pass
    def delete_image(self):
        pass
    def get_all_images(self):
        pass