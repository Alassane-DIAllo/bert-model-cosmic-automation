from flask import Flask, jsonify, request 
from bert_model import *
import os
app = Flask(__name__)

@app.route('/')
def hello():    
    return 'Alright , Server runs fine !'

@app.route('/get_sentiment', method=['POST'])
def get_sentiment():
    x = request.get_json(force=True)
    NameEntity = model.get_predictor(x)
    
    return jsonify(result=sent)

    
if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True, use_reloader=False)