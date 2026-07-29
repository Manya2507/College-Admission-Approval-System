import os
import joblib
import pandas as pd
import gradio as gr


# ==========================================================
# Load Admission Model
# ==========================================================

try:
    model = joblib.load("college_admission_approval.pkl")
    print("Model Loaded Successfully")

except Exception as e:
    print("Model Loading Error:", e)
    model = None



# ==========================================================
# Prediction Function
# ==========================================================

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
        return "❌ Model not loaded. Check admission_model.pkl file"


    try:

        input_data = pd.DataFrame([{

            "Age": Age,
            "Category": Category,
            "Family_Income": Family_Income,
            "Class10_%": Class10_Percentage,
            "Class12_%": Class12_Percentage,
            "PCM_%": PCM_Percentage,

            "Entrance_Exam": Entrance_Exam,
            "JEE_Percentile": JEE_Percentile,
            "JEE_Rank": JEE_Rank,
            "CUET_Score": CUET_Score,

            "Preferred_Branch": Preferred_Branch,
            "Preferred_College": Preferred_College,
            "College_Type": College_Type,

            "NIRF_Rank": NIRF_Rank,
            "College_Tier": College_Tier,
            "Branch_Cutoff_Rank": Branch_Cutoff_Rank,

            "Available_Seats": Available_Seats,
            "Reservation_Quota": Reservation_Quota,

            "Documents_Verified": Documents_Verified,

            "Interview_Score": Interview_Score,
            "Communication_Score": Communication_Score,
            "Aptitude_Score": Aptitude_Score,

            "Scholarship_Applied": Scholarship_Applied,
            "Scholarship_Eligibility": Scholarship_Eligibility,

            "Hostel_Required": Hostel_Required,

            "Admission_Probability": Admission_Probability,

            "Tuition_Fee": Tuition_Fee

        }])


        prediction = model.predict(input_data)[0]


        if str(prediction).lower() in ["1","yes","approved","accept"]:
            
            return """
🎉 ADMISSION APPROVED

Congratulations!

The Machine Learning model predicts that the student has a high chance of getting admission.

Model Used:
Random Forest Classifier

Status:
✅ Eligible for Admission
"""


        else:

            return """
❌ ADMISSION NOT APPROVED

The model predicts that the admission criteria are not satisfied.

Suggestions:
• Improve entrance score
• Increase academic performance
• Apply for suitable colleges
"""


    except Exception as e:

        return f"""
❌ Prediction Error

{e}
"""



# ==========================================================
# Information Section
# ==========================================================


DESCRIPTION = """

<div class="info">

<h1>🎓 College Admission Approval System</h1>


<h2>👩‍💻 Developer Details</h2>

<b>Name:</b> Manya Singla<br>
<b>College:</b> Panipat Institute of Engineering and Technology<br>
<b>Project:</b> AI Based College Admission Prediction System
<b>Github:<b> https://github.com/Manya2507/College-Admission-Approval-System/edit/main/app.py
<b>Linkedin:<b> https://www.linkedin.com/in/manya-singla-438502423/


<hr>


<h2>📌 About Project</h2>

This application predicts whether a student is likely to get admission
into a preferred college using Machine Learning.

Algorithm Used:

<b>Random Forest Classifier</b>


<hr>


<h2>🛠 Technologies Used</h2>

• Python<br>
• Pandas<br>
• Scikit Learn<br>
• Random Forest Algorithm<br>
• Joblib<br>
• Gradio


<hr>


<h2>📊 Prediction Factors</h2>

The model considers:

• Academic Performance<br>
• Entrance Examination Scores<br>
• College Ranking<br>
• Branch Preference<br>
• Reservation Category<br>
• Interview Performance<br>
• Scholarship Details<br>
• Financial Information


<hr>


<h2>🎯 Output</h2>

The system predicts:

✅ Admission Approved

or

❌ Admission Not Approved


</div>

"""



# ==========================================================
# Custom CSS
# ==========================================================


css = """

body{

background-image:
url("https://images.unsplash.com/photo-1562774053-701939374585");

background-size:cover;

background-attachment:fixed;

}



.gradio-container{

background:rgba(255,255,255,0.90);

border-radius:20px;

padding:20px;

}



.info{

height:350px;

overflow-y:scroll;

padding:20px;

font-size:16px;

color:#111;

}



h1,h2{

color:#003366;

}



footer{

display:none;

}

"""



# ==========================================================
# Gradio Interface
# ==========================================================


demo = gr.Interface(

    fn=predict_admission,


    inputs=[


        gr.Number(label="Age", value=18),

        gr.Dropdown(
            ["General","OBC","SC","ST"],
            label="Category"
        ),


        gr.Number(label="Family Income (₹)"),


        gr.Number(label="Class 10 Percentage"),

        gr.Number(label="Class 12 Percentage"),

        gr.Number(label="PCM Percentage"),


        gr.Textbox(label="Entrance Exam"),


        gr.Number(label="JEE Percentile"),

        gr.Number(label="JEE Rank"),

        gr.Number(label="CUET Score"),



        gr.Textbox(label="Preferred Branch"),

        gr.Textbox(label="Preferred College"),


        gr.Dropdown(
            ["Government","Private"],
            label="College Type"
        ),


        gr.Number(label="NIRF Rank"),


        gr.Number(label="College Tier"),


        gr.Number(label="Branch Cutoff Rank"),


        gr.Number(label="Available Seats"),


        gr.Textbox(label="Reservation Quota"),


        gr.Dropdown(
            ["Yes","No"],
            label="Documents Verified"
        ),


        gr.Number(label="Interview Score"),


        gr.Number(label="Communication Score"),


        gr.Number(label="Aptitude Score"),


        gr.Dropdown(
            ["Yes","No"],
            label="Scholarship Applied"
        ),


        gr.Dropdown(
            ["Yes","No"],
            label="Scholarship Eligibility"
        ),


        gr.Dropdown(
            ["Yes","No"],
            label="Hostel Required"
        ),


        gr.Number(label="Admission Probability"),


        gr.Number(label="Tuition Fee (₹)")


    ],


    outputs=gr.Textbox(
        label="Admission Prediction",
        lines=8
    ),


    title="🎓 AI College Admission Approval System",


    description=DESCRIPTION,


    css=css,


    theme=gr.themes.Soft()

)



# ==========================================================
# Render Launch
# ==========================================================


if __name__=="__main__":

    demo.launch(

        server_name="0.0.0.0",

        server_port=int(
            os.environ.get("PORT",7860)
        )

    )
