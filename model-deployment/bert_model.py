import ktrain

predictor = ktrain.load_predictor('bert')

def get_predictor(x):

    response = predictor.predict([x])
    
    return response 