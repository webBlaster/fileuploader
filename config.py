from flask import Flask
import cloudinary
import os
from flask_cors import CORS
from flask_talisman import Talisman
app = Flask(__name__)
Talisman(app, content_security_policy={
        'img-src': '*',
        'script-src': [
            '*'
        ],
        'style-src': [
            '*'
        ],
    }
    )
CORS(app)
app.config['SECRET_KEY'] = 'JFDDJjddjffjfffj88-999*h:dkdjffff'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

cloudinary.config( 
  cloud_name = os.environ.get('CLOUD_NAME'), 
  api_key = os.environ.get('CLOUD_API_KEY'), 
  api_secret = os.environ.get('CLOUD_API_SECRET') 
)