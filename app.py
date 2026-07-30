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
            "Age": float(data.get("Age") or 0),

            "Category":
            "Category": category_map.get(data.get("Category"), 4),



            "Family_Income":
            "Family_Income": float(data.get("Family_Income") or 0),



            "Class10_%":
            "Class10_%": float(data.get("Class10_%") or 0),



            "Class12_%":
            "Class12_%": float(data.get("Class12_%") or 0),



            "PCM_%":
            "PCM_%": float(data.get("PCM_%") or 0),



            "Entrance_Exam":
            "Entrance_Exam": exam_map.get(data.get("Entrance_Exam"), 0),



            "JEE_Percentile":
            "JEE_Percentile": float(data.get("JEE_Percentile") or 0),



            "JEE_Rank":
            "JEE_Rank": float(data.get("JEE_Rank") or 0),



            "CUET_Score":
            "CUET_Score": float(data.get("CUET_Score") or 0),


            "Preferred_Branch":
            "Preferred_Branch": branch_map.get(data.get("Preferred_Branch"), 0),


            "Preferred_College":
             "Preferred_College": college_map.get(data.get("Preferred_College"), 0),



            "College_Type":
             "College_Type": college_type_map.get(data.get("College_Type"), 0),



            "NIRF_Rank":
            "NIRF_Rank": float(data.get("NIRF_Rank") or 0),


            "College_Tier":
            "College_Tier": tier_map.get(data.get("College_Tier"), 0),



            "Branch_Cutoff_Rank":
            "Branch_Cutoff_Rank": float(data.get("Branch_Cutoff_Rank") or 0),



            "Available_Seats":
            "Available_Seats": float(data.get("Available_Seats") or 0),



            "Reservation_Quota":
             "Reservation_Quota": quota_map.get(data.get("Reservation_Quota"), 4),


            "Documents_Verified":
             "Documents_Verified": documents_map.get(data.get("Documents_Verified"), 0),



            "Interview_Score":
            "Interview_Score": float(data.get("Interview_Score") or 0),



            "Communication_Score":
            "Communication_Score": float(data.get("Communication_Score") or 0),



            "Aptitude_Score":
            "Aptitude_Score": float(data.get("Aptitude_Score") or 0),



            "Scholarship_Applied":
            "Admission_Probability": float(data.get("Admission_Probability") or 0),



            "Scholarship_Eligibility":
            "Scholarship_Eligibility": scholarship_eligibility_map.get(data.get("Scholarship_Eligibility"), 0),


            "Hostel_Required":
             "Hostel_Required": hostel_map.get(data.get("Hostel_Required"), 0),



            "Admission_Probability":
            float(data.get("Admission_Probability",0)),



            "Tuition_Fee":
            "Tuition_Fee": float(data.get("Tuition_Fee") or 0),


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
