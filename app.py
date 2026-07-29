import os
import joblib
import pandas as pd
import gradio as gr


# =========================================
# LOAD MODEL
# =========================================

MODEL_FILE = "college_admission_approval.pkl"


try:
    model = joblib.load(MODEL_FILE)
    print("✅ Model Loaded Successfully")

except Exception as e:
    print("❌ Model Loading Error:",e)
    model = None



# =========================================
# PREDICTION FUNCTION
# =========================================


def predict_admission(
    Age,
    Category,
    Family_Income,
    Class10,
    Class12,
    PCM,
    Entrance,
    JEE,
    Rank,
    CUET,
    Branch,
    College,
    College_Type,
    NIRF,
    Tier,
    Cutoff,
    Seats,
    Quota,
    Docs,
    Interview,
    Communication,
    Aptitude,
    Scholarship,
    Scholarship_Eligibility,
    Hostel,
    Probability,
    Fee
):


    if model is None:
        return "❌ Model not loaded"



    try:


        input_data = pd.DataFrame([{

            "Age":Age,
            "Category":Category,
            "Family_Income":Family_Income,

            "Class10_%":Class10,
            "Class12_%":Class12,
            "PCM_%":PCM,

            "Entrance_Exam":Entrance,

            "JEE_Percentile":JEE,
            "JEE_Rank":Rank,

            "CUET_Score":CUET,

            "Preferred_Branch":Branch,

            "Preferred_College":College,

            "College_Type":College_Type,

            "NIRF_Rank":NIRF,

            "College_Tier":Tier,

            "Branch_Cutoff_Rank":Cutoff,

            "Available_Seats":Seats,

            "Reservation_Quota":Quota,

            "Documents_Verified":Docs,

            "Interview_Score":Interview,

            "Communication_Score":Communication,

            "Aptitude_Score":Aptitude,

            "Scholarship_Applied":Scholarship,

            "Scholarship_Eligibility":Scholarship_Eligibility,

            "Hostel_Required":Hostel,

            "Admission_Probability":Probability,

            "Tuition_Fee":Fee

        }])


        prediction=model.predict(input_data)[0]


        if str(prediction).lower() in ["1","yes","approved"]:

            return """
🎉 ADMISSION APPROVED

Student has high admission chances.

Algorithm:
Random Forest Classifier
"""


        else:

            return """
❌ ADMISSION NOT APPROVED

Student has low admission chances.

Algorithm:
Random Forest Classifier
"""


    except Exception as e:

        return f"Prediction Error:\n{e}"




# =========================================
# CSS
# =========================================


css="""

body{

background:#eefaf5;

}


.gradio-container{

font-family:Arial;

}


#box{

background:white;

padding:30px;

border-radius:20px;

box-shadow:0px 10px 30px #aaa;

}



button{

background:#059669 !important;

color:white !important;

font-size:18px !important;

border-radius:15px !important;

}


label{

font-weight:bold;

}

"""



# =========================================
# HEADER
# =========================================


header="""

<div style="
text-align:center;
padding:20px;
">

<h1>
🎓 AI College Admission Approval System
</h1>


<h2>
Machine Learning Based Admission Prediction
</h2>


<hr>


<h3>
👩‍💻 Developer Details
</h3>


<p>
<b>Name:</b> Manya Singla
</p>


<p>
<b>College:</b> Panipat Institute of Engineering and Technology
</p>


<p>
<b>Technology:</b>
Python | Pandas | Scikit-Learn | Random Forest | Gradio
</p>


</div>

"""




# =========================================
# GRADIO APP
# =========================================



with gr.Blocks(
    css=css,
    title="AI College Admission System"
) as demo:


    with gr.Column(elem_id="box"):


        gr.HTML(header)



        gr.Markdown(
        """
        ## Enter Student Details
        """
        )



        with gr.Row():

            Age=gr.Number(label="Age")

            Category=gr.Dropdown(
                ["General","OBC","SC","ST"],
                label="Category"
            )

            Family_Income=gr.Number(
                label="Family Income"
            )


        with gr.Row():

            Class10=gr.Number(label="Class 10 %")

            Class12=gr.Number(label="Class 12 %")

            PCM=gr.Number(label="PCM %")



        with gr.Row():

            Entrance=gr.Textbox(
                label="Entrance Exam"
            )

            JEE=gr.Number(
                label="JEE Percentile"
            )

            Rank=gr.Number(
                label="JEE Rank"
            )



        with gr.Row():

            CUET=gr.Number(
                label="CUET Score"
            )

            Branch=gr.Textbox(
                label="Preferred Branch"
            )

            College=gr.Textbox(
                label="Preferred College"
            )



        with gr.Row():

            College_Type=gr.Dropdown(
                ["Government","Private"],
                label="College Type"
            )

            NIRF=gr.Number(
                label="NIRF Rank"
            )

            Tier=gr.Number(
                label="College Tier"
            )



        with gr.Row():

            Cutoff=gr.Number(
                label="Branch Cutoff Rank"
            )

            Seats=gr.Number(
                label="Available Seats"
            )

            Quota=gr.Textbox(
                label="Reservation Quota"
            )



        with gr.Row():

            Docs=gr.Dropdown(
                ["Yes","No"],
                label="Documents Verified"
            )

            Interview=gr.Number(
                label="Interview Score"
            )

            Communication=gr.Number(
                label="Communication Score"
            )



        with gr.Row():

            Aptitude=gr.Number(
                label="Aptitude Score"
            )

            Scholarship=gr.Dropdown(
                ["Yes","No"],
                label="Scholarship Applied"
            )

            Scholarship_Eligibility=gr.Dropdown(
                ["Yes","No"],
                label="Scholarship Eligibility"
            )



        with gr.Row():

            Hostel=gr.Dropdown(
                ["Yes","No"],
                label="Hostel Required"
            )

            Probability=gr.Number(
                label="Admission Probability"
            )

            Fee=gr.Number(
                label="Tuition Fee"
            )



        button=gr.Button(
            "🎯 Predict Admission"
        )


        output=gr.Textbox(
            label="Result",
            lines=8
        )



        button.click(

            predict_admission,

            inputs=[
                Age,
                Category,
                Family_Income,
                Class10,
                Class12,
                PCM,
                Entrance,
                JEE,
                Rank,
                CUET,
                Branch,
                College,
                College_Type,
                NIRF,
                Tier,
                Cutoff,
                Seats,
                Quota,
                Docs,
                Interview,
                Communication,
                Aptitude,
                Scholarship,
                Scholarship_Eligibility,
                Hostel,
                Probability,
                Fee
            ],

            outputs=output
        )





# =========================================
# RUN
# =========================================


if __name__=="__main__":


    demo.launch(

        server_name="0.0.0.0",

        server_port=int(
            os.environ.get(
                "PORT",
                7860
            )
        )

    )
