from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'JFDDJjddjffjfffj88-999*h:dkdjffff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False