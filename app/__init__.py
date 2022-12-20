""" My app/__init__.py file creates objects, such as the database and database
migration engine instances. These are created after the application. 
"""

from flask import Flask    
import os
from dotenv import load_dotenv

# from config import Config  # Config class (upper case) imported from config.py (lower case)

app = Flask(__name__)
# app.config.from_object method tells Flask to read and apply the Config class, 
# which it finds in config.py
# app.config.from_object(Config)
app.debug = True

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

from app import routes
