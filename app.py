# ==========================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# FLASK BACKEND + MACHINE LEARNING MODEL
# ==========================================================

import os
import joblib
import pandas as pd

from flask import Flask, render_template, request, jsonify


# ==========================================================
# CREATE APP
# ==========================================================

app = Flask(__name__)


# ==========================================================
# MAPPINGS
# ==========================================================


category_map = {
    "ST":0,
    "OBC":1,
    "SC":2,
    "EWS":3,
    "General":4
}


exam_map = {
    "CUET":0,
    "JEE Main":1
}


branch_map = {
    "AI":0,
    "Civil":1,
    "Mechanical":2,
    "CSE":3,
    "ECE":4
}


college_map = {

    "NIT Trichy":0,
    "Chitkara":1,
    "Thapar":2,
    "IIT Delhi":3

}


college_type_map = {

    "Govt":0,
    "Private":1

}


tier_map = {

    "Tier 1":0,
    "Tier 2":1,
    "Tier 3":2

}


quota_map = {

    "SC":0,
    "OBC":1,
    "EWS":2,
    "ST":3,
    "General":4

}


documents_map = {

    "No":0,
    "Yes":1

}


scholarship_applied_map = {

    "No":0,
    "Yes":1

}


scholarship_eligibility_map = {

    "Eligible":0,
    "Not Eligible":1

}


hostel_map = {

    "Yes":0,
    "No":1

}



# ==========================================================
# LOAD MODEL
# ==========================================================


MODEL_PATH="college_admission_approval.pkl"


try:

    model = joblib.load(MODEL_PATH)

    print("MODEL LOADED SUCCESSFULLY")

    print("==============================")
    print("AVAILABLE CLASSES:")
    print(model.classes_)
    print("==============================")


except Exception as e:

    print("MODEL LOADING ERROR:",e)

    model=None





# ==========================================================
# HOME PAGE
# ==========================================================


@app.route("/")
def home():

    return render_template("index.html")





# ==========================================================
# PREDICTION API
# ==========================================================


@app.route("/predict",methods=["POST"])

def predict():


    try:


        data=request.json



        input_data=pd.DataFrame([{


        "Age":float(data.get("Age") or 0),

        "Category":category_map.get(
            data.get("Category"),0
        ),

        "Family_Income":float(
            data.get("Family_Income") or 0
        ),


        "Class10_%":float(
            data.get("Class10_%") or 0
        ),


        "Class12_%":float(
            data.get("Class12_%") or 0
        ),


        "PCM_%":float(
            data.get("PCM_%") or 0
        ),


        "Entrance_Exam":exam_map.get(
            data.get("Entrance_Exam"),0
        ),


        "JEE_Percentile":float(
            data.get("JEE_Percentile") or 0
        ),


        "JEE_Rank":float(
            data.get("JEE_Rank") or 0
        ),


        "CUET_Score":float(
            data.get("CUET_Score") or 0
        ),


        "Preferred_Branch":branch_map.get(
            data.get("Preferred_Branch"),0
        ),


        "Preferred_College":college_map.get(
            data.get("Preferred_College"),0
        ),


        "College_Type":college_type_map.get(
            data.get("College_Type"),0
        ),


        "NIRF_Rank":float(
            data.get("NIRF_Rank") or 0
        ),


        "College_Tier":tier_map.get(
            data.get("College_Tier"),0
        ),


        "Branch_Cutoff_Rank":float(
            data.get("Branch_Cutoff_Rank") or 0
        ),


        "Available_Seats":float(
            data.get("Available_Seats") or 0
        ),


        "Reservation_Quota":quota_map.get(
            data.get("Reservation_Quota"),0
        ),


        "Documents_Verified":documents_map.get(
            data.get("Documents_Verified"),0
        ),


        "Interview_Score":float(
            data.get("Interview_Score") or 0
        ),


        "Communication_Score":float(
            data.get("Communication_Score") or 0
        ),


        "Aptitude_Score":float(
            data.get("Aptitude_Score") or 0
        ),


        "Scholarship_Applied":scholarship_applied_map.get(
            data.get("Scholarship_Applied"),0
        ),


        "Scholarship_Eligibility":scholarship_eligibility_map.get(
            data.get("Scholarship_Eligibility"),0
        ),


        "Hostel_Required":hostel_map.get(
            data.get("Hostel_Required"),0
        ),


        "Admission_Probability":float(
            data.get("Admission_Probability") or 0
        ),


        "Tuition_Fee":float(
            data.get("Tuition_Fee") or 0
        )


        }])




        # MODEL PREDICTION

        prediction=model.predict(input_data)[0]


        print("==============================")
        print("PREDICTION:",prediction)
        print("CLASSES:",model.classes_)
        print("==============================")



        prediction=str(prediction).lower()



        # RESULT HANDLING


        if prediction in [
            "1",
            "approved",
            "approve",
            "yes"
        ]:


            result={

            "status":"🎉 ADMISSION APPROVED",

            "message":
            "Congratulations! The student is eligible for admission."

            }



        elif prediction in [
            "0",
            "rejected",
            "reject",
            "no"
        ]:


            result={

            "status":"❌ ADMISSION REJECTED",

            "message":
            "Sorry! The student is not eligible for admission."

            }



        elif prediction in [
            "2",
            "waitlisted",
            "waitlist"
        ]:


            result={


            "status":"⏳ ADMISSION WAITLISTED",

            "message":
            "The student is waitlisted for admission."

            }



        else:


            result={

            "status":"UNKNOWN RESULT",

            "message":
            f"Model returned {prediction}"

            }



        return jsonify(result)



    except Exception as e:


        return jsonify({

            "status":"Prediction Error",

            "message":str(e)

        })





# ==========================================================
# RUN
# ==========================================================


if __name__=="__main__":


    app.run(

        host="0.0.0.0",

        port=int(
            os.environ.get(
                "PORT",
                7860
            )
        )

    )
