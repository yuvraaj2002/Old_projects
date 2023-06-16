from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for a home page


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(

            city_development_index=float(
                request.form.get('city_development_index')),
            gender=request.form.get('gender'),
            relevent_experience=request.form.get('relevent_experience'),
            enrolled_university=request.form.get('enrolled_university'),
            education_level=request.form.get('education_level'),
            major_discipline=request.form.get('major_discipline'),
            experience=int(request.form.get('experience')),
            company_size=(request.form.get('company_size')),
            company_type=request.form.get('company_type'),
            training_hours=int(request.form.get('training_hours'))
        )

        # Creating a dataframe
        pred_df = data.get_data_as_data_frame()

        # Making an object of PredictPipeline
        predict_pipeline = PredictPipeline()

        try:
            results = predict_pipeline.predict(pred_df)
            print(results)
        except Exception as e:
            print(e)
            return render_template('home.html', results='Error predicting datapoint')

        if (results == 0):
            return render_template('home.html', results='No')

        return render_template('home.html', results='Yes')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
