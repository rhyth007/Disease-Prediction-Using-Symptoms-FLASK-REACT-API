#from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
#import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import pickle
import pandas as pd
import os
from flask_cors import CORS,cross_origin
from flask import  Flask, request,jsonify,render_template

#Create Flask App


app = Flask(__name__)
CORS(app)
#Load Pickle Model
clf3 = pickle.load(open("DT.pkl","rb"))
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

    # X = []
    
    #data = pd.read_csv("training.csv")
    # X = data.iloc[:, :-1]
    X=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

    disease=['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis',
       'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 'Diabetes ',
       'Gastroenteritis', 'Bronchial Asthma', 'Hypertension ', 'Migraine',
       'Cervical spondylosis', 'Paralysis (brain hemorrhage)', 'Jaundice',
       'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
       'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E',
       'Alcoholic hepatitis', 'Tuberculosis', 'Common Cold', 'Pneumonia',
       'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins',
       'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
       'Osteoarthristis', 'Arthritis',
       '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
       'Urinary tract infection', 'Psoriasis', 'Impetigo']
 
    
    l2=[]
    for i in range(0,len(X)):
        l2.append(0)

    symptoms_dict = {}
    for index, symptom in enumerate(X):
        symptoms_dict[symptom] = index

   #input_vector = np.zeros(95)

    #print(symptoms_dict)
    # print(data)
    data = request.json
    dataF = []
    for i in data:
        dataF.append(i["Symptom"])

    print(dataF)
    # #
    # for i in dataF:
    #     if i in symptoms_dict:
    #         input_vector[symptoms_dict[i]] = 1
    # prediction = model.predict([input_vector])
    # prediction = str(prediction[0])
    # input_vector = [np.array(input_vector)]
    # prediction = model.predict(input_vector)

    # print(prediction)

    # predict = {'prediction':prediction[0]}
    # return jsonify(predict)
   #psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(X)):
        for z in dataF:
            if(z==X[k]):
              l2[k]=1

        
    inputtest = [l2]
       # print(inputtest)
    prediction = clf3.predict(inputtest)
    #print(prediction)
    predicted=prediction[0]
    
    predict = {'prediction':disease[predicted]}
    return jsonify(predict)
   
    

if __name__ == "__main__":
    app.run(debug=True)






