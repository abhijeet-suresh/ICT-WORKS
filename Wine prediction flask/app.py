# Importing the required libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

#Creating the Flask app
app = Flask(__name__)
model = pickle.load(open('redwine.pkl','rb'))

# Returing the homepage when this API's Endpoint is hit
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
        fixed_acidity=float(request.form["fixed_acidity"])
        volatile_acidity=float(request.form["volatile_acidity"])
        citric_acid=float(request.form["citric_acid"])
        residual_sugar=float(request.form["residual_sugar"])
        chlorides=float(request.form["chlorides"])
        free_sulfur_dioxide=float(request.form["free_sulfur_dioxide"])
        total_sulfur_dioxide=float(request.form["total_sulfur_dioxide"])
        density=float(request.form["density"])
        pH=float(request.form["pH"])
        sulphates=float(request.form["sulphates"])
        alcohol=float(request.form["alcohol"])

        input_data =(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol)
        input_data_as_array=np.asarray(input_data)
        input_data_reshape=input_data_as_array.reshape(1,-1)
        prediction=model.predict(input_data_reshape)
        if prediction[0]==1:
            result="Good"
        else:
            result="Bad"
        return render_template("output.html",prediction_text='The quality of wine is {}'.format(result))
if __name__ == '__main__':
    app.run(debug=False)