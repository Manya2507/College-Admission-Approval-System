# =====================================================
# AI COLLEGE ADMISSION APPROVAL SYSTEM
# PART 1
# =====================================================


import os
import base64
import joblib
import pandas as pd
import gradio as gr



# =====================================================
# LOAD MODEL
# =====================================================


MODEL_PATH = "college_admission_approval.pkl"


try:

    model = joblib.load(MODEL_PATH)

    print("✅ Model Loaded Successfully")


except Exception as e:

    print("❌ Model Loading Error:",e)

    model = None





# =====================================================
# LOAD SINGLE BACKGROUND IMAGE
# =====================================================


def load_background():

    image_path = os.path.join(
        "images",
        "background.jpg"
    )


    if os.path.exists(image_path):

        with open(
            image_path,
            "rb"
        ) as f:


            return base64.b64encode(
                f.read()
            ).decode()


    else:

        print(
            "⚠️ Background image not found"
        )

        return ""




BACKGROUND = load_background()





# =====================================================
# PREDICTION FUNCTION
# =====================================================


def predict_admission(

    Age,
    Category,
    Family_Income,

    Class10_Percentage,
    Class12_Percentage,
    PCM_Percentage,

    Entrance_Exam,
    JEE_Percentile,
    JEE_Rank,

    CUET_Score,

    Preferred_Branch,
    Preferred_College,

    College_Type,

    NIRF_Rank,
    College_Tier,

    Branch_Cutoff_Rank,
    Available_Seats,

    Reservation_Quota,

    Documents_Verified,

    Interview_Score,
    Communication_Score,
    Aptitude_Score,

    Scholarship_Applied,

    Scholarship_Eligibility,

    Hostel_Required,

    Admission_Probability,

    Tuition_Fee

):


    if model is None:

        return "❌ Model not loaded"



    try:


        data = pd.DataFrame([{

            "Age":Age,

            "Category":Category,

            "Family_Income":Family_Income,


            "Class10_%":Class10_Percentage,

            "Class12_%":Class12_Percentage,

            "PCM_%":PCM_Percentage,


            "Entrance_Exam":Entrance_Exam,

            "JEE_Percentile":JEE_Percentile,

            "JEE_Rank":JEE_Rank,


            "CUET_Score":CUET_Score,


            "Preferred_Branch":Preferred_Branch,

            "Preferred_College":Preferred_College,


            "College_Type":College_Type,


            "NIRF_Rank":NIRF_Rank,

            "College_Tier":College_Tier,


            "Branch_Cutoff_Rank":Branch_Cutoff_Rank,

            "Available_Seats":Available_Seats,


            "Reservation_Quota":Reservation_Quota,


            "Documents_Verified":Documents_Verified,


            "Interview_Score":Interview_Score,

            "Communication_Score":Communication_Score,

            "Aptitude_Score":Aptitude_Score,


            "Scholarship_Applied":Scholarship_Applied,

            "Scholarship_Eligibility":Scholarship_Eligibility,


            "Hostel_Required":Hostel_Required,


            "Admission_Probability":Admission_Probability,


            "Tuition_Fee":Tuition_Fee

        }])




        prediction = model.predict(data)[0]



        if str(prediction).lower() in [

            "1",
            "yes",
            "approved",
            "true"

        ]:


            return """

🎉 ADMISSION APPROVED


✅ Student has high probability of admission.


🤖 Algorithm:

Random Forest Classifier

"""



        else:


            return """

❌ ADMISSION NOT APPROVED


Student has low probability of admission.


🤖 Algorithm:

Random Forest Classifier

"""



    except Exception as e:


        return f"""

❌ Prediction Error


{e}

"""
