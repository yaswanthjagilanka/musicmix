from flask import Flask, request,render_template
from src.audio_puller import audio_dwnld
# from flask_ngrok import run_with_ngrok
# from flask import Flask
# from bottle import Bottle, response, request as bottle_request
# import json
# import ast

app = Flask(__name__)
# CORS(app)
# run_with_ngrok(app)


@app.route('/hello')
def hello():
    return "hello"


@app.route('/audio_collect')
def audio_collect():
    return render_template('base1.html')

@app.route('/audio_recv',methods = ['POST', 'GET'])
def audio_recv():
    result = request.form
    print (result['language'])
    for key in result.keys():
        print (key)
    data = audio_dwnld.audio_process(result)
    return render_template('return_page.html')

@app.route('/song_add')
def song_add():
    #username
    #song url
    #start time
    #end time
    #langauge
    #genre
    #type
    #name_song
    return "sucess"

app.run()