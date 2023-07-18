# __init__.py

from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"

DATABASE = "users_schema"    #placed DATABASE here instead of in my user_model.... jumst ass a import to the user_model file to link