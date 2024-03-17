from flask import Flask
from dbnew import *

dbstart()

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello world"

@app.route("/home")
def home():
    return "This is home page"



#import controller.user_controller as user_controller
#import controller.product_controller as product_controller
#from controller import user_controller, product_controller
from controller import * #bunu kullanmak için controller\__init__.py oluşturulmalı