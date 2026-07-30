# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# FLASK BACKEND
# ==========================================================


import os
import joblib
import pandas as pd

from flask import Flask, render_template, request, jsonify



# ==========================================================
# CREATE FLASK APPLICATION
# ==========================================================


app = Flask(__name__)




# ==========================================================
# LOAD MACHINE LEARNING MODEL
# ==========================================================


MODEL_PATH = "college_admission_approval.pkl"


try:

    model = joblib.load(MODEL_PATH)

    print("Model Loaded Successfully")


except Exception as e:

    print("Model Loading Error:", e)

    model = None





# ==========================================================
# HOME PAGE
# ==========================================================


@app.route("/")
def home():

    return render_template("index.html")







# ==========================================================
# PREDICTION ROUTE
# ==========================================================


@app.route("/predict", methods=["POST"])
def predict():


    try:


        if model is None:

            return jsonify({

                "status": "Model not loaded",

                "probability": 0,

                "message": "Check model file"

            })




        data = request.json




        input_data = pd.DataFrame([{


            "Age":
            float(data.get("Age",0)),


            "Category":
            data.get("Category","General"),



            "Family_Income":
            float(data.get("Family_Income",0)),



            "Class10_%":
            float(data.get("Class10_%",0)),



            "Class12_%":
            float(data.get("Class12_%",0)),



            "PCM_%":
            float(data.get("PCM_%",0)),



            "Entrance_Exam":
            data.get("Entrance_Exam",""),



            "JEE_Percentile":
            float(data.get("JEE_Percentile",0)),



            "JEE_Rank":
            float(data.get("JEE_Rank",0)),



            "CUET_Score":
            float(data.get("CUET_Score",0)),



            "Preferred_Branch":
            data.get("Preferred_Branch",""),



            "Preferred_College":
            data.get("Preferred_College",""),



            "College_Type":
            data.get("College_Type",""),



            "NIRF_Rank":
            float(data.get("NIRF_Rank",0)),



            "College_Tier":
            float(data.get("College_Tier",0)),



            "Branch_Cutoff_Rank":
            float(data.get("Branch_Cutoff_Rank",0)),



            "Available_Seats":
            float(data.get("Available_Seats",0)),



            "Reservation_Quota":
            data.get("Reservation_Quota",""),



            "Documents_Verified":
            data.get("Documents_Verified","No"),



            "Interview_Score":
            float(data.get("Interview_Score",0)),



            "Communication_Score":
            float(data.get("Communication_Score",0)),



            "Aptitude_Score":
            float(data.get("Aptitude_Score",0)),



            "Scholarship_Applied":
            data.get("Scholarship_Applied","No"),



            "Scholarship_Eligibility":
            data.get("Scholarship_Eligibility","No"),



            "Hostel_Required":
            data.get("Hostel_Required","No"),



            "Admission_Probability":
            float(data.get("Admission_Probability",0)),



            "Tuition_Fee":
            float(data.get("Tuition_Fee",0))


        }])






        prediction = model.predict(input_data)[0]






        # Probability calculation


        probability = 0


        try:


            proba = model.predict_proba(input_data)[0]


            probability = round(

                max(proba) * 100,

                2

            )


        except Exception:


            probability = 0






        if str(prediction).lower() in [

            "1",

            "yes",

            "approved",

            "true"

        ]:


            result = "ADMISSION APPROVED"

            message = "Student has high admission possibility"



        else:


            result = "ADMISSION NOT APPROVED"

            message = "Student has low admission possibility"







        return jsonify({


            "status": result,


            "probability": probability,


            "message": message


        })







    except Exception as e:


        return jsonify({


            "status": "Prediction Error",


            "probability": 0,


            "message": str(e)


        })








# ==========================================================
# RUN SERVER
# ==========================================================


if __name__ == "__main__":


    app.run(

        host="0.0.0.0",

        port=int(

            os.environ.get(

                "PORT",

                7860

            )

        )

    )
