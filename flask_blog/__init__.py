# Initialize application and bring together different components
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '49cb7e2bfba717abc959512a2a0e74086f13d028'
# config a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# create a db instance
db = SQLAlchemy(app)

from flask_blog import routes