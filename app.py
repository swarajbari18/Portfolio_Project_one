from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from portfolio_project_one.pipeline.step6_prediction_api import PredictionAPI

app = Flask(__name__)


#  HOMEPAGE
@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")




#  To train the model via WEB APP
@app.route('/train', methods=['GET'])     # so that we can train the model from the ui itself
def train():
    os.system("python main.py")
    return "Training Successfull"



#  To hit the PredictionAPI
@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionAPI()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')
    

    


    

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port= 8000, debug= True)