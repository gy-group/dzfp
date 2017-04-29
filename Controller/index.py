from flask import render_template;
from flask import session,request,abort,Blueprint;
import os;


main =  Blueprint('main',__name__,template_folder='templates')

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/home')
def home():
    return render_template("dashboard.html")

@main.route('/kjfp')
def kjfp():
    return render_template("kjfp.html")