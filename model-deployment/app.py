from flask import Flask, jsonify, request 
import bert_model as model
import os 
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


app = Flask(__name__)
@app.route('/')
def hello():    
    return 'Alright , Server runs fine !'

@app.route('/get_NER', methods=['POST'])
def get_NER():
    x = request.get_json(force=True)
    text = x["sentence"]
    NameEntity = model.get_predictor(text)
    return  jsonify(result = NameEntity)
    
if __name__=='__main__':
    app.run(host='localhost', port=5000, debug=True, use_reloader=False)