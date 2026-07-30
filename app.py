# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1/5
# FLASK BACKEND + MACHINE LEARNING MODEL
# ==========================================================


import os
import joblib
import pandas as pd

from flask import (
    Flask,
    render_template,
    request,
    jsonify
)





# ==========================================================
# CREATE FLASK APP
# ==========================================================


app = Flask(__name__)





# ==========================================================
# LOAD MACHINE LEARNING MODEL
# ==========================================================


MODEL_PATH = "college_admission_approval.pkl"



try:

    model = joblib.load(MODEL_PATH)

    print("✅ Admission Model Loaded Successfully")


except Exception as e:

    print("❌ Model Loading Error:", e)

    model = None





# ==========================================================
# HOME PAGE
# ==========================================================


@app.route("/")

def home():

    return render_template(
        "index.html"
    )







# ==========================================================
# PREDICTION API
# ==========================================================


@app.route(
    "/predict",
    methods=["POST"]
)

def predict():



    try:



        # Receive data from HTML


        data = request.json




        input_data = pd.DataFrame([{


            "Age":

            float(data["Age"]),



            "Category":

            data["Category"],



            "Family_Income":

            float(data["Family_Income"]),



            "Class10_%":

            float(data["Class10_%"]),



            "Class12_%":

            float(data["Class12_%"]),



            "PCM_%":

            float(data["PCM_%"]),



            "Entrance_Exam":

            data["Entrance_Exam"],



            "JEE_Percentile":

            float(data["JEE_Percentile"]),



            "JEE_Rank":

            float(data["JEE_Rank"]),



            "CUET_Score":

            float(data["CUET_Score"]),



            "Preferred_Branch":

            data["Preferred_Branch"],



            "Preferred_College":

            data["Preferred_College"],



            "College_Type":

            data["College_Type"],



            "NIRF_Rank":

            float(data["NIRF_Rank"]),



            "College_Tier":

            float(data["College_Tier"]),



            "Branch_Cutoff_Rank":

            float(data["Branch_Cutoff_Rank"]),



            "Available_Seats":

            float(data["Available_Seats"]),



            "Reservation_Quota":

            data["Reservation_Quota"],



            "Documents_Verified":

            data["Documents_Verified"],



            "Interview_Score":

            float(data["Interview_Score"]),



            "Communication_Score":

            float(data["Communication_Score"]),



            "Aptitude_Score":

            float(data["Aptitude_Score"]),



            "Scholarship_Applied":

            data["Scholarship_Applied"],



            "Scholarship_Eligibility":

            data["Scholarship_Eligibility"],



            "Hostel_Required":

            data["Hostel_Required"],



            "Admission_Probability":

            float(data["Admission_Probability"]),



            "Tuition_Fee":

            float(data["Tuition_Fee"])



        }])







        # Prediction


        prediction = model.predict(

            input_data

        )[0]






        # Probability


        try:


            probability = max(

                model.predict_proba(

                    input_data

                )[0]

            )


            probability = round(

                probability * 100,

                2

            )


        except:


            probability = 0







        if str(prediction).lower() in [


            "approved",

            "yes",

            "1"


        ]:



            result = {

                "status":

                "🎉 ADMISSION APPROVED",


                "message":

                "High chance of admission",


                "probability":

                probability

            }



        else:



            result = {


                "status":

                "❌ ADMISSION NOT APPROVED",


                "message":

                "Low chance of admission",


                "probability":

                probability


            }






        return jsonify(result)







    except Exception as e:



        return jsonify({


            "status":

            "❌ Prediction Error",


            "message":

            str(e),


            "probability":

            0


        })







# ==========================================================
# RUN APPLICATION
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
