# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import decimal
import flask.json
from run_models import model1, model2, model3, model4
# import load_db

app = Flask(__name__)

DATABASE_URI = os.environ.get('DATABASE_URL', '') or "postgresql://postgres:postgres@localhost:5432/COVID19_db"
print(DATABASE_URI)

engine = create_engine(DATABASE_URI)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI 

db = SQLAlchemy(app)

@app.route("/")
def world():

    return render_template("Covid_Landing.html")

@app.route("/home")
def home():

    return render_template("Covid_Home.html")

@app.route("/team")
def team():
    return render_template("Covid_About.html")

@app.route("/risk")
def risk(): 
  
    return render_template("Covid_Risk.html")

@app.route("/api/v1.0/<model>/<selFeatures>")
def model(model, selFeatures): 
    
    result=""
    if model == 'model1':
        result = model1(selFeatures)
    elif model == 'model2':
        result = model2(selFeatures)
    elif model == 'model3':
        result = model3(selFeatures)
    else:
         result = model4(selFeatures)
    # print(result)
    # print(str(result[0]))
    # return jsonify(str(result[0]))

    print(result)
    x = (str(result[0]))
    print(x)
    return x