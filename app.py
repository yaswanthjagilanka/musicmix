from flask import Flask, request
from flask_cors import CORS
from scipy.stats import zscore
import pandas as pd
from dbhandling.db_manage import *
import json
import ast
from preprocessing.preprocess import productfilter
from training.main import *

app = Flask(__name__)
CORS(app)


@app.route('/hello')
def hello():
    return "hello"

@app.route('/song_add')
def song_add():
    return "sucess"

app.run(host='0.0.0.0', port=3000)