from flask import Flask , request,render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application= Flask(__name__)
app=application



@app.route("/")

def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="GET":
        return render_template ("home.html")
    else:
        data=CustomData(
            gender=request.json.get("gender"),
            race_ethnicity=request.json.get("race_ethnicity"),
            parental_level_of_education=request.json.get("parental_level_of_education"),
            lunch=request.json.get("lunch"),
            test_preparation_course=request.json.get("test_preparation_course"),
            reading_score=float(request.json.get("reading_score")),
            writing_score=float(request.json.get("writing_score"))
        )
        pred_df=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        preds=predict_pipeline.predict(pred_df)

        return {"prediction": float(preds[0])}
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
