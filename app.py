from flask import Flask 
from bert_model import *
import os
app = Flask(__name__)

@app.route('/')
def hello():    
    return 'Alright , Server runs fine !'

@app.route('/')
def 


if __name__=='__main__':
    
    app.run(host='0.0.0.0', port=5000, debug=True)