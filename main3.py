from flask import Flask
from flask_cors import CORS
from numpy import array
import tensorflow as tf
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template



app = Flask(__name__)

# enable cors
CORS(app)


# load the models from disk
filename2 = r'C:\Users\CCM Laptop\flask_api\app\ml_models\model2.h5'

# Loading a saved model
from numpy import loadtxt
from tensorflow.keras.models import load_model
model = load_model(filename2)







@app.route('/')
def home():
    return render_template('index3.html')




# Radiation model api endpoint http://127.0.0.1:8000/api/model/radiation
@app.route('/predict',methods=['POST'])
def predict():
    first_interval = request.form.get('first_interval')
    second_interval = request.form.get('second_interval')
    third_interval = request.form.get('third_interval')



    actual_solar_radiation = array(
        [float(first_interval), float(second_interval), float(third_interval)])
    actual_solar_radiation = actual_solar_radiation.reshape((1, 3, 1))
    predictions = model.predict(actual_solar_radiation)


    # response
    return {
        "predictions": predictions.tolist()      
    }



   


app.run(host='0.0.0.0', port=8080, debug=True)