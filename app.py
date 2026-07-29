import os
import base64
import joblib
import pandas as pd
import gradio as gr



# =====================================================
# LOAD MACHINE LEARNING MODEL
# =====================================================

MODEL_PATH = "college_admission_approval.pkl"


try:

    model = joblib.load(MODEL_PATH)

    print("✅ Admission Model Loaded Successfully")


except Exception as e:

    print("❌ Model Loading Error:", e)

    model = None




# =====================================================
# LOAD BACKGROUND IMAGE
# =====================================================


def image_to_base64(path):

    with open(path, "rb") as image:

        return base64.b64encode(
            image.read()
        ).decode()



BACKGROUND_IMAGE = image_to_base64(
    "images/images(1).jpg"
)





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

        return "❌ Model not found"



    try:


        input_data = pd.DataFrame([{


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


            "Scholarship_Eligibility":
            Scholarship_Eligibility,


            "Hostel_Required":Hostel_Required,


            "Admission_Probability":
            Admission_Probability,


            "Tuition_Fee":Tuition_Fee


        }])



        result = model.predict(input_data)[0]



        if str(result).lower() in [

            "1",
            "yes",
            "approved"

        ]:


            return """

🎉 ADMISSION APPROVED


Prediction Result:
✅ Approved


Algorithm:
Random Forest Classifier

"""


        else:


            return """

❌ ADMISSION NOT APPROVED


Prediction Result:
❌ Not Approved


Algorithm:
Random Forest Classifier

"""



    except Exception as e:


        return f"❌ Prediction Error:\n{e}"
# =====================================================
# CSS WITH WORKING BACKGROUND IMAGE
# =====================================================


css = f"""

html, body {{

    margin:0;
    padding:0;

}}



.gradio-container {{

    background-image:

    linear-gradient(
        rgba(0,0,0,0.35),
        rgba(0,0,0,0.35)
    ),

    url(
    "data:image/jpg;base64,{BACKGROUND_IMAGE}"
    );


    background-size:cover !important;

    background-position:center !important;

    background-attachment:fixed !important;

}}



#main-container {{

    width:90%;

    max-width:1200px;


    margin:30px auto;


    padding:30px;



    background:

    rgba(255,255,255,0.55);



    backdrop-filter:blur(10px);



    border-radius:25px;



    box-shadow:

    0 10px 40px rgba(0,0,0,0.4);

}}



#main-container * {{

    color:black !important;

}}



button {{

    background:#087f5b !important;

    color:white !important;

    font-size:18px !important;

    font-weight:bold !important;

    border-radius:12px !important;

}}



footer {{

    display:none !important;

}}

"""





# =====================================================
# DEVELOPER INFORMATION
# =====================================================


header = """

<div style="

text-align:center;

padding:25px;

background:rgba(255,255,255,0.40);

border-radius:20px;

">


<h1>

🎓 AI College Admission Approval System

</h1>


<hr>


<h2>

👩‍💻 Developer Details

</h2>



<p>

<b>Name:</b> Manya Singla

</p>



<p>

<b>College:</b>

Panipat Institute of Engineering and Technology

</p>



<p>

<b>Project:</b>

College Admission Prediction using Machine Learning

</p>



<hr>


<h3>

💻 Technologies Used

</h3>


<p>

Python | Pandas | Scikit-Learn |

Random Forest | Joblib | Gradio

</p>



<hr>


<h3>

🤖 About Project

</h3>


<p>

This AI-based system predicts student admission approval
using academic performance, entrance exam scores,
college details and student information.

</p>


</div>

"""





# =====================================================
# CREATE GRADIO APP
# =====================================================


with gr.Blocks(

    css=css,

    title="AI College Admission Approval System"

) as demo:



    with gr.Column(

        elem_id="main-container"

    ):



        gr.HTML(header)



        gr.Markdown(

"""
# 📝 Enter Student Details

Fill all details to predict admission approval.

"""

        )



        # ==========================
        # BASIC DETAILS
        # ==========================


        with gr.Row():

            Age = gr.Number(
                label="Age"
            )


            Category = gr.Dropdown(

                choices=[
                    "General",
                    "OBC",
                    "SC",
                    "ST"
                ],

                label="Category"

            )


            Family_Income = gr.Number(

                label="Family Income (₹)"

            )





        # ==========================
        # ACADEMIC DETAILS
        # ==========================


        with gr.Row():

            Class10 = gr.Number(

                label="Class 10 Percentage"

            )


            Class12 = gr.Number(

                label="Class 12 Percentage"

            )


            PCM = gr.Number(

                label="PCM Percentage"

            )





        with gr.Row():

            Entrance = gr.Textbox(

                label="Entrance Exam"

            )


            JEE = gr.Number(

                label="JEE Percentile"

            )


            Rank = gr.Number(

                label="JEE Rank"

            )





        with gr.Row():

            CUET = gr.Number(

                label="CUET Score"

            )


            Branch = gr.Textbox(

                label="Preferred Branch"

            )


            College = gr.Textbox(

                label="Preferred College"

            )





        with gr.Row():

            College_Type = gr.Dropdown(

                choices=[

                    "Government",

                    "Private"

                ],

                label="College Type"

            )


            NIRF = gr.Number(

                label="NIRF Rank"

            )


            Tier = gr.Number(

                label="College Tier"

            )
                    # ==========================
        # COLLEGE DETAILS
        # ==========================


        with gr.Row():


            Cutoff = gr.Number(

                label="Branch Cutoff Rank"

            )


            Seats = gr.Number(

                label="Available Seats"

            )


            Quota = gr.Textbox(

                label="Reservation Quota"

            )





        # ==========================
        # VERIFICATION DETAILS
        # ==========================


        with gr.Row():


            Docs = gr.Dropdown(

                choices=[

                    "Yes",

                    "No"

                ],

                label="Documents Verified"

            )


            Interview = gr.Number(

                label="Interview Score"

            )


            Communication = gr.Number(

                label="Communication Score"

            )





        # ==========================
        # EXTRA DETAILS
        # ==========================


        with gr.Row():


            Aptitude = gr.Number(

                label="Aptitude Score"

            )


            Scholarship = gr.Dropdown(

                choices=[

                    "Yes",

                    "No"

                ],

                label="Scholarship Applied"

            )


            Scholarship_Eligibility = gr.Dropdown(

                choices=[

                    "Yes",

                    "No"

                ],

                label="Scholarship Eligibility"

            )





        with gr.Row():


            Hostel = gr.Dropdown(

                choices=[

                    "Yes",

                    "No"

                ],

                label="Hostel Required"

            )


            Probability = gr.Number(

                label="Admission Probability"

            )


            Fee = gr.Number(

                label="Tuition Fee (₹)"

            )





        # ==========================
        # BUTTON
        # ==========================


        predict_button = gr.Button(

            "🎯 Predict Admission"

        )





        # ==========================
        # OUTPUT
        # ==========================


        output = gr.Textbox(

            label="🎓 Admission Prediction Result",

            lines=8

        )





        # ==========================
        # CONNECT FUNCTION
        # ==========================


        predict_button.click(


            fn=predict_admission,


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






# =====================================================
# RUN APPLICATION
# =====================================================


if __name__ == "__main__":



    print("🚀 Starting AI College Admission System")



    demo.launch(

        server_name="0.0.0.0",

        server_port=int(

            os.environ.get(

                "PORT",

                7860

            )

        )

    )
