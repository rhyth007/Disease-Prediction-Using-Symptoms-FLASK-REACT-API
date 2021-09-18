import pickle

import  numpy as np
import pandas as pd
from flask_cors import CORS,cross_origin


from flask import  Flask, request,jsonify,render_template

#Create Flask App


app = Flask(__name__)
CORS(app)
#Load Pickle Model
model = pickle.load(open("modely.pkl","rb"))
CORS(app,resource={r"/api/*":{"origins":"*"}})
app.config['CORS HEADERS'] = 'Content-Type'
@app.route('/')
@cross_origin()
def Home():
    return str('Welcome Home')

@app.route('/api', methods=['POST', 'GET'])
@cross_origin()
def api_post():

    # int_features = [int(x) for x in request.form.values()]
    # features = [np.array(int_features)]
    # prediction = model.predict(features)

    X = []
    data = pd.read_csv("Training.csv")
    X = data.iloc[:, :-1]

    symptoms_dict = {}
    for index, symptom in enumerate(X):
        symptoms_dict[symptom] = index

    input_vector = np.zeros(132)

    #print(symptoms_dict)
    # print(data)
    data = request.json
    dataF = []
    for i in data:
        dataF.append(i["Symptom"])

    print(dataF)
    #
    for i in dataF:
        if i in symptoms_dict:
            input_vector[symptoms_dict[i]] = 1
    # prediction = model.predict([input_vector])
    # prediction = str(prediction[0])
    input_vector = [np.array(input_vector)]
    prediction = model.predict(input_vector)



    predict = {'prediction':prediction[0]}
    return jsonify(predict)
   

if __name__ == "__main__":
    app.run(debug=True)






